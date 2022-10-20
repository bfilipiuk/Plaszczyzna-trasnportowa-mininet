from mininet.topo import Topo


class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        host_berlin = self.addHost('h1', ip='192.168.68.100')
        host_hamburg = self.addHost('h2', ip='192.168.68.101')
        host_monachium = self.addHost('h3', ip='192.168.68.102')
        host_kolonia = self.addHost('h4', ip='192.168.68.103')
        host_frankfurt = self.addHost('h5', ip='192.168.68.104')
        host_stuttgart = self.addHost('h6', ip='192.168.68.105')
        host_dusseldorf = self.addHost('h7', ip='192.168.68.106')
        host_dortmund = self.addHost('h8', ip='192.168.68.107')
        host_essen = self.addHost('h9', ip='192.168.68.108')
        host_lipsk = self.addHost('h10', ip='192.168.68.109')

        switch_berlin = self.addSwitch('s1')
        switch_hamburg = self.addSwitch('s2')
        switch_monachium = self.addSwitch('s3')
        switch_kolonia = self.addSwitch('s4')
        switch_frankfurt = self.addSwitch('s5')
        switch_stuttgart = self.addSwitch('s6')
        switch_dusseldorf = self.addSwitch('s7')
        switch_dortmund = self.addSwitch('s8')
        switch_essen = self.addSwitch('s9')
        switch_lipsk = self.addSwitch('s10')

        self.addLink(host_berlin, switch_berlin, bw=100, delay='0.01ms')
        self.addLink(host_hamburg, switch_hamburg, bw=100, delay='0.01ms')
        self.addLink(host_monachium, switch_monachium, bw=100, delay='0.01ms')
        self.addLink(host_kolonia, switch_kolonia, bw=100, delay='0.01ms')
        self.addLink(host_frankfurt, switch_frankfurt, bw=100, delay='0.01ms')
        self.addLink(host_stuttgart, switch_stuttgart, bw=100, delay='0.01ms')
        self.addLink(host_dusseldorf, switch_dusseldorf, bw=100, delay='0.01ms')
        self.addLink(host_dortmund, switch_dortmund, bw=100, delay='0.01ms')
        self.addLink(host_essen, switch_essen, bw=100, delay='0.01ms')
        self.addLink(host_lipsk, switch_lipsk, bw=100, delay='0.01ms')

        self.addLink(switch_berlin, switch_hamburg, bw=100, delay='1.80ms')
        self.addLink(switch_berlin, switch_kolonia, bw=100, delay='3.38ms')
        self.addLink(switch_berlin, switch_frankfurt, bw=100, delay='2.99ms')
        self.addLink(switch_berlin, switch_lipsk, bw=100, delay='1.05ms')
        self.addLink(switch_berlin, switch_monachium, bw=100, delay='3.56ms')

        self.addLink(switch_kolonia, switch_essen, bw=100, delay='0.41ms')
        self.addLink(switch_kolonia, switch_dusseldorf, bw=100, delay='0.24ms')
        self.addLink(switch_kolonia, switch_dortmund, bw=100, delay='0.52ms')

        self.addLink(switch_frankfurt, switch_stuttgart, bw=100, delay='1.08ms')


topos = {'MyTopo': (lambda: MyTopo())}
