# Generated by Django 2.2.12 on 2020-11-10 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0005_auto_20201110_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tender',
            name='author',
        ),
    ]
