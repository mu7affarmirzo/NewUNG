# Generated by Django 2.2.12 on 2020-11-10 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0003_auto_20201110_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tender',
            name='asosiy_talablar_de',
        ),
        migrations.RemoveField(
            model_name='tender',
            name='asosiy_talablar_en',
        ),
        migrations.RemoveField(
            model_name='tender',
            name='asosiy_talablar_ru',
        ),
        migrations.RemoveField(
            model_name='tender',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='tender',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='tender',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='tenderlot',
            name='description_de',
        ),
        migrations.RemoveField(
            model_name='tenderlot',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='tenderlot',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='tenderlot',
            name='name_de',
        ),
        migrations.RemoveField(
            model_name='tenderlot',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='tenderlot',
            name='name_ru',
        ),
    ]