# Generated by Django 5.0.2 on 2024-04-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_productvariant_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
