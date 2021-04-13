from django.urls import path
from user.views import CustomObtainTokenPairView, RegisterView, UserView, \
                       RegisterSuperMarketView, RegisterProducerView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', CustomObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register_market/', RegisterSuperMarketView.as_view(), name='register_market'),
    path('register_producer/', RegisterProducerView.as_view(), name='register_producer'),
    path('', UserView.as_view(), name='auth_register'),
]