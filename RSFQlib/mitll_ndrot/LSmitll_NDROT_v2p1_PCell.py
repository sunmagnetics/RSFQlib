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
L2_width = 0.13*tp*Scaling
L3_width = 0.145*tp*Scaling
L4_width = 0.1*tp*Scaling
L5_width = 0.11*tp*Scaling
L7_width = 0.15*tp*Scaling
L8_width = 0.15*tp*Scaling
L9_width = 0.12*tp*Scaling
L10_width = 0.145*tp*Scaling
L11_width = 0.105*tp*Scaling
L12_width = 0.16*tp*Scaling
L13_width = 0.155*tp*Scaling
L14_width = 0.15*tp*Scaling
L15_width = 0.1*tp*Scaling
L16_width = 0.105*tp*Scaling
L17_width = 0.1*tp*Scaling
L18_width = 0.23*tp*Scaling
L19_width = 0.32*tp*Scaling
L21_width = 0.34*tp*Scaling
L22_width = 0.29*tp*Scaling
L23_width = 0.35*tp*Scaling
L24_width = 0.215*tp*Scaling
L25_width = 0.22*tp*Scaling
L26_width = 0.155*tp*Scaling
L27_width = 0.15*tp*Scaling
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
    __name_prefix__ = "LSmitll_NDROT_v2p1"
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
        PB1W = spira.Port(name='PB1W',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name='PB1E',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name='PB2N',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name='PB2S',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3N = spira.Port(name='PB3N',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name='PB3S',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4N = spira.Port(name='PB4N',midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name='PB4S',midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5N = spira.Port(name='PB5N',midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5S = spira.Port(name='PB5S',midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6N = spira.Port(name='PB6N',midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6S = spira.Port(name='PB6S',midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7N = spira.Port(name='PB7N',midpoint=bias.reference.elements['bias7'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7S = spira.Port(name='PB7S',midpoint=bias.reference.elements['bias7'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB8N = spira.Port(name='PB8N',midpoint=bias.reference.elements['bias8'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB8S = spira.Port(name='PB8S',midpoint=bias.reference.elements['bias8'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB9W = spira.Port(name='PB9W',midpoint=bias.reference.elements['bias9'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB9E = spira.Port(name='PB9E',midpoint=bias.reference.elements['bias9'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB10W = spira.Port(name='PB10W',midpoint=bias.reference.elements['bias10'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB10E = spira.Port(name='PB10E',midpoint=bias.reference.elements['bias10'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(11.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
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
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center+(0,0.25*tp),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=(10.5*tp,1.55*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV4 = spira.Port(name="PV4",midpoint=vias.reference.elements['via4'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV5 = spira.Port(name="PV5",midpoint=vias.reference.elements['via5'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN5 = spira.Port(name="PN5",midpoint=(2.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PN19 = spira.Port(name="PN19",midpoint=(1.5*tp,2.4425*tp),process=spira.RDD.PROCESS.M6)
        PN37 = spira.Port(name="PN37",midpoint=(7.082*tp,3.4975*tp),process=spira.RDD.PROCESS.M6)
        PN49 = spira.Port(name="PN49",midpoint=(8.5*tp,2.5*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PA.x,PJ1.y)],width=L1_width,layer=M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PN5,path=[(PN5.x,PJ1.y)],width=L2_width,layer=M6)
        L3 = spira.RoutePath(port1=PN5,port2=PJ2,path=[(PJ2.x,PN5.y)],width=L3_width,layer=M6)
        L4 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(4.5*tp,PJ2.y),(4.5*tp,PJ3.y)],width=L4_width,layer=M6)
        L5_1 = spira.RoutePath(port1=PJ3,port2=PV2,path=[(PJ3.x,PV2.y)],width=L5_width,layer=M6)
        L5_2 = spira.RoutePath(port1=PV2,port2=PJ4,path=[(PJ4.x,PV2.y)],width=L5_width,layer=M5)
        L5_3 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(PJ4.x,PJ5.y)],width=L5_width,layer=M6)
        L7 = spira.RoutePath(port1=PJ5,port2=PJ11,path=[(PJ5.x,PJ11.y)],width=L7_width,layer=M6)
        L8 = spira.RoutePath(port1=PB,port2=PJ6,path=[(PB.x,PJ6.y)],width=L8_width,layer=M6)
        L9 = spira.RoutePath(port1=PJ6,port2=PN19,path=[(PJ6.x,PN19.y)],width=L9_width,layer=M6)
        L10 = spira.RoutePath(port1=PN19,port2=PJ7,path=[(PN19.x,PJ7.y)],width=L10_width,layer=M6)
        L11 = spira.RoutePath(port1=PJ7,port2=PJ8,path=[(PJ8.x,PJ7.y)],width=L11_width,layer=M6)
        L12_1 = spira.RoutePath(port1=PJ8,port2=PJ9,path=[(PJ8.x,PJ9.y)],width=L12_width,layer=M6)
        L12_2 = spira.RoutePath(port1=PJ9,port2=PV1,path=[(PV1.x,PJ9.y)],width=L12_width,layer=M5)
        L12_3 = spira.RoutePath(port1=PV1,port2=PJ10,path=[(PV1.x,PJ10.y)],width=L12_width,layer=M6)
        L13 = spira.RoutePath(port1=PJ10,port2=PJ11,path=[(PJ11.x,PJ10.y)],width=L13_width,layer=M6)
        L14 = spira.RoutePath(port1=PCLK,port2=PJ12,path=[(PCLK.x,PJ12.y)],width=L14_width,layer=M6)
        L15 = spira.RoutePath(port1=PJ12,port2=PB6S,path=[(PB6S.x,PJ12.y)],width=L15_width,layer=M6)
        L16 = spira.RoutePath(port1=PB6S,port2=PJ13,path=[(9.1265*tp,PB6S.y),(9.1265*tp,5.5825*tp),(PJ13.x,5.5825*tp)],width=L16_width,layer=M6)
        L17 = spira.RoutePath(port1=PJ13,port2=PJ14,path=[(PJ13.x,4.5625*tp),(8.9*tp,4.5625*tp),(8.9*tp,4.2575*tp),
                                                          (8.4425*tp,4.2575*tp),(8.4425*tp,3.9175*tp),
                                                          (8.725*tp,3.9175*tp),(8.725*tp,PJ14.y)],width=L17_width,layer=M6)
        L18 = spira.RoutePath(port1=PJ14,port2=PN37,path=[(PJ14.x,PN37.y)],width=L18_width,layer=M6)
        L19_1 = spira.RoutePath(port1=PN37,port2=PJ15,path=[(PJ15.x,PN37.y)],width=L19_width,layer=M6)
        L19_2 = spira.RoutePath(port1=PJ15,port2=PV4,path=[(PJ15.x,PV4.y)],width=L19_width,layer=M5)
        L21 = spira.RoutePath(port1=PJ11,port2=PV3,path=[(PJ11.x,PV3.y)],width=L21_width,layer=M5)
        L22 = spira.RoutePath(port1=PV3,port2=PV4,path=[(PV3.x,PV4.y)],width=L22_width,layer=M5)
        L23 = spira.RoutePath(port1=PV4,port2=PJ16,path=[(PV4.x,PJ16.y)],width=L23_width,layer=M6)
        L24 = spira.RoutePath(port1=PJ16,port2=PN49,path=[(PJ16.x,PN49.y)],width=L24_width,layer=M6)
        L25 = spira.RoutePath(port1=PN49,port2=PJ17,path=[(PN49.x,PJ17.y)],width=L25_width,layer=M6)
        L26 = spira.RoutePath(port1=PJ17,port2=PJ18,path=[(PJ17.x,PJ18.y)],width=L26_width,layer=M6)
        L27_1 = spira.RoutePath(port1=PJ18,port2=PR1N,path=[(PJ18.x,PR1N.y)],width=L27_width,layer=M6)
        L27_2 = spira.RoutePath(port1=PR1S,port2=PQ,path=[(PR1S.x,PQ.y)],width=L27_width,layer=M6)

        elems += [L1, L2, L3, L4, L5_1, L5_2, L5_3, L7, L8, L9, L10, L11, 
                  L12_1, L12_2, L12_3, L13, L14, L15, L16, L17, L18, L19_1, 
                  L19_2, L21, L22, L23, L24, L25, L26, L27_1, L27_2]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PN5,port2=PB1W,path=[(PN5.x,PB1W.y)],width=LB1_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1E,port2=PV5,path=[(PV5.x,PV5.y)],width=LB2_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2S,path=[(PJ3.x,PB2S.y)],width=LB1_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PV5,path=[(PB2N.x,PV5.y)],width=LB1_width,layer=M6)
        LB3_1 = spira.RoutePath(port1=PJ5,port2=PB3S,path=[(PB3S.x,PJ5.y)],width=LB1_width,layer=M6)
        LB3_2 = spira.RoutePath(port1=PB3N,port2=PV5,path=[(PB3N.x,PV5.y)],width=LB1_width,layer=M6)
        LB4_1 = spira.RoutePath(port1=PN19,port2=PB4N,path=[(PN19.x,PB4N.y)],width=LB1_width,layer=M6)
        LB4_2 = spira.RoutePath(port1=PB4S,port2=PV5,path=[(PB4S.x,0.5*tp),(PV5.x,0.5*tp)],width=LB2_width,layer=M6)
        LB5_1 = spira.RoutePath(port1=PJ8,port2=PB5N,path=[(PJ8.x,PB5N.y)],width=LB1_width,layer=M6)
        LB5_2 = spira.RoutePath(port1=PB5S,port2=PV5,path=[(PB5S.x,0.5*tp),(PV5.x,0.5*tp)],width=LB2_width,layer=M6)
        LB6 = spira.RoutePath(port1=PB6N,port2=PV5,path=[(PB6N.x,PV5.y)],width=LB1_width,layer=M6)
        LB7_1 = spira.RoutePath(port1=PN37,port2=PB7S,path=[(PN37.x,4.12*tp),(PB7S.x,4.12*tp)],width=LB1_width,layer=M6)
        LB7_2 = spira.RoutePath(port1=PB7N,port2=PV5,path=[(PB7N.x,PV5.y)],width=LB1_width,layer=M6)
        LB8_1 = spira.RoutePath(port1=PV3,port2=PB8N,path=[(PV3.x,PB8N.y)],width=LB1_width,layer=M6)
        LB8_2 = spira.RoutePath(port1=PB8S,port2=PV5,path=[(PB8S.x,0.5*tp),(PV5.x,0.5*tp)],width=LB1_width,layer=M6)
        LB9_1 = spira.RoutePath(port1=PJ17,port2=PB9E,path=[(PJ17.x,PB9E.y)],width=LB1_width,layer=M6)
        LB9_2 = spira.RoutePath(port1=PB9W,port2=PV5,path=[(PB9W.x,0.5*tp),(PV5.x,0.5*tp)],width=LB1_width,layer=M6)
        LB10_1 = spira.RoutePath(port1=PJ18,port2=PB10W,path=[(PJ18.x,PB10W.y)],width=LB1_width,layer=M6)
        LB10_2 = spira.RoutePath(port1=PB10E,port2=PV5,path=[(PV5.x,PB10E.y)],width=LB1_width,layer=M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2, LB5_1, 
                  LB5_2, LB6, LB7_1, LB7_2, LB8_1, LB8_2, LB9_1, LB9_2, LB10_1, LB10_2]

        LBias = spira.RoutePath(port1=PV5,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="in_clk",position=(10.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(10.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(1.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.495*tp,5.1775*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.8025*tp,1.4975*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(10.4975*tp,5.2025*tp),layer=TEXT)
        elems += spira.Label(text="P4 M6 M4",position=(10.4975*tp,2.19*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(2.505*tp,6.4975*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(3.5*tp,4.4975*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(5.5*tp,5.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(5.4975*tp,5.715*tp),layer=TEXT)
        elems += spira.Label(text="J4 M5 M6",position=(5.5*tp,4.5025*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(5.5*tp,4*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(6.5*tp,4.565*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(2.4975*tp,1.5525*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(0.4975*tp,2.4325*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(2.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(3.505*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(3.5*tp,1.76*tp),layer=TEXT)
        elems += spira.Label(text="J9 M6 M5",position=(4.435*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(4.4975*tp,1.505*tp),layer=TEXT)
        elems += spira.Label(text="J11 M6 M5",position=(5.625*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB8 M6 M4",position=(6.0175*tp,2.145*tp),layer=TEXT)
        elems += spira.Label(text="J12 M6 M5",position=(10.4975*tp,4.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB6 M6 M4",position=(9.505*tp,5.335*tp),layer=TEXT)
        elems += spira.Label(text="J13 M6 M5",position=(8.465*tp,5*tp),layer=TEXT)
        elems += spira.Label(text="J14 M6 M5",position=(8.1325*tp,3.505*tp),layer=TEXT)
        elems += spira.Label(text="PB7 M6 M4",position=(7.4975*tp,4.725*tp),layer=TEXT)
        elems += spira.Label(text="J15 M6 M5",position=(6.5025*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J16 M6 M5",position=(7.4725*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="PB9 M6 M4",position=(8.335*tp,1.5025*tp),layer=TEXT)
        elems += spira.Label(text="J17 M6 M5",position=(9.5025*tp,1.495*tp),layer=TEXT)
        elems += spira.Label(text="PB10 M6 M4",position=(10.5075*tp,3.51*tp),layer=TEXT)
        elems += spira.Label(text="J18 M6 M5",position=(10.5025*tp,2.5125*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(11.5*tp,7*tp),layer=TEXT)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(11.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,2.4925*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(11.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,2.4925*tp))

        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(9.71*tp,3.51*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(9.5*tp,3.56*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(4.51*tp,3.5*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,6.29*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(0.51*tp,6.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(0.93*tp,6.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.35*tp,6.5*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.4*tp,center=(1.77*tp,6.5*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,5.87*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,5.45*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,3.885*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,3.465*tp))
        elems += spira.Box(layer=M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,3.045*tp))
        elems += spira.Box(layer=M5,width=0.25*tp,height=0.02*tp,center=(0.5*tp,5.03*tp))
        elems += spira.Box(layer=M5,width=0.02*tp,height=0.25*tp,center=(0.71*tp,3.49*tp))

        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(10.5*tp,5.2025*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.8025*tp,1.5*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(1.5*tp,5.18*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(10.5*tp,2.191*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(10.51*tp,3.505*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(9.5*tp,5.333*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.5*tp,4.72*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.5*tp,4.56*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(8.335*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.02*tp,2.148*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.505*tp,1.76*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,2.435*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,6.495*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.5*tp,5.715*tp))

        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(5.875*tp,1.72*tp),(5.875*tp,2.28*tp),(6.125*tp,2.28*tp),(6.125*tp,1.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(5.875*tp,0.72*tp),(5.875*tp,1.28*tp),(6.125*tp,1.28*tp),(6.125*tp,0.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(8.72*tp,4.72*tp),(8.72*tp,5.28*tp),(9.28*tp,5.28*tp),(9.28*tp,4.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(7.04*tp,4.04*tp),(7.04*tp,4.28*tp),(7.28*tp,4.28*tp),(7.28*tp,4.04*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(7.04*tp,3.72*tp),(7.04*tp,3.96*tp),(7.28*tp,3.96*tp),(7.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(8.72*tp,4.04*tp),(8.72*tp,4.28*tp),(8.96*tp,4.28*tp),(8.96*tp,4.04*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(8.72*tp,3.72*tp),(8.72*tp,3.96*tp),(8.96*tp,3.96*tp),(8.96*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        shape=spira.Shape(points=[(8.04*tp,2.72*tp),(8.04*tp,3.28*tp),(8.28*tp,3.28*tp),(8.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=M0)
        elems += spira.Polygon(shape=shape,layer=M4)
        elems += spira.Polygon(shape=shape,layer=M7)
        elems += spira.Box(width=0.56*tp,height=0.25*tp,center=(6.0*tp,4.0*tp),layer=M4)
        elems += spira.Box(width=0.56*tp,height=0.25*tp,center=(6.0*tp,4.0*tp),layer=M7)
        elems += spira.Box(width=0.56*tp,height=0.25*tp,center=(5.0*tp,4.0*tp),layer=M4)
        elems += spira.Box(width=0.56*tp,height=0.25*tp,center=(5.0*tp,4.0*tp),layer=M7)
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(0.845*tp,3.49*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9.845*tp,3.51*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(11*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(10*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(10*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(0.5*tp,4.895*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(11*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(10*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(11*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(10*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(10*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(11*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(11*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(10*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(11*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.3*tp,3.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.835*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,3.675*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.72*tp,3.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.14*tp,6.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,3.35*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,3.255*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,3.77*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.98*tp,6.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.72*tp,6.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.3*tp,6.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,4.095*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5.24*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.56*tp,6.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,6.08*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5.66*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,2.7825*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,2.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,2.0025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,2.0525*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.335*tp,1.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.3025*tp,3.7625*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.335*tp,5.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.335*tp,4.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,4.11*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.335*tp,3.795*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,5.7925*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.6325*tp,5.2525*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,1.0775*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,4.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.795*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,4.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.925*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.925*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.2475*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.2025*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.925*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.985*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.155*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.875*tp,0.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.875*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.5925*tp,2.9475*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.875*tp,6.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.185*tp,3.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.2675*tp,3.3375*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.865*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.875*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.3425*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.8825*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.155*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(10.985*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.265*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.2325*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.9025*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.875*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.875*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.265*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.2325*tp,3.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.2525*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.925*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.2475*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.2475*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.8775*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.92*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.56*tp,3.9525*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.165*tp,2.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.23*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.9125*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.2375*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.9225*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,0.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.225*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.265*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.155*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.26*tp,4.4175*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(11.875*tp,4.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.155*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.985*tp,5.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.265*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.875*tp,1.335*tp),transformation=r90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=r90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(6.415*tp,2.415*tp),alias='via4')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(5.9325*tp,2.415*tp),alias='via3')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(4.3825*tp,1.915*tp),alias='via1')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(5.415*tp,4.915*tp),alias='via2')
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(11.415*tp,6.415*tp),alias='via5')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_064(),midpoint=(8.39*tp,1.5*tp),transformation=r90,alias='bias9')
        elems += spira.SRef(ls_ib_095(),midpoint=(6.02*tp,0.48*tp),alias='bias8')
        elems += spira.SRef(ls_ib_099(),midpoint=(6.5*tp,4.505*tp),alias='bias3')
        elems += spira.SRef(ls_ib_132(),midpoint=(9.505*tp,6.565*tp),transformation=r180,alias='bias6')
        elems += spira.SRef(ls_ib_134(),midpoint=(0.5*tp,2.49*tp),transformation=r180,alias='bias4')
        elems += spira.SRef(ls_ib_134(),midpoint=(2.445*tp,6.495*tp),transformation=r270,alias='bias1')
        elems += spira.SRef(ls_ib_152(),midpoint=(3.505*tp,0.68*tp),alias='bias5')
        elems += spira.SRef(ls_ib_196(),midpoint=(10.455*tp,3.505*tp),transformation=r270,alias='bias10')
        elems += spira.SRef(ls_ib_198(),midpoint=(5.5*tp,5.66*tp),alias='bias2')
        elems += spira.SRef(ls_ib_224(),midpoint=(7.5*tp,4.665*tp),alias='bias7')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_078_s(),midpoint=(5.625*tp,2.5*tp),transformation=r90,alias='J11')
        elems += spira.SRef(ls_jj_086_sg(),midpoint=(1.5*tp,4.5*tp),transformation=r90,alias='J1')
        elems += spira.SRef(ls_jj_086_sg(),midpoint=(2.5*tp,1.55*tp),transformation=r180,alias='J6')
        elems += spira.SRef(ls_jj_094_sg(),midpoint=(8.46*tp,5*tp),transformation=r270,alias='J13')
        elems += spira.SRef(ls_jj_099_sg(),midpoint=(10.495*tp,4.5*tp),transformation=r270,alias='J12')
        elems += spira.SRef(ls_jj_100_sg(),midpoint=(3.5*tp,4.5*tp),transformation=r180,alias='J2')
        elems += spira.SRef(ls_jj_100_sg(),midpoint=(2.5*tp,3.5*tp),transformation=r180,alias='J7')
        elems += spira.SRef(ls_jj_116_sg(),midpoint=(5.5*tp,4*tp),transformation=r90,alias='J5')
        elems += spira.SRef(ls_jj_151_sg(),midpoint=(9.5*tp,1.5*tp),transformation=r180,alias='J17')
        elems += spira.SRef(ls_jj_163_sg(),midpoint=(7.475*tp,2.5*tp),alias='J16')
        elems += spira.SRef(ls_jj_165_s(),midpoint=(6.5*tp,3.5*tp),transformation=r90,alias='J15')
        elems += spira.SRef(ls_jj_177_s(),midpoint=(5.5*tp,4.5*tp),transformation=r90,alias='J4')
        elems += spira.SRef(ls_jj_191_sg(),midpoint=(5.5*tp,5.5*tp),transformation=r270,alias='J3')
        elems += spira.SRef(ls_jj_196_s(),midpoint=(4.44*tp,2.49*tp),alias='J9')
        elems += spira.SRef(ls_jj_218_sg(),midpoint=(8.14*tp,3.5*tp),transformation=r180,alias='J14')
        elems += spira.SRef(ls_jj_235_sg(),midpoint=(3.5*tp,2.5*tp),transformation=r90,alias='J8')
        elems += spira.SRef(ls_jj_236_sg(),midpoint=(10.5*tp,2.515*tp),transformation=r270,alias='J18')
        elems += spira.SRef(ls_jj_284_sg(),midpoint=(4.5*tp,1.5*tp),transformation=r180,alias='J10')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(ls_res_1p36(),midpoint=(10.5*tp,1.94*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 12):
                if (x in [1,10] and y in [1,5]):
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