# Generated by Django 4.0.6 on 2022-07-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userproducts_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproducts',
            name='product_description',
            field=models.CharField(default='', max_length=250),
        ),
    ]
