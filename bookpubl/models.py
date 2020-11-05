from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Book(models.Model):
    name = models.CharField(verbose_name='Name:', db_index=True, unique=True, max_length=64)
    page = models.CharField(verbose_name='Number of pages:', max_length=64)
    GEN_TYPES = (
        (1, 'Adventures'),
        (2, 'Romance'),
        (3, 'Detective'),
        (4, 'Horror'),
    )
    
    gen = models.IntegerField(verbose_name='Genre:', choices=GEN_TYPES)

    user = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
