# Generated by Django 3.1.2 on 2020-10-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_tag_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]