# Generated by Django 2.0 on 2018-02-07 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('massage', '0002_massage_masseur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=70)),
                ('street_number', models.PositiveSmallIntegerField()),
                ('post_code', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('surname', models.CharField(max_length=35)),
                ('phone', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='massage',
            name='duration',
            field=models.CharField(choices=[('30', '30 minutes'), ('45', '45 minutes'), ('60', '60 minutes')], max_length=2),
        ),
        migrations.AddField(
            model_name='address',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='massage.Client'),
        ),
    ]