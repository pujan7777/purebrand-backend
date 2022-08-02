# Generated by Django 4.0.6 on 2022-08-01 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_userproducts_userrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userproducts',
            name='user_photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userproducts',
            name='user_video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
