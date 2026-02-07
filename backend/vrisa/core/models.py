from django.contrib.auth import get_user_model
from django.contrib.gis.db import models

User = get_user_model()


class Institution(models.Model):
    name = models.CharField(max_length=200)
    legal_id = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    logo_url = models.URLField(blank=True)
    primary_color = models.CharField(max_length=20, default="#1f2937")
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Station(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="stations")
    name = models.CharField(max_length=200)
    location = models.PointField()
    station_type = models.CharField(max_length=100)
    responsible = models.CharField(max_length=200)
    calibration_certificate_url = models.URLField(blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} ({self.institution.name})"


class Sensor(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="sensors")
    sensor_type = models.CharField(max_length=100)
    variables = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.sensor_type} - {self.station.name}"


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    captured_at = models.DateTimeField()
    metric = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)

    class Meta:
        indexes = [models.Index(fields=["captured_at", "metric"])]

    def __str__(self) -> str:
        return f"{self.metric} {self.value}{self.unit}"


class Alert(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="alerts")
    title = models.CharField(max_length=200)
    message = models.TextField()
    severity = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
