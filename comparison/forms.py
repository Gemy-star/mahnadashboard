from django import forms
from django.db.models import fields
from . import models
from office.models import Preview


class ResidentDocumentForm(forms.ModelForm):
    class Meta:
        model = models.ResidentDocument
        fields = ['residentRate', 'valueBase']
        exclude = ['previews', ]
        widgets = {
            'residentRate': forms.TextInput(
                attrs={'id': 'residentRatefield', 'class': 'form-control', 'placeholder': 'الغرض من التقيم '}),
            'valueBase': forms.Select(choices=models.ResidentDocument.VALUE_BASE),
        }
        labels = {
            'residentRate': 'الغرض من التقييم',
            'valueBase': 'أساس القيمة  ',
        }


class ResidentBuildingForm(forms.ModelForm):
    class Meta:
        model = models.ResidentBuilding
        fields = ['residentDate', 'areaNumber', 'streetCount', 'areaUsage', 'address', 'residentDocument']
        widgets = {
            'residentDate': forms.DateInput(
                attrs={'id': 'residentDatefield', 'type': 'date', 'class': 'form-control',
                       'placeholder': 'تاريخ التقييم '}),
            'areaNumber': forms.NumberInput(
                attrs={'id': 'areaNumberfield', 'class': 'form-control', 'placeholder': 'مساحة الأرض'}),
            'streetCount': forms.NumberInput(
                attrs={'id': 'areaNumberfield', 'class': 'form-control', 'placeholder': 'عدد الشوارع المحيطة'}),
            'areaUsage': forms.Select(choices=models.ResidentBuilding.AREALEVEL),
            'address': forms.TextInput(
                attrs={'id': 'areaNumberfield', 'class': 'form-control', 'placeholder': 'مواقع العقار'}),
            'residentDocument': forms.Select(choices=models.ResidentDocument.objects.all().values_list()),
        }
        labels = {
            'residentDate': ' تاريخ التقييم',
            'areaNumber': 'مساحة الأرض (متر مربع)  ',
            'streetCount': 'عدد الشوارع المحيطه   ',
            'areaUsage': ' استخدام الأرض ',
            'address': '  مواقع العقار',
            'residentDocument': ' إختر مستند التقييم',

        }


class CompareBuildingForm(forms.ModelForm):
    class Meta:
        model = models.CompareBuilding
        fields = ['compareDate', 'CompareareaNumber', 'Comparearea', 'buildingValue', 'priceMeter',
                  'ComparestreetCount',
                  'areaPrecentage', 'zonePrecentage', 'locationPrecentage', 'streetPrecentage', 'usagePrecentage',
                  'CompareareaUsage', 'Compareaddress'
            , 'CompareareaLevel', 'residentBuilding']
        widgets = {
            'compareDate': forms.DateInput(
                attrs={'id': 'compareDatefield', 'type': 'date', 'class': 'form-control'}),
            'CompareareaLevel': forms.Select(choices=models.CompareBuilding.AREAlEVEL),
            'residentBuilding': forms.Select(choices=models.ResidentBuilding.objects.all().values_list()),
            'CompareareaUsage': forms.Select(choices=models.CompareBuilding.AREAUSAGE),
            'CompareareaNumber': forms.NumberInput(
                attrs={'id': 'CompareareaNumberfield', 'class': 'form-control', 'placeholder': 'رقم القطعة'}),
            'Comparearea': forms.NumberInput(
                attrs={'id': 'Compareareafield', 'class': 'form-control', 'placeholder': 'مساحة الأرض'}),
            'buildingValue': forms.NumberInput(
                attrs={'id': 'buildingValuefield', 'class': 'form-control', 'placeholder': ' قيمة العقار'}),
            'priceMeter': forms.NumberInput(
                attrs={'id': 'priceMeterfield', 'class': 'form-control', 'placeholder': ' سعر المتر'}),
            'ComparestreetCount': forms.NumberInput(
                attrs={'id': 'ComparestreetCountfield', 'class': 'form-control',
                       'placeholder': ' عدد الشوارع المحيطة'}),
            'areaPrecentage': forms.NumberInput(
                attrs={'id': 'areaPrecentagefield', 'class': 'form-control', 'placeholder': ' نسبة مساحة الأرض'}),
            'zonePrecentage': forms.NumberInput(
                attrs={'id': 'zonePrecentagefield', 'class': 'form-control', 'placeholder': ' نسبة مستوى المنطقة'}),
            'locationPrecentage': forms.NumberInput(
                attrs={'id': 'locationPrecentagefield', 'class': 'form-control', 'placeholder': ' نسبة مواقع العقار'}),
            'streetPrecentage': forms.NumberInput(
                attrs={'id': 'streetPrecentagefield', 'class': 'form-control', 'placeholder': ' نسبة الشوارع المحيطة'}),

            'usagePrecentage': forms.NumberInput(
                attrs={'id': 'usagePrecentagefield', 'class': 'form-control', 'placeholder': ' نسبة استخدام الأرض'}),

            'Compareaddress': forms.TextInput(
                attrs={'id': 'Compareaddressfield', 'class': 'form-control', 'placeholder': ' مواقع العقار '}),

        }
        labels = {
            'compareDate': 'تاريخ التقييم',
            'CompareareaLevel': 'مستوى المنطقة  ',
            'residentBuilding': 'إختر رقم مستند التقييم ',
            'CompareareaUsage': 'استخدام الأرض  ',
            'CompareareaNumber': 'رقم القطعة  ',
            'Comparearea': 'مساحة الأرض  ',
            'buildingValue': 'قيمة العقار  ',
            'priceMeter': 'سعر المتر  ',
            'ComparestreetCount': 'عدد الشوارع المحيطة  ',
            'areaPrecentage': 'نسبة مساحة الأرض  ',
            'zonePrecentage': 'نسبة مستوى المنطقة  ',
            'locationPrecentage': 'نسبة مواقع العقار  ',
            'streetPrecentage': 'نسبة الشوارع المحيطة  ',
            'usagePrecentage': 'نسبة استخدام الأرض  ',
            'Compareaddress': 'مواقع العقار  ',

        }


