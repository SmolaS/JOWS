from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class DumbbellTopo(Topo):
    def build(self):
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')

        r1 = self.addSwitch('r1')

        self.addLink(h1, r1)
        self.addLink(h2, r1)
        self.addLink(r1, h3, bw=10, delay='20ms')

def run():
    setLogLevel('info')
    topo = DumbbellTopo()
    net = Mininet(topo=topo, link=TCLink, switch=OVSKernelSwitch)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
