import django_filters
from office.models import Documents


class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Documents
        fields = ['ownerName', 'ownerNationalID', 'paperDate', 'ownerPlace', 'documentNumber']
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
