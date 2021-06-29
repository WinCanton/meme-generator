"""An ingestor class for ingesting Quotes from data file of type: `.docx`.

This is a concrete implementation of IngestorInterface class which implements
class method `parse` to handle ingestion of Quotes coming from input file
of .docx file-type.
"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """An ingestor class to extract quotes from .docx input file type.

    This class contains a concrete implementation of IngestorInterface
    `parse` abstract method for `.docx` file type, extracts quote and
    author and constructs the corresponding Quote object.
    """

    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Check input file for correct file extension and extract data.

        Input data is read and parsed into `body` and `author` variables.
        Each Quote objects created is added into a collection and
        returned.
        """
        if not cls.allowed_extension:
            raise Exception('Cannot Ingest Exception!')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.replace('"', '').split(' - ')
                quotes.append(QuoteModel(parsed[0], parsed[1]))
        return quotes
