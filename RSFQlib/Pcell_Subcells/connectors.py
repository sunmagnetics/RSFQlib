import layer_setup as ls
import spira.all as spira
from spira.technologies.mit.process.database import RDD

# M4 to M7 connector cell
class conn_M4M5M6M7(spira.Cell):
    __name_prefix__ = 'conn_M4M5M6M7'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M4,width=0.14*ls.tp,height=0.14*ls.tp,center=(0.07*ls.tp,0.07*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.08*ls.tp,height=0.08*ls.tp,center=(0.07*ls.tp,0.07*ls.tp))
        shape = spira.Shape(points=[
            [0.16,-0.015],[0.16,0.0],[0.0,0.0],[0.0,0.14],
            [0.16,0.14],[0.16,0.155],[0.33,0.155],[0.33,-0.015]
            ])
        shape = [x * ls.tp for x in shape]
        elems += spira.Polygon(shape=shape, layer=ls.M5)
        elems += spira.Box(layer=ls.I5,width=0.070*ls.tp,height=0.070*ls.tp,center=(0.245*ls.tp,0.070*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.315*ls.tp,height=0.140*ls.tp,center=(0.1575*ls.tp,0.070*ls.tp))
        elems += spira.Box(layer=ls.I6,width=0.070*ls.tp,height=0.070*ls.tp,center=(0.070*ls.tp,0.070*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.140*ls.tp,height=0.140*ls.tp,center=(0.070*ls.tp,0.070*ls.tp))

        return elems
        
    def create_ports(self,ports):
        ports += spira.Port(name="M6:P",midpoint=(0.1575*ls.tp,0.070*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# M4 to M7 connector block
class conn_M4M5M6M7_block(spira.Cell):
    __name_prefix__ = 'conn_M4M5M6M7_block'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M4,width=0.295*ls.tp,height=0.295*ls.tp,center=(0.00*ls.tp,0.00*ls.tp))
        elems += spira.Box(layer=ls.M7,width=0.29*ls.tp,height=0.29*ls.tp,center=(0.00*ls.tp,0.00*ls.tp))
        elems += spira.Box(layer=ls.I6,width=0.07*ls.tp,height=0.07*ls.tp,center=(-0.07*ls.tp,0.07*ls.tp))
        elems += spira.Box(layer=ls.I6,width=0.07*ls.tp,height=0.07*ls.tp,center=(0.07*ls.tp,-0.07*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.07*ls.tp,height=0.07*ls.tp,center=(-0.1*ls.tp,-0.1*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.07*ls.tp,height=0.07*ls.tp,center=(0.1*ls.tp,0.1*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.08*ls.tp,height=0.08*ls.tp,center=(-0.0775*ls.tp,0.0775*ls.tp))
        elems += spira.Box(layer=ls.I4,width=0.08*ls.tp,height=0.08*ls.tp,center=(0.0775*ls.tp,-0.0775*ls.tp))
        shape = spira.Shape(points=[(-0.17*ls.tp,-0.17*ls.tp),(-0.17*ls.tp,-0.03*ls.tp),(-0.145*ls.tp,-0.03*ls.tp),
                                    (-0.145*ls.tp,0.145*ls.tp),(0.03*ls.tp,0.145*ls.tp),(0.03*ls.tp,0.17*ls.tp),
                                    (0.17*ls.tp,0.17*ls.tp),(0.17*ls.tp,0.03*ls.tp),(0.145*ls.tp,0.03*ls.tp),
                                    (0.145*ls.tp,-0.145*ls.tp),(-0.03*ls.tp,-0.145*ls.tp),(-0.03*ls.tp,-0.17*ls.tp)])
        elems += spira.Polygon(layer=ls.M6,shape=shape)
        shape = spira.Shape(points=[(-0.185*ls.tp,-0.185*ls.tp),(-0.185*ls.tp,-0.015*ls.tp),(-0.147*ls.tp,-0.015*ls.tp),
                                    (-0.1475*ls.tp,0.1475*ls.tp),(0.015*ls.tp,0.1475*ls.tp),(0.015*ls.tp,0.185*ls.tp),
                                    (0.185*ls.tp,0.185*ls.tp),(0.185*ls.tp,0.015*ls.tp),(0.147*ls.tp,0.015*ls.tp),
                                    (0.1475*ls.tp,-0.1475*ls.tp),(-0.015*ls.tp,-0.1475*ls.tp),(-0.015*ls.tp,-0.185*ls.tp)])
        elems += spira.Polygon(layer=ls.M5,shape=shape)
        return elems

# M5 to M6 connector cell
class conn_M5M6(spira.Cell):
    __name_prefix__ = 'conn_M5M6'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.17*ls.tp,height=0.17*ls.tp,center=(0.085*ls.tp,0.085*ls.tp))
        elems += spira.Box(layer=ls.I5,width=0.07*ls.tp,height=0.07*ls.tp,center=(0.085*ls.tp,0.085*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.14*ls.tp,height=0.14*ls.tp,center=(0.085*ls.tp,0.085*ls.tp))
        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PV",midpoint=(0.085*ls.tp,0.085*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# M5 to M7 connector cell
class conn_M5M6M7(spira.Cell):
    __name_prefix__ = 'conn_M5M6M7'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.7,height=1.7,center=(0.35,0.35))
        elems += spira.Box(layer=ls.I5,width=0.7,height=0.7,center=(0.35,0.35))
        elems += spira.Box(layer=ls.M6,width=2.0,height=2.0,center=(0.35,0.35))
        elems += spira.Box(layer=ls.I6,width=1.3,height=1.3,center=(0.35,0.35))
        elems += spira.Box(layer=ls.M7,width=2.0,height=2.0,center=(0.35,0.35))

        return elems