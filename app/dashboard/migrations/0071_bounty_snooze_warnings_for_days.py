# Generated by Django 2.0.5 on 2018-05-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0070_auto_20180509_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='snooze_warnings_for_days',
            field=models.IntegerField(default=0),
        ),
    ]