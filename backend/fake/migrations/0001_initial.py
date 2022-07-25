# Generated by Django 4.0.6 on 2022-07-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('name_en', models.CharField(default='', max_length=250, null=True)),
                ('name_ru', models.CharField(default='', max_length=250, null=True)),
                ('name_uk', models.CharField(default='', max_length=250, null=True)),
                ('gender', models.CharField(default='m', max_length=1)),
            ],
        ),
    ]
