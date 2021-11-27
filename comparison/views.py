from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from comparison import models
from comparison import forms
# Create your views here.



class AddResidentDocument(CreateView):
    model = models.ResidentDocument
    form_class = forms.ResidentDocumentForm
    template_name = 'comparison/residentDocument/AddResidentDocument.html'
    def get_success_url(self):
        return reverse('home-page')


class UpdateResidentDocument(UpdateView):
    model = models.ResidentDocument
    form_class = forms.ResidentDocumentForm
    template_name = 'comparison/residentDocument/EditResidentDocument.html'
    def get_success_url(self):
        return reverse('home-page')


class AddResidentBuilding(CreateView):
    model = models.ResidentBuilding
    form_class = forms.ResidentBuildingForm
    template_name = 'comparison/residentBuilding/AddResidentBuilding.html'
    def get_success_url(self):
        return reverse('home-page')


class UpdateResidentBuilding(UpdateView):
    model = models.ResidentDocument
    form_class = forms.ResidentDocumentForm
    template_name = 'comparison/residentDocument/EditResidentBuilding.html'
    def get_success_url(self):
        return reverse('home-page')


class AddCompareBuilding(CreateView):
    model = models.CompareBuilding
    form_class = forms.CompareBuildingForm
    template_name = 'comparison/compareBuilding/AddCompareBuilding.html'
    def get_success_url(self):
        return reverse('home-page')


class UpdateCompareBuilding(UpdateView):
    model = models.CompareBuilding
    form_class = forms.CompareBuildingForm
    template_name = 'comparison/compareBuilding/EditCompareBuilding.html'
    def get_success_url(self):
        return reverse('home-page')



class SouqComparePage(View):
    def get(self, request , pk):
        request.session['pk_buildDoc'] = pk
        document = models.ResidentDocument.objects.get(pk=pk)
        building = models.ResidentBuilding.objects.get(residentDocument=document)
        compareBuilding = models.CompareBuilding.objects.filter(residentBuilding=building)
        data = {
            "building":building,
            "compareBuilding":compareBuilding
        }
        return render(request, 'comparison/souqComparison.html' , context = data)