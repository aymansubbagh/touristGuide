# Generated by Django 2.2.3 on 2019-07-29 06:57

import _touristGuide.validate.app_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_touristGuide', '0002_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='', upload_to=_touristGuide.validate.app_validators.user_directory_path),
        ),
    ]
