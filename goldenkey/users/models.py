from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
# Create your models here.



#User model for our customers
class CustomUser(AbstractBaseUser, PermissionsMixin):
	firstName = models.CharField(max_length=100,null=True,blank=True)
	lastName = models.CharField(max_length=100,null=True,blank=True)
	email = models.EmailField(_('email address'), unique=True)
	profilePhoto = models.ImageField(upload_to='userprofiles/',blank=True)
	cash = models.IntegerField(default=0)
	date_joined = models.DateTimeField(auto_now_add=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()
	

	def __str__(self):
		return self.email