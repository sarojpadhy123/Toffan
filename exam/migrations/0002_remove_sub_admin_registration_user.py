# Generated by Django 4.1.2 on 2022-12-15 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_admin_registration',
            name='user',
        ),
    ]
