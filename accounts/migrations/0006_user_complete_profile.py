# Generated by Django 4.0.6 on 2022-07-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userdetail_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='complete_profile',
            field=models.BooleanField(default=False),
        ),
    ]