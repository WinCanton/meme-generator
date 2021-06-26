from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    allowed_extension = ['txt']


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.allowed_extension:
            raise Exception('Cannot Ingest Exception!')

        quotes = []
        with open(path, 'r', encoding='utf-8-sig') as f:
            data = f.readlines()

        for line in data:
            body, author = line.strip().split(' - ')
            quotes.append(QuoteModel(body, author))

        return quotes
