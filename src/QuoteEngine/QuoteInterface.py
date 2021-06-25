from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class ImportInterface(ABC):
    allowed_extension = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
