# Generated by Django 2.2.12 on 2020-10-24 03:25

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tenders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('items', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('asosiy_talablar', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('file', models.FileField(upload_to=tenders.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date_published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date_updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
