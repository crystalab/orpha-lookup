import os

from django.conf import settings
from more_itertools import grouper

from orpha_lookup.apps.orpha.models import Disorder, Hpo, DisorderType, DisorderGroup, DisorderHpos, Frequency
from .errors import DataFileError
from .parser import parser
from .data_mapper import data_mapper, MapResult


class ImportService:
    batch_size = 1024
    data_path = settings.XML_UPLOAD_PATH

    parser = parser
    data_mapper = data_mapper

    disorders = Disorder.objects
    hpos = Hpo.objects
    disorder_types = DisorderType.objects
    disorder_groups = DisorderGroup.objects
    disorder_hpos = DisorderHpos.objects
    frequencies = Frequency.objects

    def import_data(self):
        if not os.path.isfile(self.data_path):
            raise DataFileError()

        for chunk in grouper(self.parser.list_disorders(self.data_path), self.batch_size):
            self._persist_data(self.data_mapper.map(chunk))

    def _persist_data(self, data: MapResult):
        self.disorder_types.bulk_update_or_create(data.disorder_types.values(), update_fields=['name'],
                                                  match_field='id')
        self.disorder_groups.bulk_update_or_create(data.disorder_groups.values(), update_fields=['name'],
                                                   match_field='id')
        self.frequencies.bulk_update_or_create(data.frequencies.values(), update_fields=['name', 'weight'],
                                               match_field='id')
        self.hpos.bulk_update_or_create(data.hpos.values(), update_fields=['hpo_id', 'name'], match_field='id')
        self.disorders.bulk_update_or_create(data.disorders.values(),
                                             update_fields=['orpha_code', 'name', 'disorder_type', 'disorder_group',
                                                            'expert_link'], match_field='id')
        self.disorder_hpos.bulk_update_or_create(data.disorder_hpos.values(),
                                                 update_fields=['disorder', 'hpo', 'frequency'], match_field='id')


import_service = ImportService()
