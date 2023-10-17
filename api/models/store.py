from django.db import models
from .user import User
from shared.abstractmodel import AbstractModel

class Store(AbstractModel):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=50)
    
