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
L1_width = 0.14*tp*Scaling
L2_width = 0.16*tp*Scaling
L3_width = 0.22*tp*Scaling
L4_width = 0.1575*tp*Scaling
L5_width = 0.16*tp*Scaling
L6_width = 0.22*tp*Scaling
L7_width = 0.155*tp*Scaling
L8_width = 0.2*tp*Scaling
L9_width = 0.215*tp*Scaling
L10_width = 0.125*tp*Scaling
LB1_width = 0.14*tp*Scaling
LB2_width = 0.16*tp*Scaling

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
    __name_prefix__ = "LSmitll_MERGET_v2p1"
    def create_elements(self, elems):
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        M0M4M7tracks = spira.SRef(M0M4M7_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        res = spira.SRef(resistors())
        tblocks = spira.SRef(trackblocks())
        elems += [M6M5Strips, IXports, M0M4M7tracks, jjfill, M4M5M6M7conns,
                  vias, bias, jjs, res, tblocks]
        # Bias ports
        PB1W = spira.Port(name='PB1W',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name='PB1E',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2W = spira.Port(name='PB2W',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2E = spira.Port(name='PB2E',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3W = spira.Port(name='PB3W',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3E = spira.Port(name='PB3E',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4N = spira.Port(name='PB4N',midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name='PB4S',midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(6.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1N = spira.Port(name='PR1N',midpoint=res.reference.elements['R1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1S = spira.Port(name='PR1S',midpoint=res.reference.elements['R1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Junction ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ5 = spira.Port(name="PJ5",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ6 = spira.Port(name="PJ6",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ7 = spira.Port(name="PJ7",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ8 = spira.Port(name="PJ8",midpoint=jjs.reference.elements['J8'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=(6.5*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN17 = spira.Port(name="PN17",midpoint=(6.51*tp,4.5125*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ4,path=[(PJ4.x,PA.y)],width=L1_width,layer=M6)
        L2 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(4.51*tp,PJ4.y),(4.51*tp,PJ5.y)],width=L2_width,layer=M6)
        L3_1 = spira.RoutePath(port1=PJ5,port2=PJ6,path=[(PJ5.x,PJ6.y)],width=L3_width,layer=M6)
        L3_2 = spira.RoutePath(port1=PJ6,port2=PV1,path=[(PJ6.x,PV1.y)],width=L3_width,layer=M5)
        L4 = spira.RoutePath(port1=PB,port2=PJ1,path=[(PJ1.x,PB.y)],width=L4_width,layer=M6)
        L5 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(4.51*tp,PJ1.y),(4.51*tp,PJ2.y)],width=L5_width,layer=M6)
        L6_1 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(PJ2.x,PJ3.y)],width=L6_width,layer=M6)
        L6_2 = spira.RoutePath(port1=PJ3,port2=PV1,path=[(PJ3.x,PV1.y)],width=L6_width,layer=M5)
        L7 = spira.RoutePath(port1=PV1,port2=PJ7,path=[(PJ7.x,PV1.y)],width=L7_width,layer=M6)
        L8 = spira.RoutePath(port1=PJ7,port2=PN17,path=[(PJ7.x,PN17.y)],width=L8_width,layer=M6)
        L9 = spira.RoutePath(port1=PN17,port2=PJ8,path=[(PJ8.x,PN17.y)],width=L9_width,layer=M6)
        L10_1 = spira.RoutePath(port1=PJ8,port2=PR1N,path=[(PR1N.x,PJ8.y)],width=L10_width,layer=M6)
        L10_2 = spira.RoutePath(port1=PR1S,port2=PQ,path=[(PR1S.x,PQ.y)],width=L10_width,layer=M6)

        elems += [L1, L2, L3_1, L3_2, L4, L5, L6_1, L6_2, L7, L8, L9, L10_1, L10_2]
        
        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1E,path=[(PJ1.x,PB1E.y)],width=LB1_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PV2,path=[(0.5*tp,PB1W.y),(0.5*tp,PV2.y)],width=LB1_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PJ4,port2=PB2E,path=[(PJ4.x,PB2E.y)],width=LB1_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2W,port2=PV2,path=[(0.5*tp,PB2W.y),(0.5*tp,PV2.y)],width=LB2_width,layer=M6)
        LB3_1 = spira.RoutePath(port1=PV1,port2=PB3E,path=[(PV1.x,PB3E.y)],width=LB1_width,layer=M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PV2,path=[(0.5*tp,PB3W.y),(0.5*tp,PV2.y)],width=LB1_width,layer=M6)
        LB4_1 = spira.RoutePath(port1=PN17,port2=PB4S,path=[(PN17.x,PB4S.y)],width=LB1_width,layer=M6)
        LB4_2 = spira.RoutePath(port1=PB4N,port2=PV2,path=[(PB4N.x,PV2.y)],width=LB1_width,layer=M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2]

        LBias = spira.RoutePath(port1=PV2,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="bias_in",position=(6.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(6.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(1.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(6.5145*tp,5.224*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(2.3495*tp,3.505*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(2.242*tp,2.49*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(2.2405*tp,4.5095*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.83*tp,1.5075*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(6.499*tp,2.2065*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(6.515*tp,2.54*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(5.4575*tp,3.5075*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(3.5025*tp,3.085*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(3.51*tp,2.64*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(2.4875*tp,1.505*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(3.5025*tp,3.9175*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(3.51*tp,4.36*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(2.485*tp,5.4975*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.82*tp,5.4875*tp),layer=TEXT)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,6.495*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(6.9875*tp,2.495*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(6.9875*tp,1.495*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,6.495*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(6.9875*tp,2.495*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(6.9875*tp,1.495*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,1.55*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,1.13*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(6.17*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.75*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.33*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.91*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.49*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.07*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(3.65*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(3.23*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(2.81*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(2.39*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.97*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.55*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.13*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,0.71*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,1.13*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,1.55*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(0.71*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,0.71*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,1.97*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.5*tp,5.5*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.83*tp,1.50875*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.82*tp,5.48375*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.515*tp,5.225*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.5*tp,2.206*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.24*tp,2.49*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.35*tp,3.505*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.24*tp,4.51*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(3.72*tp,3.72*tp),(3.72*tp,4.28*tp),(4.28*tp,4.28*tp),(4.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(3.72*tp,2.72*tp),(3.72*tp,3.28*tp),(4.28*tp,3.28*tp),(4.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(5.54*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(4.7*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(5.5*tp,2.18*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(5.5*tp,1.76*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(5.29*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(5.96*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(3.86*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(5.5*tp,1.34*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(5.5*tp,0.92*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(6.38*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(5.12*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(4.28*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(0.5*tp,0.92*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(0.5*tp,1.76*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(3.02*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(2.18*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(1.34*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(0.92*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(1.76*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(2.6*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(0.5*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(5.71*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(3.44*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3x3um(),midpoint=(0.5*tp,1.34*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,2.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.34*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.34*tp,2.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,1.835*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,4.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.34*tp,4.7375*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.34*tp,4.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.34*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.34*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.3325*tp,4.965*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,1.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.34*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.34*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.34*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.34*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.34*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.34*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.34*tp,1.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.34*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,3.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.34*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.34*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.34*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,5.835*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.34*tp,3.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.34*tp,2.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.34*tp,2.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.265*tp,3.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.9275*tp,1.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.975*tp,2.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.165*tp,1.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.975*tp,1.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.9275*tp,2.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.265*tp,2.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.165*tp,1.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.2525*tp,4.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.9275*tp,5.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.9275*tp,4.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.6175*tp,3.85*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.875*tp,5.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.265*tp,5.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.875*tp,4.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.875*tp,4.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.265*tp,4.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.875*tp,6.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.875*tp,3.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.875*tp,2.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.165*tp,6.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.875*tp,3.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.67*tp,2.635*tp),transformation=r180)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.4775*tp,3.1775*tp),transformation=r270)
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7_block(),midpoint=(4*tp,5*tp))
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(3.42*tp,3.42*tp),alias='via1')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(6.43*tp,6.42*tp),alias='via2')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_148(),midpoint=(2.295*tp,2.49*tp),transformation=r90,alias='bias2')
        elems += spira.SRef(ls_ib_148(),midpoint=(2.295*tp,4.51*tp),transformation=r90,alias='bias1')
        elems += spira.SRef(ls_ib_176(),midpoint=(6.515*tp,5.17*tp),alias='bias4')
        elems += spira.SRef(ls_ib_241(),midpoint=(2.405*tp,3.505*tp),transformation=r90,alias='bias3')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_095_s(),midpoint=(3.5*tp,3.085*tp),transformation=r270,alias='J6')
        elems += spira.SRef(ls_jj_095_s(),midpoint=(3.5*tp,3.915*tp),transformation=r270,alias='J3')
        elems += spira.SRef(ls_jj_116_sg(),midpoint=(5.46*tp,3.51*tp),transformation=r180,alias='J7')
        elems += spira.SRef(ls_jj_154_sg(),midpoint=(3.51*tp,2.64*tp),transformation=r180,alias='J5')
        elems += spira.SRef(ls_jj_154_sg(),midpoint=(3.51*tp,4.36*tp),alias='J2')
        elems += spira.SRef(ls_jj_160_sg(),midpoint=(2.47*tp,1.505*tp),transformation=r180,alias='J4')
        elems += spira.SRef(ls_jj_160_sg(),midpoint=(2.485*tp,5.495*tp),alias='J1')
        elems += spira.SRef(ls_jj_250_sg(),midpoint=(6.51*tp,2.54*tp),transformation=r90,alias='J8')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(ls_res_1p36(),midpoint=(6.5*tp,1.95*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 7):
                if (x == 1 and y in [1,5]) or (x == 6 and y == 1):
                    elems += spira.SRef(ls_tr_PTLconnection(),midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(ls_tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(ls_tr_M7(),midpoint=(0+x*tp,0+y*tp))
        return elems

# 1.5um junction fill cell
class ls_FakeJJ_1p5x1p5um(spira.Device):
    __name_prefix__ = 'ls_FakeJJ_1p5umx1p5um'
    def create_elements(self, elems):
        elems += spira.Box(layer=M4,width=0.25*tp,height=0.25*tp)
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.25*tp)
        elems += spira.Box(layer=J5,width=0.15*tp,height=0.15*tp)
        elems += spira.Box(layer=C5J,width=0.13*tp,height=0.13*tp)
        elems += spira.Box(layer=M6,width=0.2*tp,height=0.2*tp)

        return elems

# 3um junction fill cell
class ls_FakeJJ_3x3um(spira.Cell):
    __name_prefix__ = 'ls_FakeJJ_3x3um'
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

# M7 Track block fill cell
class ls_tr_M7(spira.Cell):
    __name_prefix__ = 'ls_tr_M7'
    def create_elements(self, elems):
        elems += spira.Polygon(shape=lowerHalf, layer=M7)
        elems += spira.Polygon(shape=upperHalf, layer=M7)
        elems += spira.Polygon(shape=middleCross, layer=M7)

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