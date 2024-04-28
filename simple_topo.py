from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

def simpleNetwork():
    net = Mininet(controller=RemoteController)

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simpleNetwork()
