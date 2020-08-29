from rest_framework import serializers
from .models import Data


class DataSerializer(serializers.ModelSerializer):

    uploaded_at = serializers.SerializerMethodField()

    class Meta:
        model = Data
        fields = ('file', 'uploaded_at', 'file_hash',)

    def get_uploaded_at(self, obj):
        date_added = obj.created_at
        return date_added
