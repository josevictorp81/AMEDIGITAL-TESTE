from rest_framework import serializers

from .models import Planet

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['id', 'name', 'climate', 'terrain', 'films_apparitions']
        read_only_fields = ['id', 'films_apparitions']
