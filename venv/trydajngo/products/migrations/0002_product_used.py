# Generated by Django 5.1.1 on 2024-10-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='used',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
