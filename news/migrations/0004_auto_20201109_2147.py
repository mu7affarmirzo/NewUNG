# Generated by Django 2.2.12 on 2020-11-09 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20201109_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='body_uz',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='title_uz',
        ),
    ]