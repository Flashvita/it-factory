from rest_framework import serializers
from mainapp.models import Shop, Visit


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("title", "id")


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ("longitude", "latitude", "shop")


class VisitResponseSerializer(VisitSerializer):
    class Meta(VisitSerializer.Meta):
        fields = ("created_at", "id")
