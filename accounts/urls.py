
from django.urls import path, re_path

from accounts.views.login import LoginView, LogoutView, RefreshTokenView
from accounts.views.signup import SignupView, StoreSignupView, PbAdminSignupView
from accounts.views.users import UserProductView, UserProfileView

urlpatterns = [
    path('auth/login', LoginView.as_view(), name="login"),
    path('auth/logout', LogoutView.as_view(), name="logout"),
    path('auth/refresh', RefreshTokenView.as_view(), name="refresh-token"),
    path('auth/signup', SignupView.as_view(), name="signup-user"),
    path('auth/storesignup', StoreSignupView.as_view(), name="store-signup"),
    path('auth/adminsignup', PbAdminSignupView.as_view(), name="admin-signup"),
    path('auth/userproducts', UserProductView.as_view(), name="product-view"),
    path('auth/userprofile', UserProfileView.as_view(), name="user-profile"),
]
