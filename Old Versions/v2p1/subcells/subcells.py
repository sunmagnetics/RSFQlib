import spira.all as spira
from spira.technologies.mit.process.database import RDD

# Shorthand for long layer names
M0 = spira.RDD.PLAYER.M0.METAL
I0 = spira.RDD.PLAYER.I0.VIA
M1 = spira.RDD.PLAYER.M1.METAL
I1 = spira.RDD.PLAYER.I1.VIA
M2 = spira.RDD.PLAYER.M2.METAL
I2 = spira.RDD.PLAYER.I2.VIA
M3 = spira.RDD.PLAYER.M3.METAL
I3 = spira.RDD.PLAYER.I3.VIA
M4 = spira.RDD.PLAYER.M4.GND
I4 = spira.RDD.PLAYER.I4.VIA
M5 = spira.RDD.PLAYER.M5.METAL
J5 = spira.RDD.PLAYER.J5.JUNCTION
R5 = spira.RDD.PLAYER.R5.METAL
I5 = spira.RDD.PLAYER.I5.VIA
C5J = spira.RDD.PLAYER.C5J.VIA
C5R = spira.RDD.PLAYER.C5R.VIA
M6 = spira.RDD.PLAYER.M6.METAL
I6 = spira.RDD.PLAYER.I6.VIA
M7 = spira.RDD.PLAYER.M7.METAL

# Shorthand for rotations and reflections
r90 = spira.Rotation(90)
r180 = spira.Rotation(180)
r270 = spira.Rotation(270)
m0 = spira.Reflection(True)
m45 = r270 + spira.Reflection(True)
m90 = r180 + spira.Reflection(True)
m135 = r90 + spira.Reflection(True)
m270 = m135

# trackpitch
tp = 10

# 2 Ohm resistor
class ls_res_2(spira.Cell):
    __name_prefix__ = 'ls_res_2'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.2*tp,height=0.3225*tp,center=(0.0,0.16125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.27*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,0.27*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*tp,0.27*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# 1.5um junction fill cell
class ls_FakeJJ_1p5x1p5um(spira.Device):
    __name_prefix__ = 'ls_FakeJJ_1p5x1p5um'
    def create_elements(self, elems):
        elems += spira.Box(layer=M4,width=0.25*tp,height=0.25*tp)
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.25*tp)
        elems += spira.Box(layer=J5,width=0.15*tp,height=0.15*tp)
        elems += spira.Box(layer=C5J,width=0.13*tp,height=0.13*tp)
        elems += spira.Box(layer=M6,width=0.2*tp,height=0.2*tp)

        return elems

# 3um junction fill cell
class ls_FakeJJ_3umx3um(spira.Cell):
    __name_prefix__ = 'ls_FakeJJ_3umx3um'
    def create_elements(self, elems):
        elems += spira.Box(layer=M4,width=0.4*tp,height=0.4*tp)
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.4*tp)
        elems += spira.Box(layer=J5,width=0.3*tp,height=0.3*tp)
        elems += spira.Box(layer=C5J,width=0.28*tp,height=0.28*tp)
        elems += spira.Box(layer=M6,width=0.35*tp,height=0.35*tp)

        return elems

# M4 to M7 connector cell
class ls_conn_M4M5M6M7(spira.Cell):
    __name_prefix__ = 'ls_conn_M4M5M6M7'
    def create_elements(self, elems):
        elems += spira.Box(layer=M4,width=0.14*tp,height=0.14*tp,center=(0.07*tp,0.07*tp))
        elems += spira.Box(layer=I4,width=0.08*tp,height=0.08*tp,center=(0.07*tp,0.07*tp))
        shape = spira.Shape(points=[
            [0.16,-0.015],[0.16,0.0],[0.0,0.0],[0.0,0.14],
            [0.16,0.14],[0.16,0.155],[0.33,0.155],[0.33,-0.015]
            ])
        shape = [x * tp for x in shape]
        elems += spira.Polygon(shape=shape, layer=M5)
        elems += spira.Box(layer=I5,width=0.07*tp,height=0.07*tp,center=(0.245*tp,0.07*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.14*tp,center=(0.1575*tp,0.07*tp))
        elems += spira.Box(layer=I6,width=0.07*tp,height=0.07*tp,center=(0.07*tp,0.07*tp))
        elems += spira.Box(layer=M7,width=0.14*tp,height=0.14*tp,center=(0.07*tp,0.07*tp))

        return elems

# M4 to M7 connector block
class ls_conn_M4M5M6M7_block(spira.Cell):
    __name_prefix__ = 'ls_conn_M4M5M6M7_block'
    def create_elements(self, elems):
        elems += spira.Box(layer=M4,width=0.295*tp,height=0.295*tp,center=(0.00*tp,0.00*tp))
        elems += spira.Box(layer=M7,width=0.29*tp,height=0.29*tp,center=(0.00*tp,0.00*tp))
        elems += spira.Box(layer=I6,width=0.07*tp,height=0.07*tp,center=(-0.07*tp,0.07*tp))
        elems += spira.Box(layer=I6,width=0.07*tp,height=0.07*tp,center=(0.07*tp,-0.07*tp))
        elems += spira.Box(layer=I5,width=0.07*tp,height=0.07*tp,center=(-0.1*tp,-0.1*tp))
        elems += spira.Box(layer=I5,width=0.07*tp,height=0.07*tp,center=(0.1*tp,0.1*tp))
        elems += spira.Box(layer=I4,width=0.08*tp,height=0.08*tp,center=(-0.0775*tp,0.0775*tp))
        elems += spira.Box(layer=I4,width=0.08*tp,height=0.08*tp,center=(0.0775*tp,-0.0775*tp))
        shape = spira.Shape(points=[(-0.17*tp,-0.17*tp),(-0.17*tp,-0.03*tp),(-0.145*tp,-0.03*tp),
                                    (-0.145*tp,0.145*tp),(0.03*tp,0.145*tp),(0.03*tp,0.17*tp),
                                    (0.17*tp,0.17*tp),(0.17*tp,0.03*tp),(0.145*tp,0.03*tp),
                                    (0.145*tp,-0.145*tp),(-0.03*tp,-0.145*tp),(-0.03*tp,-0.17*tp)])
        elems += spira.Polygon(layer=M6,shape=shape)
        shape = spira.Shape(points=[(-0.185*tp,-0.185*tp),(-0.185*tp,-0.015*tp),(-0.147*tp,-0.015*tp),
                                    (-0.1475*tp,0.1475*tp),(0.015*tp,0.1475*tp),(0.015*tp,0.185*tp),
                                    (0.185*tp,0.185*tp),(0.185*tp,0.015*tp),(0.147*tp,0.015*tp),
                                    (0.1475*tp,-0.1475*tp),(-0.015*tp,-0.1475*tp),(-0.015*tp,-0.185*tp)])
        elems += spira.Polygon(layer=M5,shape=shape)
        return elems

# M5 to M6 connector cell
class ls_conn_M5M6(spira.Cell):
    __name_prefix__ = 'ls_conn_M5M6'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=0.17*tp,height=0.17*tp,center=(0.085*tp,0.085*tp))
        elems += spira.Box(layer=I5,width=0.07*tp,height=0.07*tp,center=(0.085*tp,0.085*tp))
        elems += spira.Box(layer=M6,width=0.14*tp,height=0.14*tp,center=(0.085*tp,0.085*tp))
        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PV",midpoint=(0.085*tp,0.085*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 51A cell
