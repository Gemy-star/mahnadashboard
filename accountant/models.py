from django.db import models

class Voucher(models.Model):
    def VoucherNumber():
        no = Voucher.objects.count()
        if no == None:
            return  10000
        else:
            return (no*10000)+1  
    voucherId = models.CharField(max_length=255 , unique=True , default=VoucherNumber)
    voucherDate = models.DateTimeField(auto_now_add=True)
    taxCompanyNumber = models.IntegerField(null=True , blank=True)
    recordId = models.IntegerField(unique=True)
    companyAddress = models.CharField(null=True , blank=True , max_length=255)
    payMethod = models.CharField(null=True ,max_length=255 , blank=True)
    clientName = models.CharField(null=True ,max_length=255 , blank=True)
    clientPhone =models.CharField(null=True ,max_length=255 , blank=True)
    clientAddress = models.CharField(null=True ,max_length=255 , blank=True)
    clientTaxNumber = models.IntegerField(null=True , blank=True)
    taxRatio = models.SmallIntegerField(null=True , blank=True)
    totalBeforeTax = models.IntegerField(null=True , blank=True)
    voucherCode =  models.CharField(null=True ,max_length=255 , blank=True)
    voucherDescription = models.CharField(null=True ,max_length=255 , blank=True)
    @property
    def TotaltaxCost(self):
        return self.totalBeforeTax * (self.taxRatio/100)
    @property
    def Totalpay(self):
        return self.totalBeforeTax + self.TotaltaxCost    
    def __str__(self) -> str:
        return str(self.voucherId)