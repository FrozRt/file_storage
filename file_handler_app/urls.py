from django.urls import path

from . import viewsets

urlpatterns = [
    path('upload/', viewsets.DataViewSetCreate.as_view()),
    path('get/<str:file_hash>', viewsets.DataViewSetGet.as_view()),
    path('delete/<str:file_hash>', viewsets.DataViewSetDel.as_view()),

]
