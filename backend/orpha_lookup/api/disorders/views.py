from rest_framework import viewsets

from orpha_lookup.api.disorders.serializers import DisorderSerializer
from orpha_lookup.apps.orpha.models import Disorder


class DisorderViewSet(viewsets.ReadOnlyModelViewSet):
    disorders = Disorder.objects
    serializer_class = DisorderSerializer

    def get_queryset(self):
        qs = (self.disorders.all()
              .select_related('disorder_type', 'disorder_group')
              .prefetch_related('hpos__hpo', 'hpos__frequency'))

        hpo_ids = self.request.query_params.get('hpo', '').split(',')
        if len(hpo_ids) and all(hpo_id.isdigit() for hpo_id in hpo_ids):
            qs = qs.with_hpos(hpo_ids)

        return qs[:10]
