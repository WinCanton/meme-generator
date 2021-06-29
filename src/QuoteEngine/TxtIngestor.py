"""An ingestor class for ingesting Quotes from input data file of type: `txt`.

This is a concrete implementation of IngestorInterface class which implements
class method `parse` to handle ingestion of Quotes coming from input file
with text file-type.
"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """An ingestor class to extract quotes from .txt input file type.

    This class contains a concrete implementation of IngestorInterface
    `parse` abstract method for `.txt` file type, extracts quote and
    author and constructs the corresponding Quote object.
    """

    allowed_extension = ['txt']


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Check input file for correct file extension and extract data.

        Input data is read and parsed into `body` and `author` variables.
        Each Quote objects created is added into a List collection and
        returned.
        """
        if not cls.allowed_extension:
            raise Exception('Cannot Ingest Exception!')

        quotes = []
        with open(path, 'r', encoding='utf-8-sig') as f:
            data = f.readlines()

        for line in data:
            body, author = line.strip().split(' - ')
            quotes.append(QuoteModel(body, author))

        return quotes
