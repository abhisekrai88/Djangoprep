

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero
from .serializers import todoSerializer
from .models import todo


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class todoViewSet(viewsets.ModelViewSet):
    queryset = todo.objects.all().order_by('duedate')
    serializer_class = todoSerializer