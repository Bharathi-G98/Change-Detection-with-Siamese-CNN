# Generated by Django 3.0.6 on 2020-05-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changedetection', '0011_auto_20200510_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pc',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='video2',
            field=models.FileField(upload_to='media/video/'),
        ),
    ]
