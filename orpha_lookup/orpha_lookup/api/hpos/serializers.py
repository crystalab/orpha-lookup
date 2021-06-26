from rest_framework import serializers

from orpha_lookup.apps.orpha.models import Hpo


class HpoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hpo
        fields = ('id', 'name', 'hpo_id')
