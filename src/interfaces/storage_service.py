from abc import ABC, abstractmethod
from typing import List
from src.models.business import Business

class StorageService(ABC):
    @abstractmethod
    def save_businesses(self, businesses: List[Business], filename: str) -> int:
        pass 