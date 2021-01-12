# serializers.py
from rest_framework import serializers

from .models import Hero
from .models import todo


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias')

class todoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = todo 
        fields = ('id','task', 'priority', 'duedate')