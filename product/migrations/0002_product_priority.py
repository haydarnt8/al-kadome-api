# Generated by Django 4.2.3 on 2023-07-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="priority",
            field=models.IntegerField(default=0),
        ),
    ]