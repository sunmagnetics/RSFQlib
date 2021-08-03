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
L2_width = 0.25*tp*Scaling
L3_width = 0.3*tp*Scaling
L4_width = L1_width
L5_width = L2_width
L6_width = 0.13*tp*Scaling
L7_width = 0.3*tp*Scaling
L8_width = 0.29*tp*Scaling
L9_width = L1_width
L10_width = 0.17*tp*Scaling
L11_width = 0.15*tp*Scaling
L12_width = L1_width
LB_width = 0.14*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_NDRO_v2p1"
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
        elems += [M6Strips, IXports, M0tracks, jjfill, M4M5M6M7conns, vias, bias, jjs, M0blocks, tblocks]
        # Ports for inductor connections
        # Bias1
        PB1W = spira.Port(name="PB1W",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name="PB1E",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias2
        PB2W = spira.Port(name="PB2W",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2E = spira.Port(name="PB2E",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias3
        PB3N = spira.Port(name="PB3N",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name="PB3S",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias4
        PB4N = spira.Port(name="PB4N",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name="PB4S",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias5
        PB5S = spira.Port(name="PB5S",midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5N = spira.Port(name="PB5N",midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias6
        PB6W = spira.Port(name="PB6W",midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6E = spira.Port(name="PB6E",midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Ends
        PB1_end = spira.Port(name="PB1_end",midpoint=(2.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PB2_end = spira.Port(name="PB2_end",midpoint=(0.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
        PB4_5_end = spira.Port(name="PB4_5_end",midpoint=(5.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
        # JJ1
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ1L = spira.Port(name="PJ1L",midpoint=(4.0*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        # JJ2
        PJ2W = spira.Port(name="PJ2W",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ2E = spira.Port(name="PJ2E",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ3
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ4
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ5
        PJ5W = spira.Port(name="PJ5W",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ5S = spira.Port(name="PJ5S",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        # JJ6
        PJ6 = spira.Port(name="PJ6",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ7
        PJ7W = spira.Port(name="PJ7W",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ7E = spira.Port(name="PJ7E",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        # JJ8
        PJ8 = spira.Port(name="PJ8",midpoint=jjs.reference.elements['J8'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ9
        PJ9N = spira.Port(name="PJ9N",midpoint=jjs.reference.elements['J9'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ9W = spira.Port(name="PJ9W",midpoint=jjs.reference.elements['J9'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ10
        PJ10 = spira.Port(name="PJ10",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ11
        PJ11 = spira.Port(name="PJ11",midpoint=jjs.reference.elements['J11'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # VIA A
        PVAW = spira.Port(name="PVAW",midpoint=vias.reference.elements['viaA'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PVAE = spira.Port(name="PVAE",midpoint=vias.reference.elements['viaA'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        # VIA B
        PVBN = spira.Port(name="PVBN",midpoint=vias.reference.elements['viaB'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        PVBS = spira.Port(name="PVBS",midpoint=vias.reference.elements['viaB'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # VIA CLK
        PVCLKN = spira.Port(name="PVCLKN",midpoint=vias.reference.elements['viaCLK'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PVCLKS = spira.Port(name="PVCLKS",midpoint=vias.reference.elements['viaCLK'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        # VIA Q
        PVQW = spira.Port(name="PVQW",midpoint=vias.reference.elements['viaQ'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        PVQS = spira.Port(name="PVQS",midpoint=vias.reference.elements['viaQ'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pins
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center-(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center,process=spira.RDD.PROCESS.M6)
        PB_post = spira.Port(name="PB_post",midpoint=IXports.reference.elements['B'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center+(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center,process=spira.RDD.PROCESS.M6)
        PCLK_post = spira.Port(name="PCLK_post",midpoint=IXports.reference.elements['CLK'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        ## Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.width,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2_1 = spira.RoutePath(port1=PJ1,port2=PJ2E,path=[((PJ1.x+PJ2E.x)/2,(PJ1.y+PJ2E.y)/2)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L2_2 = spira.RoutePath(port1=PJ2W,port2=PVAE,path=[((PJ2W.x+PVAE.x)/2,(PJ2W.y+PVAE.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M5)
        L2_3 = spira.RoutePath(port1=PVAW,port2=PJ3,path=[((PVAW.x+PJ3.x)/2,(PVAW.y+PJ3.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PJ3,port2=PJ7W,path=[(2.5*tp,4.5*tp),(3.5*tp,4.5*tp),(3.5*tp,3.5*tp)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PB,port2=PJ4,path=[((PB.x+PJ4.x)/2,(PB.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['B'].bbox_info.height,layer=sc.M6)
        L4_post = spira.RoutePath(port1=PB_post,port2=PJ4,path=[((PB_post.x+PJ4.x)/2,(PB_post.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L5_1 = spira.RoutePath(port1=PJ4,port2=PJ5W,path=[((PJ4.x+PJ5W.x)/2,(PJ4.y+PJ5W.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        L5_2 = spira.RoutePath(port1=PJ5S,port2=PVBN,path=[((PJ5S.x+PVBN.x)/2,(PJ5S.y+PVBN.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M5)
        L5_3 = spira.RoutePath(port1=PVBS,port2=PJ6,path=[((PVBS.x+PJ6.x)/2,(PVBS.y+PJ6.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        L6 = spira.RoutePath(port1=PJ6,port2=PJ7W,path=[(3.5*tp,2.5*tp),(3.5*tp,3.5*tp)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M6)
        L7_1 = spira.RoutePath(port1=PJ7E,port2=PVQW,path=[((PJ7E.x+PVQW.x)/2,(PJ7E.y+PVQW.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M5)
        L7_2 = spira.RoutePath(port1=PVQS,port2=PJ10,path=[((PVQS.x+PJ10.x)/2,(PVQS.y+PJ10.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M6)
        L9 = spira.RoutePath(port1=PCLK,port2=PJ8,path=[((PCLK.x+PJ8.x)/2,(PCLK.y+PJ8.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['CLK'].bbox_info.height,layer=sc.M6)
        L9_post = spira.RoutePath(port1=PCLK_post,port2=PJ8,path=[((PCLK_post.x+PJ8.x)/2,(PCLK_post.y+PJ8.y)/2)],start_straight=False,end_straight=False,width=L9_width,layer=sc.M6)
        L10_1 = spira.RoutePath(port1=PJ8,port2=PVCLKN,path=[((PJ8.x+PVCLKN.x)/2,(PJ8.y+PVCLKN.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=sc.M6)
        L10_2 = spira.RoutePath(port1=PVCLKS,port2=PJ9N,path=[((PVCLKS.x+PJ9N.x)/2,(PVCLKS.y+PJ9N.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=sc.M5)      
        L10_3 = spira.RoutePath(port1=PJ9W,port2=PJ10,path=[((PJ9W.x+PJ10.x)/2,(PJ9W.y+PJ10.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=sc.M6)      
        L11 = spira.RoutePath(port1=PJ10,port2=PJ11,path=[(4.5*tp,1.5*tp)],start_straight=False,end_straight=False,width=L11_width,layer=sc.M6)
        L12 = spira.RoutePath(port1=PJ11,port2=PQ,path=[((PJ11.x+PQ.x)/2,(PJ11.y+PQ.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.width,layer=sc.M6)
        L12_post = spira.RoutePath(port1=PJ11,port2=PQ_post,path=[((PJ11.x+PQ_post.x)/2,(PJ11.y+PQ_post.y)/2)],start_straight=False,end_straight=False,width=L12_width,layer=sc.M6)
        LJ1 = spira.RoutePath(port1=PJ1,port2=PJ1L,path=[((PJ1.x+PJ1L.x)/2,(PJ1.y+PJ1L.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_1 = spira.RoutePath(port1=PB1_end,port2=PB1E,path=[((PB1_end.x+PB1E.x)/2,(PB1_end.y+PB1E.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PB3S,path=[(0.5*tp,0.5*tp),(0.5*tp,1.5*tp),(1.5*tp,1.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_3 = spira.RoutePath(port1=PB1W,port2=PB6W,path=[(0.5*tp,0.5*tp),(0.5*tp,1.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2E,path=[(2.5*tp,6.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2W,port2=PB2_end,path=[((PB2W.x+PB2_end.x)/2,(PB2W.y+PB2_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3 = spira.RoutePath(port1=PJ4,port2=PB3N,path=[((PJ4.x+PB3N.x)/2,(PJ4.y+PB3N.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ8,port2=PB4S,path=[((PJ8.x+PB4S.x)/2,(PJ8.y+PB4S.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4N,port2=PB4_5_end,path=[((PB4N.x+PB4_5_end.x)/2,(PB4N.y+PB4_5_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB5_1 = spira.RoutePath(port1=PVQS,port2=PB5S,path=[((PVQS.x+PB5S.x)/2,(PVQS.y+PB5S.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB5_2 = spira.RoutePath(port1=PB5N,port2=PB4_5_end,path=[(4.5*tp,5.5*tp),(5.5*tp,5.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB6 = spira.RoutePath(port1=PJ11,port2=PB6E,path=[((PJ11.x+PB6E.x)/2,(PJ11.y+PB6E.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        elems += [L1, L1_post, L2_1, L2_2, L2_3, L3, L4, L4_post, 
                  L5_1, L5_2, L5_3, L6, L7_1, L7_2, L9, L9_post, 
                  L10_1, L10_2, L10_3, L11, L12, L12_post]
        elems += [LJ1, LB1_1, LB1_2, LB1_3, LB2_1, LB2_2, LB3, 
                  LB4_1, LB4_2, LB5_1, LB5_2, LB6]
        elems += spira.Box(layer=sc.M4,width=0.24*tp,height=0.56*tp,center=(3.16*tp,5.0*tp))
        elems += spira.Box(layer=sc.M4,width=0.25*tp,height=0.56*tp,center=(4.0*tp,4.0*tp))
        elems += spira.Box(layer=sc.M7,width=0.24*tp,height=0.56*tp,center=(3.16*tp,5.0*tp))
        elems += spira.Box(layer=sc.M7,width=0.25*tp,height=0.56*tp,center=(4.0*tp,4.0*tp))
        # Text Labels
        elems += spira.Label(text="bias_out",position=(7*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(3.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(3.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="clk",position=(7*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(7*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="Q",position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text="P4 M6 M4",position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(3.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(3.11*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(2.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(2.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(2.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(4.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(5.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J9 M5 M6",position=(5.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(4.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J11 M6 M5",position=(3.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.51*tp,0.498*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(2.235*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(1.5*tp,3.0*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(5.5*tp,3.965*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(4.5*tp,3.937*tp),layer=TEXT)
        elems += spira.Label(text="PB6 M6 M4",position=(3.0*tp,1.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.9075*tp,6.615*tp),layer=spira.Layer(number=1,datatype=1))
        elems += spira.Label(text='GND',position=(1.5025*tp,6.92*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='clk',position=(6.995*tp,3.4075*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q',position=(3.4075*tp,0.005*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='a',position=(3.41*tp,6.995*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='b',position=(0.005*tp,3.4075*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='RB1',position=(3.4975*tp,5.2075*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(3.1075*tp,5.2025*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(2.22*tp,5.5025*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB4',position=(1.5*tp,3.79*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB5',position=(2.5*tp,3.79*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB6',position=(2.5025*tp,2.1975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB7',position=(4*tp,3.9175*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB8',position=(5.2075*tp,3.5025*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB9',position=(5.4975*tp,2.1725*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB10',position=(4.1675*tp,2.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB11',position=(3.5025*tp,1.7925*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.075*tp,0.495*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(1.94*tp,6.5025*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(1.4975*tp,2.545*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB4',position=(5.505*tp,4.4225*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB5',position=(4.4975*tp,4.51*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB6',position=(2.525*tp,1.505*tp),layer=spira.Layer(number=52,datatype=1))

        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.5075*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(5.5075*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M6,width=0.03*tp,height=0.315*tp,center=(0.015*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,1.5075*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.5075*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(2.5075*tp,0.0125*tp))

        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.5075*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(5.5075*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.03*tp,height=0.315*tp,center=(0.015*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,1.5075*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.5075*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(2.5075*tp,0.0125*tp))

        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,0.0*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(7.0*tp,3.5*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,7.0*tp),alias='A')

        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.5*tp,3.002*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.0*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.5*tp,3.963*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.517*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.235*tp,6.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,3.935*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M0,width=0.24*tp,height=0.32*tp,center=(2.16*tp,5.88*tp))
        elems += spira.Box(layer=sc.M0,width=0.3*tp,height=5.0*tp,center=(0.5*tp,4.0*tp))
        elems += spira.Box(layer=sc.M0,width=7.0*tp,height=0.3*tp,center=(3.5*tp,6.5*tp))

        elems += spira.Polygon(layer=sc.M0,shape=spira.Shape(
            points=[(4.0*tp,5.625*tp),(3.375*tp,5.625*tp),(3.375*tp,1.625*tp),
                    (2.375*tp,1.625*tp),(2.375*tp,0.5*tp),(2.625*tp,0.5*tp),
                    (2.625*tp,1.375*tp),(3.625*tp,1.375*tp),(3.625*tp,5.375*tp),
                    (4.0*tp,5.375*tp)]))

        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(5.5*tp,1.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(3.5*tp,1.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(0.5*tp,1.02*tp))
        elems += spira.Box(layer=sc.M0,width=1.75*tp,height=0.04*tp,center=(2.0*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=1.75*tp,height=0.04*tp,center=(6.0*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(4.5*tp,5.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(2.5*tp,1.98*tp))

        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(4.98*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(0.98*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(3.02*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(5.98*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=3.75*tp,center=(3.98*tp,3.0*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(2.98*tp,0.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=1.75*tp,center=(2.02*tp,1.0*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=2.875*tp,center=(3.02*tp,3.4375*tp))
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,4.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.93*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.93*tp,5.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.735*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.08*tp,4.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.025*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.125*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.125*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.735*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.085*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.93*tp,5.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.93*tp,4.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.735*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.665*tp,6.835*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,5.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.665*tp,4.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.165*tp,4.565*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,6.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,6.835*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,6.015*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,1.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,1.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,1.845*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,0.845*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,4.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,4.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,0.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,0.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,0.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,6.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,0.845*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,0.025*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.665*tp,5.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.665*tp,4.015*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.665*tp,1.475*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,1.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,0.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.07*tp,4.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,1.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.265*tp,0.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,0.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.925*tp,1.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.07*tp,3.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.155*tp,6.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.07*tp,1.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.925*tp,2.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.07*tp,0.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.07*tp,0.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.985*tp,0.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.875*tp,4.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.265*tp,4.665*tp),transformation=sc.m135)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(2.415*tp,2.915*tp),alias="viaB")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.415*tp,3.415*tp),alias="viaQ")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(5.415*tp,2.915*tp),alias="viaCLK")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(2.76*tp,5.415*tp),alias="viaA")
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_136(),midpoint=(4.5*tp,3.88*tp),alias="bias5")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(1.5*tp,2.05*tp),alias="bias3")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(3.055*tp,1.5*tp),transformation=sc.r90,alias="bias6")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(5.5*tp,4.915*tp),transformation=sc.r180,alias="bias4")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(0.565*tp,0.5*tp),transformation=sc.r270,alias="bias1")
        elems += spira.SRef(sc.ls_ib_271(),midpoint=(2.29*tp,6.5*tp),transformation=sc.r90,alias="bias2")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_074_s(),midpoint=(4*tp,3.5*tp),alias="J7")
        elems += spira.SRef(sc.ls_jj_109_sg(),midpoint=(4.5*tp,2.5*tp),transformation=sc.r90,alias="J10")
        elems += spira.SRef(sc.ls_jj_117_s(),midpoint=(5.5*tp,2.5*tp),transformation=sc.r180,alias="J9")
        elems += spira.SRef(sc.ls_jj_199_s(),midpoint=(3.11*tp,5.5*tp),transformation=sc.r180,alias="J2")
        elems += spira.SRef(sc.ls_jj_220_sg(),midpoint=(2.5*tp,5.5*tp),transformation=sc.r90,alias="J3")
        elems += spira.SRef(sc.ls_jj_235_s(),midpoint=(2.5*tp,3.5*tp),alias="J5")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,3.5*tp),alias="J4")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(3.5*tp,1.5*tp),alias="J11")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(5.5*tp,3.5*tp),transformation=sc.r90,alias="J8")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(3.5*tp,5.5*tp),transformation=sc.r180,alias="J1")
        elems += spira.SRef(sc.ls_jj_324_sg(),midpoint=(2.5*tp,2.5*tp),transformation=sc.r180,alias="J6")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 7):
                if (y == 0 and x != 2) or (y == 1 and x in [1,4,5,6]):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                elif (y in [2,3,4] and x not in[0, 3]) or (y == 5 and x in [1,2,5,6]):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                else:
                    pass
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        m0 = spira.Reflection(True)
        T2 = spira.Reflection(True) + spira.Rotation(270)
        r90 = spira.Rotation(90)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 7):
                if (x == 0 and y in [1,6]) or (x == 2 and y == 0) or (x == 5 and y == 6):
                    elems += spira.SRef(sc.ls_tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 3 and y == 5):
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter1(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter1(),midpoint=(0+x*tp,tp+y*tp), transformation=sc.m0)
                    elems += spira.SRef(sc.ls_tr_bias_pillar_half(),midpoint=(tp/2+x*tp,0+y*tp))
                elif (x == 4 and y == 5):
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter1(),midpoint=(tp+x*tp,tp+y*tp), transformation=T2)
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter1(),midpoint=(tp+x*tp,0+y*tp), transformation=sc.r90)
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