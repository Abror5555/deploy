# Generated by Django 4.1.5 on 2023-01-25 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactbody_contacttitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactbody',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contactbody',
            old_name='Email_en',
            new_name='email_en',
        ),
        migrations.RenameField(
            model_name='contactbody',
            old_name='Email_ru',
            new_name='email_ru',
        ),
        migrations.RenameField(
            model_name='contactbody',
            old_name='Email_uz',
            new_name='email_uz',
        ),
    ]