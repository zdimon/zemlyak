# Generated by Django 4.0.6 on 2022-07-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_citygroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='is_occupated',
            field=models.BooleanField(default=False),
        ),
    ]