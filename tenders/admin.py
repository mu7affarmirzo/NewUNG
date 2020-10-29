from django.contrib import admin
from tenders.models import (
    Tender,
    TenderLot,
)

class TenderLotAdmin(admin.StackedInline):
    model = TenderLot

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    inlines = [TenderLotAdmin]

    class Meta:
        model = Tender

@admin.register(TenderLot)
class TenderLotAdmin(admin.ModelAdmin):
    pass
