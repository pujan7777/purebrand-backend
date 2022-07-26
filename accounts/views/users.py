from rest_framework import views, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from accounts.models import UserProducts
from accounts.serializers.users import UserProductSerializer, UserSerializer, UserUpdateSerializer
from accounts.utils import GetRatings


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


class StoreUserView(generics.ListAPIView):
    user_product = UserProducts.objects.all()
    serializer_class = UserProductSerializer(user_product, many=True)
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        queryparam = self.request.query_params.get('store_id')
        custom_product = UserProducts.objects.filter(store_id=queryparam).all()
        serializer_new = UserProductSerializer(custom_product, many=True)
        return Response(serializer_new.data)


class UserProfileView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)


class UserProfileUpdateView(generics.ListAPIView):
    serializer_class = UserUpdateSerializer
    view_serializer = UserSerializer
    permission_classes = [IsAuthenticated, ]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(request.user, data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(self.view_serializer(request.user).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingView(generics.ListAPIView):

    def post(self, request):
        rating = GetRatings(request.data)
        return Response(rating)
