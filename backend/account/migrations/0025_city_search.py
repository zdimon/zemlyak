# Generated by Django 4.0.6 on 2022-08-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_userprofile_is_fake'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='search',
            field=models.CharField(default='', max_length=250),
        ),
    ]
