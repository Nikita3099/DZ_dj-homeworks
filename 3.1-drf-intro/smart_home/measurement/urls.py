from django.template.context_processors import static
from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateView, MeasurementCreateView, SensorDetailView

from django.conf import settings


urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor-retrieve-update'),
    path('sensors/<int:pk>/detail/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
]