from unittest.mock import Mock
from xml.etree.ElementTree import ParseError

from django.test import SimpleTestCase

from orpha_lookup.apps.data_parser.parser.errors import MalformedDataFileError
from orpha_lookup.apps.data_parser.parser.parser import Parser


class ParserTestCase(SimpleTestCase):
    def setUp(self) -> None:
        self.xml_stream = Mock()
        self.xml_stream.read_xml_file.return_value = []

        self.instance = Parser()
        self.instance.xml_stream = self.xml_stream

    def test_list_disorders_should_call_xml_stream_with_file_name(self):
        expected_path = 'test.xml'

        list(self.instance.list_disorders(expected_path))

        self.xml_stream.read_xml_file.assert_called_once_with(expected_path, 'Disorder', to_dict=True)

    def test_list_disorders_should_raise_malformed_error_when_unable_to_parse(self):
        self.xml_stream.read_xml_file.side_effect = ParseError

        with self.assertRaises(MalformedDataFileError):
            list(self.instance.list_disorders('test.xml'))

    def test_list_disorders_should_return_read_nodes(self):
        expected_response = [dict(), dict(), dict()]
        self.xml_stream.read_xml_file.return_value = expected_response

        actual_response = list(self.instance.list_disorders('test.xml'))

        self.assertListEqual(actual_response, expected_response)
