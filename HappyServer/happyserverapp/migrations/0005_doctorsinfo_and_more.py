# Generated by Django 5.0.7 on 2024-08-06 09:43

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyserverapp', '0004_rename_short_description_product_incredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='doctor_image')),
                ('qualification', models.CharField(max_length=150)),
                ('experience', models.IntegerField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='full_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='incredients',
            new_name='ingredients',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
