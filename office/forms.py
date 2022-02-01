from django import forms
from office import models


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Clients
        fields = '__all__'

        labels = {
            'name': 'صاحب الطلب ',
            'phone': 'الهاتف',
            'authorizations': ' الصلاحيات و الأختصاصات',
            'rights': ' الحقوق و الأمتيازات العينينة ',
            'benfits': 'المستفيدين من الأستخدام',
            'document_1': 'المستند الأول',
            'document_2': 'المستند الثانى',
            'document_3': 'المستند الثالث',

        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Documents
        fields = '__all__'
        exclude = ('client', 'enteredBy','completed')
        widgets = {
            'paperDate': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'id': 'paperDatefield', 'type': 'date', 'class': 'form-control', 'placeholder': ' تاريخ الصك '}),
        }
        labels = {
            'documentNumber': 'رقم الطلب',
            'ownerPlace': 'جهة صاحب الطلب',
            'ownerName': ' إسم المالك',
            'ownerNationalID': ' هوية المالك',
            'realStateType': ' نوع العقار',
            'paperNumber': ' رقم الصك',
            'paperDate': ' تاريخ الصك',
            'area': ' مساحة الأرض',
            'buildingArea': ' مسطحات البناء',
            'ratingPurpose': ' الغرض من التقييم',
        }


class PreviewForm(forms.ModelForm):
    class Meta:
        model = models.Preview
        fields = ['locationUrl', 'locationDescription', 'locationState', 'locationLevel', 'FinishType',
                  'structureType', 'locationAge', 'document', 'lat', 'lang'
                  ]
        exclude = ('document','completed')
        widgets = {
            'locationUrl': forms.URLInput(
                attrs={'id': 'LocationUrlfield', 'class': 'form-control', 'placeholder': 'رابط الموقع'}),
            'locationState': forms.Select(choices=models.Preview.LOCATION_STATUS,
                                          attrs={'id': 'locationStatefield', 'class': 'form-control'}),
            'locationDescription': forms.TextInput(
                attrs={'id': 'locationDescriptionfield', 'class': 'form-control', 'placeholder': 'الوصف'}),
            'locationAge': forms.NumberInput(
                attrs={'id': 'LocationDescriptionfield', 'class': 'form-control', 'placeholder': 'عمر العقار '}),
            'lat': forms.NumberInput(
                attrs={'id': 'latfield', 'class': 'form-control', 'placeholder': 'خط العرض '}),
            'lang': forms.NumberInput(
                attrs={'id': 'langfield', 'class': 'form-control', 'placeholder': 'خط الطول '}),
            'locationLevel': forms.Select(choices=models.Preview.ZONE_LEVEL,
                                          attrs={'id': 'locationLevelfield', 'class': 'form-control'}),
            'FinishType': forms.Select(choices=models.Preview.FINISHING,
                                       attrs={'id': 'FinishTypefield', 'class': 'form-control'}),
            'structureType': forms.Select(choices=models.Preview.STRUCTURE_TYPE,
                                          attrs={'id': 'STRUCTURE_TYPEfield', 'class': 'form-control'}),

        }
        labels = {
            'locationUrl': 'رابط الموقع',
            'locationState': 'حالة المبنى ',
            'locationDescription': 'وصف العقار ',
            'locationLevel': 'مستوى المنطقة',
            'FinishType': 'نوع التشطيب ',
            'structureType': 'نوع الهيكل الأنشائى ',
            'locationAge': 'عمر العقار ',
            'lat': 'خط العرض',
            'lang': 'خط الطول',

        }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='صور الموقع')

    class Meta:
        model = models.LocationImages
        fields = ['image']
