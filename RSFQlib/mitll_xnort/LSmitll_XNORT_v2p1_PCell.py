import sys
# Change this to the location that contains the subcells.py folder
subcell_path = '..\\subcells'
if subcell_path not in sys.path:
    sys.path.append(subcell_path)
import subcells as sc
import os
import spira.all as spira
from spira.technologies.mit.process.database import RDD

IXPORT = spira.RDD.PLAYER.IXPORT
TEXT = spira.Layer(number=182)

## Parameterization
# Trackpitch in microns
tp = 10
sc.tp = tp

# Inductor widths
Scaling = (1+(tp-10)*0.25)
L1_width = 0.2*tp*Scaling
L2_width = 0.11*tp*Scaling
L3_width = 0.09*tp*Scaling
L4_width = 0.2*tp*Scaling
L5_width = 0.2*tp*Scaling
L6_width = 0.11*tp*Scaling
L7_width = 0.09*tp*Scaling
L8_width = 0.2*tp*Scaling
L9_width = 0.26*tp*Scaling
L10_width = 0.16*tp*Scaling
L11_width = 0.15*tp*Scaling
L12_width = 0.12*tp*Scaling
L13_width = 0.18*tp*Scaling
L14_width = 0.1*tp*Scaling
L15_width = 0.135*tp*Scaling
L16_width = 0.225*tp*Scaling
L17_width = 0.09*tp*Scaling
L18_width = 0.15*tp*Scaling
L20_width = 0.24*tp*Scaling
L21_width = 0.2*tp*Scaling
L22_width = 0.09*tp*Scaling
L23_width = 0.25*tp*Scaling
L24_width = 0.2*tp*Scaling
L25_width = 0.16*tp*Scaling
LB1_width = 0.14*tp*Scaling
LB2_width = 0.2*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_XNORT_v2p1"
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
        PB5N = spira.Port(name='PB5N',midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5S = spira.Port(name='PB5S',midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6N = spira.Port(name='PB6N',midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6S = spira.Port(name='PB6S',midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7N = spira.Port(name='PB7N',midpoint=bias.reference.elements['bias7'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7S = spira.Port(name='PB7S',midpoint=bias.reference.elements['bias7'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB8N = spira.Port(name='PB8N',midpoint=bias.reference.elements['bias8'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB8S = spira.Port(name='PB8S',midpoint=bias.reference.elements['bias8'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB9W = spira.Port(name='PB9W',midpoint=bias.reference.elements['bias9'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB9E = spira.Port(name='PB9E',midpoint=bias.reference.elements['bias9'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB10W = spira.Port(name='PB10W',midpoint=bias.reference.elements['bias10'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB10E = spira.Port(name='PB10E',midpoint=bias.reference.elements['bias10'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(7.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
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
        PQ = spira.Port(name="PQ",midpoint=(7.533*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV4 = spira.Port(name="PV4",midpoint=vias.reference.elements['via4'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV5 = spira.Port(name="PV5",midpoint=vias.reference.elements['via5'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV6 = spira.Port(name="PV6",midpoint=vias.reference.elements['via6'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN21 = spira.Port(name="PN21",midpoint=(3.5*tp,3.5*tp),process=spira.RDD.PROCESS.M6)
        PN31 = spira.Port(name="PN31",midpoint=(6.5*tp,3.5*tp),process=spira.RDD.PROCESS.M6)
        PN42 = spira.Port(name="PN42",midpoint=(4.5*tp,2.5*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PA.x,PJ1.y)],width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(PJ1.x,PJ2.y)],width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(PJ2.x,PJ3.y)],width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PJ3,port2=PN21,path=[(PN21.x,PJ3.y)],width=L4_width,layer=sc.M5)
        L5 = spira.RoutePath(port1=PB,port2=PJ4,path=[(PB.x,PJ4.y)],width=L5_width,layer=sc.M6)
        L6 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(PJ4.x,PJ5.y)],width=L6_width,layer=sc.M6)
        L7 = spira.RoutePath(port1=PJ5,port2=PJ6,path=[(PJ5.x,PJ6.y)],width=L7_width,layer=sc.M6)
        L8 = spira.RoutePath(port1=PJ6,port2=PN21,path=[(PN21.x,PJ6.y)],width=L8_width,layer=sc.M5)
        L9_1 = spira.RoutePath(port1=PN21,port2=PJ7,path=[(PN21.x,PJ7.y)],width=L9_width,layer=sc.M5)
        L9_2 = spira.RoutePath(port1=PJ7,port2=PJ8,path=[(PJ7.x,PJ8.y)],width=L9_width,layer=sc.M6)
        L10 = spira.RoutePath(port1=PCLK,port2=PJ9,path=[(PCLK.x,PJ9.y)],width=L10_width,layer=sc.M6)
        L11 = spira.RoutePath(port1=PJ9,port2=PJ10,path=[(PJ9.x,PJ10.y)],width=L11_width,layer=sc.M6)
        L12 = spira.RoutePath(port1=PJ10,port2=PV5,path=[(PJ10.x,PV5.y)],width=L12_width,layer=sc.M6)
        L13_1 = spira.RoutePath(port1=PV5,port2=PJ11,path=[(PV5.x,PJ11.y)],width=L13_width,layer=sc.M5)
        L13_2 = spira.RoutePath(port1=PJ11,port2=PJ8,path=[(PJ11.x,PJ8.y)],width=L13_width,layer=sc.M6)
        L14 = spira.RoutePath(port1=PV5,port2=PJ12,path=[(PJ12.x,PV5.y)],width=L14_width,layer=sc.M6)
        L15 = spira.RoutePath(port1=PJ12,port2=PN31,path=[(PJ12.x,PN31.y)],width=L15_width,layer=sc.M6)
        L16 = spira.RoutePath(port1=PN31,port2=PJ13,path=[(PN31.x,PJ13.y)],width=L16_width,layer=sc.M6)
        L17 = spira.RoutePath(port1=PJ13,port2=PJ16,path=[(6.0*tp,PJ13.y),(6.0*tp,PJ16.y)],width=L17_width,layer=sc.M6)
        L18_1 = spira.RoutePath(port1=PJ8,port2=PV3,path=[(PJ8.x,PV3.y)],width=L18_width,layer=sc.M6)
        L18_2 = spira.RoutePath(port1=PV3,port2=PJ14,path=[(PV3.x,PJ14.y)],width=L18_width,layer=sc.M5)
        L18_3 = spira.RoutePath(port1=PJ14,port2=PN42,path=[(PJ14.x,PN42.y)],width=L18_width,layer=sc.M6)
        L20_1 = spira.RoutePath(port1=PN42,port2=PJ15,path=[(PN42.x,PJ15.y)],width=L20_width,layer=sc.M6)
        L20_2 = spira.RoutePath(port1=PJ15,port2=PV4,path=[((PJ15.x+PV4.x)/2,PJ15.y),((PJ15.x+PV4.x)/2,PV4.y)],width=L20_width,layer=sc.M5)
        L21 = spira.RoutePath(port1=PV4,port2=PJ16,path=[((PV4.x+PJ16.x)/2,PV4.y),((PV4.x+PJ16.x)/2,PJ16.y)],width=L21_width,layer=sc.M5)
        L22 = spira.RoutePath(port1=PJ16,port2=PN42,path=[(PJ16.x,2.37*tp),(5.65*tp,2.37*tp),
                                                         (5.65*tp,2.6175*tp),(5.0*tp,2.6175*tp),
                                                         (5.0*tp,PN42.y)],width=L22_width,layer=sc.M6)
        L23 = spira.RoutePath(port1=PV4,port2=PJ17,path=[(PV4.x,PJ17.y)],width=L23_width,layer=sc.M6)
        L24 = spira.RoutePath(port1=PJ17,port2=PJ18,path=[(5.53*tp,PJ17.y),(5.53*tp,PJ18.y)],width=L24_width,layer=sc.M6)
        L25_1 = spira.RoutePath(port1=PJ18,port2=PR1W,path=[(PJ18.x,PR1W.y)],width=L25_width,layer=sc.M6)
        L25_2 = spira.RoutePath(port1=PR1E,port2=PQ,path=[(PR1E.x,PQ.y)],width=L25_width,layer=sc.M6)
        

        elems += [L1, L2, L3, L4, L5, L6, L7, L8, L9_1, L9_2, L10, 
                  L11, L12, L13_1, L13_2, L14, L15, L16, L17, L18_1,
                  L18_2, L18_3, L20_1, L20_2, L21, L22, L23, L24, L25_1, L25_2]

        # Bias Inductors
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1E,path=[(PJ1.x,PB1E.y)],width=LB1_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PV6,path=[(0.5*tp,PB1W.y),(0.5*tp,PV6.y)],width=LB1_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PV2,path=[(PJ3.x,PV2.y)],width=LB1_width,layer=sc.M5)
        LB2_2 = spira.RoutePath(port1=PV2,port2=PB2S,path=[(PV2.x,PB2S.y)],width=LB1_width,layer=sc.M6)
        LB2_3 = spira.RoutePath(port1=PB2N,port2=PV6,path=[(PB2N.x,PV6.y)],width=LB1_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ4,port2=PB3E,path=[(PJ4.x,PB3E.y)],width=LB1_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PV6,path=[(0.5*tp,PB3W.y),(0.5*tp,PV6.y)],width=LB1_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ6,port2=PV1,path=[(PJ6.x,PV1.y)],width=LB1_width,layer=sc.M5)
        LB4_2 = spira.RoutePath(port1=PV1,port2=PB4N,path=[(PV1.x,PB4N.y)],width=LB1_width,layer=sc.M6)
        LB4_3 = spira.RoutePath(port1=PB4S,port2=PV6,path=[(PB4S.x,0.5*tp),(0.5*tp,0.5*tp),(0.5*tp,PV6.y)],width=LB1_width,layer=sc.M6)
        LB5_1 = spira.RoutePath(port1=PJ9,port2=PB5S,path=[(PB5S.x,PJ9.y)],width=LB1_width,layer=sc.M6)
        LB5_2 = spira.RoutePath(port1=PB5N,port2=PV6,path=[(PB5N.x,PV6.y)],width=LB1_width,layer=sc.M6)
        LB6_1 = spira.RoutePath(port1=PJ10,port2=PB6S,path=[(PB6S.x,PJ10.y)],width=LB1_width,layer=sc.M6)
        LB6_2 = spira.RoutePath(port1=PB6N,port2=PV6,path=[(PB6N.x,PV6.y)],width=LB1_width,layer=sc.M6)
        LB7_1 = spira.RoutePath(port1=PN31,port2=PB7S,path=[(PB7S.x,PN31.y)],width=LB1_width,layer=sc.M6)
        LB7_2 = spira.RoutePath(port1=PB7N,port2=PV6,path=[(PB7N.x,PV6.y)],width=LB1_width,layer=sc.M6)
        LB8_1 = spira.RoutePath(port1=PN42,port2=PB8N,path=[(4.0*tp,PN42.y),(4.0*tp,1.5*tp),(PB8N.x,1.5*tp)],width=LB1_width,layer=sc.M6)
        LB8_2 = spira.RoutePath(port1=PB8S,port2=PV6,path=[(PB8S.x,0.5*tp),(0.5*tp,0.5*tp),(0.5*tp,PV6.y)],width=LB1_width,layer=sc.M6)
        LB9_1 = spira.RoutePath(port1=PJ17,port2=PB9W,path=[(PJ17.x,PB9W.y)],width=LB1_width,layer=sc.M6)
        LB9_2 = spira.RoutePath(port1=PB9E,port2=PV6,path=[(8.5*tp,PB9E.y),(8.5*tp,PV6.y)],width=LB1_width,layer=sc.M6)
        LB10_1 = spira.RoutePath(port1=PJ18,port2=PB10W,path=[(PJ18.x,2.0*tp),(PB10W.x,2.0*tp)],width=LB1_width,layer=sc.M6)
        LB10_2 = spira.RoutePath(port1=PB10E,port2=PV6,path=[(8.5*tp,PB10E.y),(8.5*tp,PV6.y)],width=LB1_width,layer=sc.M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB2_3, LB3_1, LB3_2, LB4_1, LB4_2, LB4_3,
                  LB5_1, LB5_2, LB6_1, LB6_2, LB7_1, LB7_2, LB8_1, LB8_2, LB9_1, LB9_2, LB10_1, LB10_2]

        LBias = spira.RoutePath(port1=PV6,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=sc.M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="J18 M6 M5",position=(6.5*tp,1.4975*tp),layer=TEXT)
        elems += spira.Label(text="J17 M6 M5",position=(4.8525*tp,1*tp),layer=TEXT)
        elems += spira.Label(text="J15 M6 M5",position=(4.5025*tp,2.025*tp),layer=TEXT)
        elems += spira.Label(text="J16 M6 M5",position=(5.22*tp,2*tp),layer=TEXT)
        elems += spira.Label(text="J14 M5 M6",position=(4.5*tp,2.8725*tp),layer=TEXT)
        elems += spira.Label(text="J13 M6 M5",position=(6.5*tp,2.495*tp),layer=TEXT)
        elems += spira.Label(text="J12 M6 M5",position=(5.4975*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(4.8025*tp,4.4925*tp),layer=TEXT)
        elems += spira.Label(text="J9 M6 M5",position=(5.5025*tp,5.4925*tp),layer=TEXT)
        elems += spira.Label(text="J11 M5 M6",position=(4.5025*tp,3.9025*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(4.5*tp,3.495*tp),layer=TEXT)
        elems += spira.Label(text="J7 M5 M6",position=(4*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(2.505*tp,2*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(2.5*tp,2.4975*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(1.5025*tp,2.4975*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(2.5025*tp,5*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(2.505*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.5*tp,4.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB10 M6 M4",position=(7.49*tp,2.4925*tp),layer=TEXT)
        elems += spira.Label(text="PB9 M6 M4",position=(4.8725*tp,0.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB8 M6 M4",position=(3.5*tp,1.225*tp),layer=TEXT)
        elems += spira.Label(text="PB7 M6 M4",position=(7.4975*tp,3.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB6 M6 M4",position=(4.46*tp,5.315*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(5*tp,5.5975*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(2.5*tp,1.5275*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(1.4925*tp,3.3875*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(2.5*tp,5.4725*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.49*tp,3.6125*tp),layer=TEXT)
        elems += spira.Label(text="P4 M6 M4",position=(6.8425*tp,1.5025*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(6.215*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.5*tp,1.8675*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.5*tp,5.1725*tp),layer=TEXT)
        elems += spira.Label(text="Q",position=(7.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="Bias",position=(7.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="clk",position=(6.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(1.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(1.5*tp,5.5*tp),layer=TEXT)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(8.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(8.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(8.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(8.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))

        elems += spira.Box(layer=sc.M5,width=0.075*tp,height=0.33*tp,center=(4.4825*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(6.485*tp,4.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(2.5*tp,3.5*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(6.217*tp,5.5*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(1.5*tp,5.1725*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(1.5*tp,1.867*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.839*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.495*tp,3.615*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.495*tp,3.385*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,1.528*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,5.47*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.5*tp,1.229*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.871*tp,0.505*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.493*tp,2.495*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.5*tp,3.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.46*tp,5.315*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.0*tp,5.595*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(4.72*tp,2.04*tp),(4.72*tp,2.28*tp),(4.96*tp,2.28*tp),(4.96*tp,2.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(3.875*tp,1.72*tp),(3.875*tp,2.28*tp),(4.125*tp,2.28*tp),(4.125*tp,1.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,0.72*tp),(4.72*tp,1.28*tp),(4.96*tp,1.28*tp),(4.96*tp,0.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.125*tp,0.875*tp),(4.125*tp,1.125*tp),(4.28*tp,1.125*tp),(4.28*tp,0.875*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,2.72*tp),(4.72*tp,2.96*tp),(5.28*tp,2.96*tp),(5.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(5.875*tp,2.125*tp),(5.875*tp,2.28*tp),(6.125*tp,2.28*tp),(6.125*tp,2.125*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(5.72*tp,1.875*tp),(5.72*tp,2.125*tp),(5.875*tp,2.125*tp),(5.875*tp,1.875*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,1.72*tp),(4.72*tp,1.96*tp),(4.96*tp,1.96*tp),(4.96*tp,1.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(5.04*tp,1.72*tp),(5.04*tp,2.28*tp),(5.28*tp,2.28*tp),(5.28*tp,1.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.875*tp,5.72*tp),(4.875*tp,6.28*tp),(5.125*tp,6.28*tp),(5.125*tp,5.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,4.72*tp),(4.72*tp,5.1275*tp),(4.96*tp,5.1275*tp),(4.96*tp,4.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(1.875*tp,4.875*tp),(1.875*tp,5.125*tp),(2.28*tp,5.125*tp),(2.28*tp,4.875*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(1.875*tp,1.875*tp),(1.875*tp,2.125*tp),(2.28*tp,2.125*tp),(2.28*tp,1.875*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(2.72*tp,1.875*tp),(2.72*tp,2.125*tp),(3.28*tp,2.125*tp),(3.28*tp,1.875*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(2.72*tp,4.875*tp),(2.72*tp,5.125*tp),(3.28*tp,5.125*tp),(3.28*tp,4.875*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(3.875*tp,3.125*tp),(3.875*tp,3.28*tp),(4.125*tp,3.28*tp),(4.125*tp,3.125*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(3.72*tp,3.72*tp),(3.72*tp,3.96*tp),(4.28*tp,3.96*tp),(4.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,3.72*tp),(4.72*tp,4.28*tp),(4.96*tp,4.28*tp),(4.96*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(5.04*tp,3.72*tp),(5.04*tp,3.96*tp),(5.28*tp,3.96*tp),(5.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(6.72*tp,1.875*tp),(6.72*tp,2.125*tp),(7.28*tp,2.125*tp),(7.28*tp,1.875*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(5.04*tp,0.84*tp),(5.04*tp,1.16*tp),(5.28*tp,1.16*tp),(5.28*tp,0.84*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.29*tp,3.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.71*tp,3.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.245*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,5.74*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.275*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.695*tp,4.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,2.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,6.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,4.1325*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,5.2325*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.2225*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.155*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.92*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.155*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.935*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.9125*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.985*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.66*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.985*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.945*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.985*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.8075*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.985*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.125*tp,2.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.805*tp,2.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(6*tp,1*tp))
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.415*tp,3.07*tp),alias='via3')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.7175*tp,3.82*tp),alias='via5')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(2.415*tp,5.2075*tp),alias='via2')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.7675*tp,1.9175*tp),alias='via4')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(2.415*tp,1.6225*tp),alias='via1')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(7.415*tp,6.415*tp),alias='via6')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_053(),midpoint=(7.79*tp,0.505*tp),transformation=sc.r90,alias='bias9')
        elems += spira.SRef(sc.ls_ib_060(),midpoint=(7.5*tp,3.445*tp),alias='bias7')
        elems += spira.SRef(sc.ls_ib_168(),midpoint=(2.5*tp,0.54*tp),alias='bias4')
        elems += spira.SRef(sc.ls_ib_168(),midpoint=(2.5*tp,5.415*tp),alias='bias2')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(5*tp,5.54*tp),alias='bias5')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(8.445*tp,2.495*tp),transformation=sc.r90,alias='bias10')
        elems += spira.SRef(sc.ls_ib_195(),midpoint=(4.46*tp,5.26*tp),alias='bias6')
        elems += spira.SRef(sc.ls_ib_195(),midpoint=(1.55*tp,3.385*tp),transformation=sc.r90,alias='bias3')
        elems += spira.SRef(sc.ls_ib_195(),midpoint=(1.55*tp,3.615*tp),transformation=sc.r90,alias='bias1')
        elems += spira.SRef(sc.ls_ib_262(),midpoint=(3.5*tp,0.56*tp),alias='bias8')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_107_s(),midpoint=(4.5*tp,2.03*tp),transformation=sc.r180,alias='J15')
        elems += spira.SRef(sc.ls_jj_136_s(),midpoint=(4.5*tp,3.905*tp),transformation=sc.r90,alias='J11')
        elems += spira.SRef(sc.ls_jj_154_s(),midpoint=(5.22*tp,2*tp),transformation=sc.r180,alias='J16')
        elems += spira.SRef(sc.ls_jj_163_s(),midpoint=(4.5*tp,2.86*tp),transformation=sc.r270,alias='J14')
        elems += spira.SRef(sc.ls_jj_164_sg(),midpoint=(4.85*tp,1*tp),transformation=sc.r90,alias='J17')
        elems += spira.SRef(sc.ls_jj_200_sg(),midpoint=(5.5*tp,5.495*tp),alias='J9')
        elems += spira.SRef(sc.ls_jj_200_sg(),midpoint=(1.5*tp,2.5*tp),transformation=sc.r90,alias='J4')
        elems += spira.SRef(sc.ls_jj_200_sg(),midpoint=(1.5*tp,4.5*tp),transformation=sc.r90,alias='J1')
        elems += spira.SRef(sc.ls_jj_223_s(),midpoint=(2.5*tp,2*tp),transformation=sc.r90,alias='J6')
        elems += spira.SRef(sc.ls_jj_223_s(),midpoint=(2.5*tp,5*tp),transformation=sc.r90,alias='J3')
        elems += spira.SRef(sc.ls_jj_228_sg(),midpoint=(6.5*tp,2.51*tp),transformation=sc.r270,alias='J13')
        elems += spira.SRef(sc.ls_jj_240_s(),midpoint=(4*tp,3.5*tp),transformation=sc.r180,alias='J7')
        elems += spira.SRef(sc.ls_jj_240_sg(),midpoint=(5.5*tp,3.5*tp),transformation=sc.r180,alias='J12')
        elems += spira.SRef(sc.ls_jj_242_sg(),midpoint=(4.805*tp,4.5*tp),alias='J10')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(6.49*tp,1.5*tp),transformation=sc.r180,alias='J18')
        elems += spira.SRef(sc.ls_jj_274_sg(),midpoint=(2.5*tp,2.5*tp),alias='J5')
        elems += spira.SRef(sc.ls_jj_274_sg(),midpoint=(2.5*tp,4.5*tp),transformation=sc.r180,alias='J2')
        elems += spira.SRef(sc.ls_jj_329_sg(),midpoint=(4.5*tp,3.5*tp),transformation=sc.r270,alias='J8')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_res_1p36(),midpoint=(7.09*tp,1.5*tp),transformation=sc.r90,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 9):
                if (x == 1 and y in [1,5]) or (x == 6 and y == 5) or (x == 7 and y == 1):
                    elems += spira.SRef(sc.ls_tr_PTLconnection(),midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(sc.ls_tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(sc.ls_tr_M7(),midpoint=(0+x*tp,0+y*tp))
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