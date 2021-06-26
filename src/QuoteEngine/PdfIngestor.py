from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess


class PdfIngestor(IngestorInterface):
    allowed_extension = ['pdf']


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.allowed_extension:
            raise Exception('Cannot Ingest Exception!')

        quotes = []
        completed_process = subprocess.run(['pdftotext', '-layout', path], stdout=subprocess.PIPE)
        output = completed_process.stdout

        output_filepath = f'.{path.split(".")[-2:-1][0]}.txt'
        with open(output_filepath, 'r') as f:
            data = f.readlines()

        for line in data:
            stripped_line = line.strip().replace('"', '').split(' - ')
            if len(stripped_line) == 2:
                body, author = stripped_line
                quotes.append(QuoteModel(body, author))
        return quotes
