from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from comparison import models
from comparison import forms
from office.models import Preview


# Create your views here.

class AddResidentDocument(View):
    form = forms.ResidentDocumentForm

    def get(self, request, pk):
        return render(request, 'comparison/residentDocument/AddResidentDocument.html',
                      context={'form': self.form})

    def post(self, request, pk):
        form = forms.ResidentDocumentForm(request.POST)
        if form.is_valid():
            post_form = form.save(commit=False)
            prev = Preview.objects.get(pk=pk)
            post_form.previews = prev
            post_form.save()
            messages.success(request,
                             "لقد تمت العملية بنجاح")
            return redirect('home-page')




def SetResidentCompleted(request, pk):
    resident = models.ResidentDocument.objects.get(pk=pk)
    resident.completed = True
    resident.save()
    return redirect('home-page')


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
    def get(self, request, pk):
        request.session['pk_buildDoc'] = pk
        document = models.ResidentDocument.objects.get(pk=pk)
        building = models.ResidentBuilding.objects.get(residentDocument=document)
        compareBuilding = models.CompareBuilding.objects.filter(residentBuilding=building)
        data = {
            "building": building,
            "compareBuilding": compareBuilding
        }
        return render(request, 'comparison/souqComparison.html', context=data)


class DirectAndUnDirectPage(View):
    def get(self, request, pk):
        request.session['pk_buildDoc'] = pk
        document = models.ResidentDocument.objects.get(pk=pk)
        if models.DirectBuildingCost.objects.filter(document=document).count() > 0:
            directCost = models.DirectBuildingCost.objects.get(document=document)
            unDirectCost = models.UndirectBuildingCost.objects.get(document=document)
            data = {
                "directCost": directCost,
                "unDirectCost": unDirectCost,
                "totalCost": directCost.TotalDirectCost + unDirectCost.TotalUnDirectCost,
            }
        else:
            data = {
                "directCost": 0,
                "unDirectCost": 0,
                "totalCost": 0,
            }
        return render(request, 'comparison/directAndUndirect.html', context=data)


class AddDirectCost(CreateView):
    model = models.DirectBuildingCost
    form_class = forms.DirectBuildingCostForm
    template_name = 'comparison/direct/AddDirect.html'

    def get_success_url(self):
        return reverse('home-page')


class UpdateDirectCost(UpdateView):
    model = models.DirectBuildingCost
    form_class = forms.DirectBuildingCostForm
    template_name = 'comparison/direct/EditDirect.html'

    def get_success_url(self):
        return reverse('home-page')


class AddUnDirectCost(CreateView):
    model = models.UndirectBuildingCost
    form_class = forms.UnDirectBuildingCostForm
    template_name = 'comparison/Undirect/AddUnDirect.html'

    def get_success_url(self):
        return reverse('home-page')


class UpdateUnDirectCost(UpdateView):
    model = models.UndirectBuildingCost
    form_class = forms.UnDirectBuildingCostForm
    template_name = 'comparison/Undirect/EditUnDirect.html'

    def get_success_url(self):
        return reverse('home-page')


class DamagedPage(View):
    def get(self, request, pk):
        request.session['pk_buildDoc'] = pk
        document = models.ResidentDocument.objects.get(pk=pk)
        if models.DamagedBuildingRate.objects.filter(document=document).count() > 0:
            damaged = models.DamagedBuildingRate.objects.get(document=document)
            directCost = models.DirectBuildingCost.objects.get(document=document)
            unDirectCost = models.UndirectBuildingCost.objects.get(document=document)
            totalCost = directCost.TotalDirectCost + unDirectCost.TotalUnDirectCost
            total = damaged.DamagedRate * totalCost
            data = {
                "damaged": damaged,
                "total": total,
            }
        else:
            data = {
                "damaged": 0,
                "total": 0,
            }
        return render(request, 'comparison/DamagedPage.html', context=data)


class AddDamaged(CreateView):
    model = models.DamagedBuildingRate
    form_class = forms.DamagedBuildingRateForm
    template_name = 'comparison/damagedBuildingRate/addDamaged.html'

    def get_success_url(self):
        return reverse('home-page')


class UpdateDamaged(UpdateView):
    model = models.DamagedBuildingRate
    form_class = forms.DamagedBuildingRateForm
    template_name = 'comparison/damagedBuildingRate/EditDamaged.html'

    def get_success_url(self):
        return reverse('home-page')
