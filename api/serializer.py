from rest_framework import serializers
from .models import Progamer

class ProgamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progamer
        fields = '__all__'    #sepuede poner tupla con los campos que uno quiere eje('name', 'nickname')