class ls_ib_051(spira.Cell):
    __name_prefix__ = 'ls_ib_051'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=3.0825*tp,center=(0.0,1.54125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,3.03*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,3.02875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,3.02875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 53uA cell
class ls_ib_053(spira.Cell):
    __name_prefix__ = 'ls_ib_053'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,2.91875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,2.919*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=2.9725*tp,center=(0.0*tp,1.48625*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,2.91875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 56A cell
class ls_ib_056(spira.Cell):
    __name_prefix__ = 'ls_ib_056'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=2.8225*tp,center=(0.0,1.41125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,2.768*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,2.76875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,2.76875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 60uA cell
class ls_ib_060(spira.Cell):
    __name_prefix__ = 'ls_ib_060'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,2.58875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,2.59*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=2.6425*tp,center=(0.0*tp,1.32125*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,2.58875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 63uA cell
class ls_ib_063(spira.Cell):
    __name_prefix__ = 'ls_ib_063'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=2.3725*tp,center=(0.0625*tp,1.19625*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,0.065*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,2.328*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,2.32875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,0.06375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*tp,2.32875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*tp,0.06375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 64uA cell
class ls_ib_064(spira.Cell):
    __name_prefix__ = 'ls_ib_064'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.87125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.871*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.925*tp,center=(0.0*tp,0.9625*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.87125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 66uA cell
class ls_ib_066(spira.Cell):
    __name_prefix__ = 'ls_ib_066'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,2.3475*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,2.348*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=2.4*tp,center=(0.0*tp,1.2*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,2.3475*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 80uA cell
class ls_ib_080(spira.Cell):
    __name_prefix__ = 'ls_ib_080'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.96625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.967*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=2.02*tp,center=(0.0*tp,1.01*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.96625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 81uA cell
class ls_ib_081(spira.Cell):
    __name_prefix__ = 'ls_ib_081'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.84375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.845*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.8975*tp,center=(0.0*tp,0.94875*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.84375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 82uA cell
class ls_ib_082(spira.Cell):
    __name_prefix__ = 'ls_ib_082'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,1.92125*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.975*tp,center=(0.0,0.9875*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.922*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.92125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 87uA cell
class ls_ib_087(spira.Cell):
    __name_prefix__ = 'ls_ib_087'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,1.81125*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.865*tp,center=(0.0,0.9325*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.811*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.81125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 89uA cell
class ls_ib_089(spira.Cell):
    __name_prefix__ = 'ls_ib_089'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,1.77375*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.8275*tp,center=(0.0,0.91375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.774*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.77375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 95uA cell
class ls_ib_095(spira.Cell):
    __name_prefix__ = 'ls_ib_095'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.66875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.668*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.7225*tp,center=(0.0*tp,0.86125*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.66875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 97uA cell
class ls_ib_097(spira.Cell):
    __name_prefix__ = 'ls_ib_097'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.64*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.6925*tp,center=(0.0,0.84625*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.64*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.64*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 98uA cell
class ls_ib_098(spira.Cell):
    __name_prefix__ = 'ls_ib_098'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.52375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.525*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.5775*tp,center=(0.0*tp,0.78875*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.52375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 99uA cell
class ls_ib_099(spira.Cell):
    __name_prefix__ = 'ls_ib_099'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.61625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.616*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.67*tp,center=(0.0*tp,0.835*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.61625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 102uA cell
class ls_ib_102(spira.Cell):
    __name_prefix__ = 'ls_ib_102'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.57*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.6225*tp,center=(0.0,0.81125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.57*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.57*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 108uA cell
class ls_ib_108(spira.Cell):
    __name_prefix__ = 'ls_ib_108'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.4775*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.53*tp,center=(0.0,0.765*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.478*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.4775*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 112uA cell
class ls_ib_112(spira.Cell):
    __name_prefix__ = 'ls_ib_112'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.43375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.4875*tp,center=(0.0,0.74375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.433*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.43375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 113uA cell
class ls_ib_113(spira.Cell):
    __name_prefix__ = 'ls_ib_113'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.39*tp,center=(0.0625*tp,0.705*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,1.347*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,0.065*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,1.34625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,0.06375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*tp,1.34625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*tp,0.06375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 123uA cell
class ls_ib_123(spira.Cell):
    __name_prefix__ = 'ls_ib_123'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.3675*tp,center=(0.0,0.68375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.314*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,1.31375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.31375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 128uA cell
class ls_ib_128(spira.Cell):
    __name_prefix__ = 'ls_ib_128'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.245*tp,center=(0.0625*tp,0.6325*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,1.202*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,0.065*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,1.20125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,0.06375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*tp,1.20125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*tp,0.06375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 131uA cell
class ls_ib_131(spira.Cell):
    __name_prefix__ = 'ls_ib_131'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.22*tp,center=(0.0625*tp,0.62*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,1.177*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,0.065*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,1.17625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,0.06375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*tp,1.17625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*tp,0.06375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 132uA cell
class ls_ib_132(spira.Cell):
    __name_prefix__ = 'ls_ib_132'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.23125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.232*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.285*tp,center=(0.0*tp,0.6425*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.23125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 133uA cell
class ls_ib_133(spira.Cell):
    __name_prefix__ = 'ls_ib_133'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.275*tp,center=(0.0,0.6375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.222*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,1.2225*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.2225*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 134uA cell
class ls_ib_134(spira.Cell):
    __name_prefix__ = 'ls_ib_134'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.21375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.214*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.2675*tp,center=(0.0*tp,0.63375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.21375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 136uA cell
class ls_ib_136(spira.Cell):
    __name_prefix__ = 'ls_ib_136'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.25*tp,center=(0.0,0.625*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.197*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,1.1975*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.1975*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 141uA cell
class ls_ib_141(spira.Cell):
    __name_prefix__ = 'ls_ib_141'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.05875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.059*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.1125*tp,center=(0.0*tp,0.55625*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.05875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 142uA cell
class ls_ib_142(spira.Cell):
    __name_prefix__ = 'ls_ib_142'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,1.15125*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.205*tp,center=(0.0,0.6025*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.151*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.15125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 146uA cell
class ls_ib_146(spira.Cell):
    __name_prefix__ = 'ls_ib_146'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.12125*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.175*tp,center=(0.0,0.5875*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.122*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.12125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 148uA cell
class ls_ib_148(spira.Cell):
    __name_prefix__ = 'ls_ib_148'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.0975*tp,center=(0.0,0.54875*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.043*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.04375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.04375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 150uA cell
class ls_ib_150(spira.Cell):
    __name_prefix__ = 'ls_ib_150'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.1475*tp,center=(0.0,0.57375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.095*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.09375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.09375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 152uA cell
class ls_ib_152(spira.Cell):
    __name_prefix__ = 'ls_ib_152'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,1.08125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,1.08*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.135*tp,center=(0.0*tp,0.5675*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,1.08125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 153uA cell
class ls_ib_153(spira.Cell):
    __name_prefix__ = 'ls_ib_153'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.13*tp,center=(0.0,0.565*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.075*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.07625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.07625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 155uA cell
class ls_ib_155(spira.Cell):
    __name_prefix__ = 'ls_ib_155'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.0625*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.115*tp,center=(0.0,0.5575*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.063*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.0625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 160uA cell
class ls_ib_160(spira.Cell):
    __name_prefix__ = 'ls_ib_160'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.0325*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.085*tp,center=(0.0,0.5425*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.033*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.0325*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 168uA cell
class ls_ib_168(spira.Cell):
    __name_prefix__ = 'ls_ib_168'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.98875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.988*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.0425*tp,center=(0.0*tp,0.52125*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.98875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 173uA cell
class ls_ib_173(spira.Cell):
    __name_prefix__ = 'ls_ib_173'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.015*tp,center=(0.0,0.5075*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.962*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,0.9625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.9625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 175uA cell
class ls_ib_175(spira.Cell):
    __name_prefix__ = 'ls_ib_175'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.005*tp,center=(0.0,0.5025*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.952*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,0.95125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.95125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 176uA cell
class ls_ib_176(spira.Cell):
    __name_prefix__ = 'ls_ib_176'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.95*tp,center=(0.0,0.475*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.896*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,0.89625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.89625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 177uA cell
class ls_ib_177(spira.Cell):
    __name_prefix__ = 'ls_ib_177'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.84375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.844*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.8975*tp,center=(0.0*tp,0.44875*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.84375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 178uA cell
class ls_ib_178(spira.Cell):
    __name_prefix__ = 'ls_ib_178'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.94*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.94*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.9925*tp,center=(0.0*tp,0.49625*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.94*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 179uA cell
class ls_ib_179(spira.Cell):
    __name_prefix__ = 'ls_ib_179'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.935*tp,center=(0.0625*tp,0.4775*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,0.891*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,0.065*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,0.89125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,0.06375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*tp,0.89125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*tp,0.06375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 181uA cell
class ls_ib_181(spira.Cell):
    __name_prefix__ = 'ls_ib_181'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.92375*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.9775*tp,center=(0.0,0.48875*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.923*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.92375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 185uA cell
class ls_ib_185(spira.Cell):
    __name_prefix__ = 'ls_ib_185'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.85*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.9075*tp,center=(0.0,0.45375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.855*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.85*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 187uA cell
class ls_ib_187(spira.Cell):
    __name_prefix__ = 'ls_ib_187'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.89625*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.95*tp,center=(0.0,0.475*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.897*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.89625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 192uA cell
class ls_ib_192(spira.Cell):
    __name_prefix__ = 'ls_ib_192'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.93*tp,center=(0.0,0.465*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.877*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.87625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.87625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 195uA cell
class ls_ib_195(spira.Cell):
    __name_prefix__ = 'ls_ib_195'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.865*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.865*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.9175*tp,center=(0.0*tp,0.45875*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.865*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 196uA cell
class ls_ib_196(spira.Cell):
    __name_prefix__ = 'ls_ib_196'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.86375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.863*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.9175*tp,center=(0.0*tp,0.45875*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.86375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 198uA cell
class ls_ib_198(spira.Cell):
    __name_prefix__ = 'ls_ib_198'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.85375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.853*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.9075*tp,center=(0.0*tp,0.45375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.85375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 214uA cell
class ls_ib_214(spira.Cell):
    __name_prefix__ = 'ls_ib_214'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.8075*tp,center=(0.0625*tp,0.41375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,0.065*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0625*tp,0.763*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,0.06375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0625*tp,0.76375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0625*tp,0.76375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0625*tp,0.06375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 220uA cell
class ls_ib_220(spira.Cell):
    __name_prefix__ = 'ls_ib_220'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.8325*tp,center=(0.0,0.41625*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.778*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.77875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.77875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 224uA cell
class ls_ib_224(spira.Cell):
    __name_prefix__ = 'ls_ib_224'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.76625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.766*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.82*tp,center=(0.0*tp,0.41*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.76625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 230uA cell
class ls_ib_230(spira.Cell):
    __name_prefix__ = 'ls_ib_230'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.8025*tp,center=(0.0,0.40125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.749*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.74875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.74875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 235uA cell
class ls_ib_235(spira.Cell):
    __name_prefix__ = 'ls_ib_235'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.69375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.694*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.7475*tp,center=(0.0*tp,0.37375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.69375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 241uA cell
class ls_ib_241(spira.Cell):
    __name_prefix__ = 'ls_ib_241'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.7325*tp,center=(0.0,0.36625*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.679*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.67875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.67875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 248uA cell
class ls_ib_248(spira.Cell):
    __name_prefix__ = 'ls_ib_248'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.755*tp,center=(0.0,0.3775*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.701*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.70125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.70125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 254uA cell
class ls_ib_254(spira.Cell):
    __name_prefix__ = 'ls_ib_254'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.74*tp,center=(0.0,0.37*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.687*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.68625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.68625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 255uA cell
class ls_ib_255(spira.Cell):
    __name_prefix__ = 'ls_ib_255'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.64875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.7025*tp,center=(0.0,0.35125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.648*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.64875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 257uA cell
class ls_ib_257(spira.Cell):
    __name_prefix__ = 'ls_ib_257'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,0.68*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.7325*tp,center=(0.0,0.36625*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.68*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.68*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 260uA cell
class ls_ib_260(spira.Cell):
    __name_prefix__ = 'ls_ib_260'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.7275*tp,center=(0.0,0.36375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.673*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.67375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.67375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 262uA cell
class ls_ib_262(spira.Cell):
    __name_prefix__ = 'ls_ib_262'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.7225*tp,center=(0.0,0.36125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.669*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.66875*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.66875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 271uA cell
class ls_ib_271(spira.Cell):
    __name_prefix__ = 'ls_ib_271'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.7025*tp,center=(0.0,0.35125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.65*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,0.65*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.65*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 275uA cell
class ls_ib_275(spira.Cell):
    __name_prefix__ = 'ls_ib_275'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.695*tp,center=(0.0,0.3475*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.642*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.64125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.64125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 276uA cell
class ls_ib_276(spira.Cell):
    __name_prefix__ = 'ls_ib_276'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.60625*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.606*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.66*tp,center=(0.0*tp,0.33*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.60625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 280uA cell
class ls_ib_280(spira.Cell):
    __name_prefix__ = 'ls_ib_280'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.63125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.685*tp,center=(0.0,0.3425*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.632*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.63125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 284uA cell
class ls_ib_284(spira.Cell):
    __name_prefix__ = 'ls_ib_284'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.5925*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.592*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.645*tp,center=(0.0*tp,0.3225*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.5925*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 304uA cell
class ls_ib_304(spira.Cell):
    __name_prefix__ = 'ls_ib_304'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,0.59*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.6425*tp,center=(0.0,0.32125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.59*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.68*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 312uA cell
class ls_ib_312(spira.Cell):
    __name_prefix__ = 'ls_ib_312'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.54875*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.548*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.6025*tp,center=(0.0*tp,0.30125*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.54875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 315uA cell
class ls_ib_315(spira.Cell):
    __name_prefix__ = 'ls_ib_315'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.54375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.5975*tp,center=(0.0,0.29875*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.543*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.54375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 328uA cell
class ls_ib_328(spira.Cell):
    __name_prefix__ = 'ls_ib_328'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.45375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0*tp,0.05375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.455*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0*tp,0.055*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.5075*tp,center=(0.0*tp,0.25375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0*tp,0.45375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 340uA cell
class ls_ib_340(spira.Cell):
    __name_prefix__ = 'ls_ib_340'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.5925*tp,center=(0.0,0.29625*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.538*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.53875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.53875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 350uA cell
class ls_ib_350(spira.Cell):
    __name_prefix__ = 'ls_ib_350'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.58*tp,center=(0.0,0.29*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.525*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.52625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.52625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 63uA shunted cell
class ls_jj_063_s(spira.Cell):
    __name_prefix__ = 'ls_jj_063_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,8.5625))
        elems += spira.Box(layer=M6,width=1.7,height=2.925,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,7.81))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.43))
        elems += spira.Box(layer=R5,width=1.15,height=7.45,center=(0.0,4.625))
        elems += spira.Box(layer=M5,width=1.75,height=7.925,center=(0.0,6.1375))
        elems += spira.Box(layer=M5,width=2.0,height=3.175,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,9.225))
        elems += spira.Circle(layer=C5J,box_size=(0.66, 0.66))
        elems += spira.Circle(layer=J5,box_size=(0.95, 0.95))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 72uA shunted and grounded cell
class ls_jj_072_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_072_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,8.2))
        elems += spira.Box(layer=M6,width=1.75,height=3.0,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.8875))
        elems += spira.Box(layer=M5,width=2.05,height=3.25,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=7.2,center=(0.0,5.825))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,8.55))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.49))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,7.13))
        elems += spira.Box(layer=R5,width=1.15,height=6.725,center=(0.0,4.3125))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.5))
        elems += spira.Circle(layer=C5J,box_size=(0.7, 0.7))
        elems += spira.Circle(layer=J5,box_size=(1.1, 1.1))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 74uA shunted cell
class ls_jj_074_s(spira.Cell):
    __name_prefix__ = 'ls_jj_074_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=7.05,center=(0.0,5.75))
        elems += spira.Box(layer=M5,width=2.05,height=3.25,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.02, 1.02))
        elems += spira.Box(layer=R5,width=1.15,height=6.575,center=(0.0,4.2375))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,8.4))
        elems += spira.Circle(layer=C5J,box_size=(0.72, 0.72))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.5))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,7.0))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,7.75))
        elems += spira.Box(layer=M6,width=2.05,height=3.0,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 75uA shunted and grounded cell
class ls_jj_075_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_075_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.975))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.6625))
        elems += spira.Box(layer=M6,width=1.8,height=3.0,center=(0.0,0.6))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.91))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.47))
        elems += spira.Box(layer=R5,width=1.15,height=6.5,center=(0.0,4.2))
        elems += spira.Box(layer=M5,width=1.75,height=7.0,center=(0.0,5.7))
        elems += spira.Box(layer=M5,width=2.1,height=3.25,center=(0.0,0.575))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,8.325))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.525))
        elems += spira.Circle(layer=C5J,box_size=(0.72, 0.72))
        elems += spira.Circle(layer=J5,box_size=(1.03, 1.03))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 77uA shunted cell
class ls_jj_077_s(spira.Cell):
    __name_prefix__ = 'ls_jj_077_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.8,height=3.05,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.5625))
        elems += spira.Box(layer=M5,width=2.1,height=3.3,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=6.85,center=(0.0,5.675))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,8.225))
        elems += spira.Box(layer=R5,width=1.15,height=6.375,center=(0.0,4.1625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.51))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.81))
        elems += spira.Circle(layer=C5J,box_size=(0.74, 0.74))
        elems += spira.Circle(layer=J5,box_size=(1.04, 1.04))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 77uA shunted and grounded cell
class ls_jj_077_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_077_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.875))
        elems += spira.Box(layer=M6,width=1.8,height=3.05,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.5625))
        elems += spira.Box(layer=M5,width=2.1,height=3.3,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=6.85,center=(0.0,5.675))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,8.225))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.525))
        elems += spira.Box(layer=R5,width=1.15,height=6.375,center=(0.0,4.1625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.51))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.81))
        elems += spira.Circle(layer=C5J,box_size=(0.74, 0.74))
        elems += spira.Circle(layer=J5,box_size=(1.04, 1.04))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 78uA shunted cell
class ls_jj_078_s(spira.Cell):
    __name_prefix__ = 'ls_jj_078_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.4875))
        elems += spira.Box(layer=M6,width=1.8,height=3.025,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.73))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.48))
        elems += spira.Box(layer=R5,width=1.15,height=6.325,center=(0.0,4.1125))
        elems += spira.Box(layer=M5,width=1.75,height=6.8,center=(0.0,5.625))
        elems += spira.Box(layer=M5,width=2.1,height=3.275,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,8.15))
        elems += spira.Circle(layer=C5J,box_size=(0.74, 0.74))
        elems += spira.Circle(layer=J5,box_size=(1.05, 1.05))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 80uA shunted and grounded cell
class ls_jj_080_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_080_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.7))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,8.05))
        elems += spira.Box(layer=M6,width=1.8,height=3.05,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.3875))
        elems += spira.Box(layer=M5,width=2.1,height=3.3,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=5.5875,center=(0.0,6.675))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.525))
        elems += spira.Box(layer=R5,width=1.15,height=6.2,center=(0.0,4.075))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.51))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.64))
        elems += spira.Circle(layer=J5,box_size=(1.06, 1.06))
        elems += spira.Circle(layer=C5J,box_size=(0.76, 0.76))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 81uA shunted and grounded cell
class ls_jj_081_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_081_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.3125))
        elems += spira.Box(layer=M6,width=1.8,height=3.025,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.56))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.49))
        elems += spira.Box(layer=R5,width=1.15,height=6.15,center=(0.0,4.025))
        elems += spira.Box(layer=M5,width=1.75,height=6.625,center=(0.0,5.5375))
        elems += spira.Box(layer=M5,width=2.1,height=3.275,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.975))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.525))
        elems += spira.Circle(layer=C5J,box_size=(0.76, 0.76))
        elems += spira.Circle(layer=J5,box_size=(1.07, 1.07))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 83uA shunted and grounded cell
class ls_jj_083_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_083_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.55))
        elems += spira.Box(layer=M6,width=1.85,height=3.075,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.2375))
        elems += spira.Box(layer=M5,width=2.15,height=3.325,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=6.525,center=(0.0,5.5125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.52))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.49))
        elems += spira.Box(layer=R5,width=1.15,height=6.025,center=(0.0,4.0125))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.55))
        elems += spira.Circle(layer=C5J,box_size=(0.78, 0.78))
        elems += spira.Circle(layer=J5,box_size=(1.04, 1.04))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 86uA shunted and grounded cell
class ls_jj_086_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_086_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.4))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.0875))
        elems += spira.Box(layer=M6,width=1.85,height=3.1,center=(0.0,0.625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.34))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.53))
        elems += spira.Box(layer=R5,width=1.15,height=5.875,center=(0.0,3.9375))
        elems += spira.Box(layer=M5,width=1.75,height=6.35,center=(0.0,5.45))
        elems += spira.Box(layer=M5,width=2.15,height=3.35,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.75))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.55))
        elems += spira.Circle(layer=C5J,box_size=(0.8, 0.8))
        elems += spira.Circle(layer=J5,box_size=(1.1, 1.1))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 88uA shunted and grounded cell
class ls_jj_088_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_088_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.3))
        elems += spira.Box(layer=R5,width=1.15,height=5.775,center=(0.0,3.8625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.22))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.51))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,6.975))
        elems += spira.Box(layer=M6,width=1.85,height=3.075,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=6.25,center=(0.0,5.375))
        elems += spira.Box(layer=M5,width=2.15,height=3.325,center=(0.0,0.5875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.55))
        elems += spira.Circle(layer=C5J,box_size=(0.8, 0.8))
        elems += spira.Circle(layer=J5,box_size=(1.11, 1.11))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 89uA shunted and grounded cell
