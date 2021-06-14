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
L1_width = 0.16*tp*Scaling
L2_width = 0.11*tp*Scaling
L3_width = 0.13*tp*Scaling
L4_width = 0.09*tp*Scaling
L5_width = 0.14*tp*Scaling
L6_width = 0.17*tp*Scaling
L7_width = 0.16*tp*Scaling
L8_width = 0.11*tp*Scaling
L9_width = 0.13*tp*Scaling
L10_width = 0.09*tp*Scaling
L11_width = 0.14*tp*Scaling
L12_width = 0.2*tp*Scaling
L13_width = 0.15*tp*Scaling
L14_width = 0.12*tp*Scaling
L15_width = 0.12*tp*Scaling
L16_width = 0.105*tp*Scaling
L17_width = 0.125*tp*Scaling
L18_width = 0.27*tp*Scaling
L19_width = 0.25*tp*Scaling
L20_width = 0.22*tp*Scaling
L21_width = 0.15*tp*Scaling
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
    __name_prefix__ = "LSmitll_XORT_v2p1"
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
        PB2N = spira.Port(name='PB2N',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name='PB2S',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3W = spira.Port(name='PB3W',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3E = spira.Port(name='PB3E',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4N = spira.Port(name='PB4N',midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name='PB4S',midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5W = spira.Port(name='PB5W',midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5E = spira.Port(name='PB5E',midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6W = spira.Port(name='PB6W',midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6E = spira.Port(name='PB6E',midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7W = spira.Port(name='PB7W',midpoint=bias.reference.elements['bias7'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7E = spira.Port(name='PB7E',midpoint=bias.reference.elements['bias7'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB8W = spira.Port(name='PB8W',midpoint=bias.reference.elements['bias8'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB8E = spira.Port(name='PB8E',midpoint=bias.reference.elements['bias8'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(9.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
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
        PJ15 = spira.Port(name="PJ15",midpoint=jjs.reference.elements['J15'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ16 = spira.Port(name="PJ16",midpoint=jjs.reference.elements['J16'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ17 = spira.Port(name="PJ17",midpoint=jjs.reference.elements['J17'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ18 = spira.Port(name="PJ18",midpoint=jjs.reference.elements['J18'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center+(0,0.25*tp),process=spira.RDD.PROCESS.M6)
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center-(0,0.25*tp),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center+(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=(8.39*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN5 = spira.Port(name="PN21",midpoint=(2.5*tp,4.5*tp),process=spira.RDD.PROCESS.M6)
        PN17 = spira.Port(name="PN21",midpoint=(2.5*tp,2.5*tp),process=spira.RDD.PROCESS.M6)
        PN29 = spira.Port(name="PN29",midpoint=(6.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PN37 = spira.Port(name="PN31",midpoint=(4.0*tp,3.5*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PA.x,PJ1.y)],width=L1_width,layer=M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PN5,path=[(PJ1.x,PN5.y)],width=L2_width,layer=M6)
        L3 = spira.RoutePath(port1=PN5,port2=PJ2,path=[(PN5.x,PJ2.y)],width=L3_width,layer=M6)
        L4 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(PJ2.x,PJ3.y)],width=L4_width,layer=M6)
        L5 = spira.RoutePath(port1=PJ3,port2=PJ4,path=[(PJ3.x,PJ4.y)],width=L5_width,layer=M6)
        L6_1 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(PJ4.x,PJ5.y)],width=L6_width,layer=M6)
        L6_2 = spira.RoutePath(port1=PJ5,port2=PN37,path=[(PN37.x,PJ5.y)],width=L6_width,layer=M5)
        L7 = spira.RoutePath(port1=PB,port2=PJ6,path=[(PB.x,PJ6.y)],width=L7_width,layer=M6)
        L8 = spira.RoutePath(port1=PJ6,port2=PN17,path=[(PJ6.x,PN17.y)],width=L8_width,layer=M6)
        L9 = spira.RoutePath(port1=PN17,port2=PJ7,path=[(PN17.x,PJ7.y)],width=L9_width,layer=M6)
        L10 = spira.RoutePath(port1=PJ7,port2=PJ8,path=[(PJ7.x,PJ8.y)],width=L10_width,layer=M6)
        L11 = spira.RoutePath(port1=PJ8,port2=PJ9,path=[(PJ8.x,PJ9.y)],width=L11_width,layer=M6)
        L12_1 = spira.RoutePath(port1=PJ9,port2=PJ10,path=[(PJ9.x,PJ10.y)],width=L12_width,layer=M6)
        L12_2 = spira.RoutePath(port1=PJ10,port2=PN37,path=[(PN37.x,PJ10.y)],width=L12_width,layer=M5)
        L13 = spira.RoutePath(port1=PCLK,port2=PJ11,path=[(PJ11.x,PCLK.y)],width=L13_width,layer=M6)
        L14 = spira.RoutePath(port1=PJ11,port2=PN29,path=[(PJ11.x,PN29.y)],width=L14_width,layer=M6)
        L15 = spira.RoutePath(port1=PN29,port2=PJ12,path=[(PN29.x,PJ12.y)],width=L15_width,layer=M6)
        L16 = spira.RoutePath(port1=PJ12,port2=PJ13,path=[(PJ12.x,PJ13.y)],width=L16_width,layer=M6)
        L17 = spira.RoutePath(port1=PJ13,port2=PJ14,path=[(PJ13.x,PJ14.y)],width=L17_width,layer=M6)
        L18_1 = spira.RoutePath(port1=PJ14,port2=PV2,path=[(PJ14.x,PV2.y)],width=L18_width,layer=M6)
        L18_2 = spira.RoutePath(port1=PV2,port2=PJ15,path=[(PV2.x,PJ15.y)],width=L18_width,layer=M5)
        L18_3 = spira.RoutePath(port1=PJ15,port2=PJ17,path=[(PJ15.x,PJ17.y)],width=L18_width,layer=M6)
        L19_1 = spira.RoutePath(port1=PJ17,port2=PJ16,path=[(PJ17.x,PJ16.y)],width=L19_width,layer=M6)
        L19_2 = spira.RoutePath(port1=PJ16,port2=PN37,path=[(PJ16.x,PN37.y)],width=L19_width,layer=M5)
        L20 = spira.RoutePath(port1=PJ17,port2=PJ18,path=[(PJ17.x,PJ18.y)],width=L20_width,layer=M6)
        L21_1 = spira.RoutePath(port1=PJ18,port2=PR1W,path=[(PJ18.x,PR1W.y)],width=L21_width,layer=M6)
        L21_2 = spira.RoutePath(port1=PR1E,port2=PQ,path=[(PR1E.x,PQ.y)],width=L21_width,layer=M6)

        elems += [L1, L2, L3, L4, L5, L6_1, L6_2, L7, L8, L9, L10, 
                  L11, L12_1, L12_2, L13, L14, L15, L16, L17, L18_1,
                  L18_2, L18_3, L19_1, L19_2, L20, L21_1, L21_2]

        # Bias Inductors
        LB1_1 = spira.RoutePath(port1=PN5,port2=PB1E,path=[(PN5.x,PB1E.y)],width=LB1_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PV3,path=[(0.5*tp,PB1W.y),(0.5*tp,PV3.y)],width=LB2_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PJ4,port2=PB2S,path=[(PB2S.x,PJ4.y)],width=LB1_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PV3,path=[(PB2N.x,PV3.y)],width=LB2_width,layer=M6)
        LB3_1 = spira.RoutePath(port1=PN17,port2=PB3E,path=[(PN17.x,PB3E.y)],width=LB1_width,layer=M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PV3,path=[(0.5*tp,PB3W.y),(0.5*tp,PV3.y)],width=LB2_width,layer=M6)
        LB4_1 = spira.RoutePath(port1=PJ9,port2=PB4N,path=[(PJ9.x,PB4N.y)],width=LB1_width,layer=M6)
        LB4_2 = spira.RoutePath(port1=PB4S,port2=PV3,path=[(PB4S.x,0.5*tp),(0.5*tp,0.5*tp),(0.5*tp,PV3.y)],width=LB2_width,layer=M6)
        LB5_1 = spira.RoutePath(port1=PN29,port2=PB5E,path=[(PN29.x,PB5E.y)],width=LB1_width,layer=M6)
        LB5_2 = spira.RoutePath(port1=PB5W,port2=PV3,path=[(PB5W.x,PV3.y)],width=LB2_width,layer=M6)
        LB6_1 = spira.RoutePath(port1=PJ14,port2=PB6W,path=[(PJ14.x,PB6W.y)],width=LB1_width,layer=M6)
        LB6_2 = spira.RoutePath(port1=PB6E,port2=PV3,path=[(PV3.x,PB6E.y)],width=LB2_width,layer=M6)
        LB7_1 = spira.RoutePath(port1=PN37,port2=PV1,path=[(PN37.x,PV1.y)],width=LB1_width,layer=M5)
        LB7_2 = spira.RoutePath(port1=PV1,port2=PB7E,path=[(PV1.x,PB7E.y)],width=LB1_width,layer=M6)
        LB7_3 = spira.RoutePath(port1=PB7W,port2=PV3,path=[(0.5*tp,PB7W.y),(0.5*tp,PV3.y)],width=LB2_width,layer=M6)
        LB8_1 = spira.RoutePath(port1=PJ18,port2=PB8W,path=[(PJ18.x,PB8W.y)],width=LB1_width,layer=M6)
        LB8_2 = spira.RoutePath(port1=PB8E,port2=PV3,path=[(PV3.x,PB8E.y)],width=LB2_width,layer=M6)
        

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2, 
                  LB5_1, LB5_2, LB6_1, LB6_2, LB7_1, LB7_2, LB7_3, LB8_1, LB8_2]

        LBias = spira.RoutePath(port1=PV3,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="a",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(1.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(8.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="clk",position=(8.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.5*tp,5.1875*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.5*tp,4.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(2.1625*tp,3.9225*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(2.4975*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(3.4975*tp,5.47*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(3.5025*tp,4.535*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(4.5*tp,4.765*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(3.5025*tp,4.0925*tp),layer=TEXT)
        elems += spira.Label(text="PB7 M6 M4",position=(2.1775*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.4975*tp,1.8175*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(1.5*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(2.165*tp,3.08*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(2.5*tp,1.4975*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(3.5*tp,1.53*tp),layer=TEXT)
        elems += spira.Label(text="J9 M6 M5",position=(3.4975*tp,2.465*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(4.5*tp,2.2375*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(3.4975*tp,2.9075*tp),layer=TEXT)
        elems += spira.Label(text="J16 M5 M6",position=(4.5025*tp,3.4975*tp),layer=TEXT)
        elems += spira.Label(text="J17 M6 M5",position=(5.5*tp,3.445*tp),layer=TEXT)
        elems += spira.Label(text="J18 M6 M5",position=(6.505*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="PB8 M6 M4",position=(6.4975*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text="P4 M6 M4",position=(7.2875*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="J15 M5 M6",position=(6.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J14 M6 M5",position=(7.42*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB6 M6 M4",position=(8*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="J13 M6 M5",position=(7.4175*tp,4.4625*tp),layer=TEXT)
        elems += spira.Label(text="J12 M6 M5",position=(6.5*tp,4.4775*tp),layer=TEXT)
        elems += spira.Label(text="J11 M6 M5",position=(7.4975*tp,5.62*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(6.18*tp,5.4975*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(8.2025*tp,5.495*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(9.5*tp,7*tp),layer=TEXT)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(9.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(9.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))

        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(6.63*tp,2.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(6.36*tp,2.5*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(8.5*tp,3.985*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(5.5*tp,0.725*tp))
        elems += spira.Box(layer=M5,width=0.05*tp,height=0.4*tp,center=(5.5*tp,0.515*tp))
        elems += spira.Box(layer=M5,width=0.145*tp,height=0.025*tp,center=(8.575*tp,4.6375*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(8.745*tp,4.5*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(8.5*tp,3.565*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(8.71*tp,3.5*tp))

        elems += spira.Box(layer=M6,width=0.085*tp,height=0.2*tp,center=(4.9175*tp,4.5*tp))
        elems += spira.Box(layer=M5,width=0.06*tp,height=0.25*tp,center=(4.905*tp,4.5*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(8.2*tp,5.5*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(1.5*tp,5.1875*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(1.5*tp,1.8175*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.165*tp,3.92*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.175*tp,3.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.165*tp,3.075*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,2.229*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.5*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(8.0*tp,2.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.175*tp,5.495*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,4.77*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.289*tp,1.5*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(3.72*tp,2.72*tp),(3.72*tp,3.28*tp),(4.28*tp,3.28*tp),(4.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(3.72*tp,3.72*tp),(3.72*tp,4.28*tp),(4.28*tp,4.28*tp),(4.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(2.85*tp,2.72*tp),(2.85*tp,2.96*tp),(3.28*tp,2.96*tp),(3.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(0.72*tp,3.04*tp),(0.72*tp,3.195*tp),(2.28*tp,3.195*tp),(2.28*tp,3.04*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(0.72*tp,3.805*tp),(0.72*tp,3.96*tp),(2.28*tp,3.96*tp),(2.28*tp,3.805*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(2.85*tp,4.04*tp),(2.85*tp,4.28*tp),(3.28*tp,4.28*tp),(3.28*tp,4.04*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(4.875*tp,5.72*tp),(4.875*tp,6.2825*tp),(5.125*tp,6.2825*tp),(5.125*tp,5.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6.765*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4.825*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6.225*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6.495*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4.165*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4.845*tp,2.485*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5.5*tp,0.86*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5.555*tp,4.875*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8.61*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8.5*tp,4.12*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8.88*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8.505*tp,4.775*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5.06*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8.845*tp,3.5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(8.5*tp,3.355*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(8.5*tp,3.775*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.275*tp,0.515*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.725*tp,0.515*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,5.84*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.1625*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,5.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,5.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,1.1175*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,4.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.6375*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,3.165*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,2.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.835*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,3.695*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.22*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.275*tp,3.04*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.275*tp,2.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,5.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,2.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,2.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.765*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,4.105*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,5.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,2.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.2625*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.24*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.9075*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.8225*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.2625*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.985*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,0.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.9075*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.2625*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.985*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.155*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.9425*tp,0.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.235*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.265*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.875*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.2275*tp,0.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.265*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.2075*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.875*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.985*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.985*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.155*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.875*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.265*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,0.335*tp),transformation=r90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(9.415*tp,6.415*tp),alias='via3')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(6.915*tp,3.415*tp),alias='via2')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(2.635*tp,3.415*tp),alias='via1')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_066(),midpoint=(6.445*tp,0.5*tp),transformation=r270,alias='bias8')
        elems += spira.SRef(ls_ib_089(),midpoint=(4.5*tp,0.455*tp),alias='bias4')
        elems += spira.SRef(ls_ib_089(),midpoint=(4.5*tp,4.715*tp),alias='bias2')
        elems += spira.SRef(ls_ib_132(),midpoint=(6.23*tp,5.495*tp),transformation=r90,alias='bias5')
        elems += spira.SRef(ls_ib_134(),midpoint=(2.23*tp,3.5*tp),transformation=r90,alias='bias7')
        elems += spira.SRef(ls_ib_178(),midpoint=(8.94*tp,2.5*tp),transformation=r90,alias='bias6')
        elems += spira.SRef(ls_ib_230(),midpoint=(2.22*tp,3.075*tp),transformation=r90,alias='bias3')
        elems += spira.SRef(ls_ib_230(),midpoint=(2.22*tp,3.92*tp),transformation=r90,alias='bias1')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_072_sg(),midpoint=(7.5*tp,5.62*tp),transformation=r180,alias='J11')
        elems += spira.SRef(ls_jj_077_sg(),midpoint=(6.5*tp,4.48*tp),transformation=r90,alias='J12')
        elems += spira.SRef(ls_jj_083_sg(),midpoint=(7.415*tp,4.46*tp),transformation=r270,alias='J13')
        elems += spira.SRef(ls_jj_090_sg(),midpoint=(3.5*tp,1.53*tp),transformation=r180,alias='J8')
        elems += spira.SRef(ls_jj_090_sg(),midpoint=(3.5*tp,5.47*tp),alias='J3')
        elems += spira.SRef(ls_jj_093_sg(),midpoint=(5.5*tp,3.44*tp),alias='J17')
        elems += spira.SRef(ls_jj_116_sg(),midpoint=(2.5*tp,1.5*tp),transformation=r180,alias='J7')
        elems += spira.SRef(ls_jj_116_sg(),midpoint=(2.5*tp,5.5*tp),alias='J2')
        elems += spira.SRef(ls_jj_121_sg(),midpoint=(1.5*tp,2.5*tp),transformation=r90,alias='J6')
        elems += spira.SRef(ls_jj_121_sg(),midpoint=(1.5*tp,4.5*tp),transformation=r90,alias='J1')
        elems += spira.SRef(ls_jj_129_s(),midpoint=(6.5*tp,3.51*tp),transformation=r180,alias='J15')
        elems += spira.SRef(ls_jj_137_sg(),midpoint=(6.5*tp,1.5*tp),alias='J18')
        elems += spira.SRef(ls_jj_149_s(),midpoint=(4.5*tp,3.5*tp),alias='J16')
        elems += spira.SRef(ls_jj_169_sg(),midpoint=(7.415*tp,3.5*tp),transformation=r270,alias='J14')
        elems += spira.SRef(ls_jj_192_s(),midpoint=(3.5*tp,2.905*tp),transformation=r90,alias='J10')
        elems += spira.SRef(ls_jj_192_s(),midpoint=(3.5*tp,4.095*tp),transformation=r90,alias='J5')
        elems += spira.SRef(ls_jj_280_sg(),midpoint=(3.5*tp,2.465*tp),transformation=r90,alias='J9')
        elems += spira.SRef(ls_jj_280_sg(),midpoint=(3.5*tp,4.535*tp),transformation=r90,alias='J4')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(ls_res_1p36(),midpoint=(7.54*tp,1.5*tp),transformation=r90,alias='R1')
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