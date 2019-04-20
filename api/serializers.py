from rest_framework import serializers
from .models import BucketList


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketList
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified',)
