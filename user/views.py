from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer, \
                         SuperMarketSerializer, ProducerSerializer

from .models import SuperMarket, Producer
from rest_framework.decorators import api_view
import jwt
from django.conf import settings
import json
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)

class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token = request.headers['Authorization'].replace('Bearer ', '')
        user_data = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        content = {'status': 'User is corretly authenticated', **user_data}
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
            'pk': user.pk,
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

class ProducerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Producer.objects.all()
        serializer = ProducerSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Producer.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProducerSerializer(user)
        return Response(serializer.data)

class SuperMarketViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = SuperMarket.objects.all()
        serializer = SuperMarketSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = SuperMarket.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SuperMarketSerializer(user)
        data=serializer.data
        agricultural_producer = Producer.objects.get(pk=data['agricultural_producer'])
        data['agricultural_producer'] = ProducerSerializer(agricultural_producer).data
        return Response(data)

@api_view(["GET"])
def get_producer_supermarket(request):
    try:
        user_id = get_user_id_by_token(request.headers['Authorization'].replace('Bearer ', ''))
        try:
            supermarket = SuperMarket.objects.get(id = user_id)
            response_data = [SuperMarketSerializer(supermarket).data]
        except:
            response_data = SuperMarketSerializer(SuperMarket.objects.filter(agricultural_producer = user_id), many=True).data
        return Response(
            response_data,
            status=HTTP_200_OK
        )
    except:
        return Response(
            status=HTTP_400_BAD_REQUEST
        )

@api_view(["GET"])
def get_user_pk(request):
    try:
        user_id = get_user_id_by_token(request.headers['Authorization'].replace('Bearer ', ''))
        data = {
            'pk': user_id
        }
        return Response(
            user_id,
            status=HTTP_200_OK
        )
    except:
        return Response(
            status=HTTP_400_BAD_REQUEST
        )

def get_user_id_by_token(token):
    return jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])['user_id']