from django.urls import path
from . import views

urlpatterns = [
     path('update/voucher/<int:pk>',
         views.UpdateVoucher.as_view(), name='update-voucher'),
    path('add/voucher',
         views.AddVoucher.as_view(), name='add-voucher'),
]