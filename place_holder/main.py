from place_holder.domain import *

p = Place(PlaceType.RESTAURANT, 'some name', 'some address',
        'some description', 4)

print("p name is", p.name)
print("p description is ", p.description)
print("p rating is", p.rating)


