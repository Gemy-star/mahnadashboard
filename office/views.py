from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from office import models
from office import forms
from mahna.views import EmailThread
from django.forms import modelformset_factory


class AddDocumentAndClient(View):
    clientForm = forms.ClientForm()
    documentForm = forms.DocumentForm()

    def get(self, request):
        return render(request, 'office/documents/addDocumentAndClient.html',
                      context={'doc_form': self.documentForm, 'clientForm': self.clientForm})

    def post(self, request):
        clientForm = forms.ClientForm(request.POST)
        documentForm = forms.DocumentForm(request.POST)
        if documentForm.is_valid() and clientForm.is_valid():
            post_form = clientForm.save(commit=False)
            post_form.save()
            doc_form = documentForm.save(commit=False)
            doc_form.client = post_form
            doc_form.enteredBy = request.user
            doc_form.save()
            messages.success(request,
                             "لقد تمت العملية بنجاح")
            return redirect('home-page')


class AddClient(CreateView):
    model = models.Clients
    form_class = forms.ClientForm
    template_name = 'office/clients/addClient.html'

    def get_success_url(self):
        return reverse('all-clients')


class AllClients(View):
    def get(self, request):
        data = models.Clients.objects.all()
        return render(request, 'office/clients/allClients.html', context={"data": data})


class UpdateClient(UpdateView):
    model = models.Clients
    form_class = forms.ClientForm
    template_name = 'office/clients/editClient.html'

    def get_success_url(self):
        return reverse('all-clients')


class AddDocument(CreateView):
    model = models.Documents
    form_class = forms.DocumentForm
    template_name = 'office/documents/addDocument.html'

    def get_success_url(self):
        return reverse('home-page')


class AllDocuments(View):
    def get(self, request):
        data = models.Documents.objects.all()
        return render(request, 'office/documents/allDocuments.html', context={"data": data})


class UpdateDocument(UpdateView):
    model = models.Documents
    form_class = forms.DocumentForm
    template_name = 'office/documents/updateDocument.html'

    def get_success_url(self):
        return reverse('all-documents')


class AddPreview(View):
    ImageFormSet = modelformset_factory(models.LocationImages,
                                        form=forms.ImageForm, extra=3)
    postForm = forms.PreviewForm()

    def get(self, request):
        formset = self.ImageFormSet(queryset=models.LocationImages.objects.none())
        return render(request, 'office/previews/addpreview.html',
                      context={'postForm': self.postForm, 'formset': formset})

    def post(self, request):
        postForm = forms.PreviewForm(request.POST)
        formset = self.ImageFormSet(request.POST, request.FILES,
                                    queryset=models.LocationImages.objects.none())
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = models.LocationImages(location=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "لقد تمت العملية بنجاح")
            return redirect('home-page')
        else:
            print(postForm.errors, formset.errors)


class AllPreviews(View):
    def get(self, request):
        data = models.Preview.objects.all()
        return render(request, 'office/previews/allpreviews.html', context={"data": data})
