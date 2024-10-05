from app.infrastructure.entry_point.dto.priorities_dto import NewPriorityInput, UpdatePriorityInput
from app.domain.model.priority import Priority
from app.infrastructure.driven_adapter.persistence.entity.priorities_entity import PrioritiesEntity

class PrioritiesMapper:
    @staticmethod
    def map_new_priority_dto_to_priority(new_priority_dto: NewPriorityInput) -> Priority:
        return Priority(
            description=new_priority_dto.description,
            user_id=new_priority_dto.user_id
        )

    @staticmethod
    def map_priority_to_priority_entity(priority: Priority) -> PrioritiesEntity:
        return PrioritiesEntity(
            description=priority.description
        )
    
    @staticmethod
    def map_priority_entity_to_priority(priority_entity: PrioritiesEntity) -> Priority:
        return Priority(
            id=priority_entity.id,
            description=priority_entity.description
        )
    
    @staticmethod
    def map_priority_update_to_priority_entity(priority: Priority, existing_priority: PrioritiesEntity) -> PrioritiesEntity:
        existing_priority.description = priority.description
        return existing_priority