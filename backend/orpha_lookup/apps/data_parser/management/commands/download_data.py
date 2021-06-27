from django.core.management import BaseCommand

from orpha_lookup.apps.data_parser.download.services import download_service


class Command(BaseCommand):
    download_service = download_service

    def handle(self, *args, **options):
        self.stdout.write(f'Downloading data from {self.download_service.xml_url}')

        self.download_service.download()
        self.stdout.write('Downloading complete')
