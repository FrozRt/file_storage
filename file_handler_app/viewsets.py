from rest_framework import generics
from rest_framework.response import Response

from .models import Data
from .serializers import DataSerializer


class DataViewSetCreate(generics.CreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataViewSetGet(generics.RetrieveAPIView):
    """
    Overriding RetrieveAPIView for getting all db entries with the same hash
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    lookup_field = 'file_hash'

    def get_queryset(self):
        if 'file_hash' in self.kwargs:
            return Data.objects.filter(file_hash=self.kwargs['file_hash'])
        else:
            return Data.objects.all()

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)


class DataViewSetDel(generics.DestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    lookup_field = 'file_hash'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response
