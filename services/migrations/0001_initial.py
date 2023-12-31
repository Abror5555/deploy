# Generated by Django 4.1.5 on 2023-01-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='services/')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Servis nomi')),
                ('title_uz', models.CharField(blank=True, max_length=300, null=True, verbose_name='Servis nomi')),
                ('title_ru', models.CharField(blank=True, max_length=300, null=True, verbose_name='Servis nomi')),
                ('title_en', models.CharField(blank=True, max_length=300, null=True, verbose_name='Servis nomi')),
                ('body', models.CharField(blank=True, max_length=600, null=True, verbose_name="Servis ma'lumoti")),
                ('body_uz', models.CharField(blank=True, max_length=600, null=True, verbose_name="Servis ma'lumoti")),
                ('body_ru', models.CharField(blank=True, max_length=600, null=True, verbose_name="Servis ma'lumoti")),
                ('body_en', models.CharField(blank=True, max_length=600, null=True, verbose_name="Servis ma'lumoti")),
            ],
        ),
        migrations.CreateModel(
            name='ServicesTitile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Sayt sarlavhasi')),
                ('title_uz', models.CharField(blank=True, max_length=250, null=True, verbose_name='Sayt sarlavhasi')),
                ('title_ru', models.CharField(blank=True, max_length=250, null=True, verbose_name='Sayt sarlavhasi')),
                ('title_en', models.CharField(blank=True, max_length=250, null=True, verbose_name='Sayt sarlavhasi')),
            ],
        ),
    ]
