# Generated by Django 4.1.5 on 2023-01-23 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learningmodel',
            name='skill_en',
        ),
        migrations.RemoveField(
            model_name='learningmodel',
            name='skill_ru',
        ),
        migrations.RemoveField(
            model_name='learningmodel',
            name='skill_uz',
        ),
        migrations.RemoveField(
            model_name='learningmodel',
            name='witdh_en',
        ),
        migrations.RemoveField(
            model_name='learningmodel',
            name='witdh_ru',
        ),
        migrations.RemoveField(
            model_name='learningmodel',
            name='witdh_uz',
        ),
    ]
