from django.db import models
from accounts.models import User
from django.template.defaultfilters import slugify


# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    authorizations = models.TextField(null=True, blank=True)
    rights = models.TextField(null=True, blank=True)
    benfits = models.TextField(null=True, blank=True)
    document_1 = models.FileField(upload_to='clients_documents/', null=True, blank=True)
    document_2 = models.FileField(upload_to='clients_documents/', null=True, blank=True)
    document_3 = models.FileField(upload_to='clients_documents/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Documents(models.Model):
    REALSTATE_CHOICES = [
        (1, 'فيلا'),
        (2, 'أرض'),
        (3, 'مخطط'),
        (4, 'عمارة سكنية'),
        (5, 'عمارة مكتبة'),
        (6, 'معرض '),
        (7, 'مصنع'),
        (8, 'مكتب'),
    ]

    def DocumentNumber():
        no = Documents.objects.count()
        if no == None:
            return 1000
        else:
            return (no * 1000) + 1

    completed = models.BooleanField(null=True, default=False, blank=True)
    documentNumber = models.CharField(max_length=255, unique=True, default=DocumentNumber)
    ownerPlace = models.CharField(max_length=255, null=True, blank=True)
    ownerName = models.CharField(max_length=255, null=True, blank=True)
    ownerNationalID = models.CharField(max_length=255, null=True, unique=True)
    realStateType = models.SmallIntegerField(choices=REALSTATE_CHOICES, null=True)
    paperNumber = models.IntegerField(null=True, blank=True)
    paperDate = models.DateField(null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    buildingArea = models.IntegerField(null=True, blank=True)
    ratingPurpose = models.TextField(null=True, blank=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, null=True)
    enteredBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dateEntered = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self) -> str:
        return self.documentNumber


class Preview(models.Model):
    LOCATION_STATUS = (
        (1, 'ممتازة'),
        (2, 'جيده'),
        (3, 'سيئة')
    )
    ZONE_LEVEL = (
        (1, 'مرتفع'),
        (2, 'منخفض'),
    )
    STRUCTURE_TYPE = (
        (1, 'خرسانه مسلحة '),
        (2, ' هيكل معدنى'),
    )
    FINISHING = (
        (1, 'بدون عظم'),
        (2, 'نصف تشطيب'),
        (3, ' تشطيب كامل')
    )
    locationUrl = models.URLField(null=True, blank=True)
    locationDescription = models.TextField(null=True, blank=True)
    locationState = models.SmallIntegerField(choices=LOCATION_STATUS, null=True)
    locationLevel = models.SmallIntegerField(choices=ZONE_LEVEL, null=True)
    FinishType = models.SmallIntegerField(choices=FINISHING, null=True)
    structureType = models.SmallIntegerField(choices=STRUCTURE_TYPE, null=True)
    locationAge = models.SmallIntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lang = models.FloatField(null=True, blank=True)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    completed = models.BooleanField(null=True, default=False, blank=True)

    def __str__(self):
        return self.document.client.name


def get_image_filename(instance, filename):
    title = instance.location.document.get_realStateType_display()
    slug = slugify(title)
    return "location_images/%s-%s" % (slug, filename)


class LocationImages(models.Model):
    location = models.ForeignKey(Preview, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
