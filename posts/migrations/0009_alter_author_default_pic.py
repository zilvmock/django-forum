# Generated by Django 3.2.9 on 2021-11-14 13:38

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20211114_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='default_pic',
            field=models.ImageField(default=django.core.files.storage.FileSystemStorage(location='/media/user_avatars/happy_tux.jpg'), storage=django.core.files.storage.FileSystemStorage(location='/media/user_avatars/happy_tux.jpg'), upload_to=''),
        ),
    ]
