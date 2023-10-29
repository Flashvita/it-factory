from rest_framework import serializers
from mainapp.models import Shop, Visit


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("title", "id")


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"
        read_only_fields = ("created_at",  "id")
