# Generated by Django 5.0.1 on 2024-03-26 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productmodel_remove_productimage_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
