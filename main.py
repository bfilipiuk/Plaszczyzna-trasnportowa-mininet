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


def treeNet():
    'Create custom topo.'

    topo = Mininet(controller=None, link=TCLink)

    topo.addController('controller1', controller=RemoteController, ip='127.0.0.1', port=6654)

    host_berlin = topo.addHost('host_berlin', ip='192.168.68.100')
    host_hamburg = topo.addHost('host_hamburg', ip='192.168.68.101')
    host_monachium = topo.addHost('host_monachium', ip='192.168.68.102')
    host_kolonia = topo.addHost('host_kolonia', ip='192.168.68.103')
    host_frankfurt = topo.addHost('host_frankfurt', ip='192.168.68.104')
    host_stuttgart = topo.addHost('host_stuttgart', ip='192.168.68.105')
    host_dusseldorf = topo.addHost('host_dusseldorf', ip='192.168.68.106')
    host_dortmund = topo.addHost('host_dortmund', ip='192.168.68.107')
    host_essen = topo.addHost('host_essen', ip='192.168.68.108')
    host_lipsk = topo.addHost('host_lipsk', ip='192.168.68.109')

    switch_berlin = topo.addSwitch('switch_berlin')
    switch_hamburg = topo.addSwitch('switch_hamburg')
    switch_monachium = topo.addSwitch('switch_monachium')
    switch_kolonia = topo.addSwitch('switch_kolonia')
    switch_frankfurt = topo.addSwitch('switch_frankfurt')
    switch_stuttgart = topo.addSwitch('switch_stuttgart')
    switch_dusseldorf = topo.addSwitch('switch_dusseldorf')
    switch_dortmund = topo.addSwitch('switch_dortmund')
    switch_essen = topo.addSwitch('switch_essen')
    switch_lipsk = topo.addSwitch('switch_lipsk')

    topo.addLink(host_berlin, switch_berlin, bw=100, delay='0.01ms')
    topo.addLink(host_hamburg, switch_hamburg, bw=100, delay='0.01ms')
    topo.addLink(host_monachium, switch_monachium, bw=100, delay='0.01ms')
    topo.addLink(host_kolonia, switch_kolonia, bw=100, delay='0.01ms')
    topo.addLink(host_frankfurt, switch_frankfurt, bw=100, delay='0.01ms')
    topo.addLink(host_stuttgart, switch_stuttgart, bw=100, delay='0.01ms')
    topo.addLink(host_dusseldorf, switch_dusseldorf, bw=100, delay='0.01ms')
    topo.addLink(host_dortmund, switch_dortmund, bw=100, delay='0.01ms')
    topo.addLink(host_essen, switch_essen, bw=100, delay='0.01ms')
    topo.addLink(host_lipsk, switch_lipsk, bw=100, delay='0.01ms')

    topo.addLink(switch_berlin, switch_hamburg, bw=100, delay=delay_berlinhamburg)
    topo.addLink(switch_berlin, switch_kolonia, bw=100, delay=delay_berlinkolonia)
    topo.addLink(switch_berlin, switch_frankfurt, bw=100, delay=delay_berlinfrankfurt)
    topo.addLink(switch_berlin, switch_lipsk, bw=100, delay=delay_berlinlipsk)
    topo.addLink(switch_berlin, switch_monachium, bw=100, delay=delay_berlinmonachium)

    topo.addLink(switch_kolonia, switch_essen, bw=100, delay=delay_koloniaessen)
    topo.addLink(switch_kolonia, switch_dusseldorf, bw=100, delay=delay_koloniadusseldorf)
    topo.addLink(switch_kolonia, switch_dortmund, bw=100, delay=delay_koloniadortmund)

    topo.addLink(switch_frankfurt, switch_stuttgart, bw=100, delay=delay_frankfurtstuttgart)

    topo.start()

    dumpNodeConnections(topo.hosts)

    topo.pingAll()

    CLI(topo)

    topo.stop()


if __name__ == '__main__':
    treeNet()
