from rest_framework import serializers
from .models import ConsumerProfile



class ConsumerProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:    
        model = ConsumerProfile
        fields = (
            'id',
            'name', 
            'account'
        )
        read_only_fields = ("account", )