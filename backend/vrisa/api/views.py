from rest_framework import filters, viewsets
from core.models import Alert, Institution, Measurement, Sensor, Station
from .serializers import (
    AlertSerializer,
    InstitutionSerializer,
    MeasurementSerializer,
    SensorSerializer,
    StationSerializer,
)


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "legal_id"]


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.select_related("institution").all()
    serializer_class = StationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "station_type"]


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.select_related("station").all()
    serializer_class = SensorSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.select_related("sensor").all()
    serializer_class = MeasurementSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["captured_at", "metric"]
    ordering = ["-captured_at"]


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.select_related("station").all()
    serializer_class = AlertSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "severity"]
