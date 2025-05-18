from typing import Dict, Optional
from app.schemas import SOAPNote, GenerateNoteResponse
import uuid

class MockDB:
    def __init__(self):
        self.visits: Dict[str, GenerateNoteResponse] = {}
    
    def store_visit(self, response: GenerateNoteResponse) -> str:
        visit_id = str(uuid.uuid4())
        self.visits[visit_id] = response
        return visit_id
    
    def get_visit(self, visit_id: str) -> Optional[GenerateNoteResponse]:
        return self.visits.get(visit_id)
    
    def update_visit(self, visit_id: str, response: GenerateNoteResponse) -> bool:
        if visit_id in self.visits:
            self.visits[visit_id] = response
            return True
        return False

# Create a singleton instance
db = MockDB() 