import abc
from typing import Optional
from place_holder.domain.place import Place

class PlaceParser(abc.ABC):

    @abc.abstractmethod
    def get_key_word(self) -> str:
        pass

    @abc.abstractmethod
    def parse_by_url(self, usr: str) -> Optional[Place]:
        pass