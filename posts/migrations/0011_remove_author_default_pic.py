# Generated by Django 3.2.9 on 2021-11-14 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_author_default_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='default_pic',
        ),
    ]
