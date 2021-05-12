# Generated by Django 3.0 on 2021-05-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210512_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('inactive', 'inactive'), ('check_in', 'check_in'), ('check_out', 'check_out')], max_length=10, null=True),
        ),
    ]
