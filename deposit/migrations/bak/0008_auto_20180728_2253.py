# Generated by Django 2.0.3 on 2018-07-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0007_auto_20180728_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='aim',
            field=models.IntegerField(verbose_name='設定金額'),
        ),
    ]
