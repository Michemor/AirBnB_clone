from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updateed_at = datetime.now()
    
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"
    
    def save(self):
        self.updateed_at = datetime.now()
    
    def to_dict(self):
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updateed_at.isoformat()
        return new_dict