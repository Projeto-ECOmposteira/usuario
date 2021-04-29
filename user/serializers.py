from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import SuperMarket, Producer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

class SuperMarketSerializer(RegisterSerializer):
    class Meta:
        model = SuperMarket
        fields = ('password', 'password2', 'email', 'first_name', 'last_name',
                  'phone_number', 'owner_phone_number', 'cnpj', 'cep', 
                  'comercial_name', 'agricultural_producer'
                 )
                 
    def create(self, validated_data):
        agricultural_producer = Producer.objects.get(pk=validated_data['agricultural_producer'])
        super_maket = SuperMarket.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number = validated_data['phone_number'],
            owner_phone_number = validated_data['owner_phone_number'],
            cnpj = validated_data['cnpj'],
            cep = validated_data['cep'],
            comercial_name = validated_data['comercial_name'],
            agricultural_producer = agricultural_producer,
        )

        super_maket.set_password(validated_data['password'])
        super_maket.save()

        return super_maket

class ProducerSerializer(RegisterSerializer):
    class Meta:
        model = Producer
        fields = ('password', 'password2', 'email', 'first_name', 'last_name',
                  'phone_number',
                 )

    def create(self, validated_data):

        producer = Producer.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number = validated_data['phone_number'],
        )

        producer.set_password(validated_data['password'])
        producer.save()

        return producer