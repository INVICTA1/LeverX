# Generated by Django 3.2.3 on 2021-05-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210529_0459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.TextField()),
                ('status', models.BooleanField(default=0)),
                ('evaluation', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
            ],
        ),
        migrations.AlterField(
            model_name='lecture',
            name='file',
            field=models.CharField(max_length=255),
        ),
    ]
