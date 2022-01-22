import qrcode
from django.db import models
from django.urls import reverse
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Voucher(models.Model):
    def VoucherNumber():
        no = Voucher.objects.count()
        if no == None:
            return 10000
        else:
            return (no * 10000) + 1

    voucherId = models.CharField(max_length=255, unique=True, default=VoucherNumber)
    voucherDate = models.DateTimeField(auto_now_add=True)
    taxCompanyNumber = models.IntegerField(null=True, blank=True)
    recordId = models.IntegerField(unique=True)
    companyAddress = models.CharField(null=True, blank=True, max_length=255)
    payMethod = models.CharField(null=True, max_length=255, blank=True)
    clientName = models.CharField(null=True, max_length=255, blank=True)
    clientPhone = models.CharField(null=True, max_length=255, blank=True)
    clientAddress = models.CharField(null=True, max_length=255, blank=True)
    clientTaxNumber = models.IntegerField(null=True, blank=True)
    taxRatio = models.SmallIntegerField(null=True, blank=True)
    totalBeforeTax = models.IntegerField(null=True, blank=True)
    voucherCode = models.CharField(null=True, max_length=255, blank=True)
    voucherDescription = models.CharField(null=True, max_length=255, blank=True)
    qrcode = models.ImageField(upload_to='images/qrcode', null=True, blank=True)

    @property
    def TotaltaxCost(self):
        return self.totalBeforeTax * (self.taxRatio / 100)

    @property
    def Totalpay(self):
        return self.totalBeforeTax + self.TotaltaxCost

    def get_absolute_url(self):
        return reverse("voucher-detail", kwargs={'pk': self.id})

    def CreateQrCode(self, *args, **kwargs):
        qr_image = qrcode.make(self.get_absolute_url())
        qr_offset = Image.new('RGB', (310, 310), 'white')
        qr_offset.paste(qr_image)
        files_name = f"{self.clientName}-{self.id}qr.png"
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qrcode.save(files_name, File(stream), save=False)
        qr_offset.close()
        self.save()

    def __str__(self) -> str:
        return str(self.voucherId)