class ls_jj_089_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_089_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.25))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.55))
        elems += spira.Box(layer=M5,width=1.75,height=6.225,center=(0.0,5.3625))
        elems += spira.Box(layer=M5,width=2.15,height=3.325,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.6))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.9375))
        elems += spira.Box(layer=M6,width=1.85,height=3.075,center=(0.0,0.6125))
        elems += spira.Box(layer=R5,width=1.15,height=5.75,center=(0.0,3.85))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.18))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.52))
        elems += spira.Circle(layer=J5,box_size=(1.11, 1.11))
        elems += spira.Circle(layer=C5J,box_size=(0.824, 0.824))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 90uA shunted and grounded cell
class ls_jj_090_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_090_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.2))
        elems += spira.Box(layer=R5,width=1.15,height=5.7,center=(0.0,3.825))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.14))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.52))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.8875))
        elems += spira.Box(layer=M6,width=1.85,height=3.075,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=6.175,center=(0.0,5.3375))
        elems += spira.Box(layer=M5,width=2.15,height=3.325,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.55))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.55))
        elems += spira.Circle(layer=C5J,box_size=(0.82, 0.82))
        elems += spira.Circle(layer=J5,box_size=(1.12, 1.12))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 93uA shunted and grounded cell
class ls_jj_093_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_093_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.1))
        elems += spira.Box(layer=M6,width=1.9,height=3.15,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.7875))
        elems += spira.Box(layer=M5,width=2.2,height=3.4,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=6.025,center=(0.0,5.3125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.45))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.55))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.04))
        elems += spira.Box(layer=R5,width=1.15,height=5.55,center=(0.0,3.8))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.575))
        elems += spira.Circle(layer=C5J,box_size=(0.84, 0.84))
        elems += spira.Circle(layer=J5,box_size=(1.14, 1.14))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 94uA shunted and grounded cell
class ls_jj_094_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_094_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.05))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,6.725))
        elems += spira.Box(layer=M6,width=1.9,height=3.125,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.97))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.53))
        elems += spira.Box(layer=R5,width=1.15,height=5.5,center=(0.0,3.75))
        elems += spira.Box(layer=M5,width=1.75,height=5.975,center=(0.0,5.2625))
        elems += spira.Box(layer=M5,width=2.2,height=3.375,center=(0.0,0.5875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.575))
        elems += spira.Circle(layer=C5J,box_size=(0.84, 0.84))
        elems += spira.Circle(layer=J5,box_size=(1.14, 1.14))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 95uA shunted cell
class ls_jj_095_s(spira.Cell):
    __name_prefix__ = 'ls_jj_095_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=5.475,center=(0.0,3.7375))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.94))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.53))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.6875))
        elems += spira.Box(layer=M6,width=1.9,height=3.125,center=(0.0,0.6125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.35))
        elems += spira.Box(layer=M5,width=1.75,height=5.95,center=(0.0,5.25))
        elems += spira.Box(layer=M5,width=2.2,height=3.375,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.15, 1.15))
        elems += spira.Circle(layer=C5J,box_size=(0.84, 0.84))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 99uA shunted and grounded cell
class ls_jj_099_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_099_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.875))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.5625))
        elems += spira.Box(layer=M6,width=1.9,height=3.15,center=(0.0,0.625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.81))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.57))
        elems += spira.Box(layer=R5,width=1.15,height=5.325,center=(0.0,3.6875))
        elems += spira.Box(layer=M5,width=1.75,height=5.8,center=(0.0,5.2))
        elems += spira.Box(layer=M5,width=2.2,height=3.4,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.225))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.575))
        elems += spira.Circle(layer=C5J,box_size=(0.86, 0.86))
        elems += spira.Circle(layer=J5,box_size=(1.17, 1.17))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 100uA shunted and grounded cell
class ls_jj_100_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_100_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.825))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.5125))
        elems += spira.Box(layer=M6,width=1.95,height=3.15,center=(0.0,0.6))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.75))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.55))
        elems += spira.Box(layer=R5,width=1.15,height=5.275,center=(0.0,3.6625))
        elems += spira.Box(layer=M5,width=1.75,height=5.775,center=(0.0,5.1625))
        elems += spira.Box(layer=M5,width=2.25,height=3.4,center=(0.0,0.575))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.175))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.6))
        elems += spira.Circle(layer=C5J,box_size=(0.88, 0.88))
        elems += spira.Circle(layer=J5,box_size=(1.18, 1.18))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 104uA shunted and grounded cell
class ls_jj_104_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_104_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.725))
        elems += spira.Box(layer=M6,width=1.95,height=3.2,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,6.4))
        elems += spira.Box(layer=M5,width=2.25,height=3.45,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=5.6,center=(0.0,5.125))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.6))
        elems += spira.Box(layer=R5,width=1.15,height=5.125,center=(0.0,3.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.58))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.65))
        elems += spira.Circle(layer=C5J,box_size=(0.9, 0.9))
        elems += spira.Circle(layer=J5,box_size=(1.2, 1.2))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 107uA shunted cell
class ls_jj_107_s(spira.Cell):
    __name_prefix__ = 'ls_jj_107_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.95))
        elems += spira.Box(layer=M6,width=1.95,height=3.175,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.2875))
        elems += spira.Box(layer=M5,width=2.25,height=3.425,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=5.525,center=(0.0,5.0625))
        elems += spira.Box(layer=R5,width=1.15,height=5.05,center=(0.0,3.55))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.57))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.53))
        elems += spira.Circle(layer=J5,box_size=(1.21, 1.21))
        elems += spira.Circle(layer=C5J,box_size=(0.92, 0.92))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 109uA shunted and grounded cell
class ls_jj_109_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_109_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.55))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.6))
        elems += spira.Box(layer=M5,width=1.75,height=5.45,center=(0.0,5.025))
        elems += spira.Box(layer=M5,width=2.25,height=3.425,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.22, 1.22))
        elems += spira.Box(layer=R5,width=1.15,height=4.975,center=(0.0,3.5125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6))
        elems += spira.Circle(layer=C5J,box_size=(0.92, 0.92))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.57))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.47))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,6.225))
        elems += spira.Box(layer=M6,width=1.95,height=3.175,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 113uA shunted cell
class ls_jj_113_s(spira.Cell):
    __name_prefix__ = 'ls_jj_113_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=4.85,center=(0.0,3.5))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.39))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.61))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.1375))
        elems += spira.Box(layer=M6,width=2.0,height=3.25,center=(0.0,0.625))
        elems += spira.Box(layer=M5,width=1.75,height=5.325,center=(0.0,5.0125))
        elems += spira.Box(layer=M5,width=2.3,height=3.5,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.8))
        elems += spira.Circle(layer=C5J,box_size=(0.94, 0.94))
        elems += spira.Circle(layer=J5,box_size=(1.24, 1.24))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 116uA shunted and grounded cell
class ls_jj_116_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_116_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.35))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.7))
        elems += spira.Box(layer=M6,width=2.0,height=3.225,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.0375))
        elems += spira.Box(layer=M5,width=2.3,height=3.475,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=5.25,center=(0.0,4.95))
        elems += spira.Box(layer=R5,width=1.15,height=4.775,center=(0.0,3.4375))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.59))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.29))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.625))
        elems += spira.Circle(layer=J5,box_size=(1.26, 1.26))
        elems += spira.Circle(layer=C5J,box_size=(0.96, 0.96))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 117uA shunted cell
class ls_jj_117_s(spira.Cell):
    __name_prefix__ = 'ls_jj_117_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=5.225,center=(0.0,4.9375))
        elems += spira.Box(layer=M5,width=2.3,height=3.475,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.27, 1.27))
        elems += spira.Box(layer=R5,width=1.15,height=4.75,center=(0.0,3.425))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.675))
        elems += spira.Circle(layer=C5J,box_size=(0.96, 0.96))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.59))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.26))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.0125))
        elems += spira.Box(layer=M6,width=2.0,height=3.225,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 117uA shunted and grounded cell
class ls_jj_117_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_117_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.325))
        elems += spira.Box(layer=M5,width=1.75,height=5.225,center=(0.0,4.9375))
        elems += spira.Box(layer=M5,width=2.3,height=3.475,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.27, 1.27))
        elems += spira.Box(layer=R5,width=1.15,height=4.75,center=(0.0,3.425))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.675))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.625))
        elems += spira.Circle(layer=C5J,box_size=(0.96, 0.96))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.59))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.26))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.0125))
        elems += spira.Box(layer=M6,width=2.0,height=3.225,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 119uA shunted cell
class ls_jj_119_s(spira.Cell):
    __name_prefix__ = 'ls_jj_119_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=5.175,center=(0.0,4.9375))
        elems += spira.Box(layer=M5,width=2.35,height=3.525,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.28, 1.28))
        elems += spira.Box(layer=R5,width=1.15,height=4.675,center=(0.0,3.4375))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.65))
        elems += spira.Circle(layer=C5J,box_size=(0.98, 0.98))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.62))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.24))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.9875))
        elems += spira.Box(layer=M6,width=2.05,height=3.275,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 121uA shunted and grounded cell
class ls_jj_121_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_121_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.25))
        elems += spira.Box(layer=M6,width=2.05,height=3.275,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.9125))
        elems += spira.Box(layer=M5,width=2.35,height=3.525,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=5.1,center=(0.0,4.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.6))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.17))
        elems += spira.Box(layer=R5,width=1.15,height=4.625,center=(0.0,3.3875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.65))
        elems += spira.Circle(layer=C5J,box_size=(0.98, 0.98))
        elems += spira.Circle(layer=J5,box_size=(1.29, 1.29))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 122uA shunted cell
class ls_jj_122_s(spira.Cell):
    __name_prefix__ = 'ls_jj_122_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=2.05,height=3.3,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,5.925))
        elems += spira.Box(layer=M5,width=2.35,height=3.55,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=5.075,center=(0.0,4.9125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.575))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.65))
        elems += spira.Box(layer=R5,width=1.15,height=4.6,center=(0.0,3.4))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.63))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.17))
        elems += spira.Circle(layer=C5J,box_size=(1.0, 1.0))
        elems += spira.Circle(layer=J5,box_size=(1.29, 1.29))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 122uA shunted and grounded cell
class ls_jj_122_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_122_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.25))
        elems += spira.Box(layer=M6,width=2.05,height=3.3,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,5.925))
        elems += spira.Box(layer=M5,width=2.35,height=3.55,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=5.075,center=(0.0,4.9125))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.65))
        elems += spira.Box(layer=R5,width=1.15,height=4.6,center=(0.0,3.4))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.63))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.17))
        elems += spira.Circle(layer=C5J,box_size=(1.0, 1.0))
        elems += spira.Circle(layer=J5,box_size=(1.29, 1.29))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 125uA shunted and grounded cell
class ls_jj_125_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_125_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.175))
        elems += spira.Box(layer=M6,width=2.05,height=3.3,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.8625))
        elems += spira.Box(layer=M5,width=2.35,height=3.55,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=5.025,center=(0.0,4.8875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.525))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.65))
        elems += spira.Box(layer=R5,width=1.15,height=4.55,center=(0.0,3.375))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.64))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.11))
        elems += spira.Circle(layer=C5J,box_size=(1.0, 1.0))
        elems += spira.Circle(layer=J5,box_size=(1.31, 1.31))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 126uA shunted cell
class ls_jj_126_s(spira.Cell):
    __name_prefix__ = 'ls_jj_126_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=5,center=(0.0,4.875))
        elems += spira.Box(layer=M5,width=2.35,height=3.55,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.31, 1.31))
        elems += spira.Box(layer=R5,width=1.15,height=4.525,center=(0.0,3.3625))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.5))
        elems += spira.Circle(layer=C5J,box_size=(1.02, 1.02))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.64))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.09))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.8375))
        elems += spira.Box(layer=M6,width=2.05,height=3.3,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 126uA shunted and grounded cell
class ls_jj_126_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_126_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.15))
        elems += spira.Box(layer=R5,width=1.15,height=4.525,center=(0.0,3.3625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.09))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.64))
        elems += spira.Box(layer=M5,width=1.75,height=5,center=(0.0,4.875))
        elems += spira.Box(layer=M5,width=2.35,height=3.55,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.31, 1.31))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.5))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.65))
        elems += spira.Circle(layer=C5J,box_size=(1.02, 1.02))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.8375))
        elems += spira.Box(layer=M6,width=2.05,height=3.3,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 129uA shunted cell
class ls_jj_129_s(spira.Cell):
    __name_prefix__ = 'ls_jj_129_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.775))
        elems += spira.Box(layer=M6,width=2.1,height=3.325,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=4.925,center=(0.0,4.8375))
        elems += spira.Box(layer=M5,width=2.4,height=3.575,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.425))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.03))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.65))
        elems += spira.Box(layer=R5,width=1.15,height=4.425,center=(0.0,3.3375))
        elems += spira.Circle(layer=C5J,box_size=(1.02, 1.02))
        elems += spira.Circle(layer=J5,box_size=(1.33, 1.33))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 131uA shunted cell
class ls_jj_131_s(spira.Cell):
    __name_prefix__ = 'ls_jj_131_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.7375))
        elems += spira.Box(layer=M6,width=2.1,height=3.35,center=(0.0,0.625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.99))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.65))
        elems += spira.Box(layer=R5,width=1.15,height=4.4,center=(0.0,3.325))
        elems += spira.Box(layer=M5,width=1.75,height=4.875,center=(0.0,4.8375))
        elems += spira.Box(layer=M5,width=2.4,height=3.6,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.4))
        elems += spira.Circle(layer=C5J,box_size=(1.04, 1.04))
        elems += spira.Circle(layer=J5,box_size=(1.34, 1.34))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 132uA shunted and grounded cell
class ls_jj_132_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_132_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,6.0))
        elems += spira.Box(layer=R5,width=1.15,height=4.375,center=(0.0,3.2875))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.94))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.63))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.6875))
        elems += spira.Box(layer=M6,width=2.1,height=3.325,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=4.85,center=(0.0,4.8))
        elems += spira.Box(layer=M5,width=2.4,height=3.575,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.35))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.675))
        elems += spira.Circle(layer=C5J,box_size=(1.04, 1.04))
        elems += spira.Circle(layer=J5,box_size=(1.34, 1.34))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 134uA shunted cell
