from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Profile(models.Model):
	user = models.CharField(settings.AUTH_USER_MODEL,null=True,max_length=15)
	first_name =models.CharField(max_length=15,default='user')
	last_name =models.CharField(max_length=15,default='user')
	email_id = models.EmailField(max_length=254)
	branch   = models.CharField(max_length=4)
	year     = models.PositiveSmallIntegerField()

	class Meta:
		verbose_name = ('Profile')
		verbose_name_plural = ('Profiles')
