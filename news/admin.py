from django.contrib import admin
from django import forms

from news.models import BlogPost
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

@admin.register(BlogPost)
class BlogPostAdmin(TranslationAdmin):
    body_ru = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    body_de = forms.CharField(label='Tekst', widget=CKEditorUploadingWidget())
    body_en = forms.CharField(label='Text', widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'