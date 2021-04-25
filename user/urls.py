from django.urls import path
from user.views import CustomObtainTokenPairView, RegisterView, UserView, \
                       RegisterSuperMarketView, RegisterProducerView
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', CustomObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register_market/', RegisterSuperMarketView.as_view(), name='register_market'),
    path('register_producer/', RegisterProducerView.as_view(), name='register_producer'),

    path('password_recovery/', PasswordResetView.as_view(), name='password_reset'),
    path('password_recovery/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_recovery/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_recovery/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', UserView.as_view(), name='auth_register'),
]