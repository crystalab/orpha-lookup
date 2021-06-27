import requests
from django.conf import settings

from .errors import InvalidResponseStatusError, InvalidResponseContentError


class DownloadService:
    requests = requests
    xml_url = settings.XML_FILE_URL
    uploaded_path = settings.XML_UPLOAD_PATH

    def download(self):
        response = self.requests.get(self.xml_url, allow_redirects=True)

        if response.status_code != 200:
            raise InvalidResponseStatusError()

        if response.headers.get('content-type') != 'text/xml':
            raise InvalidResponseContentError()

        with open(self.uploaded_path, 'wb') as f:
            f.write(response.content)


download_service = DownloadService()
