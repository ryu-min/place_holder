import enum

@enum.unique
class PlaceType(enum.Enum):
    RESTAURANT = 1
    CINEMA = 2
    MUSEUM = 3
    PARK = 4
