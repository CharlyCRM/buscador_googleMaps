from typing import List
import googlemaps
from src.models.business import Business
from src.interfaces.maps_service import MapsService

class GoogleMapsService(MapsService):
    def __init__(self, api_key: str):
        self.client = googlemaps.Client(key=api_key)

    def search_businesses(self, query: str) -> List[Business]:
        results = []
        
        places_result = self.client.places(query)
        
        for place in places_result.get('results', []):
            place_id = place.get('place_id')
            if place_id:
                details = self.client.place(place_id, fields=[
                    'name', 'formatted_address', 'formatted_phone_number',
                    'website', 'opening_hours'
                ])['result']
                
                business = Business(
                    name=details.get('name', ''),
                    schedule=self._format_schedule(details.get('opening_hours', {}).get('weekday_text', [])),
                    website=details.get('website', ''),
                    address=details.get('formatted_address', ''),
                    phone=details.get('formatted_phone_number', '')
                )
                results.append(business)
        
        return results

    def _format_schedule(self, schedule_list: List[str]) -> str:
        return '; '.join(schedule_list) if schedule_list else '' 