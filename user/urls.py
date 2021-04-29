from django.urls import path, include
from user.views import CustomObtainTokenPairView, RegisterView, UserView, \
                       RegisterSuperMarketView, RegisterProducerView, \
                       ProducerViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'producers', ProducerViewSet, basename='producer')

urlpatterns = [
    path('login/', CustomObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register_market/', RegisterSuperMarketView.as_view(), name='register_market'),
    path('register_producer/', RegisterProducerView.as_view(), name='register_producer'),
    path('', UserView.as_view(), name='auth_register'),
    path('', include(router.urls)),
]