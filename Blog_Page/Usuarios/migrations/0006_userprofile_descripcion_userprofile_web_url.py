# Generated by Django 4.2.5 on 2023-10-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Usuarios", "0005_alter_userprofile_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="descripcion",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="web_url",
            field=models.URLField(
                blank=True, null=True, verbose_name="URL del Sitio Web"
            ),
        ),
    ]
