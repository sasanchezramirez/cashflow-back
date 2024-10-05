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
    def map_update_priority_dto_to_priority(update_priority_dto: UpdatePriorityInput) -> Priority:
        return Priority(
            id=update_priority_dto.id,
            description=update_priority_dto.description,
            user_id=update_priority_dto.user_id
        )