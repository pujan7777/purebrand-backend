# Generated by Django 4.0.6 on 2022-08-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_userproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproducts',
            name='customer_service_answer',
            field=models.IntegerField(blank=True),
        ),
    ]
