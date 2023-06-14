from place_holder.domain import *
from place_holder.infrastructure.storages.test_storage import TestStorage

p = Place(PlaceType.RESTAURANT, 'some name', 'some address',
        'some description', 4)

s = TestStorage()
m = PlaceManager(s)

m.add_place(p)
m.get_all_places()


