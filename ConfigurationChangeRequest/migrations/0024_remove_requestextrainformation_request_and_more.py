# Generated by Django 5.0.12 on 2025-04-22 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ConfigurationChangeRequest', '0023_remove_configurationchangerequest_requestor_role_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestextrainformation',
            name='request',
        ),
        migrations.RemoveField(
            model_name='requestcorp',
            name='request',
        ),
        migrations.RemoveField(
            model_name='requestteam',
            name='request',
        ),
        migrations.DeleteModel(
            name='ConfigurationChangeRequest',
        ),
    ]
