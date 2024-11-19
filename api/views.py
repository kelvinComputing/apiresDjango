from rest_framework import viewsets
from .serializer import ProgamerSerializer
from .models import Progamer

# Create your views here.

class ProgamerViewSet(viewsets.ModelViewSet):
    queryset = Progamer.objects.all()
    serializer_class = ProgamerSerializer
