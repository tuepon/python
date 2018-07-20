# Generated by Django 2.0.3 on 2018-07-18 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='payment',
        ),
        migrations.AlterField(
            model_name='account',
            name='aim',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
