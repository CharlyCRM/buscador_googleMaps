from abc import ABC, abstractmethod
from typing import List
from src.models.business import Business

class MapsService(ABC):
    @abstractmethod
    def search_businesses(self, query: str) -> List[Business]:
        pass 