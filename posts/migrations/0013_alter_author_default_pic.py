# Generated by Django 3.2.9 on 2021-11-14 13:45

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_author_default_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='default_pic',
            field=models.ImageField(default=django.core.files.storage.FileSystemStorage(location='./static/media/user_avatars/happy_tux.jpg'), storage=django.core.files.storage.FileSystemStorage(location='./static/media/user_avatars/happy_tux.jpg'), upload_to=''),
        ),
    ]
