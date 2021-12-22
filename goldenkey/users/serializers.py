from rest_framework import serializers

from storeapp.models import Basket
from .models import CustomUser
from rest_auth.registration.serializers import RegisterSerializer

#Serializer for CustomUser Model

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ['id', 'cash','firstName','lastName','email','profilePhoto']



#Register Serializer for registering our users

class MyCustomUserRegistrationSerializer(RegisterSerializer):
	firstName = serializers.CharField(required = False)
	lastName = serializers.CharField(required = False)
	email = serializers.EmailField()
	profilePhoto = serializers.ImageField(required = False)

	def get_cleaned_data(self):
		super(MyCustomUserRegistrationSerializer, self).get_cleaned_data()
		return {
			'password1': self.validated_data.get('password1', ''),
			'password2': self.validated_data.get('password2', ''),
			'email': self.validated_data.get('email', ''),
			'firstName': self.validated_data.get('firstName', ''),
			'lastName': self.validated_data.get('lastName', ''),
			'profilePhoto' : self.validated_data.get('profilePhoto',''),
		}

	def save(self, request):
		user = super().save(request)
		user.firstName = self.data.get('firstName')
		user.lastName = self.data.get('lastName')
		user.email = self.data.get('email')
		user.profilePhoto = self.data.get('profilePhoto')
		user.save()
		Basket.objects.get_or_create(user = user)
		return user