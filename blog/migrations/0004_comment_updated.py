# Generated by Django 5.1 on 2024-09-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
