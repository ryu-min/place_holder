from typing import Optional

from place_holder.domain.place_parser import PlaceParser
from place_holder.domain.place import Place, PlaceType


class TestParser(PlaceParser):

    def get_key_word(self) -> str:
        return "test"

    def parse_by_url(self, usr: str) -> Optional[Place]:
        p = Place(PlaceType.RESTAURANT,
                  'test name',
                  'test address',
                  'test description',
                  4)
        return p

