from place_holder.domain import PlaceStorage, Place


class TestStorage(PlaceStorage):

    def add_place(self, place: Place):
        print("call add place in test storage")

    def get_all_places(self) -> list[Place]:
        print("call get all places from test storage")
        return list()