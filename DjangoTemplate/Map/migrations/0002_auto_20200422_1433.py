# Generated by Django 3.0.5 on 2020-04-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amapinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
