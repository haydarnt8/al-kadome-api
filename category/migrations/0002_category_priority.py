# Generated by Django 4.2.2 on 2023-07-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="priority",
            field=models.IntegerField(default=10),
        ),
    ]