from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer, \
                         SuperMarketSerializer, ProducerSerializer

from .models import SuperMarket


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'status': 'User is corretly authenticated'}
        return Response(content)

class CustomObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request):
        response = super().post(request)
        user = User.objects.get(username=request.data['username'])
        isSupermarket = SuperMarket.objects.filter(username=request.data['username']).count()
        response.data['user'] = {
            'name': user.first_name + ' ' + user.last_name,
            'email': user.username,
            'isSupermarket': True if isSupermarket == 1 else False
        }
        return response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class RegisterSuperMarketView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SuperMarketSerializer

class RegisterProducerView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProducerSerializer