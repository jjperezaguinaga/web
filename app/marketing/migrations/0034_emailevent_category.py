# Generated by Django 2.1.1 on 2018-09-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0033_auto_20180905_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailevent',
            name='category',
            field=models.CharField(blank=True, db_index=True, default='', max_length=255),
        ),
    ]
