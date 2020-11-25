from rest_framework import serializers
from .models import Tender, TenderLot

class TenderLotSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = TenderLot
        fields = ['tender',
                  'name_ru', 'name_de', 'name_en',
                  'description_ru', 'description_de', 'description_en',
                  'price',
                  'id'
                  ]


class TenderSerializer(serializers.ModelSerializer):
    tenderlots = TenderLotSerializer(many=True)

    class Meta:
        model = Tender
        fields = ['title_ru', 'title_de', 'title_en',
                  'asosiy_talablar_ru', 'asosiy_talablar_de', 'asosiy_talablar_en',
                  'file',
                  'date_published',
                  'tenderlots'
                  ]