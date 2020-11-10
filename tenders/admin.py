from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from tenders.models import (
    Tender,
    TenderLot,
)

class TenderAdminForm(forms.ModelForm):
    asosiy_talablar_ru = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    asosiy_talablar_de = forms.CharField(label='Tekst', widget=CKEditorUploadingWidget())
    asosiy_talablar_en = forms.CharField(label='Text', widget=CKEditorUploadingWidget())

    class Meta:
        model = Tender
        fields = '__all__'

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


