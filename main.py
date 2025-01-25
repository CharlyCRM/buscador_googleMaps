import os
from dotenv import load_dotenv
from src.services.google_maps_service import GoogleMapsService
from src.services.excel_service import ExcelService

def main():
    load_dotenv()
    
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    if not api_key:
        print("Error: No se encontró la API key de Google Maps")
        return
    
    maps_service = GoogleMapsService(api_key)
    storage_service = ExcelService()
    
    query = input("Introduce el término de búsqueda: ")
    
    print("Buscando empresas...")
    businesses = maps_service.search_businesses(query)
    
    if not businesses:
        print("No se encontraron resultados")
        return
    
    filename = f"resultados_{query.replace(' ', '_')}.xlsx"
    total_saved = storage_service.save_businesses(businesses, filename)
    
    print(f"Se han guardado {total_saved} registros en el archivo {filename}")

if __name__ == "__main__":
    main() 