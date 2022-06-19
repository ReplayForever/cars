from rest_framework import serializers


class OrderedColorBrandSerializer(serializers.Serializer):
    brand = serializers.CharField(read_only=True)
    color = serializers.CharField(read_only=True)
    count = serializers.IntegerField(read_only=True)
