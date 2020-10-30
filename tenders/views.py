from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from tenders.models import Tender, TenderLot
from tenders.serializers import TenderSerializer, TenderLotSerializer


class ApiTenderLotsListView(ListAPIView):
    queryset = TenderLot.objects.all()
    serializer_class = TenderLotSerializer
    # pagination_class = PageNumberPagination

@api_view(['GET', ])
def api_detail_tenders_view(request, slug):
    try:
        news_tender = Tender.objects.get(slug=slug)

    except TenderSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TenderSerializer(news_tender)
        return Response(serializer.data)

class ApiTendersListView(ListAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    # pagination_class = PageNumberPagination