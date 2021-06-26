from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.allowed_extension:
            raise Exception('Cannot Ingest Exception!')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.replace('"', '').split(' - ')
                quotes.append(QuoteModel(parsed[0], parsed[1]))
        return quotes
