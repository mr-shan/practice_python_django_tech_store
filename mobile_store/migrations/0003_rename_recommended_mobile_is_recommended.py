# Generated by Django 4.0.4 on 2022-05-18 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_store', '0002_mobile_rating_mobile_recommended'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='recommended',
            new_name='is_recommended',
        ),
    ]
