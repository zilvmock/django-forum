# Generated by Django 3.2.9 on 2021-11-20 12:51

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20211114_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='user_avatars/happy_tux.jpg', force_format=None, keep_meta=True, null=True, quality=100, size=[100, 100], upload_to='user_avatars'),
        ),
    ]
