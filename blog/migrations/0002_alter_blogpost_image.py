# Generated by Django 4.1.6 on 2024-09-22 21:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Recommended resolution: 1040px * 585px",
                null=True,
                upload_to="blog-posts/",
                verbose_name="Image",
            ),
        ),
    ]
