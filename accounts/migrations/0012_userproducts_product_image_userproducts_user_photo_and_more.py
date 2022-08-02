# Generated by Django 4.0.6 on 2022-07-29 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_userdetail_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproducts',
            name='product_image',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='userproducts',
            name='user_photo',
            field=models.FileField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='userproducts',
            name='user_video',
            field=models.FileField(blank=True, null=True, upload_to='product_videos'),
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_one', models.IntegerField()),
                ('quality_two', models.IntegerField()),
                ('customer_service', models.CharField(max_length=30)),
                ('customer_service_answer', models.IntegerField()),
                ('order_one', models.IntegerField()),
                ('order_two', models.IntegerField()),
                ('install_setup', models.IntegerField()),
                ('receive_product', models.CharField(max_length=30)),
                ('arrival_time', models.IntegerField()),
                ('damage_rating', models.IntegerField()),
                ('maintenance', models.FloatField()),
                ('feedback', models.CharField(max_length=30)),
                ('feedback_value', models.CharField(max_length=250)),
                ('userproduct', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.userproducts')),
            ],
        ),
    ]