class ls_jj_134_s(spira.Cell):
    __name_prefix__ = 'ls_jj_134_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.325))
        elems += spira.Box(layer=M6,width=2.1,height=3.325,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.6625))
        elems += spira.Box(layer=M5,width=2.4,height=3.575,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=4.825,center=(0.0,4.7875))
        elems += spira.Box(layer=R5,width=1.15,height=4.35,center=(0.0,3.275))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.63))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.91))
        elems += spira.Circle(layer=J5,box_size=(1.35, 1.35))
        elems += spira.Circle(layer=C5J,box_size=(1.04, 1.04))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 135uA shunted cell
class ls_jj_135_s(spira.Cell):
    __name_prefix__ = 'ls_jj_135_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=2.1,height=3.325,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.6375))
        elems += spira.Box(layer=M5,width=2.4,height=3.575,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=4.8,center=(0.0,4.775))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.3))
        elems += spira.Box(layer=R5,width=1.15,height=4.325,center=(0.0,3.2625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.64))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.89))
        elems += spira.Circle(layer=C5J,box_size=(1.06, 1.06))
        elems += spira.Circle(layer=J5,box_size=(1.35, 1.35))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 136uA shunted cell
class ls_jj_136_s(spira.Cell):
    __name_prefix__ = 'ls_jj_136_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.6375))
        elems += spira.Box(layer=M6,width=2.1,height=3.35,center=(0.0,0.625))
        elems += spira.Box(layer=M5,width=1.75,height=4.775,center=(0.0,4.7875))
        elems += spira.Box(layer=M5,width=2.4,height=3.6,center=(0.0,0.6))
        elems += spira.Box(layer=R5,width=1.15,height=4.3,center=(0.0,3.275))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.66))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.3))
        elems += spira.Circle(layer=C5J,box_size=(1.06, 1.06))
        elems += spira.Circle(layer=J5,box_size=(1.36, 1.36))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 137uA shunted and grounded cell
class ls_jj_137_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_137_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.95))
        elems += spira.Box(layer=M6,width=2.1,height=3.35,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.6375))
        elems += spira.Box(layer=M5,width=2.4,height=3.6,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=4.775,center=(0.0,4.7875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.3))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.67))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.88))
        elems += spira.Box(layer=R5,width=1.15,height=4.3,center=(0.0,3.275))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.675))
        elems += spira.Circle(layer=C5J,box_size=(1.06, 1.06))
        elems += spira.Circle(layer=J5,box_size=(1.26, 1.26))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 138uA shunted cell
class ls_jj_138_s(spira.Cell):
    __name_prefix__ = 'ls_jj_138_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=4.75,center=(0.0,4.75))
        elems += spira.Box(layer=M5,width=2.4,height=3.575,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.37, 1.37))
        elems += spira.Box(layer=R5,width=1.15,height=4.275,center=(0.0,3.2375))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.25))
        elems += spira.Circle(layer=C5J,box_size=(1.06, 1.06))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.64))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.84))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.5875))
        elems += spira.Box(layer=M6,width=2.1,height=3.325,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 140uA shunted and grounded cell
class ls_jj_140_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_140_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.9))
        elems += spira.Box(layer=R5,width=1.15,height=4.225,center=(0.0,3.2375))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.8))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.65))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.5625))
        elems += spira.Box(layer=M6,width=2.15,height=3.35,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=4.725,center=(0.0,4.7375))
        elems += spira.Box(layer=M5,width=2.45,height=3.6,center=(0.0,0.575))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.7))
        elems += spira.Circle(layer=J5,box_size=(1.38, 1.38))
        elems += spira.Circle(layer=C5J,box_size=(1.08, 1.08))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 141uA shunted and grounded cell
class ls_jj_141_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_141_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.85))
        elems += spira.Box(layer=M6,width=2.15,height=3.35,center=(0.0,0.6))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.5375))
        elems += spira.Box(layer=M5,width=2.45,height=3.6,center=(0.0,0.575))
        elems += spira.Box(layer=M5,width=1.75,height=4.7,center=(0.0,4.725))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.2))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.7))
        elems += spira.Box(layer=R5,width=1.15,height=4.2,center=(0.0,3.225))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.65))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.79))
        elems += spira.Circle(layer=C5J,box_size=(1.08, 1.08))
        elems += spira.Circle(layer=J5,box_size=(1.38, 1.38))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 142uA shunted and grounded cell
class ls_jj_142_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_142_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.875))
        elems += spira.Box(layer=M6,width=2.15,height=3.4,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.5375))
        elems += spira.Box(layer=M5,width=2.45,height=3.65,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=4.65,center=(0.0,4.75))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.7))
        elems += spira.Box(layer=R5,width=1.15,height=4.175,center=(0.0,3.2375))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.68))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.8))
        elems += spira.Circle(layer=C5J,box_size=(1.08, 1.08))
        elems += spira.Circle(layer=J5,box_size=(1.39, 1.39))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 144uA shunted cell
class ls_jj_144_s(spira.Cell):
    __name_prefix__ = 'ls_jj_144_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=4.15,center=(0.0,3.225))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.76))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.68))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.5125))
        elems += spira.Box(layer=M6,width=2.15,height=3.4,center=(0.0,0.625))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.175))
        elems += spira.Box(layer=M5,width=1.75,height=4.625,center=(0.0,4.7375))
        elems += spira.Box(layer=M5,width=2.45,height=3.65,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.4, 1.4))
        elems += spira.Circle(layer=C5J,box_size=(1.1, 1.1))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 145uA shunted cell
class ls_jj_145_s(spira.Cell):
    __name_prefix__ = 'ls_jj_145_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=4.6,center=(0.0,4.7))
        elems += spira.Box(layer=M5,width=2.45,height=3.625,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.125))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,5.475))
        elems += spira.Box(layer=M6,width=2.15,height=3.375,center=(0.0,0.6125))
        elems += spira.Box(layer=R5,width=1.15,height=4.125,center=(0.0,3.1875))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.72))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.66))
        elems += spira.Circle(layer=J5,box_size=(1.4, 1.4))
        elems += spira.Circle(layer=C5J,box_size=(1.1, 1.1))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 149uA shunted cell
class ls_jj_149_s(spira.Cell):
    __name_prefix__ = 'ls_jj_149_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=2.15,height=3.4,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.4375))
        elems += spira.Box(layer=M5,width=2.45,height=3.65,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=4.55,center=(0.0,4.7))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.1))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.69))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.69))
        elems += spira.Box(layer=R5,width=1.15,height=4.075,center=(0.0,3.1875))
        elems += spira.Circle(layer=C5J,box_size=(1.12, 1.12))
        elems += spira.Circle(layer=J5,box_size=(1.42, 1.42))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 150uA shunted cell
class ls_jj_150_s(spira.Cell):
    __name_prefix__ = 'ls_jj_150_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.05))
        elems += spira.Box(layer=R5,width=1.15,height=4.05,center=(0.0,3.15))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.65))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.67))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,5.4))
        elems += spira.Box(layer=M6,width=2.15,height=3.375,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=4.525,center=(0.0,4.6625))
        elems += spira.Box(layer=M5,width=2.45,height=3.625,center=(0.0,0.5875))
        elems += spira.Circle(layer=C5J,box_size=(1.12, 1.12))
        elems += spira.Circle(layer=J5,box_size=(1.42, 1.42))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 150uA shunted and grounded cell
class ls_jj_150_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_150_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.5725))
        elems += spira.Box(layer=R5,width=1.15,height=4.05,center=(0.0,3.15))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.65))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.67))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,5.4))
        elems += spira.Box(layer=M6,width=2.15,height=3.375,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=4.525,center=(0.0,4.6625))
        elems += spira.Box(layer=M5,width=2.45,height=3.625,center=(0.0,0.5875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.7))
        elems += spira.Circle(layer=C5J,box_size=(1.12, 1.12))
        elems += spira.Circle(layer=J5,box_size=(1.42, 1.42))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 151uA shunted and grounded cell
class ls_jj_151_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_151_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.725))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.4125))
        elems += spira.Box(layer=M6,width=2.2,height=3.425,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.66))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.7))
        elems += spira.Box(layer=R5,width=1.15,height=4.025,center=(0.0,3.1875))
        elems += spira.Box(layer=M5,width=1.75,height=4.525,center=(0.0,4.6875))
        elems += spira.Box(layer=M5,width=2.5,height=3.675,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.075))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.725))
        elems += spira.Circle(layer=C5J,box_size=(1.12, 1.12))
        elems += spira.Circle(layer=J5,box_size=(1.43, 1.43))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 152uA shunted cell
class ls_jj_152_s(spira.Cell):
    __name_prefix__ = 'ls_jj_152_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=4.5,center=(0.0,4.65))
        elems += spira.Box(layer=M5,width=2.5,height=3.65,center=(0.0,0.575))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.3625))
        elems += spira.Box(layer=M6,width=2.2,height=3.4,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.025))
        elems += spira.Box(layer=R5,width=1.15,height=4,center=(0.0,3.15))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.62))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.68))
        elems += spira.Circle(layer=C5J,box_size=(1.14, 1.14))
        elems += spira.Circle(layer=J5,box_size=(1.43, 1.43))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 153uA shunted cell
class ls_jj_153_s(spira.Cell):
    __name_prefix__ = 'ls_jj_153_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=4.0,center=(0.0,3.15))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.61))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.68))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.3625))
        elems += spira.Box(layer=M6,width=2.2,height=3.425,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=4.475,center=(0.0,4.6625))
        elems += spira.Box(layer=M5,width=2.5,height=3.675,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.025))
        elems += spira.Circle(layer=C5J,box_size=(1.14, 1.14))
        elems += spira.Circle(layer=J5,box_size=(1.44, 1.44))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 154uA shunted cell
class ls_jj_154_s(spira.Cell):
    __name_prefix__ = 'ls_jj_154_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.0))
        elems += spira.Box(layer=M5,width=1.75,height=4.45,center=(0.0,4.65))
        elems += spira.Box(layer=M5,width=2.5,height=3.675,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.44, 1.44))
        elems += spira.Box(layer=R5,width=1.15,height=3.975,center=(0.0,3.1375))
        elems += spira.Circle(layer=C5J,box_size=(1.14, 1.14))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.68))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.6))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.3375))
        elems += spira.Box(layer=M6,width=2.2,height=3.425,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 154uA shunted and grounded cell
class ls_jj_154_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_154_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.7))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.725))
        elems += spira.Box(layer=M5,width=1.75,height=4.45,center=(0.0,4.65))
        elems += spira.Box(layer=M5,width=2.5,height=3.675,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.44, 1.44))
        elems += spira.Box(layer=R5,width=1.15,height=3.975,center=(0.0,3.1375))
        elems += spira.Circle(layer=C5J,box_size=(1.14, 1.14))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.68))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.6))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.3375))
        elems += spira.Box(layer=M6,width=2.2,height=3.425,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 157uA shunted and grounded cell
class ls_jj_157_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_157_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.65))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.725))
        elems += spira.Box(layer=M5,width=1.75,height=4.425,center=(0.0,4.6625))
        elems += spira.Box(layer=M5,width=2.5,height=3.7,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.46, 1.46))
        elems += spira.Box(layer=R5,width=1.15,height=3.95,center=(0.0,3.15))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6))
        elems += spira.Circle(layer=C5J,box_size=(1.16, 1.16))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.71))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.58))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.3375))
        elems += spira.Box(layer=M6,width=2.2,height=3.45,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 160uA shunted and grounded cell
class ls_jj_160_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_160_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.6))
        elems += spira.Box(layer=M6,width=2.0,height=3.425,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.2625))
        elems += spira.Box(layer=M5,width=2.5,height=3.675,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=4.375,center=(0.0,4.6125))
        elems += spira.Box(layer=R5,width=1.15,height=3.9,center=(0.0,3.1))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.69))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.52))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.725))
        elems += spira.Circle(layer=C5J,box_size=(1.16, 1.16))
        elems += spira.Circle(layer=J5,box_size=(1.47, 1.47))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports
# JJ 161uA shunted cell
class ls_jj_161_s(spira.Cell):
    __name_prefix__ = 'ls_jj_161_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=4.375,center=(0.0,4.6375))
        elems += spira.Box(layer=M5,width=2.5,height=3.7,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.47, 1.47))
        elems += spira.Box(layer=R5,width=1.15,height=3.9,center=(0.0,3.125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.95))
        elems += spira.Circle(layer=C5J,box_size=(1.18, 1.18))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.72))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.53))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.2875))
        elems += spira.Box(layer=M6,width=2.2,height=3.45,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 162uA shunted cell
class ls_jj_162_s(spira.Cell):
    __name_prefix__ = 'ls_jj_162_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=4.35,center=(0.0,4.6))
        elems += spira.Box(layer=M5,width=2.55,height=3.7,center=(0.0,0.575))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.9))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.2375))
        elems += spira.Box(layer=M6,width=2.25,height=3.45,center=(0.0,0.6))
        elems += spira.Box(layer=R5,width=1.15,height=3.85,center=(0.0,3.1))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.49))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.7))
        elems += spira.Circle(layer=J5,box_size=(1.48, 1.48))
        elems += spira.Circle(layer=C5J,box_size=(1.18, 1.18))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 162uA shunted cell and grounded
class ls_jj_162_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_162_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.55))
        elems += spira.Box(layer=M5,width=1.75,height=4.35,center=(0.0,4.6))
        elems += spira.Box(layer=M5,width=2.55,height=3.7,center=(0.0,0.575))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.9))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.75))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.2375))
        elems += spira.Box(layer=M6,width=2.25,height=3.45,center=(0.0,0.6))
        elems += spira.Box(layer=R5,width=1.15,height=3.85,center=(0.0,3.1))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.49))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.7))
        elems += spira.Circle(layer=J5,box_size=(1.48, 1.48))
        elems += spira.Circle(layer=C5J,box_size=(1.18, 1.18))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 163uA shunted cell
class ls_jj_163_s(spira.Cell):
    __name_prefix__ = 'ls_jj_163_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=3.85,center=(0.0,3.1))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.48))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.7))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.2375))
        elems += spira.Box(layer=M6,width=2.25,height=3.45,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.9))
        elems += spira.Box(layer=M5,width=1.75,height=4.35,center=(0.0,4.6))
        elems += spira.Box(layer=M5,width=2.55,height=3.7,center=(0.0,0.575))
        elems += spira.Circle(layer=J5,box_size=(1.48, 1.48))
        elems += spira.Circle(layer=C5J,box_size=(1.18, 1.18))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 163uA shunted and grounded cell
class ls_jj_163_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_163_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.55))
        elems += spira.Box(layer=R5,width=1.15,height=3.85,center=(0.0,3.1))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.48))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.7))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.2375))
        elems += spira.Box(layer=M6,width=2.25,height=3.45,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.9))
        elems += spira.Box(layer=M5,width=1.75,height=4.35,center=(0.0,4.6))
        elems += spira.Box(layer=M5,width=2.55,height=3.7,center=(0.0,0.575))
        elems += spira.Circle(layer=J5,box_size=(1.48, 1.48))
        elems += spira.Circle(layer=C5J,box_size=(1.18, 1.18))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 164uA shunted and grounded cell
