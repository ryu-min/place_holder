import dataclasses
from place_holder.domain.place_type import PlaceType

@dataclasses.dataclass
class Place:
    type: PlaceType
    name: str
    address: str
    description: str
    rating: int

    def __init__(self, place_type: PlaceType, name: str, address:str, description: str, rating: int):
        self.type = type
        self.name = name
        self.address = address
        self.description = description
        self.rating = rating
