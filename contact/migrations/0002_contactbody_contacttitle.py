# Generated by Django 4.1.5 on 2023-01-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Have You Any Questions ?', max_length=255, null=True, verbose_name="Saytni so'rovnomasi")),
                ('title_uz', models.CharField(blank=True, default='Have You Any Questions ?', max_length=255, null=True, verbose_name="Saytni so'rovnomasi")),
                ('title_ru', models.CharField(blank=True, default='Have You Any Questions ?', max_length=255, null=True, verbose_name="Saytni so'rovnomasi")),
                ('title_en', models.CharField(blank=True, default='Have You Any Questions ?', max_length=255, null=True, verbose_name="Saytni so'rovnomasi")),
                ('body', models.CharField(blank=True, default="I'M AT YOUR SERVICES", max_length=255, null=True, verbose_name="So'rovnoma haqida")),
                ('body_uz', models.CharField(blank=True, default="I'M AT YOUR SERVICES", max_length=255, null=True, verbose_name="So'rovnoma haqida")),
                ('body_ru', models.CharField(blank=True, default="I'M AT YOUR SERVICES", max_length=255, null=True, verbose_name="So'rovnoma haqida")),
                ('body_en', models.CharField(blank=True, default="I'M AT YOUR SERVICES", max_length=255, null=True, verbose_name="So'rovnoma haqida")),
                ('phone', models.CharField(blank=True, default='Call Us On', max_length=255, null=True, verbose_name='Telefon sarlavhasi')),
                ('phone_uz', models.CharField(blank=True, default='Call Us On', max_length=255, null=True, verbose_name='Telefon sarlavhasi')),
                ('phone_ru', models.CharField(blank=True, default='Call Us On', max_length=255, null=True, verbose_name='Telefon sarlavhasi')),
                ('phone_en', models.CharField(blank=True, default='Call Us On', max_length=255, null=True, verbose_name='Telefon sarlavhasi')),
                ('number', models.CharField(blank=True, default='+998 93 1410111', max_length=255, null=True, verbose_name='Telefon raqam')),
                ('number_link', models.CharField(blank=True, default='tel:+998931410111', max_length=500, null=True, verbose_name='Telefon link')),
                ('office', models.CharField(blank=True, default='Office', max_length=255, null=True, verbose_name='Office sarlavhasi')),
                ('office_uz', models.CharField(blank=True, default='Office', max_length=255, null=True, verbose_name='Office sarlavhasi')),
                ('office_ru', models.CharField(blank=True, default='Office', max_length=255, null=True, verbose_name='Office sarlavhasi')),
                ('office_en', models.CharField(blank=True, default='Office', max_length=255, null=True, verbose_name='Office sarlavhasi')),
                ('location', models.CharField(blank=True, default='Bukhara City, Bukhara Province, Republic of Uzbekistan', max_length=255, null=True, verbose_name='Office joylashuvi')),
                ('location_uz', models.CharField(blank=True, default='Bukhara City, Bukhara Province, Republic of Uzbekistan', max_length=255, null=True, verbose_name='Office joylashuvi')),
                ('location_ru', models.CharField(blank=True, default='Bukhara City, Bukhara Province, Republic of Uzbekistan', max_length=255, null=True, verbose_name='Office joylashuvi')),
                ('location_en', models.CharField(blank=True, default='Bukhara City, Bukhara Province, Republic of Uzbekistan', max_length=255, null=True, verbose_name='Office joylashuvi')),
                ('office_link', models.CharField(blank=True, default='https://www.google.com/maps/place/Jondor+tuman+hokimligi/@39.7441366,64.1652202,2620m/data=!3m1!1e3!4m13!1m7!3m6!1s0x3f5aa5137d7b2901:0x2e75b5ab9ac3005!2z0JbQvtC90LTQvtGALCDQo9C30LHQtdC60LjRgdGC0LDQvQ!3b1!8m2!3d39.7425904!4d64.1744425!3m4!1s0x3f5aa5a361852f17:0x242aec5674b2621a!8m2!3d39.7399073!4d64.1864513', max_length=5000, null=True, verbose_name='location link')),
                ('Email', models.CharField(blank=True, default='Email', max_length=255, null=True, verbose_name='Email adress')),
                ('Email_uz', models.CharField(blank=True, default='Email', max_length=255, null=True, verbose_name='Email adress')),
                ('Email_ru', models.CharField(blank=True, default='Email', max_length=255, null=True, verbose_name='Email adress')),
                ('Email_en', models.CharField(blank=True, default='Email', max_length=255, null=True, verbose_name='Email adress')),
                ('Email_address', models.CharField(blank=True, default='abrorkushshiyev@gmail.com', max_length=255, null=True, verbose_name='Email silkasi')),
                ('email_link', models.CharField(blank=True, default='mailto:abrorkushshiyev@gmail.com', max_length=500, null=True, verbose_name='Email link')),
                ('website', models.CharField(blank=True, default='Website', max_length=255, null=True, verbose_name='Website')),
                ('website_uz', models.CharField(blank=True, default='Website', max_length=255, null=True, verbose_name='Website')),
                ('website_ru', models.CharField(blank=True, default='Website', max_length=255, null=True, verbose_name='Website')),
                ('website_en', models.CharField(blank=True, default='Website', max_length=255, null=True, verbose_name='Website')),
                ('website_address', models.CharField(blank=True, default='abrorbek.com', max_length=255, null=True, verbose_name='Wesite silkasi')),
                ('website_link', models.CharField(blank=True, default='abrorbek.com', max_length=255, null=True, verbose_name='Wesite link')),
                ('send_email', models.CharField(blank=True, default='SEND ME EMAIL', max_length=300, null=True, verbose_name="Xabar yuborish bo'limi")),
                ('send_email_uz', models.CharField(blank=True, default='SEND ME EMAIL', max_length=300, null=True, verbose_name="Xabar yuborish bo'limi")),
                ('send_email_ru', models.CharField(blank=True, default='SEND ME EMAIL', max_length=300, null=True, verbose_name="Xabar yuborish bo'limi")),
                ('send_email_en', models.CharField(blank=True, default='SEND ME EMAIL', max_length=300, null=True, verbose_name="Xabar yuborish bo'limi")),
                ('message', models.CharField(blank=True, default="I'M VERY RESPOSIVE TO MESSAGES", max_length=300, null=True, verbose_name='Email yuborish izohi')),
                ('message_uz', models.CharField(blank=True, default="I'M VERY RESPOSIVE TO MESSAGES", max_length=300, null=True, verbose_name='Email yuborish izohi')),
                ('message_ru', models.CharField(blank=True, default="I'M VERY RESPOSIVE TO MESSAGES", max_length=300, null=True, verbose_name='Email yuborish izohi')),
                ('message_en', models.CharField(blank=True, default="I'M VERY RESPOSIVE TO MESSAGES", max_length=300, null=True, verbose_name='Email yuborish izohi')),
                ('name', models.CharField(blank=True, default='Name', max_length=200, null=True, verbose_name='Input shaxs nomi nomi')),
                ('name_uz', models.CharField(blank=True, default='Name', max_length=200, null=True, verbose_name='Input shaxs nomi nomi')),
                ('name_ru', models.CharField(blank=True, default='Name', max_length=200, null=True, verbose_name='Input shaxs nomi nomi')),
                ('name_en', models.CharField(blank=True, default='Name', max_length=200, null=True, verbose_name='Input shaxs nomi nomi')),
                ('email_send', models.CharField(blank=True, default='Email', max_length=200, null=True, verbose_name='Input email nomi')),
                ('email_send_uz', models.CharField(blank=True, default='Email', max_length=200, null=True, verbose_name='Input email nomi')),
                ('email_send_ru', models.CharField(blank=True, default='Email', max_length=200, null=True, verbose_name='Input email nomi')),
                ('email_send_en', models.CharField(blank=True, default='Email', max_length=200, null=True, verbose_name='Input email nomi')),
                ('subject', models.CharField(blank=True, default='Subject', max_length=200, null=True, verbose_name='Input subject nomi')),
                ('subject_uz', models.CharField(blank=True, default='Subject', max_length=200, null=True, verbose_name='Input subject nomi')),
                ('subject_ru', models.CharField(blank=True, default='Subject', max_length=200, null=True, verbose_name='Input subject nomi')),
                ('subject_en', models.CharField(blank=True, default='Subject', max_length=200, null=True, verbose_name='Input subject nomi')),
                ('message_send', models.CharField(blank=True, default='Message', max_length=200, null=True, verbose_name='Input message nomi')),
                ('message_send_uz', models.CharField(blank=True, default='Message', max_length=200, null=True, verbose_name='Input message nomi')),
                ('message_send_ru', models.CharField(blank=True, default='Message', max_length=200, null=True, verbose_name='Input message nomi')),
                ('message_send_en', models.CharField(blank=True, default='Message', max_length=200, null=True, verbose_name='Input message nomi')),
                ('send_message', models.CharField(blank=True, default='Send Message', max_length=200, null=True, verbose_name='Input Send Message nomi')),
                ('send_message_uz', models.CharField(blank=True, default='Send Message', max_length=200, null=True, verbose_name='Input Send Message nomi')),
                ('send_message_ru', models.CharField(blank=True, default='Send Message', max_length=200, null=True, verbose_name='Input Send Message nomi')),
                ('send_message_en', models.CharField(blank=True, default='Send Message', max_length=200, null=True, verbose_name='Input Send Message nomi')),
            ],
        ),
        migrations.CreateModel(
            name='ContactTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Contatc Me', max_length=255, null=True, verbose_name='Sayt sarlavhasi')),
                ('title_uz', models.CharField(blank=True, default='Contatc Me', max_length=255, null=True, verbose_name='Sayt sarlavhasi')),
                ('title_ru', models.CharField(blank=True, default='Contatc Me', max_length=255, null=True, verbose_name='Sayt sarlavhasi')),
                ('title_en', models.CharField(blank=True, default='Contatc Me', max_length=255, null=True, verbose_name='Sayt sarlavhasi')),
            ],
        ),
    ]
