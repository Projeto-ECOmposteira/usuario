from django.contrib.auth.models import User
from django.db import models

class SuperMarket(User):
    # parent = models.OneToOneField(User, on_delete=models.CASCADE,
    #                        related_name='super_market', primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True)
    owner_phone_number = models.CharField(max_length=15, blank=True)
    cnpj = models.CharField(max_length=14, blank=False)
    cep = models.CharField(max_length=9, blank=False)
    comercial_name = models.CharField(max_length=255, blank=False)

class Producer(User):
    # parent = models.OneToOneField(User, on_delete=models.CASCADE,
    #                        related_name='producer', primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True)