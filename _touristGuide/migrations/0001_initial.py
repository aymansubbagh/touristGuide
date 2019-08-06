# Generated by Django 2.2.3 on 2019-07-29 06:52

import _touristGuide.validate.app_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25, validators=[_touristGuide.validate.app_validators.name_validate])),
                ('user_email', models.EmailField(max_length=30, validators=[django.core.validators.EmailValidator])),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
