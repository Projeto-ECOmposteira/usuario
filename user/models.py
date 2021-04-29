from django.contrib.auth.models import User
from django.db import models

class Producer(User):
    phone_number = models.CharField(max_length=16, blank=False)

class SuperMarket(User):
    agricultural_producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16, blank=False)
    owner_phone_number = models.CharField(max_length=16, blank=False)
    cnpj = models.CharField(max_length=18, blank=False)
    cep = models.CharField(max_length=9, blank=False)
    comercial_name = models.CharField(max_length=255, blank=False)