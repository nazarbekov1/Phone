# Generated by Django 4.1 on 2022-08-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0003_remove_phone_image_phoneimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
