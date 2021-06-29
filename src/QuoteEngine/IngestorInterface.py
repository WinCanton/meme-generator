"""A Class Interface for Quote Ingestor strategy object.

This is an Abstract Base Class from which document type specific Ingestors
shall be realised.
`allowed_extension` is a Class variable which will be modified by concrete
objects to determine the type of applicable document extension for a Quote
Ingestor.

The `parse` method is implemented as an abstractmethod and will be realised
individually by concrete class implementation.
"""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract Interface class of Ingestor Strategy Object.

    This Interface class will be inherited later on by concrete implementation
    of Ingestor classes. The interface defined in this abstract class enforces
    standards for concrete implementation ingestors.
    `can_ingest` class method is final and will be inherited fully by concrete
    implementations.
    `parse` class method is defined as abstract as concrete implementation
    depends on the type of input-file's extension.
    """

    allowed_extension = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether input data file is of the correct type.

        Concrete implementation of ingestors shall use this method to check
        whether the file type of Quote file is in the `allowed_extension`
        class variable.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Quote from input data file.

        This abstract method shall be realised by concrete implementation
        of individual ingestor class according to the type of input Quote
        data file.
        """
        pass
