from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializerNew(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            'id', 
            'email', 
            'password',
            'name',
            'cpf',
            "address_street",
            "address_number",
            "complement",
            'card_holder_name',
            'card_number',
            'card_expiration',
            'card_type',
            'card_security_code',
            'card_brand'    
        ]

        def create(self, validated_data):
            user = User.objects.create(**validated_data)
            return user