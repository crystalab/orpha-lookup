from django.core.management import BaseCommand

from orpha_lookup.apps.data_parser.parser.services import import_service


class Command(BaseCommand):
    import_service = import_service

    def handle(self, *args, **options):
        self.stdout.write(f'Importing data from {self.import_service.data_path}')

        self.import_service.import_data()
