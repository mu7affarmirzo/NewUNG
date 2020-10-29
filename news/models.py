from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from ckeditor.fields import RichTextField



def upload_location(instance, filename):
    file_path = 'blog/{author_id}/{title}-filename'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path

class BlogPost(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=100, null=False, blank=False)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date_updated")
    slug = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slider = models.CharField(max_length=10, choices=STATUS)
    status = models.BooleanField(verbose_name="slider",)

    def __str__(self):
        return self.title

# class OpenD(models.Model):
#     CATEGORY = (
#         ('Logistics', 'Logistika'),
#         ('Economy', 'Ekonomika va moliya'),
#         ('Digging', 'Dobicha'),
#         ('Geology', 'Geologiya'),
#
#     )
#
#     title = models.CharField(max_length=100, null=False, blank=False)
#     body = RichTextField(blank=True, null=True)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='category', on_delete=models.CASCADE)
#     category = models.CharField(max_length=10, choices=CATEGORY)
#     file = models.FileField(upload_to=upload_location, null=True, blank=True)
#
#     def __str__(self):
#         return self.title



@receiver(post_delete, sender = BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)