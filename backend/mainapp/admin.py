from django.contrib import admin
from mainapp.models import Worker, Shop, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ("title",)


@admin.register(Visit)
class VisitingAdmin(admin.ModelAdmin):
    search_fields = ("shop__worker__name", "shop__title",)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
