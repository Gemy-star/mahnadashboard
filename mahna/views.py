import threading

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View

from office.filters import DocumentFilter
from office.models import Documents, Preview
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
        documents = Documents.objects.filter(completed=False)
        documents_for_preview = Documents.objects.filter(completed=True)
        prev_comp = Preview.objects.filter(completed=True)
        preivews_not = Preview.objects.filter(completed=False)
        all_prieviews = Preview.objects.all()
        residentDocument_not = ResidentDocument.objects.filter(completed=False)
        resident_ready = ResidentDocument.objects.filter(completed=True)
        f = DocumentFilter(request.GET, queryset=Documents.objects.all())

        context = {
            "documents": documents,
            "previews": all_prieviews,
            "previews_not": preivews_not,
            "residentDocument": ResidentDocument.objects.all(),
            "vouchers": Voucher.objects.all(),
            "prev_comp": prev_comp,
            "documents_for_preview": documents_for_preview,
            "dcoument_all": Documents.objects.all(),
            "residentDocument_not": residentDocument_not,
            "resident_ready": resident_ready,
            'filter': f,

        }
        return render(request, 'home-page.html', context=context)
