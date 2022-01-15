from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User


# Create your models here.

class Gmail(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
            verbose_name = 'Gmail'
            verbose_name_plural = 'Gmail'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('myapp:emails')



    
