# Generated by Django 3.2.9 on 2021-11-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_author_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fullname',
            field=models.CharField(max_length=40),
        ),
    ]
