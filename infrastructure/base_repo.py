from typing import Generic, List, TypeVar

T = TypeVar('T')


storage: List[T] = []
counter: int = 1


class BaseRepository(Generic[T]):
    def add(self, entity: T) -> T:
        global counter
        entity.id = counter
        storage.append(entity)
        counter += 1
        return entity

    def get(self, entity_id: int) -> T:
        for entity in storage:
            if entity.id == entity_id:
                return entity
        return None

    def get_all(self) -> List[T]:
        return storage

    def update(self, entity_id: int, updated_entity: T) -> T:
        for i in range(len(storage)):
            entity = storage[i]
            if entity.id == entity_id:
                storage[i] = updated_entity
                return updated_entity
        return None

    def delete(self, entity_id: int) -> bool:
        for i in range(len(storage)):
            entity = storage[i]
            if entity.id == entity_id:
                del storage[i]
                return True
        return False
