# Generated by Django 2.0.3 on 2018-07-29 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0008_auto_20180729_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aim',
            name='amount',
            field=models.IntegerField(default=' ', verbose_name='設定金額'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='balance',
            field=models.IntegerField(default=' ', verbose_name='残高'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='sent',
            field=models.IntegerField(default=' ', verbose_name='入金額'),
        ),
    ]
