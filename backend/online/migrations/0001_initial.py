# Generated by Django 3.0.6 on 2020-07-02 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocketConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(db_index=True, max_length=250, null=True)),
                ('agent', models.CharField(db_index=True, max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile')),
            ],
        ),
    ]
