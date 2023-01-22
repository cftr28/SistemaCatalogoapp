
import email
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30, null=True)
    def __str__(self) :
        return str(self.username)