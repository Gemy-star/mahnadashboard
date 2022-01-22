from django.urls import path
from . import views

urlpatterns = [
    path('clients/all', views.AllClients.as_view(), name='all-clients'),
    path('client/add', views.AddClient.as_view(), name='add-client'),
    path('client/update/<int:pk>',
         views.UpdateClient.as_view(), name='update-client'),
    path('documents/all', views.AllDocuments.as_view(), name='all-documents'),
    path('document/add', views.AddDocument.as_view(), name='add-document'),
    path('document/update/<int:pk>',
         views.UpdateDocument.as_view(), name='update-document'),
    path('previews/all', views.AllPreviews.as_view(), name='all-previews'),
    path('previews/details/<int:pk>', views.PreviewDetails.as_view(), name='previews-details'),
    path('preview/add', views.AddPreview.as_view(), name='add-preview'),
    path('documentAndClient/add', views.AddDocumentAndClient.as_view(), name='add-doc_client'),

]
