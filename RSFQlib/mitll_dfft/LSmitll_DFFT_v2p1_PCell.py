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
L2_width = 0.12*tp*Scaling
L3_width = 0.12*tp*Scaling
L4_width = 0.12*tp*Scaling
L5_width = 0.135*tp*Scaling
L6_width = 0.14*tp*Scaling
L7_width = 0.165*tp*Scaling
L8_width = 0.17*tp*Scaling
L9_width = 0.115*tp*Scaling
L10_width = 0.115*tp*Scaling
L11_width = 0.1*tp*Scaling
L12_width = 0.11*tp*Scaling
L13_width = 0.13*tp*Scaling
LB_width = 0.14*tp*Scaling

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
    __name_prefix__ = "LSmitll_DFFT_v2p1"
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
        PJ9 = spira.Port(name="PJ9",midpoint=jjs.reference.elements['J9'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ10 = spira.Port(name="PJ10",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=(6.5*tp,1.545*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN5 = spira.Port(name="PN5",midpoint=(2.5*tp,3.09*tp),process=spira.RDD.PROCESS.M6)
        PN15 = spira.Port(name="PN15",midpoint=(2.5*tp,3.61*tp),process=spira.RDD.PROCESS.M6)
        PN23 = spira.Port(name="PN23",midpoint=(PJ10.x,PJ9.y),process=spira.RDD.PROCESS.M6)
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PJ1.x,PA.y)],width=L1_width,layer=M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PN5,path=[(PN5.x,PJ1.y)],width=L2_width,layer=M6)
        L3 = spira.RoutePath(port1=PN5,port2=PJ2,path=[(PJ2.x,PN5.y)],width=L3_width,layer=M6)
        L4_1 = spira.RoutePath(port1=PJ2,port2=PV1,path=[(PJ2.x,PV1.y)],width=L4_width,layer=M6)
        L4_2 = spira.RoutePath(port1=PV1,port2=PJ3,path=[(PV1.x,PJ3.y)],width=L4_width,layer=M5)
        L4_3 = spira.RoutePath(port1=PJ3,port2=PJ4,path=[(PJ3.x,PJ4.y)],width=L4_width,layer=M6)
        L5 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(PJ5.x,PJ4.y)],width=L5_width,layer=M6)
        L6 = spira.RoutePath(port1=PCLK,port2=PJ6,path=[(PCLK.x,PJ6.y)],width=L6_width,layer=M6)
        L7 = spira.RoutePath(port1=PJ6,port2=PN15,path=[(PJ6.x,PN15.y)],width=L7_width,layer=M6)
        L8 = spira.RoutePath(port1=PN15,port2=PJ7,path=[(PJ7.x,PN15.y)],width=L8_width,layer=M6)
        L9_1 = spira.RoutePath(port1=PJ7,port2=PV2,path=[(PJ7.x,PV2.y)],width=L9_width,layer=M6)
        L9_2 = spira.RoutePath(port1=PV2,port2=PJ8,path=[(PJ8.x,PV2.y)],width=L9_width,layer=M5)
        L9_3 = spira.RoutePath(port1=PJ8,port2=PJ5,path=[(PJ8.x,PJ5.y)],width=L9_width,layer=M6)
        L10 = spira.RoutePath(port1=PJ5,port2=PJ9,path=[(PJ9.x,PJ5.y)],width=L10_width,layer=M6)
        L11 = spira.RoutePath(port1=PJ9,port2=PN23,path=[(PN23.x,PJ9.y)],width=L11_width,layer=M6)
        L12 = spira.RoutePath(port1=PN23,port2=PJ10,path=[(PJ10.x,PN23.y)],width=L12_width,layer=M6)
        L13_1 = spira.RoutePath(port1=PJ10,port2=PR1N,path=[(PR1N.x,PJ10.y)],width=L13_width,layer=M6)
        L13_2 = spira.RoutePath(port1=PR1S,port2=PQ,path=[(PR1S.x,PQ.y)],width=L13_width,layer=M6)

        elems += [L1, L2, L3, L4_1, L4_2, L4_3, L5, L6, L7, L8, L9_1, L9_2, L9_3, L10, L11, L12, L13_1, L13_2]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PN5,port2=PB1E,path=[(PB1E.x,PN5.y)],width=LB_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PV3,path=[(0.5*tp,PB1W.y),(0.5*tp,PV3.y)],width=LB_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2E,path=[(PJ3.x,PB2E.y)],width=LB_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2W,port2=PV3,path=[(0.5*tp,PB2W.y),(0.5*tp,PV3.y)],width=LB_width,layer=M6)
        LB3_1 = spira.RoutePath(port1=PN15,port2=PB3E,path=[(1.56*tp,PN15.y),(1.56*tp,PB3E.y)],width=LB_width,layer=M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PV3,path=[(0.5*tp,PB3W.y),(0.5*tp,PV3.y)],width=LB_width,layer=M6)
        LB4_1 = spira.RoutePath(port1=PN23,port2=PB4S,path=[(PN23.x,PB4S.y)],width=LB_width,layer=M6)
        LB4_2 = spira.RoutePath(port1=PB4N,port2=PV3,path=[(PB4N.x,PV3.y)],width=LB_width,layer=M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2]

        LBias = spira.RoutePath(port1=PV3,port2=PBias,path=[(PBias.x,PBias.y)],width=LB_width,layer=M6)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="bias",position=(6.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(6.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(1.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="clk",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(7.4985*tp,4.4015*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.815*tp,5.5025*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(2.515*tp,5.49*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(1.2225*tp,3.61*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(3.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(5.4975*tp,4.495*tp),layer=TEXT)
        elems += spira.Label(text="J8 M5 M6",position=(4.5025*tp,4.4925*tp),layer=TEXT)
        elems += spira.Label(text="J9 M6 M5",position=(6.5*tp,3.495*tp),layer=TEXT)
        elems += spira.Label(text="J3 M5 M6",position=(4.51*tp,2.495*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.2795*tp,2.4945*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(7.5*tp,2.495*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(3.505*tp,2.4775*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(6.497*tp,2.2525*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.8225*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(2.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(4.505*tp,1.4975*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(4.229*tp,0.501*tp),layer=TEXT)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,2.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,6.4925*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,2.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,6.4925*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.4925*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(3.5*tp,1.29*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(4.5*tp,3.71*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(3.5*tp,5.71*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(4.5*tp,5.71*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(5.5*tp,5.71*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(7.5*tp,1.13*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(7.5*tp,0.71*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(6.5*tp,5.29*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(6.5*tp,5.71*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.5*tp,4.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(6.23*tp,5.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.81*tp,5.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.39*tp,5.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.97*tp,5.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.5*tp,5.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.13*tp,5.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(7.09*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(6.67*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(6.25*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.83*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.41*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(7.51*tp,0.575*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(3.71*tp,5.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(6.65*tp,5.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.5*tp,3.5*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.815*tp,5.5075*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.82*tp,1.49875*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.28*tp,2.495*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.23*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.5*tp,2.256*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.5*tp,4.4*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.225*tp,3.61*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(2.72*tp,2.72*tp),(2.72*tp,2.96*tp),(3.28*tp,2.96*tp),(3.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(1.72*tp,3.04*tp),(1.72*tp,3.28*tp),(3.28*tp,3.28*tp),(3.28*tp,3.04*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(2.72*tp,3.72*tp),(2.72*tp,3.96*tp),(3.28*tp,3.96*tp),(3.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6.785*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3.5*tp,5.845*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6.5*tp,5.155*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5.5*tp,5.845*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6.5*tp,5.845*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4.5*tp,3.845*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4.5*tp,5.845*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7.645*tp,0.575*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3.505*tp,1.155*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.29*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.29*tp,3.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.76*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(7.3*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.92*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.71*tp,3.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(6.44*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.18*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.34*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.6*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(6.46*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.71*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,1.34*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(6.88*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.62*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(6.04*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.2*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,0.92*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(6.02*tp,5.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.3325*tp,1.0125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.3275*tp,5.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.835*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.7725*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.3425*tp,1.85*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.3425*tp,2.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.2275*tp,3.28*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.6625*tp,3.28*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,1.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.155*tp,3.28*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.325*tp,1.065*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.165*tp,3.28*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.6425*tp,3.28*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,4.1075*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.3275*tp,4.7625*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.835*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.3275*tp,3.79*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.8825*tp,2.5*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.155*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.875*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.875*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.265*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.2375*tp,2.3325*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.89*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.8875*tp,3.3475*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.27*tp,3.3325*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.88*tp,3.33*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.235*tp,3.33*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.215*tp,2.345*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.875*tp,0.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.245*tp,2.3225*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.915*tp,2.3225*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.215*tp,2.5*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.89*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.975*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.875*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.975*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.165*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.9325*tp,4.32*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.96*tp,2.3325*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.975*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.2075*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.2625*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.905*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.165*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.165*tp,0.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=r90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(3.915*tp,2.415*tp),alias='via1')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(3.915*tp,4.4125*tp),alias='via2')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(6.4175*tp,6.42*tp),alias='via3')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_235(),midpoint=(4.285*tp,0.5*tp),transformation=r90,alias='bias2')
        elems += spira.SRef(ls_ib_276(),midpoint=(1.335*tp,2.495*tp),transformation=r90,alias='bias1')
        elems += spira.SRef(ls_ib_284(),midpoint=(1.28*tp,3.61*tp),transformation=r90,alias='bias3')
        elems += spira.SRef(ls_ib_312(),midpoint=(7.5*tp,4.345*tp),alias='bias4')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_162_sg(),midpoint=(2.5*tp,5.5*tp),transformation=r270,alias='J6')
        elems += spira.SRef(ls_jj_162_sg(),midpoint=(2.5*tp,1.5*tp),transformation=r270,alias='J1')
        elems += spira.SRef(ls_jj_171_s(),midpoint=(4.5*tp,2.5*tp),alias='J3')
        elems += spira.SRef(ls_jj_171_s(),midpoint=(4.5*tp,4.5*tp),alias='J8')
        elems += spira.SRef(ls_jj_189_sg(),midpoint=(3.5*tp,2.5*tp),transformation=r180,alias='J2')
        elems += spira.SRef(ls_jj_198_sg(),midpoint=(3.5*tp,4.5*tp),alias='J7')
        elems += spira.SRef(ls_jj_212_sg(),midpoint=(5.5*tp,4.5*tp),alias='J5')
        elems += spira.SRef(ls_jj_212_sg(),midpoint=(6.5*tp,3.5*tp),transformation=r180,alias='J9')
        elems += spira.SRef(ls_jj_232_sg(),midpoint=(4.5*tp,1.5*tp),transformation=r90,alias='J4')
        elems += spira.SRef(ls_jj_250_sg(),midpoint=(7.5*tp,2.5*tp),transformation=r180,alias='J10')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(ls_res_1p36(),midpoint=(6.5*tp,2*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 8):
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