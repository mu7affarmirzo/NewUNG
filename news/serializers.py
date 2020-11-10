from rest_framework import serializers
from .models import BlogPost
from .translation import BlogPostTranslationOptions

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'date_updated']

