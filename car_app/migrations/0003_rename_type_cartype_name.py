# Generated by Django 4.0.5 on 2022-06-18 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("car_app", "0002_alter_cartype_brand_alter_ordercar_color_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartype",
            old_name="type",
            new_name="name",
        ),
    ]
