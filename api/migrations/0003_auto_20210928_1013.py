# Generated by Django 3.0 on 2021-09-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_patient_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='current_patient',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
    ]
