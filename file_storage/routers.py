from rest_framework import routers
from file_handler_app.viewsets import DataViewSet


router = routers.DefaultRouter()
router.register(r'', DataViewSet, basename='data')