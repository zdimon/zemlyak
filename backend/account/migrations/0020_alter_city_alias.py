# Generated by Django 4.0.6 on 2022-07-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_city_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='alias',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]