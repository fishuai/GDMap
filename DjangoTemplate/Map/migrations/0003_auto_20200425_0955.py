# Generated by Django 3.0.5 on 2020-04-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0002_auto_20200422_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='amapinfo',
            name='name',
            field=models.CharField(default='name', max_length=255),
        ),
        migrations.AlterField(
            model_name='amapinfo',
            name='open_time',
            field=models.CharField(max_length=255),
        ),
    ]
