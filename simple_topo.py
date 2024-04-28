from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def simpleNetwork():
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost
