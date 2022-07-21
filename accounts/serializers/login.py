from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


# class LoginTokenSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         return super().validate(attrs)


class LoginTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(LoginTokenSerializer, self).validate(attrs)
        data.update({'role': self.user.role})
        data.update({"first_name": self.user.first_name})
        data.update({"last_name": self.user.last_name})
        data.update({"email": self.user.email})
        data.update({"uid": self.user.uid})
        data.update({"complete_profile": self.user.complete_profile})

        return data


class RefreshTokenSerializer(TokenRefreshSerializer):
    def save(self):
        refresh = self.context['request'].data.get('refresh', '')
        RefreshToken(refresh)
