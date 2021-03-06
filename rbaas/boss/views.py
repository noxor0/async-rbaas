from typing import List
from rbaas.boss.models import Boss
from rest_framework import viewsets
from rest_framework.request import Request
from rbaas.boss.serializers import BossSerializer
from time import sleep

class BossViewSet(viewsets.ModelViewSet):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer

    def retrieve(self, request: Request, pk: int, *args, **kwargs) -> List[Boss]:
        sleep(5)  # We are doing some serious db work
        return super().retrieve(request)