from django.urls import path
from tenders.views import ApiTendersListView, api_detail_tenders_view, ApiTenderLotsListView

app_name = 'tenders'

urlpatterns = [
    path('<slug>/', api_detail_tenders_view, name='detail'),
    path('list', ApiTendersListView.as_view(), name='list'),
    path('list1', ApiTenderLotsListView.as_view(), name='list1')
]