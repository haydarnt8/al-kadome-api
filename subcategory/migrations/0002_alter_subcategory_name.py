# Generated by Django 4.2.2 on 2023-07-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subcategory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subcategory",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]
