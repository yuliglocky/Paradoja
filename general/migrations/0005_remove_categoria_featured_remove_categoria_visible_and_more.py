# Generated by Django 4.2.4 on 2023-10-18 23:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("general", "0004_alter_categoria_options_categoria_visible_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="categoria",
            name="featured",
        ),
        migrations.RemoveField(
            model_name="categoria",
            name="visible",
        ),
        migrations.AlterField(
            model_name="categoria",
            name="nombre",
            field=models.CharField(max_length=200),
        ),
    ]