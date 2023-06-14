from place_holder.domain.place_storage import PlaceStorage
from place_holder.domain.place import Place


class PlaceManager:

    def __init__(self, storage: PlaceStorage):
        self.place_storage = storage

    def add_place(self, place: Place):
        self.place_storage.add_place(place)

    def get_all_places(self) -> list[Place]:
        return self.place_storage.get_all_places()





