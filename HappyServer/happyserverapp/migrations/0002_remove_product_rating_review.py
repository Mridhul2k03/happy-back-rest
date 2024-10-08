# Generated by Django 5.0.7 on 2024-08-06 08:37

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyserverapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('review', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='happyserverapp.product')),
            ],
        ),
    ]
