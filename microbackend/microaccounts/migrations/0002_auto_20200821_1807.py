# Generated by Django 3.0.8 on 2020-08-21 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microaccounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='admin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='staff',
            new_name='is_staff',
        ),
    ]
