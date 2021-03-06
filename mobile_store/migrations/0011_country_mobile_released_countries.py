# Generated by Django 4.0.4 on 2022-05-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_store', '0010_mobile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='mobile',
            name='released_countries',
            field=models.ManyToManyField(to='mobile_store.country'),
        ),
    ]
