# Generated by Django 4.2.3 on 2023-11-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(upload_to="photos/blog"),
        ),
    ]
