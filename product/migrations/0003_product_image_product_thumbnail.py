# Generated by Django 4.2.9 on 2024-01-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
        migrations.AddField(
            model_name="product",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]
