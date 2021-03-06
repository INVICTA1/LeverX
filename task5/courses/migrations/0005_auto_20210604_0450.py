# Generated by Django 3.2.3 on 2021-06-04 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_homework_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='solution',
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField()),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework', to='courses.homework')),
            ],
        ),
    ]
