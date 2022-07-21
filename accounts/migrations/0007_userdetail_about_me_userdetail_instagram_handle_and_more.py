# Generated by Django 4.0.6 on 2022-07-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_complete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='about_me',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='instagram_handle',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='tiktok_handle',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='twitter_handle',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]