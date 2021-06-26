from rest_framework import serializers

from orpha_lookup.api.hpos.serializers import HpoSerializer
from orpha_lookup.apps.orpha.models import Disorder, DisorderHpos


class DisorderHpoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisorderHpos
        fields = ('hpo', 'frequency')

    frequency = serializers.CharField(source='frequency.name')
    hpo = HpoSerializer()


class DisorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disorder
        fields = ('id', 'orpha_code', 'name', 'expert_link', 'disorder_type', 'disorder_group', 'score', 'hpos')

    disorder_type = serializers.CharField(source='disorder_type.name')
    disorder_group = serializers.CharField(source='disorder_group.name')
    hpos = serializers.ListSerializer(child=DisorderHpoSerializer())
    score = serializers.SerializerMethodField()

    def get_score(self, disorder: Disorder):
        return getattr(disorder, 'score', None)
