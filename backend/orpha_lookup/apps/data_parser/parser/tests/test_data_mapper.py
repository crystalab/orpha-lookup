from django.test import SimpleTestCase

from orpha_lookup.apps.data_parser.parser.data_mapper import DataMapper, MapResult


class DataMapperTestCase(SimpleTestCase):
    MIN_DISEASE_NODE = {
        'id': 1,
        'OrphaCode': 2,
        'Name': {'_value': 'Test disorder'},
        'DisorderType': {'id': 10, 'Name': {'_value': 'Test disorder type'}},
        'DisorderGroup': {'id': 20, 'Name': {'_value': 'Test disorder group'}},
        'HPODisorderAssociationList': {'count': 0},
    }

    DISEASE_NODE = {
        'id': 1,
        'OrphaCode': 2,
        'Name': {'_value': 'Test disorder'},
        'ExpertLink': {'_value': 'https://test.com/'},
        'DisorderType': {'id': 10, 'Name': {'_value': 'Test disorder type'}},
        'DisorderGroup': {'id': 20, 'Name': {'_value': 'Test disorder group'}},
        'HPODisorderAssociationList': {
            'count': 6,
            'HPODisorderAssociation': [
                {'id': 100,
                 'HPO': {'id': 1000, 'HPOId': 'HP:000', 'HPOTerm': 'Test HPO 0'},
                 'HPOFrequency': {'id': 10000, 'Name': {'_value': 'Excluded (0%)'}}},
                {'id': 101,
                 'HPO': {'id': 1001, 'HPOId': 'HP:001', 'HPOTerm': 'Test HPO 1'},
                 'HPOFrequency': {'id': 10001, 'Name': {'_value': 'Very rare (<4-1%)'}}},
                {'id': 102,
                 'HPO': {'id': 1002, 'HPOId': 'HP:002', 'HPOTerm': 'Test HPO 2'},
                 'HPOFrequency': {'id': 10002, 'Name': {'_value': 'Occasional (29-5%)'}}},
                {'id': 103,
                 'HPO': {'id': 1003, 'HPOId': 'HP:003', 'HPOTerm': 'Test HPO 3'},
                 'HPOFrequency': {'id': 10003, 'Name': {'_value': 'Frequent (79-30%)'}}},
                {'id': 104,
                 'HPO': {'id': 1004, 'HPOId': 'HP:004', 'HPOTerm': 'Test HPO 4'},
                 'HPOFrequency': {'id': 10004, 'Name': {'_value': 'Very frequent (99-80%)'}}},
                {'id': 105,
                 'HPO': {'id': 1005, 'HPOId': 'HP:005', 'HPOTerm': 'Test HPO 5'},
                 'HPOFrequency': {'id': 10005, 'Name': {'_value': 'Obligate (100%)'}}},
            ]
        },
    }

    def setUp(self) -> None:
        self.instance = DataMapper()

    def test_map_should_return_empty_result_when_called_with_empty_input(self):
        actual_result = self.instance.map([])

        self.assertEqual(actual_result, MapResult())

    def test_map_should_map_disorder_fields(self):
        actual_result = self.instance.map([self.DISEASE_NODE])

        self.assertEqual(len(actual_result.disorders), 1)
        self.assertEqual(actual_result.disorders[1].id, 1)
        self.assertEqual(actual_result.disorders[1].orpha_code, 2)
        self.assertEqual(actual_result.disorders[1].name, 'Test disorder')
        self.assertEqual(actual_result.disorders[1].expert_link, 'https://test.com/')
        self.assertEqual(actual_result.disorders[1].disorder_type_id, 10)
        self.assertEqual(actual_result.disorders[1].disorder_group_id, 20)

    def test_map_should_map_disorder_type(self):
        actual_result = self.instance.map([self.DISEASE_NODE])

        self.assertEqual(len(actual_result.disorder_types), 1)
        self.assertEqual(actual_result.disorder_types[10].id, 10)
        self.assertEqual(actual_result.disorder_types[10].name, 'Test disorder type')

    def test_map_should_map_disorder_group(self):
        actual_result = self.instance.map([self.DISEASE_NODE])

        self.assertEqual(len(actual_result.disorder_groups), 1)
        self.assertEqual(actual_result.disorder_groups[20].id, 20)
        self.assertEqual(actual_result.disorder_groups[20].name, 'Test disorder group')

    def test_map_should_map_hpos(self):
        actual_result = self.instance.map([self.DISEASE_NODE])

        self.assertEqual(len(actual_result.hpos), 6)
        for i in range(6):
            id = 1000 + i
            self.assertEqual(actual_result.hpos[id].id, id)
            self.assertEqual(actual_result.hpos[id].hpo_id, f'HP:00{i}')
            self.assertEqual(actual_result.hpos[id].name, f'Test HPO {i}')

    def test_map_should_map_hpo_association(self):
        actual_result = self.instance.map([self.DISEASE_NODE])

        self.assertEqual(len(actual_result.disorder_hpos), 6)
        for i in range(6):
            id = 100 + i
            self.assertEqual(actual_result.disorder_hpos[id].id, id)
            self.assertEqual(actual_result.disorder_hpos[id].disorder_id, 1)
            self.assertEqual(actual_result.disorder_hpos[id].hpo_id, 1000 + i)
            self.assertEqual(actual_result.disorder_hpos[id].frequency_id, 10000 + i)

    def test_map_should_map_frequencies(self):
        actual_result = self.instance.map([self.DISEASE_NODE])

        self.assertEqual(len(actual_result.frequencies), 6)
        for i in range(6):
            id = 10000 + i
            self.assertEqual(actual_result.frequencies[id].id, id)

        self.assertEqual(actual_result.frequencies[10000].name, 'Excluded (0%)')
        self.assertEqual(actual_result.frequencies[10000].weight, 0)
        self.assertEqual(actual_result.frequencies[10001].name, 'Very rare (<4-1%)')
        self.assertEqual(actual_result.frequencies[10001].weight, 2)
        self.assertEqual(actual_result.frequencies[10002].name, 'Occasional (29-5%)')
        self.assertEqual(actual_result.frequencies[10002].weight, 17)
        self.assertEqual(actual_result.frequencies[10003].name, 'Frequent (79-30%)')
        self.assertEqual(actual_result.frequencies[10003].weight, 55)
        self.assertEqual(actual_result.frequencies[10004].name, 'Very frequent (99-80%)')
        self.assertEqual(actual_result.frequencies[10004].weight, 90)
        self.assertEqual(actual_result.frequencies[10005].name, 'Obligate (100%)')
        self.assertEqual(actual_result.frequencies[10005].weight, 100)

    def test_map_should_work_with_min_node(self):
        actual_result = self.instance.map([self.MIN_DISEASE_NODE])

        self.assertEqual(len(actual_result.disorders), 1)
        self.assertEqual(len(actual_result.disorder_types), 1)
        self.assertEqual(len(actual_result.disorder_groups), 1)
        self.assertEqual(len(actual_result.frequencies), 0)
        self.assertEqual(len(actual_result.hpos), 0)
        self.assertEqual(len(actual_result.disorder_hpos), 0)
        self.assertIsNone(actual_result.disorders[1].expert_link)
