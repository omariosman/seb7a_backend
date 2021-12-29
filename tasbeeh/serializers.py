
from rest_framework import serializers
from .models import Zekr

class ZekrSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Zekr
        fields = ['id', 'name', 'counter']

        

class PostZekrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zekr
        fields = ['name']

class UpdateZekrSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Zekr
        fields = ['id', 'name']


class DeleteZekrSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Zekr
        fields = ['id']


class IncrementCounterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Zekr
        fields = ['id', 'name']

