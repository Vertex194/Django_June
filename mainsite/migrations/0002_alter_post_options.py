# Generated by Django 4.2.11 on 2024-07-13 05:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainsite", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-slug"]},
        ),
    ]
