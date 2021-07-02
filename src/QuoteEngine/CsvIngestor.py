"""An ingestor class for ingesting Quotes from input data file of type: `.csv`.

This is a concrete implementation of IngestorInterface class which implements
class method `parse` to handle ingestion of Quotes coming from input file
of .csv file-type.
"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas as pd


class CsvIngestor(IngestorInterface):
    """An ingestor class to extract quotes from .csv input file type.

    This class contains a concrete implementation of IngestorInterface
    `parse` abstract method for `.csv` file type, extracts quote and
    author and constructs the corresponding Quote object.
    """

    allowed_extension = ['csv']

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
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            quotes.append(QuoteModel(row['body'], row['author']))

        return quotes
