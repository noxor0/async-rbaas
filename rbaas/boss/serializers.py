from rbaas.boss.models import Boss
from rest_framework import serializers


class BossSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boss
        fields = ['health', 'name']