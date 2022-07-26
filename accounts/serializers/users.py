
from email.policy import default
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
        fields = ('email', 'first_name', 'last_name', 'profile')
        extra_kwargs = {
            'email': {'required': False}
        }


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetail
        fields = ('profile_picture', 'complete_profile', 'tiktok_handle',
                  'twitter_handle', 'about_me', 'instagram_handle')

    def update(self, instance, validated_data):
        instagram_handle = validated_data.pop('instagram_handle')
        twitter_handle = validated_data.pop('twitter_handle')
        tiktok_handle = validated_data.pop('tiktok_handle')
        about_me = validated_data.pop('about_me')
        complete_profile = validated_data.pop("complete_profile")
        profile_picture = validated_data.pop("profile_picture")
        userdata = UserDetail.objects.update_or_create(user=instance, defaults={
            "tiktok_handle": tiktok_handle,
            "twitter_handle": twitter_handle,
            "instagram_handle": instagram_handle,
            "about_me": about_me,
            "complete_profile": complete_profile,
            "profile_picture": profile_picture
        })
        return userdata
