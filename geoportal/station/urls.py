from django.urls import path
from station.views import UpdateStationView, DeleteStationView, StationDetailView, station_list, create_Station

app_name = 'station'

urlpatterns = [
    # path('create/', CreateStationView.as_view(), name='station-create'),
    path('create/', create_Station, name='station-create'),
    path('', station_list, name='station-list'),
    # path('list/', StationListView.as_view(), name='station-list'),
    path('<int:pk>/update/', UpdateStationView.as_view(), name='station-update'),
    path('delete/<int:pk>/', DeleteStationView.as_view(), name='station-delete'),
    path('<int:pk>/', StationDetailView.as_view(), name='station-detail'),
]
