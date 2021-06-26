from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from django.db import models
from django.db.models import Index
from django.db.models.functions import Lower
from model_utils.models import TimeStampedModel

from orpha_lookup.apps.orpha.managers import DisorderQuerySet


class DisorderType(TimeStampedModel):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class DisorderGroup(TimeStampedModel):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Frequency(TimeStampedModel):
    class Meta:
        verbose_name_plural = 'Frequencies'

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    name = models.CharField(max_length=256)
    weight = models.FloatField()

    def __str__(self):
        return self.name


class Hpo(TimeStampedModel):
    class Meta:
        indexes = [Index(Lower('name'), name='lower_name_idx')]

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    hpo_id = models.CharField(max_length=256)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Disorder(TimeStampedModel):
    objects = DisorderQuerySet.as_manager()

    orpha_code = models.IntegerField(unique=True)
    expert_link = models.CharField(max_length=256, null=True, default=None)
    name = models.CharField(max_length=256)
    disorder_type = models.ForeignKey(to=DisorderType, on_delete=models.SET_NULL, null=True)
    disorder_group = models.ForeignKey(to=DisorderGroup, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class DisorderHpos(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    disorder = models.ForeignKey(to=Disorder, on_delete=models.CASCADE, related_name='hpos')
    hpo = models.ForeignKey(to=Hpo, on_delete=models.CASCADE)
    frequency = models.ForeignKey(to=Frequency, on_delete=models.PROTECT)
