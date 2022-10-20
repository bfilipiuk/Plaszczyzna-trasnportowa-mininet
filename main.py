from mininet.cli import CLI
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.util import dumpNodeConnections

def treeNet():
    'Create custom topo.'

    topo = Mininet(controller=None, link=TCLink)

    topo.addController('controller1', controller=RemoteController, ip='127.0.0.1', port=6633)

    host_berlin = topo.addHost('h1', ip='192.168.68.100')
    host_hamburg = topo.addHost('h2', ip='192.168.68.101')
    host_monachium = topo.addHost('h3', ip='192.168.68.102')
    host_kolonia = topo.addHost('h4', ip='192.168.68.103')
    host_frankfurt = topo.addHost('h5', ip='192.168.68.104')
    host_stuttgart = topo.addHost('h6', ip='192.168.68.105')
    host_dusseldorf = topo.addHost('h7', ip='192.168.68.106')
    host_dortmund = topo.addHost('h8', ip='192.168.68.107')
    host_essen = topo.addHost('h9', ip='192.168.68.108')
    host_lipsk = topo.addHost('h10', ip='192.168.68.109')

    switch_berlin = topo.addSwitch('s1')
    switch_hamburg = topo.addSwitch('s2')
    switch_monachium = topo.addSwitch('s3')
    switch_kolonia = topo.addSwitch('s4')
    switch_frankfurt = topo.addSwitch('s5')
    switch_stuttgart = topo.addSwitch('s6')
    switch_dusseldorf = topo.addSwitch('s7')
    switch_dortmund = topo.addSwitch('s8')
    switch_essen = topo.addSwitch('s9')
    switch_lipsk = topo.addSwitch('s10')

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

    topo.addLink(switch_berlin, switch_hamburg, bw=100, delay='1.80ms')
    topo.addLink(switch_berlin, switch_kolonia, bw=100, delay='3.38ms')
    topo.addLink(switch_berlin, switch_frankfurt, bw=100, delay='2.99ms')
    topo.addLink(switch_berlin, switch_lipsk, bw=100, delay='1.05ms')
    topo.addLink(switch_berlin, switch_monachium, bw=100, delay='3.56ms')

    topo.addLink(switch_kolonia, switch_essen, bw=100, delay='0.41ms')
    topo.addLink(switch_kolonia, switch_dusseldorf, bw=100, delay='0.24ms')
    topo.addLink(switch_kolonia, switch_dortmund, bw=100, delay='0.52ms')

    topo.addLink(switch_frankfurt, switch_stuttgart, bw=100, delay='1.08ms')

    topo.start()

    dumpNodeConnections(topo.hosts)

    topo.pingAll()

    CLI(topo)

    topo.stop()


if __name__ == '__main__':
    treeNet()
