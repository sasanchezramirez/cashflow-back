from app.infrastructure.driven_adapter.persistence.entity.saves_entity import SavesEntity
from app.domain.model.saves import Saves

class SavesMapper:
    @staticmethod
    def map_saves_to_saves_entity(saves: Saves):
        return SavesEntity(
            month=saves.month,
            saves=saves.saves,
            user_id=saves.user_id
        )
    
    @staticmethod
    def map_saves_entity_to_saves(saves_entity: SavesEntity):
        return Saves(
            id=saves_entity.id,
            month=saves_entity.month,
            saves=saves_entity.saves,
            user_id=saves_entity.user_id
        )