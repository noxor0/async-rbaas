from rbaas.boss.models import Boss
from rest_framework import viewsets
from rest_framework import permissions
from rbaas.boss.serializers import BossSerializer


class BossViewSet(viewsets.ModelViewSet):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer