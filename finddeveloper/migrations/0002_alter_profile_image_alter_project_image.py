# Generated by Django 4.2.5 on 2023-09-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddeveloper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='developer/project/image/pexels-photo-4622893_3ulZXIM.webp', upload_to='developer/profile/image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='developer/project/image/pexels-photo-4622893_3ulZXIM.webp', upload_to='developer/project/image'),
        ),
    ]
