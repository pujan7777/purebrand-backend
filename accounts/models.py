import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from accounts.constants import ACCEPT_STATUS_CHOICE, RATING_STARS
from .managers import UserManager


NUMERIC_VALIDATOR = RegexValidator(r'^[0-9+]', 'Only numeric characters')
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    PUREBRANDS = 1
    STORE = 2
    USERS = 3

    ROLE_CHOICES = (
        (PUREBRANDS, 'Purebrands'),
        (STORE, 'Store'),
        (USERS, 'Host user')
    )
    uid = models.UUIDField(unique=True, editable=False,
                           default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    deleted_at = models.DateTimeField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete_profile = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email


class UserDetail(models.Model):
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(default="", null=True, max_length=250)
    street_number = models.CharField(max_length=30, blank=True, default="")
    city = models.CharField(max_length=30, blank=True, default="")
    state = models.CharField(max_length=30, blank=True, default="")
    zip_code = models.CharField(max_length=5, validators=[
                                NUMERIC_VALIDATOR], blank=True, default="")
    instagram_handle = models.CharField(max_length=30, blank=True, default="")
    twitter_handle = models.CharField(max_length=30, blank=True, default="")
    tiktok_handle = models.CharField(max_length=30, blank=True, default="")
    about_me = models.CharField(max_length=250, blank=True, default="")

    def __str__(self):
        return self.user.email


class StoreDetails(models.Model):

    user = models.OneToOneField(
        User, related_name="store_profile", on_delete=models.CASCADE)
    store_name = models.CharField(max_length=250)
    min_amount = models.IntegerField(blank=False)
    store_id = models.BigIntegerField(blank=False, unique=True)

    def __str__(self):
        return self.store_name


class UserProducts(models.Model):
    email = models.EmailField(max_length=250)
    product_id = models.BigIntegerField(blank=False)
    product_name = models.CharField(blank=False, max_length=250)
    store_id = models.BigIntegerField(blank=False)
    price = models.IntegerField(blank=False)
    store_name = models.CharField(max_length=250)
    accept_status = models.CharField(
        choices=ACCEPT_STATUS_CHOICE, max_length=255, default="PENDING")
    product_description = models.CharField(max_length=250, default="")
    product_rating = models.CharField(
        choices=RATING_STARS, default="ZERO", max_length=250)
    decline_reason = models.CharField(max_length=250, default="None")

    def __str__(self):
        return self.email


# class ProductImage(models.Model):
#     product_id = models.ForeignKey(
#         UserProducts, related_name="product_image", on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="product/")
#     size = models.IntegerField(default=0)

#     class Meta:
#         db_table = 'uploads'
