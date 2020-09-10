from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from user_profiles.models import ConsumerProfile
from user_profiles.serializers import ConsumerProfileSerializer
User = get_user_model()
from djoser.conf import settings

class UserCreatePasswordRetypeSerializer(UserCreateSerializer):
    default_error_messages = {
        "password_mismatch": settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR
    }
    # basically is getting the properties of the super class (fields), then adding re_password
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["re_password"] = serializers.CharField(
            style={"input_type": "password"}
        )
        self.fields["consumer_profile_serializer"] = ConsumerProfileSerializer()

    def validate(self, attrs):
        self.fields.pop("consumer_profile_serializer", None)
        self.fields.pop("re_password", None)
        re_password = attrs.pop("re_password")
        consumer_profile_serializer = attrs.pop("consumer_profile_serializer")
        print("\n\n\n\n\n\n",consumer_profile_serializer)
        if attrs["password"] == re_password:
            consumer_profile = ConsumerProfile(name=consumer_profile_serializer["name"])
            print("\n\n\n\n\n\n",consumer_profile.name)
            attrs["consumer_profile"] = consumer_profile
            print("\n\n\n\n\n\n",attrs["consumer_profile"].name)
            attrs = super().validate(attrs)
            return attrs
        else:
            self.fail("password_mismatch")


class UserCreateSerializerNew(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        model = User
        fields = [
            'id', 
            'email', 
            'password',
        
            ## personal_info
            # 'name',
            # 'cpf',
            # "address_street",
            # "address_number",
            # "complement",
            ## cardholder_data
            # 'card_holder_name',
            # 'card_number',
            # 'card_expiration',
            # 'card_type',
            # 'card_security_code',
            # 'card_brand'    
        ]

    def create(self, validated_data):
        print("\n\n\n\n\n\n\n{}\n\n\n\n\n\n\n\n\n\n".format(validated_data))
        consumer_profile = validated_data.pop("consumer_profile")

        user = User.objects.create(**validated_data)
        consumer_profile.account = user
        ConsumerProfile.objects.create(name=consumer_profile.name, account=consumer_profile.account)
        return user