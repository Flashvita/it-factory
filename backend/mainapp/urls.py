
from django.urls import path
from .views import (
    ShopListApiView,
    VisitCreateApiView
)

urlpatterns = [
    path('my-shops', ShopListApiView.as_view(), name="my-shops"),
    path('visit', VisitCreateApiView.as_view(), name="visit-create"),
]