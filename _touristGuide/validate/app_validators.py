from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def name_validate(name):
		if name not in ["ayman", "ahmad", "amjad", "waleed"]:
			raise ValidationError(
			_(f'{name}s is not valid, please enter one of these names ["ayman", "ahmad", "amjad", "waleed"]')
			)

def user_directory_path(instance, filename):
		#file will be uploaded to MEDIA_ROOT/user_<id>/filename
		return f'user_{instance.id}/{filename}'