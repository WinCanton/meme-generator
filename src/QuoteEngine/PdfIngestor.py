"""An ingestor class for ingesting Quotes from data file of type: `.pdf`.

This is a concrete implementation of IngestorInterface class which implements
class method `parse` to handle ingestion of Quotes coming from input file
of .pdf file-type.
"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess


class PdfIngestor(IngestorInterface):
    """An ingestor class to extract quotes from .pdf input file type.

    This class contains a concrete implementation of IngestorInterface
    `parse` abstract method for `.pdf` file type, extracts quote and
    author and constructs the corresponding Quote object.
    """

    allowed_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Check input file for correct file extension and extract data.

        External command line utility (pdftotext) is used to provide
        the functionality needed to parse pdf file into a text format file.
        Python subprocess module is used to use this external utility.
        Quote data is subsequently parsed from this text file and the
        corresponding Quote object then created and added into a collection
        to return.
        """
        if not cls.allowed_extension:
            raise Exception('Cannot Ingest Exception!')

        quotes = []
        completed_process = subprocess.run(['pdftotext', '-layout', path],
                                           stdout=subprocess.PIPE)
        output = completed_process.stdout

        output_filepath = f'.{path.split(".")[-2:-1][0]}.txt'
        with open(output_filepath, 'r') as f:
            data = f.readlines()

        for line in data:
            stripped_line = line.strip().replace('"', '').split(' - ')
            if len(stripped_line) == 2:
                body, author = stripped_line
                quotes.append(QuoteModel(body, author))

        completed_process = subprocess.run(['rm', output_filepath],
                                           stdout=subprocess.PIPE)
        return quotes
