# Generated by Django 2.0 on 2018-02-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massage', '0006_auto_20180208_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='client',
        ),
        migrations.AddField(
            model_name='client',
            name='addresses',
            field=models.ManyToManyField(to='massage.Address'),
        ),
    ]
