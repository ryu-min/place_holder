from typing import Optional

from place_holder.domain.place_storage import PlaceStorage
from place_holder.domain.place import Place
from place_holder.domain.place_parser import PlaceParser


class PlaceManager:

    def __init__(self, storage: PlaceStorage, parsers: list[PlaceParser]):
        self.place_storage = storage
        self.place_parsers = parsers

    def add_place(self, place: Place):
        self.place_storage.add_place(place)

    def get_all_places(self) -> list[Place]:
        return self.place_storage.get_all_places()

    def parse_url(self, url: str) -> Optional[Place]:
        for p in self.place_parsers:
            key = p.get_key_word()
            if key in url:
                return p.parse_by_url(url)
        return None