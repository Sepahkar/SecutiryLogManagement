# Generated by Django 5.0.12 on 2025-04-17 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ConfigurationChangeRequest', '0021_changetype_downtime_duration_worsecase_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='changetype',
            old_name='downtime_duration_worsecase',
            new_name='downtime_duration_worstcase',
        ),
        migrations.RenameField(
            model_name='configurationchangerequest',
            old_name='downtime_duration_worsecase',
            new_name='downtime_duration_worstcase',
        ),
    ]
