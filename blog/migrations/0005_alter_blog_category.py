# Generated by Django 4.2.3 on 2023-11-14 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_blogcategory_blog_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.blogcategory"
            ),
        ),
    ]
