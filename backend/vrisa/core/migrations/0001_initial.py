from django.db import migrations, models
import django.contrib.gis.db.models.fields
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Institution",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("legal_id", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=255)),
                ("logo_url", models.URLField(blank=True)),
                ("primary_color", models.CharField(default="#1f2937", max_length=20)),
                ("approved", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Station",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("location", django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ("station_type", models.CharField(max_length=100)),
                ("responsible", models.CharField(max_length=200)),
                ("calibration_certificate_url", models.URLField(blank=True)),
                ("approved", models.BooleanField(default=False)),
                (
                    "institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="stations", to="core.institution"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sensor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sensor_type", models.CharField(max_length=100)),
                ("variables", models.JSONField(default=list)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="sensors", to="core.station"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Measurement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("captured_at", models.DateTimeField()),
                ("metric", models.CharField(max_length=50)),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("unit", models.CharField(max_length=20)),
                (
                    "sensor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="measurements", to="core.sensor"
                    ),
                ),
            ],
            options={
                "indexes": [models.Index(fields=["captured_at", "metric"], name="core_meas_captur_6f5f5d_idx")],
            },
        ),
        migrations.CreateModel(
            name="Alert",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("message", models.TextField()),
                ("severity", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("resolved", models.BooleanField(default=False)),
                (
                    "station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="alerts", to="core.station"
                    ),
                ),
            ],
        ),
    ]
