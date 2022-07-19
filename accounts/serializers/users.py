from statistics import mode
from rest_framework import serializers
from accounts.models import UserProducts


class UserProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProducts
        fields = ('email', 'product_id', 'product_name', 'store_id',
                  'price', 'store_name', 'accept_status', 'product_rating', 'product_description')
