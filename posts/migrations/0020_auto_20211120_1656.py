# Generated by Django 3.2.9 on 2021-11-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20211120_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=models.TextField(),
        ),
    ]
