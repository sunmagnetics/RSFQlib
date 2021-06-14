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
L1_width = 0.08*tp*Scaling
L3_width = 0.25*tp*Scaling
L4_width = 0.25*tp*Scaling
L5_width = 0.08*tp*Scaling
L6_width = 0.105*tp*Scaling
L7_width = 0.15*tp*Scaling
L8_width = 0.14*tp*Scaling
L10_width = 0.25*tp*Scaling
L11_width = 0.0975*tp*Scaling
L12_width = 0.11*tp*Scaling
L13_width = 0.125*tp*Scaling
L14_width = 0.15*tp*Scaling
LB1_width = 0.14*tp*Scaling
LB2_width = 0.2*tp*Scaling

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
    __name_prefix__ = "LSmitll_SFQDC_v2p1"
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
        PB1N = spira.Port(name='PB1N',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name='PB1S',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name='PB2N',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name='PB2S',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3N = spira.Port(name='PB3N',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name='PB3S',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4N = spira.Port(name='PB4N',midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name='PB4S',midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(4.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1W = spira.Port(name='PR1W',midpoint=res.reference.elements['R1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1E = spira.Port(name='PR1E',midpoint=res.reference.elements['R1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
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
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN9 = spira.Port(name="PN9",midpoint=(1.0575*tp,3.5*tp),process=spira.RDD.PROCESS.M6)
        PN25 = spira.Port(name="PN25",midpoint=(4.5*tp,3.5*tp),process=spira.RDD.PROCESS.M6)
        PGND = spira.Port(name="PGND",midpoint=(1.905*tp,3.515*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PA.x,PJ1.y)],width=L1_width,layer=M6)
        L3_1 = spira.RoutePath(port1=PJ1,port2=PV1,path=[(PJ1.x,PV1.y)],width=L3_width,layer=M6)
        L3_2 = spira.RoutePath(port1=PV1,port2=PN9,path=[(PV1.x,PN9.y)],width=L3_width,layer=M5)
        L4_1 = spira.RoutePath(port1=PN9,port2=PJ3,path=[(PN9.x,PJ3.y)],width=L4_width,layer=M5)
        L4_2 = spira.RoutePath(port1=PJ3,port2=PJ5,path=[((PJ3.x+PJ5.x)/2,PJ3.y),((PJ3.x+PJ5.x)/2,PJ5.y)],width=L4_width,layer=M6)
        L5_1 = spira.RoutePath(port1=PN9,port2=PJ2,path=[(PN9.x,PJ2.y)],width=L5_width,layer=M5)
        L5_2 = spira.RoutePath(port1=PJ2,port2=PJ4,path=[((PJ2.x+PJ4.x)/2,PJ2.y),((PJ2.x+PJ4.x)/2,PJ4.y)],width=L5_width,layer=M6)
        L6 = spira.RoutePath(port1=PJ5,port2=PV2,path=[(1.96875*tp,PJ5.y),(1.96875*tp,4.5425*tp),(PV2.x,4.5425*tp)],width=L6_width,layer=M6)
        L7 = spira.RoutePath(port1=PJ4,port2=PV2,path=[(PV2.x,PJ4.y)],width=L7_width,layer=M6)
        L8_1 = spira.RoutePath(port1=PV2,port2=PR1E,path=[(PV2.x,PR1E.y)],width=L8_width,layer=M6)
        L8_2 = spira.RoutePath(port1=PR1W,port2=PGND,path=[(PR1W.x,PGND.y)],width=L8_width,layer=M6)
        L10 = spira.RoutePath(port1=PV2,port2=PJ6,path=[((PV2.x+PJ6.x)/2,PV2.y),((PV2.x+PJ6.x)/2,PJ6.y)],width=L10_width,layer=M5)
        L11 = spira.RoutePath(port1=PJ6,port2=PJ7,path=[(PJ6.x,PJ7.y)],width=L11_width,layer=M6)
        L12 = spira.RoutePath(port1=PJ7,port2=PN25,path=[(3.8775*tp,PJ7.y),(3.8775*tp,3.1425*tp),
                                                         (4.21*tp,3.1425*tp),(4.21*tp,PN25.y)],width=L12_width,layer=M6)
        L13 = spira.RoutePath(port1=PN25,port2=PJ8,path=[(PN25.x,PJ8.y)],width=L13_width,layer=M6)
        L14 = spira.RoutePath(port1=PJ8,port2=PQ,path=[(PJ8.x,PQ.y)],width=L13_width,layer=M6)

        elems += [L1, L3_1, L3_2, L4_1, L4_2, L5_1, L5_2, 
                  L6, L7, L8_1, L8_2, L10, L11, L12, L13, L14]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1S,path=[(PJ1.x,PB1S.y)],width=LB1_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1N,port2=PV3,path=[(PB1N.x,PV3.y)],width=LB2_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PJ5,port2=PB2S,path=[(PJ5.x,4.6325*tp),(PB2S.x,4.6325*tp)],width=LB1_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PV3,path=[(PB2N.x,PV3.y)],width=LB2_width,layer=M6)
        LB3_1 = spira.RoutePath(port1=PJ6,port2=PB3S,path=[(PJ6.x,3.925*tp),(PB3S.x,3.925*tp)],width=LB1_width,layer=M6)
        LB3_2 = spira.RoutePath(port1=PB3N,port2=PV3,path=[(PB3N.x,PV3.y)],width=LB2_width,layer=M6)
        LB4_1 = spira.RoutePath(port1=PN25,port2=PB4S,path=[(PN25.x,PB4S.y)],width=LB1_width,layer=M6)
        LB4_2 = spira.RoutePath(port1=PB4N,port2=PV3,path=[(PB4N.x,PV3.y)],width=LB2_width,layer=M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2]

        LBias = spira.RoutePath(port1=PV3,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="P3 M6 M4",position=(1.5*tp,5.075*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(1.415*tp,4.2475*tp),layer=TEXT)
        elems += spira.Label(text="J3 M5 M6",position=(1.0575*tp,4.2425*tp),layer=TEXT)
        elems += spira.Label(text="P5 M6 M4",position=(3.5*tp,5.155*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(0.5025*tp,5.41*tp),layer=TEXT)
        elems += spira.Label(text="P6 M6 M4",position=(4.5*tp,3.9725*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(3.475*tp,3.5225*tp),layer=TEXT)
        elems += spira.Label(text="J6 M5 M6",position=(3.04*tp,3.525*tp),layer=TEXT)
        elems += spira.Label(text="P4 M6 M4",position=(2.4175*tp,3.5075*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0.005*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(0.485*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(5.5025*tp,3.4975*tp),layer=TEXT)
        elems += spira.Label(text="P7 M6 M4",position=(6*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(1.44*tp,2.7325*tp),layer=TEXT)
        elems += spira.Label(text="J2 M5 M6",position=(1.05*tp,2.72*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(6*tp,3.4975*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(4.5*tp,7*tp),layer=TEXT)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,6.65*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,6.23*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,5.81*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,5.39*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,4.97*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,4.55*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(2.5*tp,5.585*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,1.71*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,2.13*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(4.5*tp,2.13*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(4.5*tp,1.71*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(3.5*tp,1.71*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(3.5*tp,2.13*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(2.5*tp,1.71*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(1.5*tp,1.71*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,1.71*tp))

        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.31*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.89*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.05*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.47*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(3.63*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(3.21*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(2.37*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(2.79*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.95*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.53*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(0.69*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.11*tp,0.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.31*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.89*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.05*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.47*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(3.63*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(3.21*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(2.37*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(2.79*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.95*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.53*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(0.69*tp,1.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.11*tp,1.5*tp))

        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(6.0*tp,3.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,5.41*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.42*tp,3.515*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.5*tp,5.075*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,3.975*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.5*tp,5.16*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(1.72*tp,4.125*tp),(1.72*tp,4.28*tp),(2.125*tp,4.28*tp),(2.125*tp,4.125*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(0.875*tp,2.72*tp),(0.875*tp,3.28*tp),(1.28*tp,3.28*tp),(1.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(0.875*tp,3.72*tp),(0.875*tp,4.28*tp),(1.28*tp,4.28*tp),(1.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(3.72*tp,3.04*tp),(3.72*tp,3.28*tp),(4.28*tp,3.28*tp),(4.28*tp,3.04*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(3.72*tp,2.72*tp),(3.72*tp,2.96*tp),(4.28*tp,2.96*tp),(4.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(3.04*tp,2.72*tp),(3.04*tp,3.28*tp),(3.28*tp,3.28*tp),(3.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(1.72*tp,2.72*tp),(1.72*tp,2.96*tp),(2.28*tp,2.96*tp),(2.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(2.72*tp,2.72*tp),(2.72*tp,3.28*tp),(2.96*tp,3.28*tp),(2.96*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(3.04*tp,3.72*tp),(3.04*tp,3.96*tp),(3.28*tp,3.96*tp),(3.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(2.72*tp,3.72*tp),(2.72*tp,4.28*tp),(2.96*tp,4.28*tp),(2.96*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.42*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.58*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,1.92*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.58*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.16*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.74*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.9*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.32*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.48*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,2.34*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.16*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,5.375*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,5.795*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.84*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,4.34*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,4.76*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,5.18*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,5.6*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,6.02*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,6.44*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.32*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,1.92*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,2.34*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.42*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.84*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.52*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.52*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.68*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.26*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.48*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.1*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,1.92*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,1.92*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,1.92*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1.92*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,2.34*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.9*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.74*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.68*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.1*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.26*tp,1.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.8025*tp,4.52*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.3475*tp,4.7675*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.805*tp,2.3175*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,3.795*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.4025*tp,2.3175*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.8575*tp,2.3175*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.3375*tp,2.3175*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.89*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.915*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.59*tp,2.9*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.245*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.875*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.8775*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.935*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.915*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.2475*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.2275*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.9075*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.57*tp,2.9675*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.6475*tp,2.4*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.93*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.0675*tp,2.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.235*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.53*tp,3.99*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.165*tp,2.33*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.21*tp,2.7775*tp),transformation=m90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.1775*tp,2.41*tp),transformation=m90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(2.71*tp,3.4275*tp),alias='via2')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(0.7375*tp,3.415*tp),alias='via1')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(4.415*tp,6.415*tp),alias='via3')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_080(),midpoint=(4.5*tp,3.92*tp),alias='bias4')
        elems += spira.SRef(ls_ib_150(),midpoint=(1.5*tp,5.02*tp),alias='bias2')
        elems += spira.SRef(ls_ib_220(),midpoint=(3.5*tp,5.105*tp),alias='bias3')
        elems += spira.SRef(ls_ib_280(),midpoint=(0.5*tp,5.355*tp),alias='bias1')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_150_s(),midpoint=(1.06*tp,4.25*tp),transformation=r180,alias='J3')
        elems += spira.SRef(ls_jj_150_s(),midpoint=(3.045*tp,3.54*tp),transformation=r180,alias='J6')
        elems += spira.SRef(ls_jj_150_sg(),midpoint=(3.475*tp,3.535*tp),transformation=r180,alias='J7')
        elems += spira.SRef(ls_jj_175_sg(),midpoint=(1.415*tp,4.245*tp),transformation=r180,alias='J5')
        elems += spira.SRef(ls_jj_200_s(),midpoint=(1.055*tp,2.73*tp),alias='J2')
        elems += spira.SRef(ls_jj_200_sg(),midpoint=(5.5*tp,3.5*tp),transformation=r180,alias='J8')
        elems += spira.SRef(ls_jj_300_sg(),midpoint=(1.445*tp,2.75*tp),alias='J4')
        elems += spira.SRef(ls_jj_325_sg(),midpoint=(0.48*tp,3.5*tp),transformation=r180,alias='J1')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(ls_res_5p74(),midpoint=(2.475*tp,3.515*tp),transformation=r90,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 6):
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