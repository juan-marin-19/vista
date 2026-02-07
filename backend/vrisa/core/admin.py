from django.contrib import admin
from .models import Alert, Institution, Measurement, Sensor, Station


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "legal_id", "approved")
    search_fields = ("name", "legal_id")


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "institution", "station_type", "approved")
    list_filter = ("institution", "station_type", "approved")


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("sensor_type", "station", "is_active")
    list_filter = ("sensor_type", "is_active")


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("sensor", "metric", "value", "unit", "captured_at")
    list_filter = ("metric",)


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ("title", "station", "severity", "resolved")
    list_filter = ("severity", "resolved")
