from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework import generics

from .models import Data
from .serializers import DataSerializer


class DataViewSetCreate(generics.CreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataViewSetGet(generics.RetrieveAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    lookup_field = 'hash_name'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class DataViewSetDel(generics.DestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    lookup_field = 'hash_name'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response
