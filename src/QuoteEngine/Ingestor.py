"""A class that encapsulates various ingestor helper classes.

This is a class that simplifies and unified the usage of different
ingestors. The appropriate ingestor shall be utilised to perform data
ingestion depending on the type of the input file.
"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .TxtIngestor import TxtIngestor
from .PdfIngestor import PdfIngestor
from .CsvIngestor import CsvIngestor


class Ingestor(IngestorInterface):
    """A unifying class that simplifies the use of ingestor helper classes.

    Checks shall be performed on the extension of the input file in order to
    determine the appropriate ingestor class to use.
    """

    ingestors = [DocxIngestor, TxtIngestor, PdfIngestor, CsvIngestor]


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Perform ingestion of data based on file extension.

        Check file type of the input data file and decide an ingestor
        to use.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
