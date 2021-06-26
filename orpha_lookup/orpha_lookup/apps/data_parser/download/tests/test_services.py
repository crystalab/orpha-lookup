from unittest.mock import Mock, patch, mock_open

from django.test import SimpleTestCase

from orpha_lookup.apps.data_parser.download.errors import InvalidResponseStatusError, InvalidResponseContentError
from orpha_lookup.apps.data_parser.download.services import DownloadService


class DownloadServiceTestCase(SimpleTestCase):
    test_url = 'https://test.url'
    test_upload_path = '/tmp/upload/data.xml'
    test_content = '<xml />'

    def setUp(self) -> None:
        self.response = Mock()
        self.response.status_code = 200
        self.response.headers = {'content-type': 'text/xml'}
        self.response.content = self.test_content

        self.instance = DownloadService()
        self.instance.xml_url = self.test_url
        self.instance.uploaded_path = self.test_upload_path
        self.instance.requests = Mock()
        self.instance.requests.get.return_value = self.response

    def test_download_should_raise_invalid_response_status_error_when_non_200_code_returned(self):
        self.response.status_code = 404

        with self.assertRaises(InvalidResponseStatusError):
            self.instance.download()

    def test_download_should_raise_invalid_response_content_error_when_non_xml_data_returned(self):
        self.response.headers['content-type'] = 'text/json'

        with self.assertRaises(InvalidResponseContentError):
            self.instance.download()

    @patch('builtins.open', mock_open())
    def test_download_should_call_requests_get(self):
        self.instance.download()

        self.instance.requests.get.assert_called_once_with(self.test_url, allow_redirects=True)

    def test_download_should_write_file(self):
        with patch('builtins.open', mock_open()) as open_mock:
            self.instance.download()

            open_mock.assert_called_once_with(self.test_upload_path, 'wb')
            open_mock.return_value.write.assert_called_once_with(self.test_content)
