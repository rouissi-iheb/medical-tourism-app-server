# Generated by Django 3.1.4 on 2021-01-05 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rendezvous',
            old_name='doctor',
            new_name='doctorId',
        ),
        migrations.RenameField(
            model_name='rendezvous',
            old_name='patient',
            new_name='patientId',
        ),
    ]
