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
L1_width = 0.25*tp*Scaling
L2_width = 0.075*tp*Scaling
L3_width = 0.1*tp*Scaling
L4_width = 0.15*tp*Scaling
L5_width = L1_width
L6_width = L2_width
L7_width = L3_width
L8_width = L4_width
L9_width = 0.25*tp*Scaling
L10_width = L1_width
L11_width = 0.2*tp*Scaling
L12_width = 0.2*tp*Scaling
L13_width = L1_width
LB_width = 0.14*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_XOR_v2p1"
    def create_elements(self, elems):
        M6Strips = spira.SRef(M6_strips())
        IXports = spira.SRef(IX_ports())
        M0tracks = spira.SRef(M0_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        M0blocks = spira.SRef(M0_blocks())
        tblocks = spira.SRef(trackblocks())
        elems += [M6Strips, IXports, M0tracks, jjfill, M4M5M6M7conns, 
                  vias, bias, jjs, M0blocks, tblocks]
        # Bias Pillar Ports
        PBP1 = spira.Port(name="PBP1",midpoint=(0.5*tp,2.5*tp),process=spira.RDD.PROCESS.M6)
        PBP2 = spira.Port(name="PBP2",midpoint=(0.5*tp,4.5*tp),process=spira.RDD.PROCESS.M6)
        PBP3 = spira.Port(name="PBP3",midpoint=(1.5*tp,4.0*tp),process=spira.RDD.PROCESS.M6)
        PBP4 = spira.Port(name="PBP4",midpoint=(5.5*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        PBP5 = spira.Port(name="PBP5",midpoint=(5.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PBP6 = spira.Port(name="PBP6",midpoint=(6.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        # Bias Ports
        PB1W = spira.Port(name="PB1W",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name="PB1E",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name="PB2N",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name="PB2S",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3W = spira.Port(name="PB3W",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3E = spira.Port(name="PB3E",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4N = spira.Port(name="PB4N",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name="PB4S",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5W = spira.Port(name="PB5W",midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5E = spira.Port(name="PB5E",midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6N = spira.Port(name="PB6N",midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6S = spira.Port(name="PB6S",midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
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
        PJ10 = spira.Port(name="PJ10",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint-(0.085*tp,0),process=spira.RDD.PROCESS.M6)
        PJ11 = spira.Port(name="PJ11",midpoint=jjs.reference.elements['J11'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Via Ports
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV4 = spira.Port(name="PV4",midpoint=vias.reference.elements['via4'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center,process=spira.RDD.PROCESS.M6)
        PB_post = spira.Port(name="PB_post",midpoint=IXports.reference.elements['B'].center-(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center,process=spira.RDD.PROCESS.M6)
        PCLK_post = spira.Port(name="PCLK_post",midpoint=IXports.reference.elements['CLK'].center+(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(1.5*tp,3.175*tp),(1.4*tp,3.175*tp),(1.4*tp,2.975*tp),
                                                       (1.6*tp,2.975*tp),(1.6*tp,2.775*tp),(1.5*tp,2.775*tp)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L3_1 = spira.RoutePath(port1=PJ2,port2=PV1,path=[((PJ2.x+PV1.x)/2,(PJ2.y+PV1.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L3_2 = spira.RoutePath(port1=PV1,port2=PJ3,path=[((PV1.x+PJ3.x)/2,(PV1.y+PJ3.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M5)
        L4 = spira.RoutePath(port1=PJ3,port2=PJ7,path=[(2.5*tp,PJ3.y),(2.5*tp,PJ7.y)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PB,port2=PJ4,path=[((PB.x+PJ4.x)/2,(PB.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['B'].bbox_info.width,layer=sc.M6)
        L5_post = spira.RoutePath(port1=PB_post,port2=PJ4,path=[((PB_post.x+PJ4.x)/2,(PB_post.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        L6 = spira.RoutePath(port1=PJ5,port2=PJ4,path=[(2.775*tp,5.5*tp),(2.775*tp,5.4*tp),(2.975*tp,5.4*tp),
                                                       (2.975*tp,5.6*tp),(3.175*tp,5.6*tp),(3.175*tp,5.5*tp)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M6)
        L7_1 = spira.RoutePath(port1=PJ5,port2=PV2,path=[((PJ5.x+PV2.x)/2,(PJ5.y+PV2.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M6)
        L7_2 = spira.RoutePath(port1=PV2,port2=PJ6,path=[((PV2.x+PJ6.x)/2,(PV2.y+PJ6.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M5)
        L8 = spira.RoutePath(port1=PJ6,port2=PJ7,path=[(PJ6.x,4.5*tp),(PJ7.x,4.5*tp)],start_straight=False,end_straight=False,width=L8_width,layer=sc.M6)
        L9_1 = spira.RoutePath(port1=PJ7,port2=PV4,path=[((PJ7.x+PV4.x)/2,(PJ7.y+PV4.y)/2)],start_straight=False,end_straight=False,width=L9_width,layer=sc.M5)
        L9_2 = spira.RoutePath(port1=PV4,port2=PJ10,path=[((PV4.x+PJ10.x)/2,(PV4.y+PJ10.y)/2)],start_straight=False,end_straight=False,width=L9_width,layer=sc.M6)
        L10 = spira.RoutePath(port1=PCLK,port2=PJ8,path=[((PCLK.x+PJ8.x)/2,(PCLK.y+PJ8.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['CLK'].bbox_info.width,layer=sc.M6)
        L10_post = spira.RoutePath(port1=PCLK_post,port2=PJ8,path=[((PCLK_post.x+PJ8.x)/2,(PCLK_post.y+PJ8.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=sc.M6)
        L11_1 = spira.RoutePath(port1=PJ8,port2=PJ9,path=[((PJ8.x+PJ9.x)/2,(PJ8.y+PJ9.y)/2)],start_straight=False,end_straight=False,width=L11_width,layer=sc.M6)
        L11_2 = spira.RoutePath(port1=PJ9,port2=PV3,path=[((PJ9.x+PV3.x)/2,(PJ9.y+PV3.y)/2)],start_straight=False,end_straight=False,width=L11_width,layer=sc.M5)
        L11_3 = spira.RoutePath(port1=PV3,port2=PJ10,path=[((PV3.x+PJ10.x)/2,(PV3.y+PJ10.y)/2)],start_straight=False,end_straight=False,width=L11_width,layer=sc.M6)
        L12 = spira.RoutePath(port1=PJ10,port2=PJ11,path=[(PJ11.x,PJ10.y)],start_straight=False,end_straight=False,width=L12_width,layer=sc.M6)
        L13 = spira.RoutePath(port1=PQ,port2=PJ11,path=[((PQ.x+PJ11.x)/2,(PQ.y+PJ11.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.height,layer=sc.M6)
        L13_post = spira.RoutePath(port1=PQ_post,port2=PJ11,path=[((PQ_post.x+PJ11.x)/2,(PQ_post.y+PJ11.y)/2)],start_straight=False,end_straight=False,width=L13_width,layer=sc.M6)
        elems += [L1, L1_post, L2, L3_1, L3_2, L4, L5, L5_post, L6, L7_1, L7_2,
                  L8, L9_1, L9_2, L10, L10_post, L11_1, L11_2, L11_3, L12, L13, L13_post]

        LJ1L = spira.RoutePath(port1=PJ1,port2=PBP3,path=[((PJ1.x+PBP3.x)/2,(PJ1.y+PBP3.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_1 = spira.RoutePath(port1=PBP5,port2=PB1W,path=[(PBP5.x,PB1W.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1E,port2=PBP6,path=[(PBP6.x,PB1E.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2S,path=[(PJ3.x,0.5*tp),(PB2S.x,0.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PBP1,path=[((PB2N.x+PBP1.x)/2,(PB2N.y+PBP1.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ4,port2=PB3W,path=[((PJ4.x+PB3W.x)/2,(PJ4.y+PB3W.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3E,port2=PBP5,path=[((PB3E.x+PBP5.x)/2,(PB3E.y+PBP5.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ6,port2=PB4N,path=[(PJ6.x,6.5*tp),(PB4N.x,6.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4S,port2=PBP2,path=[((PB4S.x+PBP2.x)/2,(PB4S.y+PBP2.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB5_1 = spira.RoutePath(port1=PJ8,port2=PB5W,path=[((PJ8.x+PB5W.x)/2,(PJ8.y+PB5W.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB5_2 = spira.RoutePath(port1=PB5E,port2=PBP4,path=[((PB5E.x+PBP4.x)/2,(PB5E.y+PBP4.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB6_1 = spira.RoutePath(port1=PJ11,port2=PB6S,path=[((PJ11.x+PB6S.x)/2,(PJ11.y+PB6S.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB6_2 = spira.RoutePath(port1=PB6N,port2=PBP5,path=[((PB6N.x+PBP5.x)/2,(PB6N.y+PBP5.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        elems += [LJ1L, LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2, LB5_1, LB5_2, LB6_1, LB6_2]
        # M4M7 blocks
        elems += spira.Box(layer=sc.M4,width=0.56*tp,height=0.24*tp,center=(2.0*tp,1.84*tp))
        elems += spira.Box(layer=sc.M4,width=0.56*tp,height=0.24*tp,center=(1.0*tp,1.84*tp))
        elems += spira.Box(layer=sc.M4,width=0.56*tp,height=0.24*tp,center=(3.0*tp,1.84*tp))
        elems += spira.Box(layer=sc.M4,width=0.24*tp,height=0.56*tp,center=(1.84*tp,5.0*tp))
        elems += spira.Box(layer=sc.M4,width=0.24*tp,height=0.56*tp,center=(1.84*tp,6.0*tp))
        elems += spira.Box(layer=sc.M7,width=0.56*tp,height=0.24*tp,center=(2.0*tp,1.84*tp))
        elems += spira.Box(layer=sc.M7,width=0.56*tp,height=0.24*tp,center=(1.0*tp,1.84*tp))
        elems += spira.Box(layer=sc.M7,width=0.56*tp,height=0.24*tp,center=(3.0*tp,1.84*tp))
        elems += spira.Box(layer=sc.M7,width=0.24*tp,height=0.56*tp,center=(1.84*tp,5.0*tp))
        elems += spira.Box(layer=sc.M7,width=0.24*tp,height=0.56*tp,center=(1.84*tp,6.0*tp))
        # Text Labels
        elems += spira.Label(text="J9 M6 M5",position=(3.5*tp,1.87*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(3.92*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(3.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text="clk",position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text="P4 M6 M4",position=(7*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(7*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB6 M6 M4",position=(5.5*tp,3.94*tp),layer=TEXT)
        elems += spira.Label(text="J11 M6 M5",position=(5.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(3.59*tp,2.53*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(0.5*tp,6.455*tp),layer=TEXT)
        elems += spira.Label(text="J6 M5 M6",position=(1.85*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(2.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(3.98*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(3.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(3.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(3.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(3.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(0.5*tp,0.61*tp),layer=TEXT)
        elems += spira.Label(text="J3 M5 M6",position=(1.5*tp,1.85*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(1.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(6.45*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_out",position=(7*tp,6.5*tp),layer=TEXT)
        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(6.9875*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(6.9875*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(6.9875*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(6.9875*tp,5.4925*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,0.0*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,7.0*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(7.0*tp,3.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.978*tp,5.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.45*tp,6.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,6.455*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.5*tp,3.94*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.918*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,0.61*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(1.4*tp,4*tp),(1.4*tp,4.6*tp),(6.4*tp,4.6*tp),(6.4*tp,5.5*tp),(6.6*tp,5.5*tp),(6.6*tp,4.4*tp),(1.6*tp,4.4*tp),(1.6*tp,4*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(0*tp,6.35*tp),(0*tp,6.65*tp),(7*tp,6.65*tp),(7*tp,6.35*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(5.35*tp,5.5*tp),(5.35*tp,6.5*tp),(5.65*tp,6.5*tp),(5.65*tp,5.5*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(0.35*tp,1.5*tp),(0.35*tp,6.5*tp),(0.65*tp,6.5*tp),(0.65*tp,1.5*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(0.35*tp,1.35*tp),(0.35*tp,1.65*tp),(5.5*tp,1.65*tp),(5.5*tp,1.35*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(1.125*tp,6*tp),(1.125*tp,6.04*tp),(4.875*tp,6.04*tp),(4.875*tp,6*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(5*tp,5.125*tp),(5*tp,5.875*tp),(5.04*tp,5.875*tp),(5.04*tp,5.125*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(1.125*tp,4.96*tp),(1.125*tp,5*tp),(4.875*tp,5*tp),(4.875*tp,4.96*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(0.96*tp,5.125*tp),(0.96*tp,5.875*tp),(1*tp,5.875*tp),(1*tp,5.125*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(1.96*tp,3.125*tp),(1.96*tp,3.875*tp),(2*tp,3.875*tp),(2*tp,3.125*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(2.125*tp,4*tp),(2.125*tp,4.04*tp),(6.875*tp,4.04*tp),(6.875*tp,4*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(1.125*tp,3*tp),(1.125*tp,3.04*tp),(1.875*tp,3.04*tp),(1.875*tp,3*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(0.96*tp,2.125*tp),(0.96*tp,2.875*tp),(1*tp,2.875*tp),(1*tp,2.125*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(1.125*tp,1.96*tp),(1.125*tp,2*tp),(5.875*tp,2*tp),(5.875*tp,1.96*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(5.96*tp,1.125*tp),(5.96*tp,1.875*tp),(6*tp,1.875*tp),(6*tp,1.125*tp)]))
        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(points=[(0.125*tp,1*tp),(0.125*tp,1.04*tp),(5.875*tp,1.04*tp),(5.875*tp,1*tp)]))
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.6*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,6.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.72*tp,1.445*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,2.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,2.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.86*tp,1.445*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,1.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,1.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,2.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(-0.665*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,4.23*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.445*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.055*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,3.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(-0.665*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,4.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(5.195*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.165*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(3.875*tp,4.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.985*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(5.875*tp,4.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(6.065*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(6.975*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(6.975*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(5.265*tp,4.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(3.875*tp,7.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(3.875*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(5.945*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(5.985*tp,1.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(4.565*tp,3.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(1.565*tp,5.83*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(2.265*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(3.265*tp,7.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(3.265*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.265*tp,1.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(1.635*tp,4.76*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(2.23*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(1.945*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.165*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(4.93*tp,0.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.735*tp,-0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.735*tp,0.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(1.93*tp,0.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.125*tp,-0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(5.93*tp,0.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.125*tp,0.665*tp))
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(3.415*tp,2.915*tp),alias='via4')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(1.415*tp,2.075*tp),alias='via1')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(3.415*tp,2.1*tp),alias='via3')
        elems += spira.SRef(sc.ls_conn_M5M6(),transformation=sc.r270,midpoint=(2.075*tp,5.585*tp),alias='via2')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_112(),midpoint=(0.5*tp,0.555*tp),alias='bias2')
        elems += spira.SRef(sc.ls_ib_112(),transformation=sc.r180,midpoint=(0.5*tp,6.51*tp),alias='bias4')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(5.5*tp,3.885*tp),alias='bias6')
        elems += spira.SRef(sc.ls_ib_175(),transformation=sc.r90,midpoint=(4.87*tp,1.5*tp),alias='bias5')
        elems += spira.SRef(sc.ls_ib_175(),transformation=sc.r90,midpoint=(4.93*tp,5.5*tp),alias='bias3')
        elems += spira.SRef(sc.ls_ib_175(),transformation=sc.r90,midpoint=(6.505*tp,6.5*tp),alias='bias1')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_089_sg(),transformation=sc.r90,midpoint=(3.585*tp,2.53*tp),alias='J10')
        elems += spira.SRef(sc.ls_jj_145_s(),transformation=sc.r90,midpoint=(3.5*tp,1.875*tp),alias='J9')
        elems += spira.SRef(sc.ls_jj_162_s(),transformation=sc.r270,midpoint=(3.5*tp,3.5*tp),alias='J7')
        elems += spira.SRef(sc.ls_jj_171_s(),transformation=sc.r90,midpoint=(1.85*tp,5.5*tp),alias='J6')
        elems += spira.SRef(sc.ls_jj_171_s(),transformation=sc.r90,midpoint=(1.5*tp,1.85*tp),alias='J3')
        elems += spira.SRef(sc.ls_jj_209_sg(),midpoint=(2.5*tp,5.5*tp),alias='J5')
        elems += spira.SRef(sc.ls_jj_209_sg(),transformation=sc.r90,midpoint=(1.5*tp,2.5*tp),alias='J2')
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r90,midpoint=(5.5*tp,3.5*tp),alias='J11')
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r90,midpoint=(3.5*tp,1.5*tp),alias='J8')
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r180,midpoint=(3.5*tp,5.5*tp),alias='J4')
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r270,midpoint=(1.5*tp,3.5*tp),alias='J1')
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 7):
                if (y == 0) or (y == 1 and x == 6) or (y == 2 and x != 0) or (y == 3 and x not in [0,1]):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                elif (y == 5 and x not in [0,5,6]):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                else:
                    pass
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(-1, 8):
            for x in range(-1, 8):
                if (x == 0 and y in [2,4]) or (x == 5 and y in [1,5]) or (x == 6 and y == 5):
                    elems += spira.SRef(sc.ls_tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif (x in [-1,7] and y == 3) or (x == 3 and y in [-1,7]):
                    elems += spira.SRef(sc.ls_tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(sc.ls_tr_M7(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 2 and y == 3):
                    elems += spira.SRef(sc.ls_tr_bias_pillar_half(),midpoint=(0+x*tp,tp/2+y*tp),transformation=sc.r90)
                    elems += spira.SRef(sc.ls_tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(sc.ls_tr_M7(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 1 and y == 3):
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter1(),midpoint=(0+tp*x,0+tp*y))
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter2(),midpoint=(10+tp*x,0+tp*y))
                elif (x == 1 and y == 4):
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter1(),midpoint=(0+tp*x,10+tp*y),transformation=sc.r270)
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter1(),midpoint=(10+tp*x,10+tp*y),transformation=sc.m135)
                elif (x in [-1,7] or y in [-1,7]):
                    pass
                else:
                    elems += spira.SRef(sc.ls_tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
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