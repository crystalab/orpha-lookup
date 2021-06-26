from unittest.mock import Mock, patch

from django.test import SimpleTestCase

from orpha_lookup.apps.data_parser.parser.data_mapper import MapResult
from orpha_lookup.apps.data_parser.parser.errors import DataFileError
from orpha_lookup.apps.data_parser.parser.services import ImportService


class ImportServiceTestCase(SimpleTestCase):
    def setUp(self) -> None:
        self.data_mapper = Mock()
        self.data_mapper.map.return_value = MapResult()

        self.parser = Mock()
        self.parser.list_disorders.return_value = []

        self.instance = ImportService()
        self.instance.parser = self.parser
        self.instance.data_mapper = self.data_mapper
        self.instance.disorders = Mock()
        self.instance.hpos = Mock()
        self.instance.disorder_types = Mock()
        self.instance.disorder_groups = Mock()
        self.instance.disorder_hpos = Mock()
        self.instance.frequencies = Mock()

    @patch('os.path.isfile', lambda file: False)
    def test_import_data_should_raise_data_file_error_when_file_absent(self):
        with self.assertRaises(DataFileError):
            self.instance.import_data()

    @patch('os.path.isfile', lambda file: True)
    def test_import_data_should_call_parser_list_disorders(self):
        self.instance.import_data()

        self.parser.list_disorders.assert_called_once()

    @patch('os.path.isfile', lambda file: True)
    def test_import_data_should_call_data_mapper_map(self):
        self.parser.list_disorders.return_value = [dict()]

        self.instance.import_data()

        self.data_mapper.map.assert_called_once()

    @patch('os.path.isfile', lambda file: True)
    def test_import_data_should_call_manager_bulk_operations(self):
        self.parser.list_disorders.return_value = [dict()]

        self.instance.import_data()

        self.instance.disorder_types.bulk_update_or_create.assert_called_once()
        self.instance.disorder_groups.bulk_update_or_create.assert_called_once()
        self.instance.frequencies.bulk_update_or_create.assert_called_once()
        self.instance.hpos.bulk_update_or_create.assert_called_once()
        self.instance.disorders.bulk_update_or_create.assert_called_once()
        self.instance.disorder_hpos.bulk_update_or_create.assert_called_once()
