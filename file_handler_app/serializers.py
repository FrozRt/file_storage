from rest_framework import serializers
from .models import Data


class DataSerializer(serializers.ModelSerializer):

    since_added = serializers.SerializerMethodField()

    class Meta:
        model = Data
        fields = ('file', 'hash_name', 'since_added')

    def get_since_added(self, obj):
        date_added = obj.created_at
        return date_added
