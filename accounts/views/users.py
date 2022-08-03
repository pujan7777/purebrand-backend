from rest_framework import views, generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from accounts.models import UserProducts
from accounts.serializers.users import StoreReviewSerializer, UserProductSerializer, UserReviewRequest, UserSerializer, \
    UserUpdateSerializer
from accounts.utils import GetRatings


class UserProductView(generics.ListAPIView):
    user_product = UserProducts.objects.all()
    serializer_class = UserProductSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        queryparam = self.request.query_params.get('email')
        custom_product = UserProducts.objects.filter(email=queryparam)
        serializer = self.serializer_class(custom_product, many=True)
        return Response(serializer.data)

    # will be removed after another view is completed
    def post(self, request, *args, **kwargs):
        serializer = UserProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        email_param = self.request.query_params.get('email')
        product_param = self.request.query_params.get('product_id')
        store_param = self.request.query_params.get('store_id')
        delete_item = UserProducts.objects.get(email=email_param, product_id=product_param, store_id=store_param)
        delete_item.delete()
        return Response("Delete Successful", status=status.HTTP_200_OK)


class StoreUserView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = StoreReviewSerializer

    def get(self, *args, **kwargs):
        queryparam = self.request.query_params.get('store_id')
        custom_product = UserProducts.objects.filter(store_id=queryparam)
        serializer = self.serializer_class(custom_product, many=True)
        return Response(serializer.data)


class UserProfileView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)


class UserProfileUpdateView(APIView):
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
    serializer_class = None

    def post(self, request):
        rating = GetRatings(request.data)
        return Response(rating)


class ReviewRequestView(APIView):
    serializer_class = UserReviewRequest
    permission_classes = [IsAuthenticated, ]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
