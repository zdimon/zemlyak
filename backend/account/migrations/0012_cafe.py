# Generated by Django 4.0.6 on 2022-07-22 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_userprofile_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('link', models.CharField(default='', max_length=250)),
                ('desc', models.TextField(default='')),
                ('image', models.ImageField(upload_to='cafe')),
                ('alias', models.CharField(max_length=250)),
                ('country_alias', models.CharField(default='', max_length=250)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.city')),
            ],
        ),
    ]
