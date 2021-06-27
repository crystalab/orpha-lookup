from django.urls import reverse
from rest_framework.test import APITestCase

from orpha_lookup.apps.orpha.tests.factories import HpoFactory


class HpoViewSetTestCase(APITestCase):
    def setUp(self):
        pass

    def test_get_hpos(self):
        hpo = HpoFactory()

        response = self.client.get(path=reverse('api:hpos:suggest'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], hpo.id)

    def test_get_hpos_returns_nothing_when_no_matches(self):
        HpoFactory(name='test')

        response = self.client.get(path=reverse('api:hpos:suggest'), data={'search': 'a'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_get_hpos_returns_only_matched(self):
        HpoFactory(name='test')
        hpo = HpoFactory(name='macro')

        response = self.client.get(path=reverse('api:hpos:suggest'), data={'search': 'mac'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], hpo.id)

    def test_get_hpos_should_limit_by_10(self):
        HpoFactory.create_batch(11)

        response = self.client.get(path=reverse('api:hpos:suggest'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)
