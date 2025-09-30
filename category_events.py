from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Any

@dataclass
class DomainEvent:
    category_id: str
    timestamp: datetime
    event_type: str = field(init=False)
    
    def __post_init__(self):
        self.event_type = self.__class__.__name__

@dataclass
class CategoryCreated(DomainEvent):
    name: str = None
    description: str = None
    is_active: bool = True

@dataclass
class CategoryUpdated(DomainEvent):
    updated_fields: Dict[str, Any] = None

@dataclass
class CategoryActivated(DomainEvent):
    pass

@dataclass
class CategoryDeactivated(DomainEvent):
    pass