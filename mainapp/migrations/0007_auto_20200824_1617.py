# Generated by Django 3.0.7 on 2020-08-24 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20200824_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appoint_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]