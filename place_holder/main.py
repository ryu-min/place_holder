from place_holder.domain import *
from place_holder.infrastructure.storages.test_storage import TestStorage
from place_holder.infrastructure.parsers.test_parser import TestParser



p = Place(PlaceType.RESTAURANT, 'some name', 'some address',
        'some description', 4)

parsers = list[PlaceParser]()
parsers.append(TestParser())

s = TestStorage()
m = PlaceManager(s, parsers)

m.add_place(p)
m.get_all_places()

received_place = m.parse_url("some url with test")
if received_place:
        print("receive place with name", received_place.name)
else:
        print("not recieve place")


