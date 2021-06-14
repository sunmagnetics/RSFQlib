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
L2_width = 0.125*tp*Scaling
L3_width = 0.105*tp*Scaling
L4_width = 0.2*tp*Scaling
L5_width = 0.15*tp*Scaling
L6_width = 0.125*tp*Scaling
L7_width = 0.105*tp*Scaling
L8_width = 0.2*tp*Scaling
L10_width = 0.125*tp*Scaling
L12_width = 0.09*tp*Scaling
L13_width = 0.15*tp*Scaling
L14_width = 0.095*tp*Scaling
L15_width = 0.095*tp*Scaling
L16_width = 0.16*tp*Scaling
L17_width = 0.205*tp*Scaling
L18_width = 0.12*tp*Scaling
L19_width = 0.27*tp*Scaling
L20_width = 0.125*tp*Scaling
L21_width = 0.14*tp*Scaling
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
    __name_prefix__ = "LSmitll_OR2T_v2p1"
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
        PB1N = spira.Port(name='PB1N',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name='PB1S',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name='PB2N',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name='PB2S',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3W = spira.Port(name='PB3W',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3E = spira.Port(name='PB3E',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4N = spira.Port(name='PB4N',midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name='PB4S',midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5W = spira.Port(name='PB5W',midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5E = spira.Port(name='PB5E',midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6N = spira.Port(name='PB6N',midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6S = spira.Port(name='PB6S',midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7N = spira.Port(name='PB7N',midpoint=bias.reference.elements['bias7'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7S = spira.Port(name='PB7S',midpoint=bias.reference.elements['bias7'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(8.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
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
        PJ9 = spira.Port(name="PJ9",midpoint=jjs.reference.elements['J9'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ10 = spira.Port(name="PJ10",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ11 = spira.Port(name="PJ11",midpoint=jjs.reference.elements['J11'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ12 = spira.Port(name="PJ12",midpoint=jjs.reference.elements['J12'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ13 = spira.Port(name="PJ13",midpoint=jjs.reference.elements['J13'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ14 = spira.Port(name="PJ14",midpoint=jjs.reference.elements['J14'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center+(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=(8.5*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV4 = spira.Port(name="PV4",midpoint=vias.reference.elements['via4'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN5 = spira.Port(name="PN5",midpoint=(3.5*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        PN13 = spira.Port(name="PN13",midpoint=(3.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PN29 = spira.Port(name="PN29",midpoint=(7.5*tp,4.5*tp),process=spira.RDD.PROCESS.M6)
        PN37 = spira.Port(name="PN37",midpoint=(8.5*tp,3.5*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PA.x,PJ1.y)],width=L1_width,layer=M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PN5,path=[(PJ1.x,PN5.y)],width=L2_width,layer=M6)
        L3 = spira.RoutePath(port1=PN5,port2=PJ2,path=[(PN5.x,1.8*tp),(3.6*tp,1.8*tp),
                                                       (3.6*tp,2.0*tp),(3.4*tp,2.0*tp),
                                                       (3.4*tp,2.2*tp),(PJ2.x,2.2*tp)],width=L3_width,layer=M6)
        L4_1 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(PJ2.x,PJ3.y)],width=L4_width,layer=M6)
        L4_2 = spira.RoutePath(port1=PJ3,port2=PV1,path=[(PJ3.x,PV1.y)],width=L4_width,layer=M5)
        L5 = spira.RoutePath(port1=PB,port2=PJ4,path=[(PB.x,PJ4.y)],width=L5_width,layer=M6)
        L6 = spira.RoutePath(port1=PJ4,port2=PN13,path=[(PJ4.x,PN13.y)],width=L6_width,layer=M6)
        L7 = spira.RoutePath(port1=PN13,port2=PJ5,path=[(PN13.x,5.2*tp),(3.4*tp,5.2*tp),
                                                       (3.4*tp,5.0*tp),(3.6*tp,5.0*tp),
                                                       (3.6*tp,4.8*tp),(PJ5.x,4.8*tp)],width=L7_width,layer=M6)
        L8_1 = spira.RoutePath(port1=PJ5,port2=PJ6,path=[(PJ5.x,PJ6.y)],width=L8_width,layer=M6)
        L8_2 = spira.RoutePath(port1=PJ6,port2=PV1,path=[(PJ6.x,PV1.y)],width=L8_width,layer=M5)
        L10_1 = spira.RoutePath(port1=PV1,port2=PJ7,path=[(PV1.x,PJ7.y)],width=L10_width,layer=M5)
        L10_2 = spira.RoutePath(port1=PJ7,port2=PJ8,path=[(PJ7.x,PJ8.y)],width=L10_width,layer=M6)
        L12_1 = spira.RoutePath(port1=PJ8,port2=PV2,path=[(PJ8.x,PV2.y)],width=L12_width,layer=M6)
        L12_2 = spira.RoutePath(port1=PV2,port2=PJ11,path=[(PV2.x,PJ11.y)],width=L12_width,layer=M5)
        L13 = spira.RoutePath(port1=PCLK,port2=PJ9,path=[(PCLK.x,PJ9.y)],width=L13_width,layer=M6)
        L14 = spira.RoutePath(port1=PJ9,port2=PN29,path=[(PJ9.x,5.21*tp),(7.6*tp,5.21*tp),
                                                         (7.6*tp,4.97*tp),(7.4*tp,4.97*tp),
                                                         (7.4*tp,4.73*tp),(PN29.x,4.73*tp)],width=L14_width,layer=M6)
        L15 = spira.RoutePath(port1=PN29,port2=PJ10,path=[(PJ10.x,PN29.y)],width=L15_width,layer=M6)
        L16 = spira.RoutePath(port1=PJ10,port2=PJ11,path=[(PJ10.x,PJ11.y)],width=L16_width,layer=M6)
        L17_1 = spira.RoutePath(port1=PJ11,port2=PV3,path=[(PJ11.x,PV3.y)],width=L17_width,layer=M5)
        L17_2 = spira.RoutePath(port1=PV3,port2=PJ12,path=[(PV3.x,PJ12.y)],width=L17_width,layer=M6)
        L18 = spira.RoutePath(port1=PJ12,port2=PN37,path=[(PJ12.x,PN37.y)],width=L18_width,layer=M6)
        L19 = spira.RoutePath(port1=PN37,port2=PJ13,path=[(PN37.x,PJ13.y)],width=L19_width,layer=M6)
        L20 = spira.RoutePath(port1=PJ13,port2=PJ14,path=[(PJ14.x,PJ13.y)],width=L20_width,layer=M6)
        L21_1 = spira.RoutePath(port1=PJ14,port2=PR1W,path=[(PJ14.x,PR1W.y)],width=L21_width,layer=M6)
        L21_2 = spira.RoutePath(port1=PR1E,port2=PQ,path=[(PR1E.x,PQ.y)],width=L21_width,layer=M6)

        elems += [L1, L2, L3, L4_1, L4_2, L5, L6, L7, L8_1, L8_2, L10_1, L10_2, 
                  L12_1, L12_2, L13, L14, L15, L16, L17_1, L17_2, L18, L19, L20, L21_1, L21_2]

        # Bias Inductors
        LB1_1 = spira.RoutePath(port1=PN5,port2=PB1N,path=[(4.14*tp,PN5.y),(4.14*tp,PB1N.y)],width=LB1_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1S,port2=PV4,path=[(PB1S.x,0.5*tp),(0.5*tp,0.5*tp),(0.5*tp,PV4.y)],width=LB2_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PN13,port2=PB2S,path=[(4.14*tp,PN13.y),(4.14*tp,PB2S.y)],width=LB1_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PV4,path=[(PB1S.x,PV4.y)],width=LB2_width,layer=M6)
        LB3_1 = spira.RoutePath(port1=PV1,port2=PB3E,path=[(PV1.x,PB3E.y)],width=LB1_width,layer=M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PV4,path=[(0.5*tp,PB3W.y),(0.5*tp,PV4.y)],width=LB2_width,layer=M6)
        LB4_1 = spira.RoutePath(port1=PJ8,port2=PB4N,path=[(PJ8.x,PB4N.y)],width=LB1_width,layer=M6)
        LB4_2 = spira.RoutePath(port1=PB4S,port2=PV4,path=[(PB4S.x,0.5*tp),(0.5*tp,0.5*tp),(0.5*tp,PV4.y)],width=LB2_width,layer=M6)
        LB5_1 = spira.RoutePath(port1=PN29,port2=PB5W,path=[(PN29.x,PB5W.y)],width=LB1_width,layer=M6)
        LB5_2 = spira.RoutePath(port1=PB5E,port2=PV4,path=[(PB5E.x,PV4.y)],width=LB2_width,layer=M6)
        LB6_1 = spira.RoutePath(port1=PN37,port2=PB6N,path=[(PN37.x,PB6N.y)],width=LB1_width,layer=M6)
        LB6_2 = spira.RoutePath(port1=PB6S,port2=PV4,path=[(PB6S.x,0.5*tp),(0.5*tp,0.5*tp),(0.5*tp,PV4.y)],width=LB2_width,layer=M6)
        LB7_1 = spira.RoutePath(port1=PJ14,port2=PB7N,path=[(PJ14.x,PB7N.y)],width=LB1_width,layer=M6)
        LB7_2 = spira.RoutePath(port1=PB7S,port2=PV4,path=[(PB7S.x,0.5*tp),(0.5*tp,0.5*tp),(0.5*tp,PV4.y)],width=LB2_width,layer=M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2,
                  LB5_1, LB5_2, LB6_1, LB6_2, LB7_1, LB7_2]

        LBias = spira.RoutePath(port1=PV4,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="q",position=(8.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="clk",position=(8.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(8.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(1.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="PB7 M6 M4",position=(6.5025*tp,1.4925*tp),layer=TEXT)
        elems += spira.Label(text="PB6 M6 M4",position=(9.5*tp,3.495*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(8.03*tp,4.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(5.5125*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(2.2275*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(4.5*tp,5.46*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(4.5*tp,1.54*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(8.2125*tp,5.4975*tp),layer=TEXT)
        elems += spira.Label(text="P4 M6 M4",position=(7.795*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="J14 M6 M5",position=(7.435*tp,1.4975*tp),layer=TEXT)
        elems += spira.Label(text="J13 M6 M5",position=(8.5*tp,2.5525*tp),layer=TEXT)
        elems += spira.Label(text="J12 M6 M5",position=(7.4975*tp,3.505*tp),layer=TEXT)
        elems += spira.Label(text="J11 M6 M5",position=(6.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(6.5*tp,3.875*tp),layer=TEXT)
        elems += spira.Label(text="J9 M6 M5",position=(7.57*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(4.51*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J7 M5 M6",position=(4.1475*tp,3.4975*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(3.5*tp,4.11*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(3.5*tp,4.4625*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(2.5025*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.7975*tp,5.5075*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(3.5025*tp,2.89*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(3.5*tp,2.54*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(2.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.7975*tp,1.5*tp),layer=TEXT)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(9.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(9.9875*tp,6.4925*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(9.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(9.9875*tp,6.4925*tp))

        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(1.495*tp,2.71*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.87*tp,4.5*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,4.53*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.29*tp,4.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.71*tp,4.5*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(1.5*tp,4.445*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(1.29*tp,4.48*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(2.13*tp,4.48*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(2.4*tp,4.48*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(2.49*tp,4.345*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(2.445*tp,2.635*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.325*tp,center=(2.31*tp,2.5375*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.89*tp,2.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.47*tp,2.5*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,4.95*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,5.37*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(5.71*tp,5.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(6.13*tp,5.5*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(8.2125*tp,5.5*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.7975*tp,5.5*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.7975*tp,1.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.225*tp,3.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(8.03*tp,4.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(9.5*tp,3.495*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.794*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.505*tp,1.494*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.51*tp,2.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,5.46*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,1.54*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(5.72*tp,3.72*tp),(5.72*tp,3.96*tp),(6.28*tp,3.96*tp),(6.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(2.72*tp,2.72*tp),(2.72*tp,2.96*tp),(3.28*tp,2.96*tp),(3.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(4.04*tp,3.72*tp),(4.04*tp,4.28*tp),(4.28*tp,4.28*tp),(4.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(2.72*tp,4.04*tp),(2.72*tp,4.28*tp),(3.28*tp,4.28*tp),(3.28*tp,4.04*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2.445*tp,2.77*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2.445*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1.495*tp,2.845*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2.49*tp,4.21*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1.155*tp,4.48*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2.535*tp,4.48*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2.265*tp,4.48*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,4.32*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(6.34*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,5.16*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,5.58*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.92*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,4.235*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.92*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.1*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.08*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,4.74*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.26*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.66*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.68*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,4.655*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,4.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,3.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,4.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,4.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.3325*tp,5.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,5.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,5.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.835*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.3325*tp,5.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.82*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,2.09*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.02*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,2.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,2.115*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,3.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,5.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,2.8225*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,3.1225*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.265*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,0.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.2225*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.945*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.265*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.8775*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.2625*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.155*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.875*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.265*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.155*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,0.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.945*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.265*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.265*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.2675*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.9875*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.975*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.985*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.985*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,5.335*tp),transformation=r90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(3.415*tp,3.415*tp),alias='via1')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(8.415*tp,6.415*tp),alias='via4')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(6.99*tp,3.415*tp),alias='via3')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(5.895*tp,3.415*tp),alias='via2')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_081(),midpoint=(9.5*tp,1.65*tp),alias='bias6')
        elems += spira.SRef(ls_ib_081(),midpoint=(5.51*tp,0.655*tp),alias='bias4')
        elems += spira.SRef(ls_ib_098(),midpoint=(9.555*tp,4.5*tp),transformation=r90,alias='bias5')
        elems += spira.SRef(ls_ib_141(),midpoint=(4.5*tp,5.405*tp),alias='bias2')
        elems += spira.SRef(ls_ib_141(),midpoint=(4.5*tp,1.595*tp),transformation=r180,alias='bias1')
        elems += spira.SRef(ls_ib_177(),midpoint=(6.505*tp,0.65*tp),alias='bias7')
        elems += spira.SRef(ls_ib_328(),midpoint=(2.28*tp,3.5*tp),transformation=r90,alias='bias3')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_063_s(),midpoint=(6.5*tp,3.5*tp),transformation=r180,alias='J11')
        elems += spira.SRef(ls_jj_075_sg(),midpoint=(6.5*tp,3.875*tp),transformation=r90,alias='J10')
        elems += spira.SRef(ls_jj_081_sg(),midpoint=(7.57*tp,5.5*tp),transformation=r90,alias='J9')
        elems += spira.SRef(ls_jj_117_sg(),midpoint=(2.5*tp,5.5*tp),transformation=r180,alias='J4')
        elems += spira.SRef(ls_jj_117_sg(),midpoint=(2.5*tp,1.5*tp),alias='J1')
        elems += spira.SRef(ls_jj_131_s(),midpoint=(3.5*tp,4.11*tp),transformation=r90,alias='J6')
        elems += spira.SRef(ls_jj_131_s(),midpoint=(3.5*tp,2.89*tp),transformation=r90,alias='J3')
        elems += spira.SRef(ls_jj_140_sg(),midpoint=(7.5*tp,3.5*tp),alias='J12')
        elems += spira.SRef(ls_jj_162_sg(),midpoint=(8.5*tp,2.55*tp),transformation=r270,alias='J13')
        elems += spira.SRef(ls_jj_172_sg(),midpoint=(4.51*tp,3.5*tp),alias='J8')
        elems += spira.SRef(ls_jj_190_sg(),midpoint=(7.435*tp,1.5*tp),transformation=r180,alias='J14')
        elems += spira.SRef(ls_jj_195_sg(),midpoint=(3.5*tp,4.465*tp),transformation=r90,alias='J5')
        elems += spira.SRef(ls_jj_195_sg(),midpoint=(3.5*tp,2.535*tp),transformation=r90,alias='J2')
        elems += spira.SRef(ls_jj_220_s(),midpoint=(4.145*tp,3.5*tp),alias='J7')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(ls_res_1p36(),midpoint=(8.05*tp,1.5*tp),transformation=r90,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 10):
                if (x == 1 and y in [1,5]) or (x == 8 and y in [1,5]):
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