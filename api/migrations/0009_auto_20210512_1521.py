# Generated by Django 3.0 on 2021-05-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210507_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('inactive', 'inactive'), ('check_in', 'check_in'), ('check_out', 'check_out')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='zip_code',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
