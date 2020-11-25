from rest_framework import serializers
from .models import BlogPost
from .translation import BlogPostTranslationOptions

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title_ru', 'title_de', 'title_en', 'body_ru', 'body_de', 'body_en','image', 'date_updated', 'slug']

