# Generated by Django 5.0.12 on 2025-03-12 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfigurationChangeRequest', '0015_committee_changetype_committee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='administrator_nationalCode',
            field=models.ForeignKey(db_column='administrator_nationalcode', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='administrator', to='ConfigurationChangeRequest.user', verbose_name='کد ملی دبیر کمیته'),
        ),
    ]
