import layer_setup as ls
import spira.all as spira
from spira.technologies.mit.process.database import RDD
      
# 1.36 Ohm resistor
class res_1p36(spira.Cell):
    __name_prefix__ = 'res_1p36'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.4*ls.tp,height=0.31*ls.tp,center=(0.0,0.155*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.256*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0,0.25625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*ls.tp,0.25625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# 2 Ohm resistor
class res_2(spira.Cell):
    __name_prefix__ = 'res_2'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.2*ls.tp,height=0.3225*ls.tp,center=(0.0,0.16125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.27*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.0,0.27*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*ls.tp,0.27*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# 3.54 Ohm resistor
class res_3p54(spira.Cell):
    __name_prefix__ = 'res_3p54'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0,0.30125*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.355*ls.tp,center=(0.0,0.1775*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.302*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.055*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*ls.tp,0.30125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# 4 Ohm resistor
class res_4(spira.Cell):
    __name_prefix__ = 'res_4'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0,0.32875*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.3825*ls.tp,center=(0.0,0.19125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.328*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.055*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*ls.tp,0.32875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# 5.74 Ohm resistor
class res_5p74(spira.Cell):
    __name_prefix__ = 'res_5p74'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.4825*ls.tp,center=(0.0,0.24125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.428*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0,0.42875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*ls.tp,0.42875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports