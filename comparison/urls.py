from django.urls import path
from . import views

urlpatterns = [
    path('SouqCompare/<int:pk>',
         views.SouqComparePage.as_view(), name='souq-compare'),
    path('residentDocument/add', views.AddResidentDocument.as_view(),
         name='add-residentDocument'),
    path('residentDocument/update/<int:pk>',
         views.UpdateResidentDocument.as_view(), name='update-residentDocument'),
    path('compareDocument/add', views.AddCompareBuilding.as_view(),
         name='add-compareDocument'),
    path('compareDocument/update/<int:pk>',
         views.UpdateCompareBuilding.as_view(), name='update-compareDocument'),
    path('residentBuilding/add', views.AddResidentBuilding.as_view(),
         name='add-residentBuilding'),
    path('residentBuilding/update/<int:pk>',
         views.UpdateResidentBuilding.as_view(), name='update-residentBuilding'),
]
