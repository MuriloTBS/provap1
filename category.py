from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List, Dict, Any
from events.category_events import CategoryCreated, CategoryUpdated, CategoryActivated, CategoryDeactivated

@dataclass
class Category:
    id: str
    name: str
    description: str
    is_active: bool = True
    events: List = field(default_factory=list, init=False)
    
    def __post_init__(self):
        self._validate()
        self.events.append(
            CategoryCreated(
                category_id=self.id,
                timestamp=datetime.now(),
                name=self.name,
                description=self.description,
                is_active=self.is_active
            )
        )
    
    def _validate(self):
        if len(self.name) > 255:
            raise ValueError("Name must be less than 255 characters")
        if len(self.description) > 1024:
            raise ValueError("Description must be less than 1024 characters")
        if not self.name.strip():
            raise ValueError("Name cannot be empty")
    
    def update(self, name: Optional[str] = None, description: Optional[str] = None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        
        self._validate()
        
        self.events.append(
            CategoryUpdated(
                category_id=self.id,
                timestamp=datetime.now(),
                updated_fields={
                    'name': name,
                    'description': description
                }
            )
        )
    
    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.events.append(
                CategoryActivated(
                    category_id=self.id,
                    timestamp=datetime.now()
                )
            )
    
    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.events.append(
                CategoryDeactivated(
                    category_id=self.id,
                    timestamp=datetime.now()
                )
            )
    
    def to_dict(self) -> dict:
        """Exporta o estado da entidade para dicionário"""
        return {
            'class_name': 'Category',
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_active': self.is_active
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Reconstrói uma instância da entidade a partir de dicionário"""
        if data.get('class_name') != 'Category':
            raise ValueError("Invalid data format: class_name must be 'Category'")
        
        required_fields = ['id', 'name', 'description', 'is_active']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            is_active=data['is_active']
        )
    
    def clear_events(self):
        """Limpa a lista de eventos (útil após processamento)"""
        self.events.clear()
    
    def get_events(self) -> List:
        """Retorna uma cópia da lista de eventos"""
        return self.events.copy()