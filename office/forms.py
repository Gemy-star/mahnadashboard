from django import forms
from office import models


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Clients
        fields = ['name', 'phone', 'authorizations', 'rights', 'benfits']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'namefield', 'class': 'form-control', 'placeholder': 'صاحب الطلب '}),
            'phone': forms.TextInput(
                attrs={'id': 'phonefield', 'class': 'form-control', 'placeholder': 'الهاتف '}),
            'authorizations': forms.TextInput(
                attrs={'id': 'authorizationsfield', 'class': 'form-control', 'placeholder': ' الصلاحيات و الأختصاصات  '}),
            'rights': forms.TextInput(
                attrs={'id': 'rightsfield', 'class': 'form-control', 'placeholder': 'الحقوق و الأمتيازات العينينة '}),
            'benfits': forms.TextInput(
                attrs={'id': 'benfitsfield', 'class': 'form-control', 'placeholder': 'المستفيدين من الأستخدام '}),
        }
        labels = {
            'name': 'صاحب الطلب ',
            'phone': 'الهاتف',
            'authorizations': ' الصلاحيات و الأختصاصات',
            'rights': ' الحقوق و الأمتيازات العينينة ',
            'benfits': 'المستفيدين من الأستخدام',
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Documents
        fields = ['documentNumber','ownerPlace', 'ownerName', 'ownerNationalID', 'realStateType', 'paperNumber',
                  'paperDate', 'area', 'buildingArea', 'ratingPurpose']
        labels = {
            'documentNumber':'رقم الطلب',
            'ownerPlace' : 'جهة صاحب الطلب' , 
            'ownerName' : ' إسم المالك' , 
            'ownerNationalID' : ' هوية المالك' , 
            'realStateType' : ' نوع العقار' , 
            'paperNumber' : ' رقم الصك' , 
            'paperDate' : ' تاريخ الصك' , 
            'area' : ' مساحة الأرض' , 
            'buildingArea' : ' مسطحات البناء' , 
            'ratingPurpose' : ' الغرض من التقييم' , 
        }
        widgets = {
            'documentNumber':forms.TextInput(
                attrs={'id': 'ownerPlacefield','readonly':True, 'class': 'form-control', 'placeholder': 'جهة صاحب الطلب '}),
            'ownerPlace': forms.TextInput(
                attrs={'id': 'ownerPlacefield', 'class': 'form-control', 'placeholder': 'جهة صاحب الطلب '}),
            'ownerName': forms.TextInput(
                attrs={'id': 'ownernamefield', 'class': 'form-control', 'placeholder': '  إسم المالك'}),
            'ownerNationalID': forms.NumberInput(
                attrs={'id': 'ownerNationalIDfield', 'class': 'form-control', 'placeholder': ' هوية المالك'}),
            'realStateType': forms.Select(choices=models.Documents.REALSTATE_CHOICES),
            'paperNumber': forms.NumberInput(
                attrs={'id': 'paperNumberfield', 'class': 'form-control', 'placeholder': ' رقم الصك '}),
            'paperDate': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'id': 'paperDatefield', 'type': 'date', 'class': 'form-control', 'placeholder': ' تاريخ الصك '}),
            'area': forms.NumberInput(
                attrs={'id': 'areafield', 'class': 'form-control', 'placeholder': 'مساحة الأرض'}),
            'buildingArea': forms.NumberInput(
                attrs={'id': 'buildingAreafield', 'class': 'form-control', 'placeholder': 'مسطحات البناء'}),
            'ratingPurpose': forms.TextInput(
                attrs={'id': 'ratingPurposefield', 'class': 'form-control', 'placeholder': ' الغرض من التقييم'}),
        }



class PreviewForm(forms.ModelForm):
    class Meta:
        model = models.Preview
        fields = ['locationUrl', 'locationDescription', 'locationState', 'locationLevel', 'FinishType',
        'structureType','locationAge' , 'document'
        ]
        widgets = {
            'locationUrl': forms.URLInput(
                attrs={'id': 'LocationUrlfield', 'class': 'form-control', 'placeholder': 'رابط الموقع'}),
            'locationState': forms.Select(choices=models.Preview.LOCATION_STATUS,
                                   attrs={'id': 'locationStatefield', 'class': 'form-control'}),
            'locationDescription': forms.TextInput(
                attrs={'id': 'locationDescriptionfield', 'class': 'form-control', 'placeholder': 'الوصف'}),
             'locationAge': forms.NumberInput(
                attrs={'id': 'LocationDescriptionfield', 'class': 'form-control', 'placeholder': 'عمر العقار '}),
            'locationLevel': forms.Select(choices=models.Preview.ZONE_LEVEL,
                                       attrs={'id': 'locationLevelfield', 'class': 'form-control'}),
            'FinishType': forms.Select(choices=models.Preview.FINISHING,
                                      attrs={'id': 'FinishTypefield', 'class': 'form-control'}),
            'structureType': forms.Select(choices=models.Preview.STRUCTURE_TYPE,
                                      attrs={'id': 'STRUCTURE_TYPEfield', 'class': 'form-control'}),                          
             'document': forms.Select(choices=models.Documents.objects.all(),
                                      attrs={'id': 'documentfield', 'class': 'form-control'}),                          
        }
        labels = {
            'locationUrl': 'رابط الموقع',
            'locationState': 'حالة المبنى ',
            'locationDescription': 'وصف العقار ',
            'locationLevel': 'مستوى المنطقة',
            'FinishType': 'نوع التشطيب ',
            'structureType': 'نوع الهيكل الأنشائى ',
            'locationAge': 'عمر العقار ',
            'document': 'إختر رقم الطلب ',

        }

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='صور الموقع')

    class Meta:
        model = models.LocationImages
        fields = ['image']        