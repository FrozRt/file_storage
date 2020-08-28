from django.urls import path

from . import viewsets

urlpatterns = [
    # path('', snippet_list),
    path('upload/', viewsets.DataViewSetCreate.as_view()),
    path('get/<str:hash_name>', viewsets.DataViewSetGet.as_view()),
    path('delete/<str:hash_name>', viewsets.DataViewSetDel.as_view()),

]
