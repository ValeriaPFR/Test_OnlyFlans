# Generated by Django 5.0.6 on 2024-06-04 17:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="flan",
            old_name="descripcion",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="flan",
            old_name="ingredientes",
            new_name="ingredients",
        ),
        migrations.RenameField(
            model_name="flan",
            old_name="nombre",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="flan",
            old_name="preparacion",
            new_name="preparation",
        ),
        migrations.AddField(
            model_name="flan",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="flan",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="flan",
            name="img_url",
            field=models.URLField(),
        ),
    ]
