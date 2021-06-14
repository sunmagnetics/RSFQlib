import sys
import os
import spira.all as spira
from spira.technologies.mit.process.database import RDD
from spira.technologies.mit import devices as dev
from spira.yevon.geometry.coord import Coord
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
IXPORT = spira.RDD.PLAYER.IXPORT
TEXT = spira.Layer(number=182)
# Shorthand for rotations and reflections
r90 = spira.Rotation(90)
r180 = spira.Rotation(180)
r270 = spira.Rotation(270)
m0 = spira.Reflection(True)
m45 = r270 + spira.Reflection(True)
m90 = r180 + spira.Reflection(True)
m135 = r90 + spira.Reflection(True)
m270 = m135

## Parameterization
# Trackpitch in microns
tp = 10

# Inductor widths
Scaling = (1+(tp-10)*0.25)
L1_width = 0.15*tp*Scaling
L2_width = 0.12*tp*Scaling
L3_width = 0.18*tp*Scaling
L4_width = 0.11*tp*Scaling
L5_width = 0.17*tp*Scaling
L6_width = 0.1*tp*Scaling
LB_width = 0.15*tp*Scaling

# Common Shapes
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

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_DCSFQ_v2p1"
    def create_elements(self, elems):
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        tblocks = spira.SRef(trackblocks())
        elems += [M6M5Strips, IXports, jjfill, M4M5M6M7conns,
                  vias, bias, jjs, tblocks]
        # Bias ports
        PB1N = spira.Port(name='PB1N',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name='PB1S',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name='PB2N',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name='PB2S',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(1.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
        # Junction ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)

        PGND = spira.Port(name="PGND",midpoint=(0.5*tp,0.9925*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PV1,path=[(PV1.x,PA.y)],width=L1_width,layer=M6)
        L2 = spira.RoutePath(port1=PGND,port2=PV1,path=[(PV1.x,PGND.y)],width=L2_width,layer=M5)
        L3 = spira.RoutePath(port1=PV1,port2=PJ1,path=[(PJ1.x,PV1.y)],width=L3_width,layer=M5)
        L4 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(PJ1.x,PJ2.y)],width=L4_width,layer=M6)
        L5 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(PJ2.x,1.5*tp),(PJ3.x,1.5*tp)],width=L5_width,layer=M6)
        L6 = spira.RoutePath(port1=PQ,port2=PJ3,path=[(PQ.x,PJ3.y)],width=L6_width,layer=M6)

        elems += [L1, L2, L3, L4, L5, L6]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1S,path=[(PJ1.x,PB1S.y)],width=LB_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1N,port2=PV2,path=[(PB1N.x,PB1N.y)],width=LB_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2S,path=[(PJ3.x,PB2S.y)],width=LB_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PV2,path=[(PV2.x,PB2N.y)],width=LB_width,layer=M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2]

        LBias = spira.RoutePath(port1=PV2,port2=PBias,path=[(PBias.x,PBias.y)],width=LB_width,layer=M5)

        elems += LBias

        elems += spira.Box(layer=M4,width=0.25*tp,height=0.56*tp,center=(0.845*tp,3.0*tp))
        elems += spira.Box(layer=M7,width=0.25*tp,height=0.56*tp,center=(0.845*tp,3.0*tp))

        # Text Labels
        elems += spira.Label(text="P2 M6 M4",position=(3*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="bias",position=(1.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(3*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(0*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(2.5025*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(1.4975*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M5 M6",position=(0.8625*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(2.5*tp,3.605*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0*tp,2.5125*tp),layer=TEXT)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.015*tp,center=(2.5075*tp,4.9925*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.015*tp,center=(2.5075*tp,4.9925*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(2.37*tp,0.505*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.95*tp,0.505*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.53*tp,0.505*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.11*tp,0.505*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(0.69*tp,0.505*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,4.295*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(0.51*tp,4.505*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(0.51*tp,5.505*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(0.51*tp,6.505*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(2.51*tp,6.505*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(2.51*tp,5.505*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,2.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(3.0*tp,2.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(1.5*tp,3.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(2.5*tp,3.6025*tp))
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.3*tp,5.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,6.005*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5.005*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,6.005*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.72*tp,5.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.3*tp,5.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.3*tp,6.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.72*tp,6.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.72*tp,6.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.3*tp,6.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.16*tp,0.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.72*tp,5.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.72*tp,4.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.3*tp,4.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,4.085*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.9*tp,0.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.48*tp,0.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.32*tp,0.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.74*tp,0.505*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.58*tp,0.505*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.9075*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.875*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.875*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.255*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.265*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.875*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.875*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.875*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.905*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.23*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.6*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.265*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.665*tp,1.265*tp),transformation=r180)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.665*tp,1.2325*tp),transformation=r180)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.665*tp,2.875*tp),transformation=r180)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.665*tp,4.985*tp),transformation=r180)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.1725*tp),transformation=r180)
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(2*tp,4*tp))
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(1.415*tp,6.415*tp),alias='via2')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(0.415*tp,2.415*tp),alias='via1')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_175(),midpoint=(2.5*tp,3.5475*tp),alias='bias2')
        elems += spira.SRef(ls_ib_275(),midpoint=(1.5*tp,3.445*tp),alias='bias1')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_225_s(),midpoint=(0.865*tp,2.4975*tp),transformation=r180,alias="J1")
        elems += spira.SRef(ls_jj_225_sg(),midpoint=(1.5*tp,2.5*tp),alias="J2")
        elems += spira.SRef(ls_jj_250_sg(),midpoint=(2.5*tp,2.5*tp),transformation=r90,alias="J3")
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                elems += spira.SRef(ls_tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                elems += spira.SRef(ls_tr_M7(),midpoint=(0+x*tp,0+y*tp))
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

# M7 Track block fill cell
class ls_tr_M7(spira.Cell):
    __name_prefix__ = 'ls_tr_M7'
    def create_elements(self, elems):
        elems += spira.Polygon(shape=lowerHalf, layer=M7)
        elems += spira.Polygon(shape=upperHalf, layer=M7)
        elems += spira.Polygon(shape=middleCross, layer=M7)

        return elems

# Track block cell
class ls_tr_u_M4(spira.Cell):
    __name_prefix__ = 'ls_tr_u_M4'
    def create_elements(self, elems):
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

sys.stdout.write("Adjusting settings.\n")
F = RDD.FILTERS.OUTPUT.PORTS
F['cell_ports'] = False
F['edge_ports'] = False
F['contact_ports'] = False
F = RDD.FILTERS.PCELL.DEVICE
F['boolean'] = True
F['contact_attach'] = True
F = RDD.FILTERS.PCELL.CIRCUIT
F['boolean'] = False

D = PCELL()
sys.stdout.write("Writing output.\n")
D.gdsii_output(os.path.splitext(__file__)[0])