import os
from pathlib import Path

import PIL
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from . import models
from . import forms
from django.http import HttpResponse
from django.views import View
from accounts.models import User
from mahna.utils import render_to_pdf
from django.template.loader import get_template
from datetime import datetime
from django.views.generic.detail import DetailView


# Create your views here.
class AddVoucher(CreateView):
    model = models.Voucher
    form_class = forms.VoucherForms
    template_name = 'accountant/addVoucher.html'

    def form_valid(self, form):
        voucher = form.save(commit=True)
        voucher.CreateQrCode()
        return super(AddVoucher, self).form_valid(form)

    def get_success_url(self):
        return reverse('home-page')


class UpdateVoucher(UpdateView):
    model = models.Voucher
    form_class = forms.VoucherForms
    template_name = 'accountant/EditVoucher.html'

    def get_success_url(self):
        return reverse('home-page')


class VoucherReport(View):
    def get(self, request, pk):
        template = get_template('reports/voucher.html')
        full_path = 'http://127.0.0.1:9000/static/images/'
        voucher = models.Voucher.objects.get(pk=pk)
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "static_root": os.path.join(Path(__file__).resolve().parent.parent, "static"),
            "company": "مكتب عبد الله الهنا",
            "user": user_obj,
            "voucher": voucher,
            "full_path": full_path,
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('reports/voucher.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f'{voucher.clientName}.pdf'
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class VoucherDetail(DetailView):
    model = models.Voucher
    template_name = 'accountant/voucherDetail.html'
