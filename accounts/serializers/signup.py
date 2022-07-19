
from ..models import StoreDetails, User, UserDetail, NUMERIC_VALIDATOR
from rest_framework import serializers


class SignupSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=15)
    address = serializers.JSONField()
    street_number = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    state = serializers.CharField(max_length=30)
    zip_code = serializers.CharField(
        max_length=5, validators=[NUMERIC_VALIDATOR])

    def validate(self, data):
        error = {}

        if not data['password'] == data['confirm_password']:
            error['confirm_password'] = "Passwords do not match."

        if User.objects.filter(email=data['email']).exists():
            error['email'] = "User with this email exists."

        if error:
            raise serializers.ValidationError(error)

        data.pop('confirm_password')
        return data

    def create(self, validated_data):
        email = validated_data.pop('email')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        password = validated_data.pop('password')

        user = User.objects.create_user(
            email=email, password=password, **{"first_name": first_name, "last_name": last_name})

        UserDetail.objects.create(user=user, **validated_data)
        return user


class StoreSignupSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)
    store_name = serializers.CharField(max_length=50)
    store_id = serializers.IntegerField()
    min_amount = serializers.IntegerField()

    def validate(self, data):
        error = {}

        if not data['password'] == data['confirm_password']:
            error['confirm_password'] = "Passwords do not match."

        if User.objects.filter(email=data['email']).exists():
            error['email'] = "User with this email exists."

        if error:
            raise serializers.ValidationError(error)

        data.pop('confirm_password')
        return data

    def create(self, validated_data):
        email = validated_data.pop('email')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        password = validated_data.pop('password')

        user = User.objects.create_storeuser(
            email=email, password=password, **{"first_name": first_name, "last_name": last_name})
        StoreDetails.objects.create(user=user, **validated_data)
        return user


class PbAdminSignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

    def validate(self, data):
        error = {}

        if not data['password'] == data['confirm_password']:
            error['confirm_password'] = "Passwords do not match."

        if User.objects.filter(email=data['email']).exists():
            error['email'] = "User with this email exists."

        if error:
            raise serializers.ValidationError(error)

        data.pop('confirm_password')
        return data

    def create(self, validated_data):
        email = validated_data.pop('email')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        password = validated_data.pop('password')

        user = User.objects.create_adminuser(
            email=email, password=password, **{"first_name": first_name, "last_name": last_name})
        return user
