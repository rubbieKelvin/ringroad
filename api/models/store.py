from django.db import models
from .user import User
from shared.abstractmodel import AbstractModel, serialization
from shared.abstractmodel.serialization import SerializationStructure, struct

class Store(AbstractModel):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    @property
    def serializers(self) -> SerializationStructure:
        return struct('id', 'date_created', 'name', 'description',owner=struct('id'),)
    
    def __str__(self):
        return self.name
