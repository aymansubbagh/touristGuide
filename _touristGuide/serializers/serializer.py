from rest_framework import serializers
from _touristGuide.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'user_name', 'user_email', 'user_image')