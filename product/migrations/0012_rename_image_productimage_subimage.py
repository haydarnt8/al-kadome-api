# Generated by Django 4.2.2 on 2023-07-16 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0011_alter_productimage_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productimage",
            old_name="image",
            new_name="subImage",
        ),
    ]
