from rest_framework import views, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import UserProducts
from accounts.serializers.users import UserProductSerializer


class UserProductView(generics.ListAPIView):
    user_product = UserProducts.objects.all()
    serializer_class = UserProductSerializer(user_product, many=True)
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        queryparam = self.request.query_params.get('email')
        custom_product = UserProducts.objects.filter(email=queryparam).all()
        serializer_new = UserProductSerializer(custom_product, many=True)
        return Response(serializer_new.data)

    def post(self, request, *args, **kwargs):
        serializer = UserProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
