from rest_framework import viewsets

from orpha_lookup.api.hpos.serializers import HpoSerializer
from orpha_lookup.apps.orpha.models import Hpo


class HpoViewSet(viewsets.ReadOnlyModelViewSet):
    hpos = Hpo.objects
    serializer_class = HpoSerializer

    def get_queryset(self):
        qs = self.hpos.all()

        search_term = self.request.query_params.get('search')
        if search_term:
            qs = qs.filter(name__startswith=search_term)

        return qs[:10]
