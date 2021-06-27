from xml.etree.ElementTree import ParseError
import xml_stream

from orpha_lookup.apps.data_parser.parser.errors import MalformedDataFileError


class Parser:
    xml_stream = xml_stream

    def list_disorders(self, path: str):
        try:
            for disorder in self.xml_stream.read_xml_file(path, 'Disorder', to_dict=True):
                yield disorder
        except ParseError:
            raise MalformedDataFileError()


parser = Parser()
