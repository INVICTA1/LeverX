# Generated by Django 3.2.3 on 2021-06-04 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_comment_homework'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='homework',
            new_name='solution',
        ),
    ]
