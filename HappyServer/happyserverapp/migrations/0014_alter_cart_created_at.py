# Generated by Django 5.0.7 on 2024-08-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyserverapp', '0013_alter_cart_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
