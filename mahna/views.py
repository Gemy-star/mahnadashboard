import threading

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from office.models import Documents , Preview
from accounts.models import User
from comparison.models import ResidentDocument
from accountant.models import Voucher
class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)


class HomePage(View):
    login_required = True
    def get(self, request):
        context= {
            "documents":Documents.objects.all(),
            "previewcount": Preview.objects.all().count(),
            "residentDocument":ResidentDocument.objects.all(),
            "vouchers":Voucher.objects.all()

        }
        return render(request, 'home-page.html' , context=context)
