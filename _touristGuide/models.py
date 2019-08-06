from django.db import models
from django.core.validators import EmailValidator
from .validate.app_validators import name_validate, user_directory_path

# Create your models here.
class User(models.Model):
	class Meta:
		db_table = 'users'
	user_name = models.CharField(max_length=25, validators=[name_validate])
	user_email = models.EmailField(max_length=30, validators=[EmailValidator])
	user_image = models.ImageField(upload_to = user_directory_path, default="")
	
	
	