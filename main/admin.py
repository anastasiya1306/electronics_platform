from django.contrib import admin

from main.models import Provider, Network, Product


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'arrears']
    list_filter = ['city']
    search_fields = ['name']
    actions = ['clear_arrears']

    def clear_arrears(self, request, queryset):
        """Очищаем задолженность"""
        queryset.update(arrears=0)

    clear_arrears.short_description = "Очистить задолженность"


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'house_number', 'provider']
    list_filter = ['city']
    search_fields = ['name']
    raw_id_fields = ['provider']  # перегружаем виджет отображения, который не делает лишних запросов в БД


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'date_release', 'network', 'created_at']
    list_filter = ['name']
    search_fields = ['name']
    raw_id_fields = ['network']
