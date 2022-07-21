import profile
from statistics import mode
from rest_framework import serializers
from accounts.models import User, UserDetail, UserProducts


class UserProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProducts
        fields = ('email', 'product_id', 'product_name', 'store_id',
                  'price', 'store_name', 'accept_status', 'product_rating', 'product_description')


class _UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetail
        exclude = ('id', 'user')
        extra_kwargs = {
            'phone_number': {'required': False}
        }


class UserSerializer(serializers.ModelSerializer):
    profile = _UserProfileSerializer()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'complete_profile', 'profile')
        extra_kwargs = {
            'email': {'required': False}
        }

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile', {})
        UserDetail.objects.update_or_create(user=instance, defaults=profile)
        return super().update(instance, validated_data)
