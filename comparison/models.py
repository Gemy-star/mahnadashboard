from django.db import models
from office.models import Documents
# Create your models here.
class ResidentDocument(models.Model):
    residentRate = models.CharField(max_length=255 , null=True , blank=True)
    VALUE_BASE = (
              (1 , 'عادله'),
              (2 , 'تصفية'),
              (3 , 'سوقية'),
              (4 , 'بيع قصرى'),
              (5, 'احادية'),
    )
    valueBase = models.SmallIntegerField(choices=VALUE_BASE , null=True , blank=True)  
    document = models.OneToOneField(Documents , on_delete=models.CASCADE , null=True)
    def __str__(self) -> str:
        return str(self.pk)


class ResidentBuilding (models.Model):
    residentDate = models.DateField(null=True , blank=True)
    areaNumber = models.IntegerField(null=True , blank=True)
    streetCount = models.IntegerField(null=True , blank=True , default=0)
    AREALEVEL = (
        (1 ,'سكنى'),
        (2 , 'تجارى'),
        (3 , 'مكتبى'),
    )
    areaUsage = models.SmallIntegerField(choices=AREALEVEL , null=True , blank =True)
    address = models.CharField(max_length=255 , null=True , blank=True)
    residentDocument = models.OneToOneField(ResidentDocument , on_delete=models.CASCADE , null=True)
    def __str__(self) -> str:
        return str(self.pk)


class CompareBuilding(models.Model):
    compareDate = models.DateField(null=True , blank=True)
    CompareareaNumber = models.IntegerField(null=True , blank=True)
    Comparearea = models.IntegerField(null=True , blank=True)
    buildingValue = models.IntegerField(null=True , blank=True)
    priceMeter = models.IntegerField(null=True , blank=True)
    ComparestreetCount = models.IntegerField(null=True , blank=True)
    areaPrecentage = models.SmallIntegerField(null=True , blank=True)
    zonePrecentage = models.SmallIntegerField(null=True , blank=True)
    locationPrecentage = models.SmallIntegerField(null=True , blank=True)
    streetPrecentage = models.SmallIntegerField(null=True , blank=True)
    usagePrecentage = models.SmallIntegerField(null=True , blank=True)

    AREAUSAGE = (
        (1 ,'سكنى'),
        (2 , 'تجارى'),
        (3 , 'مكتبى'),
    )
    AREAlEVEL =(
          (1 ,'عالى'),
        (2 , 'متوسط'),
        (3 , 'منخفض'),
    )
    CompareareaUsage = models.SmallIntegerField(choices=AREAUSAGE , null=True , blank =True)
    Compareaddress = models.CharField(max_length=255 , null=True , blank=True)
    CompareareaLevel =  models.SmallIntegerField(choices=AREAlEVEL , null=True , blank =True)
    residentBuilding = models.ForeignKey(ResidentBuilding , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.pk)




    