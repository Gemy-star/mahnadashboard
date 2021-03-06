from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from office import models
from office import forms
from django.forms import modelformset_factory
from django.views.generic.detail import DetailView
from django.utils import timezone


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


def SetDocumentCompleted(request, pk):
    document = models.Documents.objects.get(pk=pk)
    document.completed = True
    document.save()
    return redirect('home-page')


def SetPreviewCompleted(request, pk):
    preview = models.Preview.objects.get(pk=pk)
    preview.completed = True
    preview.save()
    return redirect('home-page')


class AllClients(View):
    def get(self, request):
        data = models.Clients.objects.all()
        return render(request, 'office/clients/allClients.html', context={"data": data})


class UpdateClient(UpdateView):
    model = models.Clients
    form_class = forms.ClientForm
    template_name = 'office/clients/editClient.html'

    def get_success_url(self):
        return reverse_lazy('all-clients')


class DeleteDocument(DeleteView):
    model = models.Documents
    template_name = 'partials/_deleteEntry.html'
    success_url = reverse_lazy('home-page')


class DeleteClient(DeleteView):
    model = models.Clients
    template_name = 'partials/_deleteEntry.html'
    success_url = reverse_lazy('home-page')


class DeletePreview(DeleteView):
    model = models.Preview
    template_name = 'partials/_deleteEntry.html'
    success_url = reverse_lazy('home-page')


class UpdateDocument(UpdateView):
    model = models.Documents
    form_class = forms.DocumentForm
    template_name = 'office/documents/updateDocument.html'

    def get_success_url(self):
        return reverse_lazy('home-page')


class AllDocuments(View):
    def get(self, request):
        data = models.Documents.objects.all()
        return render(request, 'office/documents/allDocuments.html', context={"data": data})


class AddPreview(View):
    ImageFormSet = modelformset_factory(models.LocationImages,
                                        form=forms.ImageForm, extra=3)
    postForm = forms.PreviewForm()

    def get(self, request, pk):
        formset = self.ImageFormSet(queryset=models.LocationImages.objects.none())
        return render(request, 'office/previews/addpreview.html',
                      context={'postForm': self.postForm, 'formset': formset})

    def post(self, request, pk):
        postForm = forms.PreviewForm(request.POST)
        formset = self.ImageFormSet(request.POST, request.FILES,
                                    queryset=models.LocationImages.objects.none())
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            document = models.Documents.objects.get(pk=pk)
            post_form.document = document
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


class PreviewDetails(DetailView):
    model = models.Preview
    template_name = 'office/previews/previewsDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DocumentDetails(DetailView):
    model = models.Documents
    template_name = 'office/documents/document-details.html'
