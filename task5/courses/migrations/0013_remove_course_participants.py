# Generated by Django 3.2.3 on 2021-05-30 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20210530_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='participants',
        ),
    ]
