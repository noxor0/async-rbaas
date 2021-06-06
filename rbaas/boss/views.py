from typing import List
from rbaas.boss.models import Boss
from rest_framework import viewsets
from rest_framework.request import Request
from rbaas.boss.serializers import BossSerializer
from time import sleep

class BossViewSet(viewsets.ModelViewSet):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer

    def list(self, request: Request) -> List[Boss]:
        sleep(5)
        return super().list(request)