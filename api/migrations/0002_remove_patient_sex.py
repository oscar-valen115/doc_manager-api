# Generated by Django 3.0 on 2021-09-28 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='sex',
        ),
    ]
