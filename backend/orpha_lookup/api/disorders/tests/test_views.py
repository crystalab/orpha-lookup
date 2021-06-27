from django.urls import reverse
from rest_framework.test import APITestCase

from orpha_lookup.apps.orpha.tests.factories import DisorderFactory, HpoFactory, DisorderHposFactory


class DisorderViewSetTestCase(APITestCase):
    def setUp(self):
        pass

    def test_get_disorders(self):
        disorder = DisorderFactory()

        response = self.client.get(path=reverse('api:disorders:list'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], disorder.id)

    def test_get_disorders_without_score(self):
        DisorderFactory()

        response = self.client.get(path=reverse('api:disorders:list'))

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.data[0]['score'])

    def test_get_disorder_with_score(self):
        assoc = DisorderHposFactory(frequency__weight=100)

        response = self.client.get(path=reverse('api:disorders:list'), data={'hpo': assoc.hpo_id})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))
        self.assertEquals(response.data[0]['score'], 100)
