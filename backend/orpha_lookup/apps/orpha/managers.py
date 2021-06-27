from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from django.db.models import Sum, Q, ExpressionWrapper, FloatField
from django.db.models.functions import Coalesce


class DisorderQuerySet(BulkUpdateOrCreateQuerySet):
    def with_hpos(self, hpo_ids):
        score = ExpressionWrapper(
            Coalesce(Sum('hpos__frequency__weight', filter=Q(hpos__hpo_id__in=hpo_ids)), 0.00),
            output_field=FloatField()
        )

        return (self.prefetch_related('hpos__frequency')
                .annotate(score=score)
                .order_by('-score'))
