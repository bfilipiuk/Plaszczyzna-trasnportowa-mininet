import math
from geopy import Nominatim
from geopy.distance import geodesic
import mininet

miasta = [
    'Berlin',
    'Hamburg',
    'Monachium',
    'Kolonia',
    'Frankfurt nad Menem',
    'Stuttgart',
    'Dusseldorf',
    'Dortmund',
    'Essen',
    'Lipsk'
]


class City:
    def __init__(self, name):
        self.name = name

    def cords(self):
        geolocator = Nominatim(user_agent="Locator")
        location = geolocator.geocode(self.name)

        return location.latitude, location.longitude


def distance(a_cords, b_cords):
    return geodesic(a_cords, b_cords)


def delay(distance_between_cities):
    dist = (str(distance_between_cities * math.sqrt(2) / 200))
    tab = dist.split()

    return str(round(float(tab[0]), 2)) + 'ms'


berlin = City('Berlin')
hamburg = City('Hamburg')
monachium = City('Monachium')
kolonia = City('Kolonia')
frankfurt = City('Frankfurt nad Menem')
stuttgart = City('Stuttgart')
dusseldorf = City('Dusseldorf')
dortmund = City('Dortmund')
essen = City('Essen')
lipsk = City('Lipsk')

delay_berlinlipsk = delay(distance(berlin.cords(), lipsk.cords()))
delay_berlinhamburg = delay(distance(berlin.cords(), hamburg.cords()))
delay_berlinmonachium = delay(distance(berlin.cords(), monachium.cords()))
delay_berlinkolonia = delay(distance(berlin.cords(), kolonia.cords()))
delay_berlinfrankfurt = delay(distance(berlin.cords(), frankfurt.cords()))

delay_koloniaessen = delay(distance(kolonia.cords(), essen.cords()))
delay_koloniadortmund = delay(distance(kolonia.cords(), dortmund.cords()))
delay_koloniadusseldorf = delay(distance(kolonia.cords(), dusseldorf.cords()))

delay_frankfurtstuttgart = delay(distance(frankfurt.cords(), stuttgart.cords()))

print(delay_berlinlipsk)
print(delay_frankfurtstuttgart)
print(delay_berlinkolonia)


def treeNet(net):
    "Create custom topo."
