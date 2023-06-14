import abc
from place_holder.domain.place import Place


class PlaceStorage(abc.ABC):
    @abc.abstractmethod
    def add_place(self, place: Place):
        pass

    @abc.abstractmethod
    def get_all_places(self) -> list[Place]:
        pass


