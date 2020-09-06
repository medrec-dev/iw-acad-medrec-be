# Generated by Django 3.0.7 on 2020-09-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20200904_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='checkup_id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patient_contact',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patient_symptoms',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_regnum',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
