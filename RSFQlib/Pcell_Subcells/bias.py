import layer_setup as ls
import spira.all as spira
from spira.technologies.mit.process.database import RDD

# Bias 51uA cell
class ib_051(spira.Cell):
    __name_prefix__ = 'ib_051'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=3.0825*ls.tp,center=(0.000*ls.tp,1.54125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,3.030*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,3.02875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,3.02875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 53uA cell
class ib_053(spira.Cell):
    __name_prefix__ = 'ib_053'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,2.91875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,2.919*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=2.9725*ls.tp,center=(0.000*ls.tp,1.48625*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,2.91875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 56A cell
class ib_056(spira.Cell):
    __name_prefix__ = 'ib_056'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=2.8225*ls.tp,center=(0.000*ls.tp,1.41125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,2.768*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,2.76875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,2.76875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 60uA cell
class ib_060(spira.Cell):
    __name_prefix__ = 'ib_060'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,2.58875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,2.590*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=2.6425*ls.tp,center=(0.000*ls.tp,1.32125*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,2.58875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 63uA cell
class ib_063(spira.Cell):
    __name_prefix__ = 'ib_063'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=2.3725*ls.tp,center=(0.0625*ls.tp,1.19625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,2.328*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,2.32875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,0.06375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*ls.tp,2.32875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*ls.tp,0.06375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 64uA cell
class ib_064(spira.Cell):
    __name_prefix__ = 'ib_064'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.87125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.871*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.925*ls.tp,center=(0.000*ls.tp,0.9625*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.87125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 66uA cell
class ib_066(spira.Cell):
    __name_prefix__ = 'ib_066'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,2.3475*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,2.348*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=2.400*ls.tp,center=(0.000*ls.tp,1.200*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,2.3475*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 80uA cell
class ib_080(spira.Cell):
    __name_prefix__ = 'ib_080'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.96625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.967*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=2.020*ls.tp,center=(0.000*ls.tp,1.010*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.96625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 81uA cell
class ib_081(spira.Cell):
    __name_prefix__ = 'ib_081'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.84375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.845*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.8975*ls.tp,center=(0.000*ls.tp,0.94875*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.84375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 82uA cell
class ib_082(spira.Cell):
    __name_prefix__ = 'ib_082'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.92125*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.975*ls.tp,center=(0.000*ls.tp,0.9875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.922*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.92125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 87uA cell
class ib_087(spira.Cell):
    __name_prefix__ = 'ib_087'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.81125*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.865*ls.tp,center=(0.000*ls.tp,0.9325*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.811*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.81125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 89uA cell
class ib_089(spira.Cell):
    __name_prefix__ = 'ib_089'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.77375*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.8275*ls.tp,center=(0.000*ls.tp,0.91375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.774*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.77375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 95uA cell
class ib_095(spira.Cell):
    __name_prefix__ = 'ib_095'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.66875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.668*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.7225*ls.tp,center=(0.000*ls.tp,0.86125*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.66875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 97uA cell
class ib_097(spira.Cell):
    __name_prefix__ = 'ib_097'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.640*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.6925*ls.tp,center=(0.000*ls.tp,0.84625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.640*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.640*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 98uA cell
class ib_098(spira.Cell):
    __name_prefix__ = 'ib_098'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.52375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.525*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.5775*ls.tp,center=(0.000*ls.tp,0.78875*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.52375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 99uA cell
class ib_099(spira.Cell):
    __name_prefix__ = 'ib_099'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.61625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.616*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.670*ls.tp,center=(0.000*ls.tp,0.835*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.61625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 102uA cell
class ib_102(spira.Cell):
    __name_prefix__ = 'ib_102'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.570*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.6225*ls.tp,center=(0.000*ls.tp,0.81125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.570*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.570*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 108uA cell
class ib_108(spira.Cell):
    __name_prefix__ = 'ib_108'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.4775*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.530*ls.tp,center=(0.000*ls.tp,0.765*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.478*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.4775*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 112uA cell
class ib_112(spira.Cell):
    __name_prefix__ = 'ib_112'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.43375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.4875*ls.tp,center=(0.000*ls.tp,0.74375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.433*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.43375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 113uA cell
class ib_113(spira.Cell):
    __name_prefix__ = 'ib_113'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.390*ls.tp,center=(0.0625*ls.tp,0.705*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,1.347*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,1.34625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,0.06375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*ls.tp,1.34625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*ls.tp,0.06375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 114uA cell
class ib_114(spira.Cell):
    __name_prefix__ = 'ib_114'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.4625*ls.tp,center=(0.000*ls.tp,0.73125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.410*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.40875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.40875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        
        
# Bias 115uA cell
class ib_115(spira.Cell):
    __name_prefix__ = 'ib_115'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.4525*ls.tp,center=(0.000*ls.tp,0.72625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.398*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.39875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.39875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 122uA cell
class ib_122(spira.Cell):
    __name_prefix__ = 'ib_122'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.3775*ls.tp,center=(0.000*ls.tp,0.68875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.324*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.32375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.32375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 123uA cell
class ib_123(spira.Cell):
    __name_prefix__ = 'ib_123'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.3675*ls.tp,center=(0.000*ls.tp,0.68375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.314*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.31375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.31375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 124uA cell
class ib_124(spira.Cell):
    __name_prefix__ = 'ib_124'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.3575*ls.tp,center=(0.000*ls.tp,0.67875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.304*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.30375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.30375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 128uA cell
class ib_128(spira.Cell):
    __name_prefix__ = 'ib_128'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.245*ls.tp,center=(0.0625*ls.tp,0.6325*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,1.202*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,1.20125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,0.06375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*ls.tp,1.20125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*ls.tp,0.06375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 129uA cell
class ib_129(spira.Cell):
    __name_prefix__ = 'ib_129'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.310*ls.tp,center=(0.0625*ls.tp,0.655*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,1.257*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,1.25625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,0.06375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*ls.tp,1.25625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*ls.tp,0.06375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 131uA cell
class ib_131(spira.Cell):
    __name_prefix__ = 'ib_131'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.220*ls.tp,center=(0.0625*ls.tp,0.620*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,1.177*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,1.17625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,0.06375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*ls.tp,1.17625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*ls.tp,0.06375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 132uA cell
class ib_132(spira.Cell):
    __name_prefix__ = 'ib_132'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.23125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.232*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.285*ls.tp,center=(0.000*ls.tp,0.6425*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.23125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 133uA cell
class ib_133(spira.Cell):
    __name_prefix__ = 'ib_133'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.275*ls.tp,center=(0.000*ls.tp,0.6375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.222*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.2225*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.2225*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 134uA cell
class ib_134(spira.Cell):
    __name_prefix__ = 'ib_134'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.21375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.214*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.2675*ls.tp,center=(0.000*ls.tp,0.63375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.21375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 136uA cell
class ib_136(spira.Cell):
    __name_prefix__ = 'ib_136'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.250*ls.tp,center=(0.000*ls.tp,0.625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.197*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.1975*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.1975*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 139uA cell
class ib_139(spira.Cell):
    __name_prefix__ = 'ib_139'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.2275*ls.tp,center=(0.000*ls.tp,0.61375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.174*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.17375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.17375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 141uA cell
class ib_141(spira.Cell):
    __name_prefix__ = 'ib_141'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.05875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.059*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.1125*ls.tp,center=(0.000*ls.tp,0.55625*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.05875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 142uA cell
class ib_142(spira.Cell):
    __name_prefix__ = 'ib_142'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,1.15125*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.205*ls.tp,center=(0.000*ls.tp,0.6025*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.151*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.15125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 146uA cell
class ib_146(spira.Cell):
    __name_prefix__ = 'ib_146'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.12125*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.175*ls.tp,center=(0.000*ls.tp,0.5875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.122*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.12125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 147uA cell
class ib_147(spira.Cell):
    __name_prefix__ = 'ib_147'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.115*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.1675*ls.tp,center=(0.000*ls.tp,0.58375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.115*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.115*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 148uA cell
class ib_148(spira.Cell):
    __name_prefix__ = 'ib_148'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.0975*ls.tp,center=(0.000*ls.tp,0.54875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.043*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.04375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.04375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 150uA cell
class ib_150(spira.Cell):
    __name_prefix__ = 'ib_150'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.1475*ls.tp,center=(0.000*ls.tp,0.57375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.095*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.09375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.09375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 152uA cell
class ib_152(spira.Cell):
    __name_prefix__ = 'ib_152'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.08125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.080*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.135*ls.tp,center=(0.000*ls.tp,0.5675*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.08125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 153uA cell
class ib_153(spira.Cell):
    __name_prefix__ = 'ib_153'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.130*ls.tp,center=(0.000*ls.tp,0.565*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.075*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.07625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.07625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 155uA cell
class ib_155(spira.Cell):
    __name_prefix__ = 'ib_155'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.0625*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.115*ls.tp,center=(0.000*ls.tp,0.5575*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.063*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.0625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 156uA cell
class ib_156(spira.Cell):
    __name_prefix__ = 'ib_156'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.05625*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.110*ls.tp,center=(0.000*ls.tp,0.555*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.057*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.05625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports    

# Bias 158uA cell
class ib_158(spira.Cell):
    __name_prefix__ = 'ib_158'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.04375*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.0975*ls.tp,center=(0.000*ls.tp,0.54875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.044*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.04375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports          

# Bias 160uA cell
class ib_160(spira.Cell):
    __name_prefix__ = 'ib_160'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.0325*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.085*ls.tp,center=(0.000*ls.tp,0.5425*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.033*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.0325*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 162uA cell
class ib_162(spira.Cell):
    __name_prefix__ = 'ib_162'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,1.02125*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.075*ls.tp,center=(0.000*ls.tp,0.5375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,1.021*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,1.02125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        
        
# Bias 167uA cell
class ib_167(spira.Cell):
    __name_prefix__ = 'ib_167'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.99375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.993*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.0425*ls.tp,center=(0.000*ls.tp,0.52375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.99375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 168uA cell
class ib_168(spira.Cell):
    __name_prefix__ = 'ib_168'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.98875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.988*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.0425*ls.tp,center=(0.000*ls.tp,0.52125*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.98875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 170uA cell
class ib_170(spira.Cell):
    __name_prefix__ = 'ib_170'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.9775*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.978*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.030*ls.tp,center=(0.000*ls.tp,0.515*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.9775*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 171uA cell
class ib_171(spira.Cell):
    __name_prefix__ = 'ib_171'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.9725*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.972*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.025*ls.tp,center=(0.000*ls.tp,0.5125*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.9725*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 173uA cell
class ib_173(spira.Cell):
    __name_prefix__ = 'ib_173'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.015*ls.tp,center=(0.000*ls.tp,0.5075*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.962*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,0.9625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.9625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 175uA cell
class ib_175(spira.Cell):
    __name_prefix__ = 'ib_175'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=1.005*ls.tp,center=(0.000*ls.tp,0.5025*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.952*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,0.95125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.95125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 176uA cell
class ib_176(spira.Cell):
    __name_prefix__ = 'ib_176'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.950*ls.tp,center=(0.000*ls.tp,0.475*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.896*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,0.89625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.89625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 177uA cell
class ib_177(spira.Cell):
    __name_prefix__ = 'ib_177'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.84375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.844*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.8975*ls.tp,center=(0.000*ls.tp,0.44875*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.84375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 178uA cell
class ib_178(spira.Cell):
    __name_prefix__ = 'ib_178'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.940*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.940*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.9925*ls.tp,center=(0.000*ls.tp,0.49625*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.940*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 179uA cell
class ib_179(spira.Cell):
    __name_prefix__ = 'ib_179'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.935*ls.tp,center=(0.0625*ls.tp,0.4775*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,0.891*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,0.89125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,0.06375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*ls.tp,0.89125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*ls.tp,0.06375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 181uA cell
class ib_181(spira.Cell):
    __name_prefix__ = 'ib_181'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.92375*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.9775*ls.tp,center=(0.000*ls.tp,0.48875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.923*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.92375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 183uA cell
class ib_183(spira.Cell):
    __name_prefix__ = 'ib_183'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.915*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.9675*ls.tp,center=(0.000*ls.tp,0.48375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.915*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.915*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 185uA cell
class ib_185(spira.Cell):
    __name_prefix__ = 'ib_185'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.850*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.9075*ls.tp,center=(0.000*ls.tp,0.45375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.855*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.850*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 187uA cell
class ib_187(spira.Cell):
    __name_prefix__ = 'ib_187'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.89625*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.950*ls.tp,center=(0.000*ls.tp,0.475*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.897*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.89625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 192uA cell
class ib_192(spira.Cell):
    __name_prefix__ = 'ib_192'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.930*ls.tp,center=(0.000*ls.tp,0.465*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.877*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.87625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.87625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 193uA cell
class ib_193(spira.Cell):
    __name_prefix__ = 'ib_193'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.9275*ls.tp,center=(0.000*ls.tp,0.46375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.873*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.87375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.87375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports     

# Bias 194uA cell
class ib_194(spira.Cell):
    __name_prefix__ = 'ib_194'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.9225*ls.tp,center=(0.000*ls.tp,0.46125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.869*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.86875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.86875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports          

# Bias 195uA cell
class ib_195(spira.Cell):
    __name_prefix__ = 'ib_195'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.865*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.865*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.9175*ls.tp,center=(0.000*ls.tp,0.45875*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.865*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 196uA cell
class ib_196(spira.Cell):
    __name_prefix__ = 'ib_196'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.86375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.863*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.9175*ls.tp,center=(0.000*ls.tp,0.45875*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.86375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 198uA cell
class ib_198(spira.Cell):
    __name_prefix__ = 'ib_198'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.85375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.853*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.9075*ls.tp,center=(0.000*ls.tp,0.45375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.85375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 200uA cell
class ib_200(spira.Cell):
    __name_prefix__ = 'ib_200'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.84625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.846*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.900*ls.tp,center=(0.000*ls.tp,0.450*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.84625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        
        
# Bias 203uA cell
class ib_203(spira.Cell):
    __name_prefix__ = 'ib_203'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.83375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.835*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.8875*ls.tp,center=(0.000*ls.tp,0.44375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.83375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports      
        
# Bias 206uA cell
class ib_206(spira.Cell):
    __name_prefix__ = 'ib_206'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.8775*ls.tp,center=(0.000*ls.tp,0.43875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.824*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.82375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.82375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports          
        
# Bias 207uA cell
class ib_207(spira.Cell):
    __name_prefix__ = 'ib_207'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.875*ls.tp,center=(0.000*ls.tp,0.4375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.820*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.8215*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.8215*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports         

# Bias 210uA cell
class ib_210(spira.Cell):
    __name_prefix__ = 'ib_210'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.8625*ls.tp,center=(0.000*ls.tp,0.43125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.810*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.810*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.810*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports         
        
# Bias 212uA cell
class ib_212(spira.Cell):
    __name_prefix__ = 'ib_212'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.8575*ls.tp,center=(0.000*ls.tp,0.42875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.803*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.80375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.80375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.06375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 214uA cell
class ib_214(spira.Cell):
    __name_prefix__ = 'ib_214'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.8075*ls.tp,center=(0.0625*ls.tp,0.41375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,0.065*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.0625*ls.tp,0.763*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,0.06375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.0625*ls.tp,0.76375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*ls.tp,0.76375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*ls.tp,0.06375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 218uA cell
class ib_218(spira.Cell):
    __name_prefix__ = 'ib_218'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.8375*ls.tp,center=(0.000*ls.tp,0.41875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.784*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.78375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.78375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 220uA cell
class ib_220(spira.Cell):
    __name_prefix__ = 'ib_220'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.8325*ls.tp,center=(0.000*ls.tp,0.41625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.778*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.77875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.77875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 222uA cell
class ib_222(spira.Cell):
    __name_prefix__ = 'ib_222'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.825*ls.tp,center=(0.000*ls.tp,0.4125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.772*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.77125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.77125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 224uA cell
class ib_224(spira.Cell):
    __name_prefix__ = 'ib_224'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.76625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.766*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.820*ls.tp,center=(0.000*ls.tp,0.410*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.76625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 225uA cell
class ib_225(spira.Cell):
    __name_prefix__ = 'ib_225'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.7625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.763*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.815*ls.tp,center=(0.000*ls.tp,0.4075*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.7625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        
        
# Bias 229uA cell
class ib_229(spira.Cell):
    __name_prefix__ = 'ib_229'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.805*ls.tp,center=(0.000*ls.tp,0.4025*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.751*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.75125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.75125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 230uA cell
class ib_230(spira.Cell):
    __name_prefix__ = 'ib_230'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.8025*ls.tp,center=(0.000*ls.tp,0.40125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.749*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.74875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.74875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 231uA cell
class ib_231(spira.Cell):
    __name_prefix__ = 'ib_231'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.800*ls.tp,center=(0.000*ls.tp,0.400*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.745*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.74625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.74625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 235uA cell
class ib_235(spira.Cell):
    __name_prefix__ = 'ib_235'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.69375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.694*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7475*ls.tp,center=(0.000*ls.tp,0.37375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.69375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 237p5uA cell
class ib_237p5(spira.Cell):
    __name_prefix__ = 'ib_237p5'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.7275*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.728*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.780*ls.tp,center=(0.000*ls.tp,0.390*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.7275*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        
        
# Bias 239uA cell
class ib_239(spira.Cell):
    __name_prefix__ = 'ib_239'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.72375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.724*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7775*ls.tp,center=(0.000*ls.tp,0.38875*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.72375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 241uA cell
class ib_241(spira.Cell):
    __name_prefix__ = 'ib_241'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7325*ls.tp,center=(0.000*ls.tp,0.36625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.679*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.67875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.67875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 242uA cell
class ib_242(spira.Cell):
    __name_prefix__ = 'ib_242'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.770*ls.tp,center=(0.000*ls.tp,0.385*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.716*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.71625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.71625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports      

# Bias 245uA cell
class ib_245(spira.Cell):
    __name_prefix__ = 'ib_245'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7625*ls.tp,center=(0.000*ls.tp,0.38125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.708*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.70875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.70875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 248uA cell
class ib_248(spira.Cell):
    __name_prefix__ = 'ib_248'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.755*ls.tp,center=(0.000*ls.tp,0.3775*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.701*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.70125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.70125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 249uA cell
class ib_249(spira.Cell):
    __name_prefix__ = 'ib_249'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7525*ls.tp,center=(0.000*ls.tp,0.37625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.699*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.69875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.69875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 254uA cell
class ib_254(spira.Cell):
    __name_prefix__ = 'ib_254'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.740*ls.tp,center=(0.000*ls.tp,0.370*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.687*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.68625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.68625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 255uA cell
class ib_255(spira.Cell):
    __name_prefix__ = 'ib_255'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.64875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7025*ls.tp,center=(0.000*ls.tp,0.35125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.648*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.64875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 257uA cell
class ib_257(spira.Cell):
    __name_prefix__ = 'ib_257'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,0.680*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7325*ls.tp,center=(0.000*ls.tp,0.36625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.680*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.680*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 260uA cell
class ib_260(spira.Cell):
    __name_prefix__ = 'ib_260'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7275*ls.tp,center=(0.000*ls.tp,0.36375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.673*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.67375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.67375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 262uA cell
class ib_262(spira.Cell):
    __name_prefix__ = 'ib_262'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7225*ls.tp,center=(0.000*ls.tp,0.36125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.669*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.66875*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.66875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 267uA cell
class ib_267(spira.Cell):
    __name_prefix__ = 'ib_267'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7125*ls.tp,center=(0.000*ls.tp,0.35625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.658*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.65875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.65875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports         
        
# Bias 268uA cell
class ib_268(spira.Cell):
    __name_prefix__ = 'ib_268'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.710*ls.tp,center=(0.000*ls.tp,0.355*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.656*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,0.65625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.65625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 271uA cell
class ib_271(spira.Cell):
    __name_prefix__ = 'ib_271'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.7025*ls.tp,center=(0.000*ls.tp,0.35125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.650*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,0.650*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.650*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 273uA cell
class ib_273(spira.Cell):
    __name_prefix__ = 'ib_273'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.700*ls.tp,center=(0.000*ls.tp,0.350*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.646*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,0.64625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.64625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 275uA cell
class ib_275(spira.Cell):
    __name_prefix__ = 'ib_275'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.695*ls.tp,center=(0.000*ls.tp,0.3475*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.642*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.64125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.64125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 276uA cell
class ib_276(spira.Cell):
    __name_prefix__ = 'ib_276'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.60625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.606*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.660*ls.tp,center=(0.000*ls.tp,0.330*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.60625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 280uA cell
class ib_280(spira.Cell):
    __name_prefix__ = 'ib_280'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.63125*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.685*ls.tp,center=(0.000*ls.tp,0.3425*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.632*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.63125*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 283uA cell
class ib_283(spira.Cell):
    __name_prefix__ = 'ib_283'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.62625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.626*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.680*ls.tp,center=(0.000*ls.tp,0.340*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.62625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 284uA cell
class ib_284(spira.Cell):
    __name_prefix__ = 'ib_284'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.5925*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.592*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.645*ls.tp,center=(0.000*ls.tp,0.3225*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.5925*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 292uA cell
class ib_292(spira.Cell):
    __name_prefix__ = 'ib_292'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.610*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.610*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.6625*ls.tp,center=(0.000*ls.tp,0.33125*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.610*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports        

# Bias 304uA cell
class ib_304(spira.Cell):
    __name_prefix__ = 'ib_304'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.125*ls.tp,center=(0.000*ls.tp,0.590*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.6425*ls.tp,center=(0.000*ls.tp,0.32125*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.590*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.680*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 312uA cell
class ib_312(spira.Cell):
    __name_prefix__ = 'ib_312'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.54875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.548*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.6025*ls.tp,center=(0.000*ls.tp,0.30125*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.54875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 315uA cell
class ib_315(spira.Cell):
    __name_prefix__ = 'ib_315'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.54375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.5975*ls.tp,center=(0.000*ls.tp,0.29875*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.543*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.54375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 328uA cell
class ib_328(spira.Cell):
    __name_prefix__ = 'ib_328'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.45375*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.455*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.5075*ls.tp,center=(0.000*ls.tp,0.25375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.45375*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 340uA cell
class ib_340(spira.Cell):
    __name_prefix__ = 'ib_340'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.5925*ls.tp,center=(0.000*ls.tp,0.29625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.538*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.53875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.53875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 350uA cell
class ib_350(spira.Cell):
    __name_prefix__ = 'ib_350'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.580*ls.tp,center=(0.000*ls.tp,0.290*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.525*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.52625*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.52625*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# Bias 373uA cell
class ib_373(spira.Cell):
    __name_prefix__ = 'ib_373'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=0.115*ls.tp,height=0.5525*ls.tp,center=(0.000*ls.tp,0.27625*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.499*ls.tp))
        elems += spira.Box(layer=ls.C5R,width=0.052*ls.tp,height=0.052*ls.tp,center=(0.000*ls.tp,0.055*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.49875*ls.tp))
        elems += spira.Box(layer=ls.M6,width=0.125*ls.tp,height=0.1275*ls.tp,center=(0.000*ls.tp,0.05375*ls.tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.000*ls.tp,0.49875*ls.tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.000*ls.tp,0.05375*ls.tp),process=spira.RDD.PROCESS.M6)

        return ports