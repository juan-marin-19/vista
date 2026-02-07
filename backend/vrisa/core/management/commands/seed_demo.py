from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from core.models import Alert, Institution, Measurement, Sensor, Station


class Command(BaseCommand):
    help = "Seed demo data for VRISA."

    def handle(self, *args, **options):
        institution, _ = Institution.objects.get_or_create(
            legal_id="900123456",
            defaults={
                "name": "DAGMA",
                "address": "Cali, Colombia",
                "logo_url": "https://example.com/logo.png",
                "approved": True,
            },
        )
        station, _ = Station.objects.get_or_create(
            institution=institution,
            name="Estación Centro",
            defaults={
                "location": Point(-76.531985, 3.451648),
                "station_type": "Urbana",
                "responsible": "Equipo DAGMA",
                "approved": True,
            },
        )
        sensor, _ = Sensor.objects.get_or_create(
            station=station,
            sensor_type="Calidad del aire",
            defaults={"variables": ["PM2.5", "PM10", "NO2", "O3"]},
        )
        now = datetime.utcnow()
        for idx in range(6):
            Measurement.objects.get_or_create(
                sensor=sensor,
                captured_at=now - timedelta(hours=idx),
                metric="PM2.5",
                defaults={"value": 18.5 + idx, "unit": "µg/m³"},
            )
        Alert.objects.get_or_create(
            station=station,
            title="Alerta preventiva",
            defaults={"message": "Nivel de PM2.5 en aumento.", "severity": "media"},
        )
        self.stdout.write(self.style.SUCCESS("Demo data seeded."))
