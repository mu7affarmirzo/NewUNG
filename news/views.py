from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from news.models import BlogPost
from news.serializers import BlogSerializer

@api_view(['GET', ])
def api_detail_news_view(request, slug):
    try:
        news_post = BlogPost.objects.get(slug=slug)

    except BlogSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogSerializer(news_post)
        return Response(serializer.data)

class ApiNewsListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    # pagination_class = PageNumberPagination
