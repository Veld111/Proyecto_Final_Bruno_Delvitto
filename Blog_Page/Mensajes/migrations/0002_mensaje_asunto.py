# Generated by Django 4.2.5 on 2023-10-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Mensajes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mensaje",
            name="asunto",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
