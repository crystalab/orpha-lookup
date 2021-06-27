from dataclasses import dataclass, field

from typing import Dict

from orpha_lookup.apps.data_parser.parser.errors import UnresolvedFrequencyError
from orpha_lookup.apps.orpha.models import Disorder, DisorderType, DisorderGroup, DisorderHpos, Hpo, Frequency


@dataclass
class MapResult:
    hpos: Dict[int, Hpo] = field(default_factory=dict)
    frequencies: Dict[int, Frequency] = field(default_factory=dict)
    disorders: Dict[int, Disorder] = field(default_factory=dict)
    disorder_hpos: Dict[int, DisorderHpos] = field(default_factory=dict)
    disorder_types: Dict[int, DisorderType] = field(default_factory=dict)
    disorder_groups: Dict[int, DisorderGroup] = field(default_factory=dict)


class DataMapper:
    def map(self, disorder_nodes: list) -> MapResult:
        result = MapResult()

        for disorder_node in disorder_nodes:
            if disorder_node is None:
                continue

            disorder = self._map_disorder(disorder_node)
            disorder_type = self._map_disorder_type(disorder_node['DisorderType'])
            disorder_group = self._map_disorder_group(disorder_node['DisorderGroup'])

            result.disorders[disorder.id] = disorder
            result.disorder_types[disorder_type.id] = disorder_type
            result.disorder_groups[disorder_group.id] = disorder_group

            assoc_list_node = disorder_node['HPODisorderAssociationList']
            if assoc_list_node['count'] == 0 or 'HPODisorderAssociation' not in assoc_list_node:
                continue

            for assoc_node in assoc_list_node['HPODisorderAssociation']:
                hpos = self._map_hpo(assoc_node['HPO'])
                disorder_hpo = self._map_disorder_hpo_association(assoc_node, disorder_node['id'])
                frequency = self._map_frequency(assoc_node['HPOFrequency'])

                result.hpos[hpos.id] = hpos
                result.disorder_hpos[disorder_hpo.id] = disorder_hpo
                result.frequencies[frequency.id] = frequency

        return result

    def _map_disorder(self, node: dict) -> Disorder:
        disorder = Disorder(id=node['id'], orpha_code=node['OrphaCode'], name=node['Name']['_value'],
                            disorder_type_id=node['DisorderType']['id'], disorder_group_id=node['DisorderGroup']['id'])

        if 'ExpertLink' in node:
            disorder.expert_link = node['ExpertLink']['_value']

        return disorder

    def _map_disorder_type(self, node: dict) -> DisorderType:
        return DisorderType(id=node['id'], name=node['Name']['_value'])

    def _map_disorder_group(self, node: dict) -> DisorderGroup:
        return DisorderGroup(id=node['id'], name=node['Name']['_value'])

    def _map_disorder_hpo_association(self, node: dict, disorder_id) -> DisorderHpos:
        return DisorderHpos(id=node['id'], hpo_id=node['HPO']['id'], disorder_id=disorder_id,
                            frequency_id=node['HPOFrequency']['id'])

    def _map_frequency(self, node: dict) -> Frequency:
        return Frequency(id=node['id'], name=node['Name']['_value'], weight=self._map_weight(node['Name']['_value']))

    def _map_weight(self, name: str) -> float:
        if name == 'Obligate (100%)':
            return 100
        if name == 'Very frequent (99-80%)':
            return 90
        elif name == 'Frequent (79-30%)':
            return 55
        elif name == 'Occasional (29-5%)':
            return 17
        elif name == 'Very rare (<4-1%)':
            return 2
        elif name == 'Excluded (0%)':
            return 0

        raise UnresolvedFrequencyError()

    def _map_hpo(self, node: dict) -> Hpo:
        return Hpo(id=node['id'], hpo_id=node['HPOId'], name=node['HPOTerm'])


data_mapper = DataMapper()
