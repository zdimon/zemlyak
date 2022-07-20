# Generated by Django 3.0.6 on 2020-05-31 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_media', models.CharField(choices=[('photo', 'Photo'), ('video', 'Video')], default='photo', max_length=5, verbose_name='Type of media')),
                ('role_media', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=10, verbose_name='Role of media')),
                ('orient', models.CharField(choices=[('land', 'Landscape'), ('port', 'Portrait')], default='port', max_length=5, verbose_name='Orientation')),
                ('is_main', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=250)),
                ('video', models.FileField(blank=True, upload_to='user_video')),
                ('image', models.ImageField(blank=True, upload_to='user_photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile')),
            ],
        ),
    ]
