import os
from pathlib import Path

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


# Create your views here.
class AddVoucher(CreateView):
    model = models.Voucher
    form_class = forms.VoucherForms
    template_name = 'accountant/addVoucher.html'

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
        voucher = models.Voucher.objects.get(pk=pk)
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "static_root": os.path.join(Path(__file__).resolve().parent.parent, "static"),
            "company": "مكتب عبد الله الهنا",
            "user": user_obj,
            "voucher": voucher,
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('reports/voucher.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
