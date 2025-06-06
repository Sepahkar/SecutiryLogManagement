# Generated by Django 5.0.12 on 2025-04-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfigurationChangeRequest', '0025_configurationchangerequest_requestcorp_request_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurationchangerequest',
            name='changing_date_actual',
            field=models.CharField(help_text='تاریخ واقعی تغییرات به شمسی.', max_length=10, null=True, verbose_name='تاریخ و ساعت واقعی تغییرات'),
        ),
        migrations.AlterField(
            model_name='configurationchangerequest',
            name='changing_time_actual',
            field=models.CharField(help_text=' ساعت واقعی تغییرات در قالب HH:MM.', max_length=5, null=True, verbose_name='تاریخ و ساعت واقعی تغییرات'),
        ),
    ]
