from .base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models

class Account(BaseModel):
    owner = models.ManyToManyField(User, related_name='accounts')

    class Meta:
        abstract = False

    def __str__(self):
        return self.owner