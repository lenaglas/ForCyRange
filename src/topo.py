"""
FP topology
"""


from mininet.topo import Topo

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, lg, info
from mininet.topolib import TreeNet
from mininet.link import TCLink

from mininet.node import RemoteController

from utils import LOCK_MAC, HUB_MAC
from utils import LOCK_ADDR, HUB_ADDR, NETMASK


class SmartHomeTopo(Topo):

    """Filling plant (FP): 3 plcs + hmi + attacker"""

    def build(self):

        switch = self.addSwitch('s1')
        
        smartLock = self.addHost(
            'smartLock')
        

        iotHub = self.addHost(
            'iotHub')
        
        
        self.addLink(iotHub,switch)
        self.addLink(smartLock,switch)
        


if __name__ == '__main__':
    lg.setLogLevel( 'info')
    topo = SmartHomeTopo()
    #net = TreeNet( depth=1, waitConnected=True )
    net = Mininet(topo=topo, waitConnected=True, link=TCLink )

    net.addNAT().configDefault()
  
    net.start()
  
    info( "*** Hosts are running and should have internet connectivity\n" )
    info( "*** Type 'exit' or control-D to shut down network\n" )
    
    #CLI(net)
    s1, smartLock, iotHub = net.get('s1', 'smartLock', 'iotHub')
   
    smartLock.cmd('screen -dmSL tank python3 smartDoor.py')
    iotHub.cmd('screen -dmSL iot python3 malware.py')
    CLI( net )
        
        