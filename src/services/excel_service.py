from typing import List
import pandas as pd
from src.models.business import Business
from src.interfaces.storage_service import StorageService

class ExcelService(StorageService):
    def save_businesses(self, businesses: List[Business], filename: str) -> int:
        data = {
            'Nombre': [],
            'Horario': [],
            'Página Web': [],
            'Dirección': [],
            'Teléfono': []
        }
        
        for business in businesses:
            data['Nombre'].append(business.name)
            data['Horario'].append(business.schedule)
            data['Página Web'].append(business.website)
            data['Dirección'].append(business.address)
            data['Teléfono'].append(business.phone)
        
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        
        return len(businesses) 