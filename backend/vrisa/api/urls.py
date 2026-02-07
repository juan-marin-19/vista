from rest_framework.routers import DefaultRouter
from .views import AlertViewSet, InstitutionViewSet, MeasurementViewSet, SensorViewSet, StationViewSet

router = DefaultRouter()
router.register("institutions", InstitutionViewSet)
router.register("stations", StationViewSet)
router.register("sensors", SensorViewSet)
router.register("measurements", MeasurementViewSet)
router.register("alerts", AlertViewSet)

urlpatterns = router.urls
