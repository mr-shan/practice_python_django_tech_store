# Generated by Django 4.0.4 on 2022-05-18 03:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='mobile',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]
