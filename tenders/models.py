from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

def upload_location(instance, filename):
    file_path = 'tender/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path



class Tender(models.Model):

    title = models.CharField(max_length=100, null=False, blank=False)
    # items = RichTextField(blank=True, null=True)
    asosiy_talablar = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date_updated")
    slug = models.SlugField(blank=True, unique=True)
    # author = models.ForeignKey(User, related_name='tender_created', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    @property
    def tenderlots(self):
        return self.tenderlot_set.all()

class TenderLot(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = RichTextField(blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
