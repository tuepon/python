# Generated by Django 2.0.3 on 2018-07-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0006_auto_20180728_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='balance',
        ),
        migrations.AlterField(
            model_name='deposit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
