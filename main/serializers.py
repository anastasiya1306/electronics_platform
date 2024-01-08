from rest_framework import serializers

from main.models import Provider, Network, Product


class ProviderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class NetworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