class ls_jj_164_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_164_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.575))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.2375))
        elems += spira.Box(layer=M6,width=2.5,height=3.5,center=(0.0,0.625))
        elems += spira.Box(layer=M5,width=1.75,height=4.3,center=(0.0,4.625))
        elems += spira.Box(layer=M5,width=2.55,height=3.75,center=(0.0,0.6))
        elems += spira.Box(layer=R5,width=1.15,height=3.825,center=(0.0,3.1125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.5))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.73))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.75))
        elems += spira.Circle(layer=C5J,box_size=(1.18, 1.18))
        elems += spira.Circle(layer=J5,box_size=(1.49, 1.49))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 165uA shunted cell
class ls_jj_165_s(spira.Cell):
    __name_prefix__ = 'ls_jj_165_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.2125))
        elems += spira.Box(layer=M6,width=2.25,height=3.475,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.46))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.71))
        elems += spira.Box(layer=R5,width=1.15,height=3.825,center=(0.0,3.0875))
        elems += spira.Box(layer=M5,width=1.75,height=4.3,center=(0.0,4.6))
        elems += spira.Box(layer=M5,width=2.55,height=3.725,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.875))
        elems += spira.Circle(layer=C5J,box_size=(1.2, 1.2))
        elems += spira.Circle(layer=J5,box_size=(1.49, 1.49))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 166uA shunted and grounded cell
class ls_jj_166_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_166_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.525))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,8.05))
        elems += spira.Box(layer=M6,width=2.25,height=3.475,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,5.2))
        elems += spira.Box(layer=M5,width=2.55,height=3.725,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=4.275,center=(0.0,4.5875))
        elems += spira.Box(layer=R5,width=1.15,height=3.8,center=(0.0,3.075))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.71))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.45))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.75))
        elems += spira.Circle(layer=C5J,box_size=(1.2, 1.2))
        elems += spira.Circle(layer=J5,box_size=(1.49, 1.49))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 169uA shunted and grounded cell
class ls_jj_169_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_169_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.5))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.75))
        elems += spira.Box(layer=M5,width=1.75,height=4.25,center=(0.0,4.6))
        elems += spira.Box(layer=M5,width=2.55,height=3.75,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.51, 1.51))
        elems += spira.Box(layer=R5,width=1.15,height=3.775,center=(0.0,3.0875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.35,0.35))
        elems += spira.Circle(layer=C5J,box_size=(1.2, 1.2))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.74))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.44))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.1875))
        elems += spira.Box(layer=M6,width=2.25,height=3.5,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 171uA shunted cell
class ls_jj_171_s(spira.Cell):
    __name_prefix__ = 'ls_jj_171_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=4.225,center=(0.0,4.5875))
        elems += spira.Box(layer=M5,width=2.55,height=3.75,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.825))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.1625))
        elems += spira.Box(layer=M6,width=2.25,height=3.5,center=(0.0,0.625))
        elems += spira.Box(layer=R5,width=1.15,height=3.75,center=(0.0,3.075))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.42))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.74))
        elems += spira.Circle(layer=J5,box_size=(1.52, 1.52))
        elems += spira.Circle(layer=C5J,box_size=(1.22, 1.22))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 172uA shunted and grounded cell
class ls_jj_172_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_172_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.45))
        elems += spira.Box(layer=M6,width=2.25,height=3.475,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.1375))
        elems += spira.Box(layer=M5,width=2.55,height=3.725,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=4.225,center=(0.0,4.5625))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.8))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.75))
        elems += spira.Box(layer=R5,width=1.15,height=3.75,center=(0.0,3.05))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.72))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.38))
        elems += spira.Circle(layer=C5J,box_size=(1.22, 1.22))
        elems += spira.Circle(layer=J5,box_size=(1.52, 1.52))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 175uA shunted and grounded cell
class ls_jj_175_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_175_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.425))
        elems += spira.Box(layer=M6,width=2.3,height=3.5,center=(0.0,0.6))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.1125))
        elems += spira.Box(layer=M5,width=2.6,height=3.75,center=(0.0,0.575))
        elems += spira.Box(layer=M5,width=1.75,height=4.2,center=(0.0,4.55))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.775))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.775))
        elems += spira.Box(layer=R5,width=1.15,height=3.7,center=(0.0,3.05))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.73))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.35))
        elems += spira.Circle(layer=C5J,box_size=(1.24, 1.24))
        elems += spira.Circle(layer=J5,box_size=(1.53, 1.53))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 176uA shunted and grounded cell
class ls_jj_176_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_176_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.45))
        elems += spira.Box(layer=R5,width=1.15,height=3.675,center=(0.0,3.0625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.37))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.75))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.1125))
        elems += spira.Box(layer=M6,width=2.3,height=3.55,center=(0.0,0.625))
        elems += spira.Box(layer=M5,width=1.75,height=4.15,center=(0.0,4.575))
        elems += spira.Box(layer=M5,width=2.6,height=3.8,center=(0.0,0.6))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.775))
        elems += spira.Circle(layer=C5J,box_size=(1.24, 1.24))
        elems += spira.Circle(layer=J5,box_size=(1.54, 1.54))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 177uA shunted cell
class ls_jj_177_s(spira.Cell):
    __name_prefix__ = 'ls_jj_177_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.1125))
        elems += spira.Box(layer=M6,width=2.3,height=3.55,center=(0.0,0.625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.36))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.76))
        elems += spira.Box(layer=R5,width=1.15,height=3.675,center=(0.0,3.0625))
        elems += spira.Box(layer=M5,width=1.75,height=4.15,center=(0.0,4.575))
        elems += spira.Box(layer=M5,width=2.6,height=3.8,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.775))
        elems += spira.Circle(layer=C5J,box_size=(1.24, 1.24))
        elems += spira.Circle(layer=J5,box_size=(1.54, 1.54))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 186uA shunted cell
class ls_jj_186_s(spira.Cell):
    __name_prefix__ = 'ls_jj_186_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=4.05,center=(0.0,4.525))
        elems += spira.Box(layer=M5,width=2.65,height=3.825,center=(0.0,0.5875))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,5.025))
        elems += spira.Box(layer=M6,width=2.35,height=3.575,center=(0.0,0.6125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.675))
        elems += spira.Box(layer=R5,width=1.15,height=3.55,center=(0.0,3.025))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.28))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.77))
        elems += spira.Circle(layer=C5J,box_size=(1.28, 1.28))
        elems += spira.Circle(layer=J5,box_size=(1.58, 1.58))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 189uA shunted and grounded cell
class ls_jj_189_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_189_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.325))
        elems += spira.Box(layer=M6,width=2.34,height=3.6,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,5.0))
        elems += spira.Box(layer=M5,width=2.65,height=3.85,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=4.0,center=(0.0,4.525))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.8))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.78))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.25))
        elems += spira.Box(layer=R5,width=1.15,height=3.525,center=(0.0,3.0125))
        elems += spira.Circle(layer=C5J,box_size=(1.3, 1.3))
        elems += spira.Circle(layer=J5,box_size=(1.59, 1.59))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 190uA shunted and grounded cell
class ls_jj_190_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_190_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.3))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.9625))
        elems += spira.Box(layer=M6,width=2.35,height=3.575,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.22))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.76))
        elems += spira.Box(layer=R5,width=1.15,height=3.5,center=(0.0,2.9875))
        elems += spira.Box(layer=M5,width=1.75,height=4.0,center=(0.0,4.5))
        elems += spira.Box(layer=M5,width=2.65,height=3.825,center=(0.0,0.5875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.8))
        elems += spira.Circle(layer=C5J,box_size=(1.3, 1.3))
        elems += spira.Circle(layer=J5,box_size=(1.6, 1.6))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 191uA shunted and grounded cell
class ls_jj_191_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_191_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.3))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.8))
        elems += spira.Box(layer=M5,width=1.75,height=4,center=(0.0,4.525))
        elems += spira.Box(layer=M5,width=2.65,height=3.85,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.6, 1.6))
        elems += spira.Box(layer=R5,width=1.15,height=3.525,center=(0.0,3.0125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.65))
        elems += spira.Circle(layer=C5J,box_size=(1.3, 1.3))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.78))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.24))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.9875))
        elems += spira.Box(layer=M6,width=2.35,height=3.6,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 192uA shunted cell
class ls_jj_192_s(spira.Cell):
    __name_prefix__ = 'ls_jj_192_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=3.975,center=(0.0,4.5125))
        elems += spira.Box(layer=M5,width=2.65,height=3.85,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.6, 1.6))
        elems += spira.Box(layer=R5,width=1.15,height=3.5,center=(0.0,3.0))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.625))
        elems += spira.Circle(layer=C5J,box_size=(1.3, 1.3))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.79))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.23))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,4.975))
        elems += spira.Box(layer=M6,width=2.35,height=3.6,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 195uA shunted and grounded cell
class ls_jj_195_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_195_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.275))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.9375))
        elems += spira.Box(layer=M6,width=2.35,height=3.575,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.18))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.77))
        elems += spira.Box(layer=R5,width=1.15,height=3.5,center=(0.0,2.975))
        elems += spira.Box(layer=M5,width=1.75,height=3.975,center=(0.0,4.4875))
        elems += spira.Box(layer=M5,width=2.65,height=3.825,center=(0.0,0.5875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.8))
        elems += spira.Circle(layer=C5J,box_size=(1.32, 1.32))
        elems += spira.Circle(layer=J5,box_size=(1.62, 1.62))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 196uA shunted cell
class ls_jj_196_s(spira.Cell):
    __name_prefix__ = 'ls_jj_196_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.9375))
        elems += spira.Box(layer=M6,width=2.34,height=3.6,center=(0.0,0.625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.2))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.79))
        elems += spira.Box(layer=R5,width=1.15,height=3.475,center=(0.0,2.9875))
        elems += spira.Box(layer=M5,width=1.75,height=3.95,center=(0.0,4.45))
        elems += spira.Box(layer=M5,width=2.65,height=3.85,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.6))
        elems += spira.Circle(layer=C5J,box_size=(1.32, 1.32))
        elems += spira.Circle(layer=J5,box_size=(1.62, 1.62))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 198uA shunted and grounded cell
class ls_jj_198_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_198_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.25))
        elems += spira.Box(layer=M6,width=2.4,height=3.625,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.9375))
        elems += spira.Box(layer=M5,width=2.7,height=3.875,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.95,center=(0.0,4.5))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.6))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.825))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.8))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.18))
        elems += spira.Box(layer=R5,width=1.15,height=3.45,center=(0.0,3.0))
        elems += spira.Circle(layer=C5J,box_size=(1.32, 1.32))
        elems += spira.Circle(layer=J5,box_size=(1.63, 1.63))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 199uA shunted cell
class ls_jj_199_s(spira.Cell):
    __name_prefix__ = 'ls_jj_199_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=3.925,center=(0.0,4.4625))
        elems += spira.Box(layer=M5,width=2.7,height=3.85,center=(0.0,0.575))
        elems += spira.Circle(layer=J5,box_size=(1.63, 1.63))
        elems += spira.Box(layer=R5,width=1.15,height=3.425,center=(0.0,2.9625))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.55))
        elems += spira.Circle(layer=C5J,box_size=(1.34, 1.34))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.78))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.15))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,4.9))
        elems += spira.Box(layer=M6,width=2.4,height=3.6,center=(0.0,0.6))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 200uA shunted cell
class ls_jj_200_s(spira.Cell):
    __name_prefix__ = 'ls_jj_200_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=3.425,center=(0.0,2.9875))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.17))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.8))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.9125))
        elems += spira.Box(layer=M6,width=2.4,height=3.625,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=3.925,center=(0.0,4.4875))
        elems += spira.Box(layer=M5,width=2.7,height=3.875,center=(0.0,0.5875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.825))
        elems += spira.Circle(layer=C5J,box_size=(1.34, 1.34))
        elems += spira.Circle(layer=J5,box_size=(1.63, 1.63))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 200uA shunted and grounded cell
class ls_jj_200_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_200_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.25))
        elems += spira.Box(layer=R5,width=1.15,height=3.425,center=(0.0,2.9875))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.17))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.8))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.9125))
        elems += spira.Box(layer=M6,width=2.4,height=3.625,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=3.925,center=(0.0,4.4875))
        elems += spira.Box(layer=M5,width=2.7,height=3.875,center=(0.0,0.5875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.825))
        elems += spira.Circle(layer=C5J,box_size=(1.34, 1.34))
        elems += spira.Circle(layer=J5,box_size=(1.63, 1.63))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 201uA shunted cell
class ls_jj_201_s(spira.Cell):
    __name_prefix__ = 'ls_jj_201_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=3.9,center=(0.0,4.5))
        elems += spira.Box(layer=M5,width=2.7,height=3.9,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.64, 1.64))
        elems += spira.Box(layer=R5,width=1.15,height=3.425,center=(0.0,2.9875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.575))
        elems += spira.Circle(layer=C5J,box_size=(1.34, 1.34))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.8))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.16))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.9125))
        elems += spira.Box(layer=M6,width=2.4,height=3.625,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 204uA shunted and grounded cell
class ls_jj_204_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_204_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.175))
        elems += spira.Box(layer=R5,width=1.15,height=3.4,center=(0.0,2.95))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.11))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.79))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.8625))
        elems += spira.Box(layer=M6,width=2.4,height=3.625,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=3.875,center=(0.0,4.4625))
        elems += spira.Box(layer=M5,width=2.7,height=3.875,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.525))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.825))
        elems += spira.Circle(layer=C5J,box_size=(1.36, 1.36))
        elems += spira.Circle(layer=J5,box_size=(1.65, 1.65))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 206uA shunted and grounded cell
class ls_jj_206_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_206_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.2))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.825))
        elems += spira.Box(layer=M5,width=1.75,height=3.85,center=(0.0,4.45))
        elems += spira.Box(layer=M5,width=2.7,height=3.875,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.66, 1.66))
        elems += spira.Box(layer=R5,width=1.15,height=3.375,center=(0.0,2.9375))
        elems += spira.Circle(layer=C5J,box_size=(1.36, 1.36))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.79))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.1))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,4.85))
        elems += spira.Box(layer=M6,width=2.4,height=3.625,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 209uA shunted and grounded cell
class ls_jj_209_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_209_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.2))
        elems += spira.Box(layer=M5,width=1.75,height=3.85,center=(0.0,4.475))
        elems += spira.Box(layer=M5,width=2.7,height=3.9,center=(0.0,0.6))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.8625))
        elems += spira.Box(layer=M6,width=2.4,height=3.65,center=(0.0,0.625))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.825))
        elems += spira.Box(layer=R5,width=1.15,height=3.375,center=(0.0,2.9625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.1))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.82))
        elems += spira.Circle(layer=C5J,box_size=(1.38, 1.38))
        elems += spira.Circle(layer=J5,box_size=(1.67, 1.67))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 212uA shunted and grounded cell
