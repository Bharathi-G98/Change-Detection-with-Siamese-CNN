# Generated by Django 3.0.6 on 2020-05-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changedetection', '0009_remove_image_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pdf',
            field=models.FileField(upload_to='media/video/'),
        ),
    ]
