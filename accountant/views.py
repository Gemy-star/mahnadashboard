from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from . import models
from . import forms
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