class ls_jj_212_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_212_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.15))
        elems += spira.Box(layer=M6,width=2.45,height=3.675,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.8375))
        elems += spira.Box(layer=M5,width=2.75,height=3.925,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.825,center=(0.0,4.4625))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.5))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.85))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.83))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.09))
        elems += spira.Box(layer=R5,width=1.15,height=3.325,center=(0.0,2.9625))
        elems += spira.Circle(layer=C5J,box_size=(1.38, 1.38))
        elems += spira.Circle(layer=J5,box_size=(1.68, 1.68))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 218uA shunted and grounded cell
class ls_jj_218_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_218_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.125))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,4.8))
        elems += spira.Box(layer=M6,width=2.45,height=3.7,center=(0.0,0.625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.05))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.84))
        elems += spira.Box(layer=R5,width=1.25,height=3.175,center=(0.0,2.9375))
        elems += spira.Box(layer=M5,width=1.75,height=3.75,center=(0.0,4.45))
        elems += spira.Box(layer=M5,width=2.75,height=3.95,center=(0.0,0.6))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.85))
        elems += spira.Circle(layer=C5J,box_size=(1.4, 1.4))
        elems += spira.Circle(layer=J5,box_size=(1.7, 1.7))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 220uA shunted cell
class ls_jj_220_s(spira.Cell):
    __name_prefix__ = 'ls_jj_220_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.97625))
        elems += spira.Box(layer=M6,width=2.4,height=3.675,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.01))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.82))
        elems += spira.Box(layer=R5,width=1.15,height=3.275,center=(0.0,2.9125))
        elems += spira.Box(layer=M5,width=1.75,height=3.75,center=(0.0,4.425))
        elems += spira.Box(layer=M5,width=2.75,height=3.925,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.425))
        elems += spira.Circle(layer=C5J,box_size=(1.42, 1.42))
        elems += spira.Circle(layer=J5,box_size=(1.71, 1.71))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 220uA shunted and grounded cell
class ls_jj_220_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_220_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.1))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.85))
        elems += spira.Box(layer=M5,width=1.75,height=3.75,center=(0.0,4.425))
        elems += spira.Box(layer=M5,width=2.75,height=3.925,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.71, 1.71))
        elems += spira.Box(layer=R5,width=1.15,height=3.275,center=(0.0,2.9125))
        elems += spira.Circle(layer=C5J,box_size=(1.42, 1.42))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.82))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.01))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7625))
        elems += spira.Box(layer=M6,width=2.45,height=3.675,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 221uA shunted and grounded cell
class ls_jj_221_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_221_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.075))
        elems += spira.Box(layer=M6,width=2.45,height=3.675,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7625))
        elems += spira.Box(layer=M5,width=2.75,height=3.925,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.75,center=(0.0,4.425))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.425))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.85))
        elems += spira.Box(layer=R5,width=1.15,height=3.275,center=(0.0,2.9125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.82))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.01))
        elems += spira.Circle(layer=C5J,box_size=(1.42, 1.42))
        elems += spira.Circle(layer=J5,box_size=(1.72, 1.72))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 222uA shunted and grounded cell
class ls_jj_222_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_222_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.1))
        elems += spira.Box(layer=M5,width=1.75,height=3.725,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.75,height=3.925,center=(0.0,0.5875))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.75))
        elems += spira.Box(layer=M6,width=2.45,height=3.675,center=(0.0,0.6125))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.85))
        elems += spira.Box(layer=R5,width=1.15,height=3.25,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.82))
        elems += spira.Circle(layer=C5J,box_size=(1.42, 1.42))
        elems += spira.Circle(layer=J5,box_size=(1.72, 1.72))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 223uA shunted cell
class ls_jj_223_s(spira.Cell):
    __name_prefix__ = 'ls_jj_223_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7375))
        elems += spira.Box(layer=M6,width=2.45,height=3.675,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=3.725,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.75,height=3.925,center=(0.0,0.5875))
        elems += spira.Box(layer=R5,width=1.15,height=3.25,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.0))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.82))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.4))
        elems += spira.Circle(layer=C5J,box_size=(1.42, 1.42))
        elems += spira.Circle(layer=J5,box_size=(1.72, 1.72))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 225uA shunted cell
class ls_jj_225_s(spira.Cell):
    __name_prefix__ = 'ls_jj_225_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=3.225,center=(0.0,2.9125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.98))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.83))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7375))
        elems += spira.Box(layer=M6,width=2.5,height=3.7,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.725,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.8,height=3.95,center=(0.0,0.575))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.4))
        elems += spira.Circle(layer=C5J,box_size=(1.44, 1.44))
        elems += spira.Circle(layer=J5,box_size=(1.73, 1.73))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 225uA shunted and grounded cell
class ls_jj_225_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_225_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.05))
        elems += spira.Box(layer=R5,width=1.15,height=3.225,center=(0.0,2.9125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.98))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.83))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7375))
        elems += spira.Box(layer=M6,width=2.5,height=3.7,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.725,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.8,height=3.95,center=(0.0,0.575))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.4))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.2875))
        elems += spira.Circle(layer=C5J,box_size=(1.44, 1.44))
        elems += spira.Circle(layer=J5,box_size=(1.73, 1.73))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 227uA shunted and grounded cell
class ls_jj_227_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_227_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.05))
        elems += spira.Box(layer=R5,width=1.15,height=3.2,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.97))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.83))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,4.725))
        elems += spira.Box(layer=M6,width=2.5,height=3.725,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=3.675,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.8,height=3.975,center=(0.0,0.5875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.2875))
        elems += spira.Circle(layer=C5J,box_size=(1.44, 1.44))
        elems += spira.Circle(layer=J5,box_size=(1.74, 1.74))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 228uA shunted cell
class ls_jj_228_s(spira.Cell):
    __name_prefix__ = 'ls_jj_228_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=3.675,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.8,height=3.975,center=(0.0,0.5875))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7125))
        elems += spira.Box(layer=M6,width=2.5,height=3.725,center=(0.0,0.6125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.375))
        elems += spira.Box(layer=R5,width=1.15,height=3.2,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.97))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.83))
        elems += spira.Circle(layer=J5,box_size=(1.74, 1.74))
        elems += spira.Circle(layer=C5J,box_size=(1.44, 1.44))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 228uA shunted and grounded cell
class ls_jj_228_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_228_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.05))
        elems += spira.Box(layer=M5,width=1.75,height=3.675,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.8,height=3.975,center=(0.0,0.5875))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7125))
        elems += spira.Box(layer=M6,width=2.5,height=3.725,center=(0.0,0.6125))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.875))
        elems += spira.Box(layer=R5,width=1.15,height=3.2,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.97))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.83))
        elems += spira.Circle(layer=J5,box_size=(1.74, 1.74))
        elems += spira.Circle(layer=C5J,box_size=(1.44, 1.44))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 231uA shunted cell
class ls_jj_231_s(spira.Cell):
    __name_prefix__ = 'ls_jj_231_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=3.2,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.84))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.95))
        elems += spira.Box(layer=M6,width=2.5,height=3.725,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.375))
        elems += spira.Box(layer=M5,width=2.8,height=3.975,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.675,center=(0.0,4.4125))
        elems += spira.Circle(layer=J5,box_size=(1.75, 1.75))
        elems += spira.Circle(layer=C5J,box_size=(1.46, 1.46))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 232uA shunted and grounded cell
class ls_jj_232_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_232_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.05))
        elems += spira.Box(layer=M6,width=2.5,height=3.75,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,4.725))
        elems += spira.Box(layer=M5,width=2.8,height=4.0,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.65,center=(0.0,4.425))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.875))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.86))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.97))
        elems += spira.Box(layer=R5,width=1.15,height=3.175,center=(0.0,2.9125))
        elems += spira.Circle(layer=C5J,box_size=(1.46, 1.46))
        elems += spira.Circle(layer=J5,box_size=(1.76, 1.76))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 234uA shunted cell
class ls_jj_234_s(spira.Cell):
    __name_prefix__ = 'ls_jj_234_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.35))
        elems += spira.Box(layer=M6,width=2.5,height=3.725,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6875))
        elems += spira.Box(layer=M5,width=2.8,height=3.975,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.65,center=(0.0,4.4))
        elems += spira.Box(layer=R5,width=1.15,height=3.175,center=(0.0,2.8875))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.84))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.94))
        elems += spira.Circle(layer=J5,box_size=(1.76, 1.76))
        elems += spira.Circle(layer=C5J,box_size=(1.46, 1.46))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 235uA shunted cell
class ls_jj_235_s(spira.Cell):
    __name_prefix__ = 'ls_jj_235_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=3.65,center=(0.0,4.425))
        elems += spira.Box(layer=M5,width=2.8,height=4,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.77, 1.77))
        elems += spira.Box(layer=R5,width=1.15,height=3.175,center=(0.0,2.9125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.375))
        elems += spira.Circle(layer=C5J,box_size=(1.46, 1.46))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.87))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.96))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7125))
        elems += spira.Box(layer=M6,width=2.5,height=3.75,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 235uA shunted and grounded cell
class ls_jj_235_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_235_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.025))
        elems += spira.Box(layer=M5,width=1.75,height=3.65,center=(0.0,4.425))
        elems += spira.Box(layer=M5,width=2.8,height=4,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.77, 1.77))
        elems += spira.Box(layer=R5,width=1.15,height=3.175,center=(0.0,2.9125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.375))
        elems += spira.Circle(layer=C5J,box_size=(1.46, 1.46))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.87))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.96))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7125))
        elems += spira.Box(layer=M6,width=2.5,height=3.75,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 236uA shunted and grounded cell
class ls_jj_236_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_236_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6875))
        elems += spira.Box(layer=M6,width=2.5,height=3.725,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.93))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.85))
        elems += spira.Box(layer=R5,width=1.25,height=3.175,center=(0.0,2.8875))
        elems += spira.Box(layer=M5,width=1.75,height=3.65,center=(0.0,4.4))
        elems += spira.Box(layer=M5,width=2.8,height=3.975,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.35))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.875))
        elems += spira.Circle(layer=C5J,box_size=(1.48, 1.48))
        elems += spira.Circle(layer=J5,box_size=(1.77, 1.77))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 240uA shunted cell
class ls_jj_240_s(spira.Cell):
    __name_prefix__ = 'ls_jj_240_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=1.65,height=2.775,center=(0.0,4.6625))
        elems += spira.Box(layer=M6,width=2.55,height=3.775,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=3.6,center=(0.0,4.4))
        elems += spira.Box(layer=M5,width=2.85,height=4.025,center=(0.0,0.5875))
        elems += spira.Box(layer=R5,width=1.15,height=3.125,center=(0.0,2.8875))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.91))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.85))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.325))
        elems += spira.Circle(layer=C5J,box_size=(1.48, 1.48))
        elems += spira.Circle(layer=J5,box_size=(1.79, 1.79))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 240uA shunted and grounded cell
class ls_jj_240_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_240_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,4.975))
        elems += spira.Box(layer=M6,width=1.65,height=2.775,center=(0.0,4.6625))
        elems += spira.Box(layer=M6,width=2.55,height=3.775,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=3.6,center=(0.0,4.4))
        elems += spira.Box(layer=M5,width=2.85,height=4.025,center=(0.0,0.5875))
        elems += spira.Box(layer=R5,width=1.15,height=3.125,center=(0.0,2.8875))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.91))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.85))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.325))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.9))
        elems += spira.Circle(layer=C5J,box_size=(1.48, 1.48))
        elems += spira.Circle(layer=J5,box_size=(1.79, 1.79))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 242uA shunted and grounded cell
class ls_jj_242_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_242_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.0))
        elems += spira.Box(layer=M6,width=1.65,height=2.75,center=(0.0,4.675))
        elems += spira.Box(layer=M6,width=2.55,height=3.8,center=(0.0,0.625))
        elems += spira.Box(layer=M5,width=1.75,height=3.575,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.85,height=4.05,center=(0.0,0.6))
        elems += spira.Box(layer=R5,width=1.15,height=3.1,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.93))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.88))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.9))
        elems += spira.Circle(layer=C5J,box_size=(1.5, 1.5))
        elems += spira.Circle(layer=J5,box_size=(1.79, 1.79))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 250uA shunted and grounded cell
class ls_jj_250_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_250_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,4.95))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.9))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.4))
        elems += spira.Box(layer=M5,width=2.85,height=4.05,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.82, 1.82))
        elems += spira.Box(layer=R5,width=1.15,height=3.075,center=(0.0,2.8875))
        elems += spira.Circle(layer=C5J,box_size=(1.52, 1.52))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.89))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.63750))
        elems += spira.Box(layer=M6,width=2.55,height=3.8,center=(0.0,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 253uA shunted and grounded cell
class ls_jj_253_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_253_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,4.95))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.925))
        elems += spira.Box(layer=M5,width=1.75,height=3.575,center=(0.0,4.3875))
        elems += spira.Box(layer=M5,width=2.9,height=4.05,center=(0.0,0.575))
        elems += spira.Circle(layer=J5,box_size=(1.83, 1.83))
        elems += spira.Box(layer=R5,width=1.1,height=3.075,center=(0.0,2.8875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.3))
        elems += spira.Circle(layer=C5J,box_size=(1.54, 1.54))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,1.88))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,3.89))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.63750))
        elems += spira.Box(layer=M6,width=2.6,height=3.8,center=(0.0,0.6))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 257uA shunted and grounded cell
class ls_jj_257_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_257_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.0))
        elems += spira.Box(layer=M6,width=2.6,height=3.85,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6375))
        elems += spira.Box(layer=M5,width=2.9,height=4.1,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.525,center=(0.0,4.4125))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.925))
        elems += spira.Box(layer=R5,width=1.1,height=3.05,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,1.91))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,3.9))
        elems += spira.Circle(layer=J5,box_size=(1.85, 1.85))
        elems += spira.Circle(layer=C5J,box_size=(1.54, 1.54))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 258uA shunted and grounded cell