class UnDirectBuildingCostForm(forms.ModelForm):
    class Meta:
        model = models.UndirectBuildingCost
        fields = ['document', 'technicalFees', 'developerFees', 'serviceFees']
        widgets = {
            'document': forms.Select(choices=models.ResidentDocument.objects.all().values_list()),
            'technicalFees': forms.NumberInput(
                attrs={'id': 'technicalFeesfield', 'class': 'form-control', 'placeholder': ' رسوم مهنيه   '}),
            'serviceFees': forms.NumberInput(
                attrs={'id': 'serviceFeesfield', 'class': 'form-control', 'placeholder': '   رسوم المرافق  '}),
            'developerFees': forms.NumberInput(
                attrs={'id': 'developerFeesfield', 'class': 'form-control', 'placeholder': '    ربح المطور  '}),
        }
        labels = {
            'document': 'إختر مستند التقييم',
            'technicalFees': '  رسوم مهنية  ',
            'serviceFees': 'رسوم المرافق',
            'developerFees': '  ربح المطور',

        }


class DirectBuildingCostForm(forms.ModelForm):
    class Meta:
        model = models.DirectBuildingCost
        fields = ['document', 'areaBuildCost', 'priceMeterCost']
        widgets = {
            'document': forms.Select(choices=models.ResidentDocument.objects.all().values_list()),
            'areaBuildCost': forms.NumberInput(
                attrs={'id': 'areaBuildCostfield', 'class': 'form-control', 'placeholder': 'تكاليف مساحات البناء '}),
            'priceMeterCost': forms.NumberInput(
                attrs={'id': 'authorizationsfield', 'class': 'form-control', 'placeholder': ' تكلفة المتر المربع  '}),
        }
        labels = {
            'document': 'إختر مستند التقييم',
            'areaBuildCost': 'تكاليف مساحات البناء  ',
            'priceMeterCost': 'تكلفة المتر المربع',
        }


class DamagedBuildingRateForm(forms.ModelForm):
    class Meta:
        model = models.DamagedBuildingRate
        fields = ['normalAge', 'buildingAge', 'document']
        widgets = {
            'buildingAge': forms.NumberInput(
                attrs={'id': 'buildingAgefield', 'class': 'form-control', 'placeholder': 'عمر البناء '}),
            'normalAge': forms.NumberInput(
                attrs={'id': 'normalAgefield', 'class': 'form-control', 'placeholder': 'عمر الأفتراضى للمبنى  '}),
            'document': forms.Select(choices=models.ResidentDocument.objects.all().values_list()),
        }
        labels = {
            'buildingAge': ' عمر البناء ',
            'normalAge': 'عمر الأفتراضى للمبنى   ',
            'document': 'إختر مستند التقييم ',
        }
