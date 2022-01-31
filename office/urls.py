from django.urls import path
from . import views

urlpatterns = [
    path('clients/all', views.AllClients.as_view(), name='all-clients'),
    path('client/update/<int:pk>',
         views.UpdateClient.as_view(), name='update-client'),
    path('documents/all', views.AllDocuments.as_view(), name='all-documents'),
    path('previews/all', views.AllPreviews.as_view(), name='all-previews'),
    path('previews/details/<int:pk>', views.PreviewDetails.as_view(), name='previews-details'),
    path('preview/add/<int:pk>', views.AddPreview.as_view(), name='add-preview'),
    path('documentAndClient/add', views.AddDocumentAndClient.as_view(), name='add-doc_client'),
    path('document/set/<int:pk>', views.SetDocumentCompleted, name='set_doc_completed'),
    path('preview/set/<int:pk>', views.SetPreviewCompleted, name='set_preview_completed'),

]



