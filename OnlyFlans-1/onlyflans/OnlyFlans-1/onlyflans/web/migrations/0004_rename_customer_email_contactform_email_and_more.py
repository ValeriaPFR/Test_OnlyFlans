# Generated by Django 5.0.6 on 2024-06-06 01:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_contactform_rename_edad_cliente_age_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contactform",
            old_name="customer_email",
            new_name="email",
        ),
        migrations.RenameField(
            model_name="contactform",
            old_name="customer_name",
            new_name="name",
        ),
    ]
