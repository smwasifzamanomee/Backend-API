from rest_framework import serializers

from .models import Menu

class LittleLemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'