class ls_jj_258_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_258_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,4.95))
        elems += spira.Box(layer=M6,width=2.6,height=3.825,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6125))
        elems += spira.Box(layer=M5,width=2.9,height=4.075,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.525,center=(0.0,4.3875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.925))
        elems += spira.Box(layer=R5,width=1.1,height=3.05,center=(0.0,2.875))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,1.88))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,3.87))
        elems += spira.Circle(layer=J5,box_size=(1.85, 1.85))
        elems += spira.Circle(layer=C5J,box_size=(1.54, 1.54))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 260uA shunted and grounded cell
class ls_jj_260_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_260_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.0))
        elems += spira.Box(layer=M6,width=2.6,height=3.85,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6625))
        elems += spira.Box(layer=M5,width=2.9,height=4.1,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.425))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.925))
        elems += spira.Box(layer=R5,width=1.15,height=3.075,center=(0.0,2.9125))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,1.91))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,3.92))
        elems += spira.Circle(layer=J5,box_size=(1.86, 1.86))
        elems += spira.Circle(layer=C5J,box_size=(1.56, 1.56))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 266uA shunted and grounded cell
class ls_jj_266_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_266_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.0))
        elems += spira.Box(layer=M6,width=2.65,height=3.875,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,4.675))
        elems += spira.Box(layer=M5,width=2.95,height=4.125,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.425))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.95))
        elems += spira.Box(layer=R5,width=1.15,height=3.05,center=(0.0,2.925))
        elems += spira.Box(layer=C5R,width=0.6,height=0.52,center=(0.0,1.92))
        elems += spira.Box(layer=C5R,width=0.6,height=0.52,center=(0.0,3.93))
        elems += spira.Circle(layer=J5,box_size=(1.88, 1.88))
        elems += spira.Circle(layer=C5J,box_size=(1.79, 1.79))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 271uA shunted and grounded cell
class ls_jj_271_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_271_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.0))
        elems += spira.Box(layer=M6,width=2.65,height=3.9,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6875))
        elems += spira.Box(layer=M5,width=2.95,height=4.15,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.45))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.95))
        elems += spira.Box(layer=R5,width=1.25,height=3.075,center=(0.0,2.9375))
        elems += spira.Box(layer=C5R,width=0.62,height=0.52,center=(0.0,1.93))
        elems += spira.Box(layer=C5R,width=0.62,height=0.52,center=(0.0,3.94))
        elems += spira.Circle(layer=J5,box_size=(1.89, 1.89))
        elems += spira.Circle(layer=C5J,box_size=(1.6, 1.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.35))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 274uA shunted and grounded cell
class ls_jj_274_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_274_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,4.975))
        elems += spira.Box(layer=M6,width=1.65,height=2.775,center=(0.0,4.6625))
        elems += spira.Box(layer=M6,width=2.65,height=3.875,center=(0.0,0.6125))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.425))
        elems += spira.Box(layer=M5,width=2.95,height=4.125,center=(0.0,0.5875))
        elems += spira.Box(layer=R5,width=1.25,height=3.075,center=(0.0,2.9125))
        elems += spira.Box(layer=C5R,width=0.62,height=0.52,center=(0.0,3.9))
        elems += spira.Box(layer=C5R,width=0.62,height=0.52,center=(0.0,1.91))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.325))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.95))
        elems += spira.Circle(layer=C5J,box_size=(1.6, 1.6))
        elems += spira.Circle(layer=J5,box_size=(1.9, 1.9))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 280uA shunted and grounded cell
class ls_jj_280_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_280_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5))
        elems += spira.Box(layer=M6,width=2.65,height=3.9,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6875))
        elems += spira.Box(layer=M5,width=2.95,height=4.15,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.45))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.35))
        elems += spira.Box(layer=C5R,width=0.68,height=0.52,center=(0.0,1.95))
        elems += spira.Box(layer=C5R,width=0.68,height=0.52,center=(0.0,3.94))
        elems += spira.Box(layer=R5,width=1.2,height=3.075,center=(0.0,2.9375))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.95))
        elems += spira.Circle(layer=C5J,box_size=(1.62, 1.62))
        elems += spira.Circle(layer=J5,box_size=(1.92, 1.92))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 284uA shunted and grounded cell
class ls_jj_284_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_284_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6875))
        elems += spira.Box(layer=M6,width=2.7,height=3.925,center=(0.0,0.6125))
        elems += spira.Box(layer=C5R,width=0.68,height=0.52,center=(0.0,3.93))
        elems += spira.Box(layer=C5R,width=0.68,height=0.52,center=(0.0,1.93))
        elems += spira.Box(layer=R5,width=1.25,height=3.075,center=(0.0,2.9375))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.45))
        elems += spira.Box(layer=M5,width=3.0,height=4.175,center=(0.0,0.5875))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.35))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.975))
        elems += spira.Circle(layer=C5J,box_size=(1.64, 1.64))
        elems += spira.Circle(layer=J5,box_size=(1.94, 1.94))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 285uA shunted and grounded cell
class ls_jj_285_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_285_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5))
        elems += spira.Box(layer=M6,width=2.7,height=3.925,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,4.675))
        elems += spira.Box(layer=M5,width=3.0,height=4.175,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.525,center=(0.0,4.4375))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.975))
        elems += spira.Box(layer=R5,width=1.25,height=3.05,center=(0.0,2.925))
        elems += spira.Box(layer=C5R,width=0.68,height=0.52,center=(0.0,1.93))
        elems += spira.Box(layer=C5R,width=0.68,height=0.52,center=(0.0,3.92))
        elems += spira.Circle(layer=C5J,box_size=(1.64, 1.64))
        elems += spira.Circle(layer=J5,box_size=(1.94, 1.94))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 300uA shunted and grounded cell
class ls_jj_300_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_300_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.05))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,3.0))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.5))
        elems += spira.Box(layer=M5,width=3.05,height=4.25,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.99, 1.99))
        elems += spira.Box(layer=R5,width=1.3,height=3.075,center=(0.0,2.9875))
        elems += spira.Circle(layer=C5J,box_size=(1.7, 1.7))
        elems += spira.Box(layer=C5R,width=0.78,height=0.52,center=(0.0,1.98))
        elems += spira.Box(layer=C5R,width=0.78,height=0.52,center=(0.0,3.99))
        elems += spira.Box(layer=M6,width=1.5,height=2.775,center=(0.0,4.7375))
        elems += spira.Box(layer=M6,width=2.75,height=4.0,center=(0.0,0.625))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.4))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 303uA shunted and grounded cell
class ls_jj_303_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_303_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.05))
        elems += spira.Box(layer=M6,width=2.75,height=3.975,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.5,height=2.75,center=(0.0,4.7))
        elems += spira.Box(layer=M5,width=3.05,height=4.225,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.525,center=(0.0,4.4625))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,3.0))
        elems += spira.Box(layer=R5,width=1.3,height=3.05,center=(0.0,2.95))
        elems += spira.Box(layer=C5R,width=0.78,height=0.52,center=(0.0,1.96))
        elems += spira.Box(layer=C5R,width=0.78,height=0.52,center=(0.0,3.95))
        elems += spira.Circle(layer=J5,box_size=(2.0, 2.0))
        elems += spira.Circle(layer=C5J,box_size=(1.7, 1.7))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 315uA shunted and grounded cell
class ls_jj_315_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_315_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.05))
        elems += spira.Box(layer=M6,width=2.8,height=4.025,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.55,height=2.775,center=(0.0,4.7125))
        elems += spira.Box(layer=M5,width=3.1,height=4.275,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.525,center=(0.0,4.4875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,3.025))
        elems += spira.Box(layer=R5,width=1.35,height=3.05,center=(0.0,2.975))
        elems += spira.Box(layer=C5R,width=0.8,height=0.52,center=(0.0,1.98))
        elems += spira.Box(layer=C5R,width=0.8,height=0.52,center=(0.0,3.97))
        elems += spira.Circle(layer=J5,box_size=(2.04, 2.04))
        elems += spira.Circle(layer=C5J,box_size=(1.74, 1.74))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 324uA shunted and grounded cell
class ls_jj_324_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_324_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.1))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,3.025))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.5))
        elems += spira.Box(layer=M5,width=3.1,height=4.275,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(2.07, 2.07))
        elems += spira.Box(layer=R5,width=1.4,height=3.075,center=(0.0,2.9875))
        elems += spira.Circle(layer=C5J,box_size=(1.76, 1.76))
        elems += spira.Box(layer=C5R,width=0.84,height=0.52,center=(0.0,1.99))
        elems += spira.Box(layer=C5R,width=0.84,height=0.52,center=(0.0,4.00))
        elems += spira.Box(layer=M6,width=1.6,height=2.775,center=(0.0,4.7375))
        elems += spira.Box(layer=M6,width=2.8,height=4.025,center=(0.0,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 325uA shunted and grounded cell
class ls_jj_325_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_325_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.05))
        elems += spira.Box(layer=M6,width=2.8,height=4.025,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.6,height=2.775,center=(0.0,4.7375))
        elems += spira.Box(layer=M5,width=3.1,height=4.275,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.5))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,3.025))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.4))
        elems += spira.Box(layer=R5,width=1.4,height=3.075,center=(0.0,2.9875))
        elems += spira.Box(layer=C5R,width=0.84,height=0.52,center=(0.0,1.99))
        elems += spira.Box(layer=C5R,width=0.84,height=0.52,center=(0.0,3.99))
        elems += spira.Circle(layer=C5J,box_size=(1.76, 1.76))
        elems += spira.Circle(layer=J5,box_size=(2.07, 2.07))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 329uA shunted and grounded cell
class ls_jj_329_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_329_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.075))
        elems += spira.Box(layer=M6,width=1.65,height=2.775,center=(0.0,4.7625))
        elems += spira.Box(layer=M6,width=2.85,height=4.05,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.575,center=(0.0,4.5125))
        elems += spira.Box(layer=M5,width=3.15,height=4.3,center=(0.0,0.575))
        elems += spira.Box(layer=R5,width=1.45,height=3.075,center=(0.0,3.0125))
        elems += spira.Box(layer=C5R,width=0.88,height=0.52,center=(0.0,4.01))
        elems += spira.Box(layer=C5R,width=0.88,height=0.52,center=(0.0,2.0))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.425))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,3.05))
        elems += spira.Circle(layer=C5J,box_size=(1.78, 1.78))
        elems += spira.Circle(layer=J5,box_size=(2.08, 2.08))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# M5 to M7 connector cell
class ls_conn_M5M6M7(spira.Cell):
    __name_prefix__ = 'ls_conn_M5M6M7'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.7,height=1.7,center=(0.35,0.35))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.35,0.35))
        elems += spira.Box(layer=M6,width=2.0,height=2.0,center=(0.35,0.35))
        elems += spira.Box(layer=I6,width=1.3,height=1.3,center=(0.35,0.35))
        elems += spira.Box(layer=M7,width=2.0,height=2.0,center=(0.35,0.35))

        return elems

