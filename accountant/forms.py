from django import forms
from . import models

class VoucherForms(forms.ModelForm):
    class Meta:
        model = models.Voucher
        fields = ['voucherId','taxCompanyNumber' , 'recordId' , 'companyAddress' ,
          'payMethod' , 'clientName' , 'clientPhone' , 'clientAddress' , 'clientTaxNumber' , 'taxRatio',
          'totalBeforeTax','voucherCode' , 'voucherDescription' ]
        widgets = {
            'voucherId': forms.NumberInput(
                attrs={'id': 'voucherIdfield', 'class': 'form-control', 'placeholder': 'رقم الفاتورة'}),
            'taxCompanyNumber': forms.NumberInput(
                attrs={'id': 'taxCompanyNumberfield', 'class': 'form-control', 'placeholder': ' الرقم الضريبى للشركة '}),
             'recordId': forms.NumberInput(
                attrs={'id': 'recordIdfield', 'class': 'form-control', 'placeholder': ' رقم القيد  '}),
             'companyAddress': forms.TextInput(
                attrs={'id': 'companyAddress', 'class': 'form-control', 'placeholder': ' عنوان الشركة  '}),
             'payMethod': forms.TextInput(
                attrs={'id': 'payMethod', 'class': 'form-control', 'placeholder': ' طريقة السداد  '}),
              'clientName': forms.TextInput(
                attrs={'id': 'clientName', 'class': 'form-control', 'placeholder': ' اسم العميل  '}),
                'clientPhone': forms.TextInput(
                attrs={'id': 'clientPhone', 'class': 'form-control', 'placeholder': ' هاتف العميل  '}),
                'clientAddress': forms.TextInput(
                attrs={'id': 'clientAddress', 'class': 'form-control', 'placeholder': ' عنوان العميل  '}),         
           'clientTaxNumber': forms.NumberInput(
                attrs={'id': 'clientTaxNumber', 'class': 'form-control', 'placeholder': ' الرقم للضريبى للعميل  '}),  
                 'taxRatio': forms.TextInput(
                attrs={'id': 'taxRatio', 'class': 'form-control', 'placeholder': ' معدل  الضريبة  '}),  
           'totalBeforeTax': forms.TextInput(
                attrs={'id': 'totalBeforeTax', 'class': 'form-control', 'placeholder': ' المبلغ  قبل الضريبة  '}),  
          'voucherDescription': forms.TextInput(
                attrs={'id': 'voucherDescription', 'class': 'form-control', 'placeholder': ' وصف  الفاتورة  '}),  
           'voucherCode': forms.TextInput(
                attrs={'id': 'voucherCode', 'class': 'form-control', 'placeholder': ' رمز  الصنف  '}),  
          }  
        labels = {
            'voucherId': ' رقم الفاتورة ',
            'taxCompanyNumber': 'الرقم الضريبى للشركة ',
            'recordId': 'رقم القيد  ',
            'companyAddress': 'عنوان الشركة  ',
            'payMethod': 'طريقة السداد  ',
            'clientName': 'اسم العميل  ',
            'clientPhone': 'هاتف العميل ',
            'clientAddress': 'عنوان العميل  ',
            'clientTaxNumber': 'الرقم الضريبى للعميل ',
            'taxRatio': 'معدل الضريبة  ',
            'totalBeforeTax': 'المبلغ قبل الضريبة ',
            'voucherCode': 'رمز الصنف  ',
            'voucherDescription': 'وصف الفاتورة  ',
        }