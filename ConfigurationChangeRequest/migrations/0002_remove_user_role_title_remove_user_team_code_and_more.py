# Generated by Django 5.0.12 on 2025-02-13 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfigurationChangeRequest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role_title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='team_code',
        ),
        migrations.CreateModel(
            name='UserTeamRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_title', models.CharField(help_text='لطفاً سمت خود را وارد کنید.', max_length=100, verbose_name='سمت کاربر')),
                ('manager_national_code', models.ForeignKey(db_column='manager_national_code', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='direct_manager', to='ConfigurationChangeRequest.user', verbose_name='کد ملی مدیر مستقیم')),
                ('national_code', models.ForeignKey(db_column='national_code', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='ConfigurationChangeRequest.user', verbose_name='کد ملی کاربر')),
                ('team_code', models.ForeignKey(blank=True, db_column='team_code', help_text='تیم مربوط به کاربر را انتخاب کنید.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ConfigurationChangeRequest.team', verbose_name='تیم کاربر')),
            ],
            options={
                'verbose_name': 'سمت کاربر',
                'verbose_name_plural': 'سمت های کاربران',
            },
        ),
    ]