# 1.36 Ohm resistor
class ls_res_1p36(spira.Cell):
    __name_prefix__ = 'ls_res_1p36'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.4*tp,height=0.31*tp,center=(0.0,0.155*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.256*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.25625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*tp,0.25625*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# 3.54 Ohm resistor
class ls_res_3p54(spira.Cell):
    __name_prefix__ = 'ls_res_3p54'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.30125*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.355*tp,center=(0.0,0.1775*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.302*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*tp,0.30125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports
        
# 4 Ohm resistor
class ls_res_4(spira.Cell):
    __name_prefix__ = 'ls_res_4'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.32875*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.3825*tp,center=(0.0,0.19125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.328*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*tp,0.32875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# 5.74 Ohm resistor
class ls_res_5p74(spira.Cell):
    __name_prefix__ = 'ls_res_5p74'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.4825*tp,center=(0.0,0.24125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.428*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.42875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0*tp,0.42875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0*tp,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# M0 Track block fill cell
class ls_tr_M0(spira.Cell):
    __name_prefix__ = 'ls_tr_M0'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=M0)
        elems += spira.Polygon(shape=upperHalf, layer=M0)
        elems += spira.Polygon(shape=middleCross, layer=M0)

        return elems

# M1 Track block fill cell
class ls_tr_M1(spira.Cell):
    __name_prefix__ = 'ls_tr_M1'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=M1)
        elems += spira.Polygon(shape=upperHalf, layer=M1)
        elems += spira.Polygon(shape=middleCross, layer=M1)

        return elems

# M7 Track block fill cell
class ls_tr_M7(spira.Cell):
    __name_prefix__ = 'ls_tr_M7'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=M7)
        elems += spira.Polygon(shape=upperHalf, layer=M7)
        elems += spira.Polygon(shape=middleCross, layer=M7)

        return elems

# Track block with bias pillar cell
class ls_tr_bias_pillar_M0M6(spira.Cell):
    __name_prefix__ = 'ls_tr_bias_pillar_M0M6'
    def create_elements(self, elems):
        # Common shapes
        top = spira.Shape(points=[
            (0.0,0.875),(0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.28),
            (0.77,0.28),(0.77,0.72),(0.96,0.72),(0.96,0.875),(0.875,0.875),(0.875,0.96),
            (0.72,0.96),(0.72,0.77),(0.28,0.77),(0.28,0.96),(0.125,0.96),(0.125,0.875)
            ])
        top = [x * tp for x in top]
        bot = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.72),(0.23,0.72),(0.23,0.28),
            (0.04,0.28),(0.04,0.125),(0.125,0.125),(0.125,0.04),(0.28,0.04),(0.28,0.23),
            (0.72,0.23),(0.72,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        bot = [x * tp for x in bot]

        elems += spira.Box(layer=M0,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I0,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))
        elems += spira.Box(layer=I0,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Polygon(shape=top, layer=M1)
        elems += spira.Polygon(shape=bot, layer=M1)
        elems += spira.Box(layer=M1,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I1,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I1,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I2,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))
        elems += spira.Box(layer=I2,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I3,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I3,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Polygon(shape=top, layer=M4)
        elems += spira.Polygon(shape=bot, layer=M4)
        elems += spira.Box(layer=M4,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I4,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))
        elems += spira.Box(layer=I4,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        elems += spira.Box(layer=M5,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I5,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I5,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=M6,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.SRef(ls_tr_M7())
        
        return elems

# Track block with half of a bias pillar
class ls_tr_bias_pillar_half(spira.Cell):
    __name_prefix__ = "ls_tr_bias_pillar_half"
    def create_elements(self, elems):
        elems += spira.Box(layer=M0,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.9375*tp))
        elems += spira.Box(layer=M0,width=0.22*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M0,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.0625*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.565*tp,0.935*tp))
        elems += spira.Box(layer=I0,width=0.12*tp,height=0.12*tp,center=(0.5*tp,0.39*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.435*tp,0.065*tp))
        elems += spira.Box(layer=M1,width=0.22*tp,height=1*tp,center=(0.11*tp,0.5*tp))
        elems += spira.Box(layer=M1,width=0.22*tp,height=1*tp,center=(0.89*tp,0.5*tp))
        elems += spira.Box(layer=M1,width=0.155*tp,height=0.04*tp,center=(0.2975*tp,0.98*tp))
        elems += spira.Box(layer=M1,width=0.155*tp,height=0.04*tp,center=(0.7025*tp,0.98*tp))
        elems += spira.Box(layer=M1,width=0.155*tp,height=0.04*tp,center=(0.2975*tp,0.02*tp))
        elems += spira.Box(layer=M1,width=0.155*tp,height=0.04*tp,center=(0.7025*tp,0.02*tp))
        elems += spira.Box(layer=M1,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.0625*tp))
        elems += spira.Box(layer=M1,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.9375*tp))
        elems += spira.Box(layer=M1,width=0.08*tp,height=0.105*tp,center=(0.5*tp,0.8225*tp))
        elems += spira.Box(layer=M1,width=0.08*tp,height=0.105*tp,center=(0.5*tp,0.1775*tp))
        elems += spira.Box(layer=M1,width=0.12*tp,height=0.44*tp,center=(0.28*tp,0.5*tp))
        elems += spira.Box(layer=M1,width=0.12*tp,height=0.44*tp,center=(0.72*tp,0.5*tp))
        elems += spira.Box(layer=M1,width=0.22*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.435*tp,0.935*tp))
        elems += spira.Box(layer=I1,width=0.12*tp,height=0.12*tp,center=(0.5*tp,0.61*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.565*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.9375*tp))
        elems += spira.Box(layer=M2,width=0.22*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M2,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.0625*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.565*tp,0.935*tp))
        elems += spira.Box(layer=I2,width=0.12*tp,height=0.12*tp,center=(0.5*tp,0.39*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.435*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.22*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M3,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.0625*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.435*tp,0.935*tp))
        elems += spira.Box(layer=I3,width=0.12*tp,height=0.12*tp,center=(0.5*tp,0.61*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.565*tp,0.065*tp))
        elems += spira.Box(layer=M4,width=0.22*tp,height=1*tp,center=(0.11*tp,0.5*tp))
        elems += spira.Box(layer=M4,width=0.22*tp,height=1*tp,center=(0.89*tp,0.5*tp))
        elems += spira.Box(layer=M4,width=0.155*tp,height=0.04*tp,center=(0.2975*tp,0.98*tp))
        elems += spira.Box(layer=M4,width=0.155*tp,height=0.04*tp,center=(0.7025*tp,0.98*tp))
        elems += spira.Box(layer=M4,width=0.155*tp,height=0.04*tp,center=(0.2975*tp,0.02*tp))
        elems += spira.Box(layer=M4,width=0.155*tp,height=0.04*tp,center=(0.7025*tp,0.02*tp))
        elems += spira.Box(layer=M4,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.0625*tp))
        elems += spira.Box(layer=M4,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.9375*tp))
        elems += spira.Box(layer=M4,width=0.08*tp,height=0.105*tp,center=(0.5*tp,0.8225*tp))
        elems += spira.Box(layer=M4,width=0.08*tp,height=0.105*tp,center=(0.5*tp,0.1775*tp))
        elems += spira.Box(layer=M4,width=0.12*tp,height=0.44*tp,center=(0.28*tp,0.5*tp))
        elems += spira.Box(layer=M4,width=0.12*tp,height=0.44*tp,center=(0.72*tp,0.5*tp))
        elems += spira.Box(layer=M4,width=0.22*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I4,width=0.12*tp,height=0.12*tp,center=(0.5*tp,0.39*tp))
        elems += spira.Box(layer=M5,width=0.22*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I5,width=0.12*tp,height=0.12*tp,center=(0.5*tp,0.61*tp))
        elems += spira.Box(layer=M6,width=0.22*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M7,width=0.22*tp,height=1*tp,center=(0.11*tp,0.5*tp))
        elems += spira.Box(layer=M7,width=0.22*tp,height=1*tp,center=(0.89*tp,0.5*tp))
        elems += spira.Box(layer=M7,width=0.155*tp,height=0.04*tp,center=(0.2975*tp,0.98*tp))
        elems += spira.Box(layer=M7,width=0.155*tp,height=0.04*tp,center=(0.7025*tp,0.98*tp))
        elems += spira.Box(layer=M7,width=0.155*tp,height=0.04*tp,center=(0.2975*tp,0.02*tp))
        elems += spira.Box(layer=M7,width=0.155*tp,height=0.04*tp,center=(0.7025*tp,0.02*tp))
        elems += spira.Box(layer=M7,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.0625*tp))
        elems += spira.Box(layer=M7,width=0.25*tp,height=0.125*tp,center=(0.5*tp,0.9375*tp))
        elems += spira.Box(layer=M7,width=0.08*tp,height=0.75*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M7,width=0.56*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        return elems

# PTL connection cell
class ls_tr_PTLconnection(spira.Cell):
    __name_prefix__ = 'ls_tr_PTLconnection'
    def create_elements(self, elems):
        # Common shape
        top = spira.Shape(points=[
            (0.0,0.875),(0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.28),
            (0.77,0.28),(0.77,0.72),(0.96,0.72),(0.96,0.875),(0.875,0.875),(0.875,0.96),
            (0.72,0.96),(0.72,0.77),(0.28,0.77),(0.28,0.96),(0.125,0.96),(0.125,0.875)
            ])
        top = [x * tp for x in top]
        bot = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.72),(0.23,0.72),(0.23,0.28),
            (0.04,0.28),(0.04,0.125),(0.125,0.125),(0.125,0.04),(0.28,0.04),(0.28,0.23),
            (0.72,0.23),(0.72,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        bot = [x * tp for x in bot]
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=M0)
        elems += spira.Polygon(shape=upperHalf, layer=M0)
        elems += spira.Polygon(shape=middleCross, layer=M0)
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M1,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I1,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I1,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Polygon(shape=top, layer=M2)
        elems += spira.Polygon(shape=bot, layer=M2)
        elems += spira.Box(layer=M2,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I2,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))
        elems += spira.Box(layer=I2,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I3,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I3,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Polygon(shape=top, layer=M4)
        elems += spira.Polygon(shape=bot, layer=M4)
        elems += spira.Box(layer=M4,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I4,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))
        elems += spira.Box(layer=I4,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        elems += spira.Box(layer=M5,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I5,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I5,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=M6,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.SRef(ls_tr_M7())

        return elems

# PTL connection cell
class ls_tr_PTLconnection_M3M6(spira.Cell):
    __name_prefix__ = 'ls_tr_PTLconnection_M3M6'
    def create_elements(self, elems):
        # Common shape
        top = spira.Shape(points=[
            (0.0,0.875),(0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.28),
            (0.77,0.28),(0.77,0.72),(0.96,0.72),(0.96,0.875),(0.875,0.875),(0.875,0.96),
            (0.72,0.96),(0.72,0.77),(0.28,0.77),(0.28,0.96),(0.125,0.96),(0.125,0.875)
            ])
        top = [x * tp for x in top]
        bot = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.72),(0.23,0.72),(0.23,0.28),
            (0.04,0.28),(0.04,0.125),(0.125,0.125),(0.125,0.04),(0.28,0.04),(0.28,0.23),
            (0.72,0.23),(0.72,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        bot = [x * tp for x in bot]
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=M0)
        elems += spira.Polygon(shape=upperHalf, layer=M0)
        elems += spira.Polygon(shape=middleCross, layer=M0)
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Polygon(shape=lowerHalf, layer=M1)
        elems += spira.Polygon(shape=upperHalf, layer=M1)
        elems += spira.Polygon(shape=middleCross, layer=M1)
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Polygon(shape=lowerHalf, layer=M2)
        elems += spira.Polygon(shape=upperHalf, layer=M2)
        elems += spira.Polygon(shape=middleCross, layer=M2)
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I3,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I3,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Polygon(shape=top, layer=M4)
        elems += spira.Polygon(shape=bot, layer=M4)
        elems += spira.Box(layer=M4,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I4,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))
        elems += spira.Box(layer=I4,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        elems += spira.Box(layer=M5,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I5,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I5,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=M6,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.SRef(ls_tr_M7())

        return elems

# Track block cell
class ls_tr_u_M4_alt(spira.Cell):
    __name_prefix__ = 'ls_tr_u_M4_alt'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * tp for x in middleCross]
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Polygon(shape=lowerHalf, layer=M1)
        elems += spira.Polygon(shape=upperHalf, layer=M1)
        elems += spira.Polygon(shape=middleCross, layer=M1)
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Polygon(shape=lowerHalf, layer=M4)
        elems += spira.Polygon(shape=upperHalf, layer=M4)
        elems += spira.Polygon(shape=middleCross, layer=M4)

        return elems

# Track block cell
class ls_tr_u_M4(spira.Cell):
    __name_prefix__ = 'ls_tr_u_M4'
    def create_elements(self, elems):
        lowerHalf = spira.Shape(points=[
            (0.0,0.0),(0.0,0.875),(0.04,0.875),(0.04,0.125),(0.125,0.125),
            (0.125,0.04),(0.875,0.04),(0.875,0.125),(1.0,0.125),(1.0,0.0)
            ])
        lowerHalf = [x * tp for x in lowerHalf]
        upperHalf = spira.Shape(points=[
            (0.0,1.0),(1.0,1.0),(1.0,0.125),(0.96,0.125),(0.96,0.875),
            (0.875,0.875),(0.875,0.96),(0.125,0.96),(0.125,0.875),(0.0,0.875)
            ])
        upperHalf = [x * tp for x in upperHalf]
        middleCross = spira.Shape(points=[
            (0.28,0.04),(0.28,0.28),(0.04,0.28),(0.04,0.72),(0.28,0.72),(0.28,0.96),
            (0.72,0.96),(0.72,0.72),(0.96,0.72),(0.96,0.28),(0.72,0.28),(0.72,0.04)
            ])
        middleCross = [x * tp for x in middleCross]
        elems += spira.Polygon(shape=lowerHalf, layer=M0)
        elems += spira.Polygon(shape=upperHalf, layer=M0)
        elems += spira.Polygon(shape=middleCross, layer=M0)
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Polygon(shape=lowerHalf, layer=M2)
        elems += spira.Polygon(shape=upperHalf, layer=M2)
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Polygon(shape=lowerHalf, layer=M4)
        elems += spira.Polygon(shape=upperHalf, layer=M4)
        elems += spira.Polygon(shape=middleCross, layer=M4)

        return elems

# Quarter 1 of trackblock cell
class ls_tr_u_M4_quarter1(spira.Cell):
    __name_prefix__ = "ls_tr_u_M4_quarter1"
    def create_elements(self, elems):
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=M1,width=0.22*tp,height=0.5*tp,center=(0.39*tp,0.25*tp))
        elems += spira.Box(layer=M1,width=0.28*tp,height=0.22*tp,center=(0.14*tp,0.39*tp))
        elems += spira.Box(layer=M1,width=0.04*tp,height=0.155*tp,center=(0.02*tp,0.2025*tp))
        elems += spira.Box(layer=M1,width=0.155*tp,height=0.04*tp,center=(0.2025*tp,0.02*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I3,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M4,width=0.22*tp,height=0.5*tp,center=(0.39*tp,0.25*tp))
        elems += spira.Box(layer=M4,width=0.28*tp,height=0.22*tp,center=(0.14*tp,0.39*tp))
        elems += spira.Box(layer=M4,width=0.04*tp,height=0.155*tp,center=(0.02*tp,0.2025*tp))
        elems += spira.Box(layer=M4,width=0.155*tp,height=0.04*tp,center=(0.2025*tp,0.02*tp))
        elems += spira.Box(layer=M4,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=M7,width=0.22*tp,height=0.5*tp,center=(0.39*tp,0.25*tp))
        elems += spira.Box(layer=M7,width=0.28*tp,height=0.22*tp,center=(0.14*tp,0.39*tp))
        elems += spira.Box(layer=M7,width=0.04*tp,height=0.155*tp,center=(0.02*tp,0.2025*tp))
        elems += spira.Box(layer=M7,width=0.155*tp,height=0.04*tp,center=(0.2025*tp,0.02*tp))
        elems += spira.Box(layer=M7,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        return elems

# Quarter 2 of trackblock cell
class ls_tr_u_M4_quarter2(spira.Cell):
    __name_prefix__ = "ls_tr_u_M4_quarter2"
    def create_elements(self, elems):
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(-0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(-0.065*tp,0.065*tp))
        elems += spira.Box(layer=M1,width=0.22*tp,height=0.5*tp,center=(-0.39*tp,0.25*tp))
        elems += spira.Box(layer=M1,width=0.28*tp,height=0.22*tp,center=(-0.14*tp,0.39*tp))
        elems += spira.Box(layer=M1,width=0.04*tp,height=0.155*tp,center=(-0.02*tp,0.2025*tp))
        elems += spira.Box(layer=M1,width=0.155*tp,height=0.04*tp,center=(-0.2025*tp,0.02*tp))
        elems += spira.Box(layer=M1,width=0.125*tp,height=0.125*tp,center=(-0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(-0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I2,width=0.06*tp,height=0.06*tp,center=(-0.065*tp,0.065*tp))
        elems += spira.Box(layer=M3,width=0.125*tp,height=0.125*tp,center=(-0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=M4,width=0.22*tp,height=0.5*tp,center=(-0.39*tp,0.25*tp))
        elems += spira.Box(layer=M4,width=0.28*tp,height=0.22*tp,center=(-0.14*tp,0.39*tp))
        elems += spira.Box(layer=M4,width=0.04*tp,height=0.155*tp,center=(-0.02*tp,0.2025*tp))
        elems += spira.Box(layer=M4,width=0.155*tp,height=0.04*tp,center=(-0.2025*tp,0.02*tp))
        elems += spira.Box(layer=M4,width=0.125*tp,height=0.125*tp,center=(-0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=M7,width=0.22*tp,height=0.5*tp,center=(-0.39*tp,0.25*tp))
        elems += spira.Box(layer=M7,width=0.28*tp,height=0.22*tp,center=(-0.14*tp,0.39*tp))
        elems += spira.Box(layer=M7,width=0.04*tp,height=0.155*tp,center=(-0.02*tp,0.2025*tp))
        elems += spira.Box(layer=M7,width=0.155*tp,height=0.04*tp,center=(-0.2025*tp,0.02*tp))
        elems += spira.Box(layer=M7,width=0.125*tp,height=0.125*tp,center=(-0.0625*tp,0.0625*tp))
        return elems