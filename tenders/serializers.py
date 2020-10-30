from rest_framework import serializers
from .models import Tender, TenderLot

class TenderLotSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = TenderLot
        fields = ['tender', 'name', 'description', 'price', 'id']


class TenderSerializer(serializers.ModelSerializer):
    tenderlots = TenderLotSerializer(many=True)

    class Meta:
        model = Tender
        fields = ['title', 'asosiy_talablar', 'file', 'date_published', 'author', 'tenderlots']