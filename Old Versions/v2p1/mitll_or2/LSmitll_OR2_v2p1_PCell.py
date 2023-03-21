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
L2_width = 0.24*tp*Scaling
L3_width = 0.23*tp*Scaling
L4_width = L1_width
L5_width = 0.23*tp*Scaling
L6_width = 0.2*tp*Scaling
L7_width = 0.25*tp*Scaling
L8_width = 0.1*tp*Scaling
L9_width = L1_width
L10_width = 0.145*tp*Scaling
L11_width = 0.22*tp*Scaling
L12_width = L1_width
LB1_width = 0.14*tp*Scaling
LB2_width = 0.16*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_OR2_v2p1"
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
        PB1W = spira.Port(name="PB1W",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name="PB1E",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias2
        PB2W = spira.Port(name="PB2W",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2E = spira.Port(name="PB2E",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias3
        PB3W = spira.Port(name="PB3W",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3E = spira.Port(name="PB3E",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias4
        PB4W = spira.Port(name="PB4W",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4E = spira.Port(name="PB4E",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias5
        PB5W = spira.Port(name="PB5W",midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5E = spira.Port(name="PB5E",midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias6
        PB6W = spira.Port(name="PB6W",midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6E = spira.Port(name="PB6E",midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Ends
        PB1_end = spira.Port(name="PB1_end",midpoint=(0.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PB2_4_6_end = spira.Port(name="PB2_4_6_end",midpoint=(7.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PB3_end = spira.Port(name="PB3_end",midpoint=(1.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PB5_end = spira.Port(name="PB5_end",midpoint=(0.5*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # VIAS
        PV1M5 = spira.Port(name="PV1M5",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        PV1M6 = spira.Port(name="PV1M6",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2M5 = spira.Port(name="PV2M5",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        PV2M6 = spira.Port(name="PV2M6",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ1
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ2
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ3
        PJ3M5 = spira.Port(name="PJ3M5",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ3M6 = spira.Port(name="PJ3M6",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ4
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ5
        PJ5 = spira.Port(name="PJ5",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ6
        PJ6M5 = spira.Port(name="PJ6M5",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ6M6 = spira.Port(name="PJ6M5",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ7
        PJ7M5 = spira.Port(name="PJ7M5",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ7M6 = spira.Port(name="PJ7M6",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ8
        PJ8 = spira.Port(name="PJ8",midpoint=jjs.reference.elements['J8'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ9
        PJ9 = spira.Port(name="PJ9",midpoint=jjs.reference.elements['J9'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ10
        PJ10M5 = spira.Port(name="PJ10M5",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ10M6 = spira.Port(name="PJ10M6",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ11
        PJ11 = spira.Port(name="PJ11",midpoint=jjs.reference.elements['J11'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ12
        PJ12 = spira.Port(name="PJ12",midpoint=jjs.reference.elements['J12'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pins
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center,process=spira.RDD.PROCESS.M6)
        PB_post = spira.Port(name="PB_post",midpoint=IXports.reference.elements['B'].center-(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center,process=spira.RDD.PROCESS.M6)
        PCLK_post = spira.Port(name="PCLK_post",midpoint=IXports.reference.elements['CLK'].center+(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PL6 = spira.Port(name="PL6",midpoint=(3.5*tp,2.5*tp),process=spira.RDD.PROCESS.M6)
        ## Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(PJ1.x,2.56*tp),(PJ2.x,2.56*tp)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L3_1 = spira.RoutePath(port1=PJ2,port2=PJ3M6,path=[((PJ2.x+PJ3M6.x)/2,(PJ2.y+PJ3M6.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L3_2 = spira.RoutePath(port1=PJ3M5,port2=PV1M5,path=[((PJ3M5.x+PV1M5.x)/2,(PJ3M5.y+PV1M5.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M5)
        L4 = spira.RoutePath(port1=PB,port2=PJ4,path=[((PB.x+PJ4.x)/2,(PB.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['B'].bbox_info.width,layer=sc.M6)
        L4_post = spira.RoutePath(port1=PB_post,port2=PJ4,path=[((PB_post.x+PJ4.x)/2,(PB_post.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(2.56*tp,PJ4.y),(2.56*tp,PJ5.y)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        L6_1 = spira.RoutePath(port1=PJ5,port2=PJ6M6,path=[((PJ5.x+PJ6M6.x)/2,(PJ5.y+PJ6M6.y)/2)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M6)
        L6_2 = spira.RoutePath(port1=PJ6M5,port2=PV1M5,path=[((PJ6M5.x+PV1M5.x)/2,(PJ6M5.y+PV1M5.y)/2)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M5)
        L6_3 = spira.RoutePath(port1=PV1M6,port2=PL6,path=[((PV1M6.x+PL6.x)/2,(PV1M6.y+PL6.y)/2)],start_straight=False,end_straight=False,width=LB2_width,layer=sc.M6)
        L7_1 = spira.RoutePath(port1=PV1M5,port2=PJ7M5,path=[((PV1M5.x+PJ7M5.x)/2,(PV1M5.y+PJ7M5.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M5)
        L7_2 = spira.RoutePath(port1=PJ7M6,port2=PJ8,path=[(PJ7M6.x,PJ8.y)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M6)
        L8 = spira.RoutePath(port1=PJ8,port2=PJ11,path=[(PJ8.x,4.14*tp),(5.4*tp,4.14*tp),(5.4*tp,3.74*tp),(5.6*tp,3.74*tp),(5.6*tp,3.34*tp),(5.4*tp,3.34*tp),(5.4*tp,2.94*tp),
                                                        (5.6*tp,2.94*tp),(5.6*tp,2.54*tp),(5.4*tp,2.54*tp),(5.4*tp,2.14*tp),(5.6*tp,2.14*tp),(5.6*tp,1.84*tp),(5.5*tp,1.84*tp)],start_straight=False,end_straight=False,width=L8_width,layer=sc.M6)
        L9 = spira.RoutePath(port1=PCLK,port2=PJ9,path=[((PCLK.x+PJ9.x)/2,(PCLK.y+PJ9.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['CLK'].bbox_info.width,layer=sc.M6)
        L9_post = spira.RoutePath(port1=PCLK_post,port2=PJ9,path=[((PCLK_post.x+PJ9.x)/2,(PCLK_post.y+PJ9.y)/2)],start_straight=False,end_straight=False,width=L9_width,layer=sc.M6)
        L10_1 = spira.RoutePath(port1=PJ9,port2=PV2M6,path=[((PJ9.x+PV2M6.x)/2,(PJ9.y+PV2M6.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=sc.M6)
        L10_2 = spira.RoutePath(port1=PV2M5,port2=PJ10M5,path=[((PV2M5.x+PJ10M5.x)/2,(PV2M5.y+PJ10M5.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=sc.M5)
        L10_3 = spira.RoutePath(port1=PJ10M6,port2=PJ11,path=[((PJ10M6.x+PJ11.x)/2,(PJ10M6.y+PJ11.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=sc.M6)
        L11 = spira.RoutePath(port1=PJ11,port2=PJ12,path=[(PJ12.x,PJ11.y)],start_straight=False,end_straight=False,width=L11_width,layer=sc.M6)
        L12 = spira.RoutePath(port1=PQ,port2=PJ12,path=[((PQ.x+PJ12.x)/2,(PQ.y+PJ12.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.height,layer=sc.M6)
        L12_post = spira.RoutePath(port1=PQ_post,port2=PJ12,path=[((PQ_post.x+PJ12.x)/2,(PQ_post.y+PJ12.y)/2)],start_straight=False,end_straight=False,width=L12_width,layer=sc.M6)
        
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1E,path=[((PJ1.x+PB1E.x)/2,(PJ1.y+PB1E.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PB1_end,path=[(PB1_end.x,PB1W.y)],start_straight=False,end_straight=False,width=LB1_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ4,port2=PB2W,path=[(4.5*tp,PJ4.y),(4.5*tp,PB2W.y)],start_straight=False,end_straight=False,width=LB2_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2E,port2=PB2_4_6_end,path=[(PB2_4_6_end.x,PB2E.y)],start_straight=False,end_straight=False,width=LB2_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PB5_end,port2=PB3W,path=[(PB5_end.x,PB3W.y)],start_straight=False,end_straight=False,width=LB2_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3E,port2=PB3_end,path=[((PB3E.x+PB3_end.x)/2,(PB3E.y+PB3_end.y)/2)],start_straight=False,end_straight=False,width=LB2_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ8,port2=PB4W,path=[(PJ8.x,PB4W.y)],start_straight=False,end_straight=False,width=LB1_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4E,port2=PB2_4_6_end,path=[((PB4E.x+PB2_4_6_end.x)/2,(PB4E.y+PB2_4_6_end.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=sc.M6)
        LB5_1 = spira.RoutePath(port1=PJ9,port2=PB5E,path=[((PJ9.x+PB5E.x)/2,(PJ9.y+PB5E.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=sc.M6)
        LB5_2 = spira.RoutePath(port1=PB5W,port2=PB5_end,path=[((PB5W.x+PB5_end.x)/2,(PB5W.y+PB5_end.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=sc.M6)
        LB6_1 = spira.RoutePath(port1=PJ12,port2=PB6W,path=[((PJ12.x+PB6W.x)/2,(PJ12.y+PB6W.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=sc.M6)
        LB6_2 = spira.RoutePath(port1=PB6E,port2=PB2_4_6_end,path=[(PB2_4_6_end.x,PB6E.y)],start_straight=False,end_straight=False,width=LB1_width,layer=sc.M6)
        elems += [L1, L1_post, L2, L3_1, L3_2, L4, L4_post, 
                  L5, L6_1, L6_2, L6_3, L7_1, L7_2, L8, L9, 
                  L9_post, L10_1, L10_2, L10_3, L11, L12, L12_post] 
        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2,
                  LB4_1, LB4_2, LB5_1, LB5_2, LB6_1, LB6_2]
        elems += spira.Box(layer=sc.M4,width=0.56*tp,height=0.27*tp,center=(3*tp,4*tp))
        elems += spira.Box(layer=sc.M4,width=0.27*tp,height=0.56*tp,center=(3*tp,3*tp))
        elems += spira.Box(layer=sc.M7,width=0.56*tp,height=0.27*tp,center=(3*tp,4*tp))
        elems += spira.Box(layer=sc.M7,width=0.27*tp,height=0.56*tp,center=(3*tp,3*tp))
        # Text Labels
        elems += spira.Label(text='P1 M6 M4',position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='J1 M6 M5',position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='PB1 M6 M4',position=(1.495*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text='J2 M6 M5',position=(2.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='J3 M6 M5',position=(3*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='P2 M6 M4',position=(3.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text='J4 M6 M5',position=(3.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text='PB2 M6 M4',position=(5.488*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='J5 M6 M5',position=(3.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text='J6 M6 M5',position=(3.5*tp,4*tp),layer=TEXT)
        elems += spira.Label(text='PB3 M6 M4',position=(1.08*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text='J7 M5 M6',position=(4.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='J8 M6 M5',position=(5.33*tp,4.45*tp),layer=TEXT)
        elems += spira.Label(text='PB4 M6 M4',position=(5.8*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text='J11 M6 M5',position=(5.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='P3 M6 M4',position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text='J9 M6 M5',position=(3.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='PB5 M6 M4',position=(2.375*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='J10 M5 M6',position=(4.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='J12 M6 M5',position=(6.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='PB6 M6 M4',position=(6.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text='P4 M6 M4',position=(8*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='a',position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='b',position=(3.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text='q',position=(8*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='clk',position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text='bias_in',position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='bias_out',position=(8*tp,6.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.155*tp,6.5025*tp),layer=spira.Layer(number=1,datatype=1))
        elems += spira.Label(text='GND',position=(0.475*tp,6.835*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='a',position=(0.005*tp,3.4075*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='b',position=(3.4075*tp,6.995*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='clk',position=(3.4075*tp,0.005*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q',position=(7.995*tp,3.4075*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='RB1',position=(1.7925*tp,3.5025*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(2.5025*tp,3.7975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(2.9925*tp,3.1875*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB4',position=(3.4975*tp,5.205*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB5',position=(3.8025*tp,4.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB6',position=(3.19*tp,4.005*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB7',position=(4.4975*tp,3.205*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB8',position=(5.6325*tp,4.45*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB9',position=(3.4975*tp,1.79*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB10',position=(4.4975*tp,1.8125*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB11',position=(5.5*tp,1.1875*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB12',position=(6.2175*tp,3.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.0625*tp,4.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(5.9725*tp,6.4975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(0.8125*tp,0.495*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB4',position=(6.3625*tp,5.4975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB5',position=(1.8975*tp,1.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB6',position=(6.98*tp,4.5*tp),layer=spira.Layer(number=52,datatype=1))

        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.015*tp,1.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.015*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(1.5075*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.015*tp,1.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.015*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(1.5075*tp,0.0125*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,7.0*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(8.0*tp,3.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,0.0*tp),alias='CLK')

        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.495*tp,4.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.488*tp,6.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.375*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.08*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.503*tp,4.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.804*tp,5.5*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Polygon(shape=spira.Shape(points=[(3.4*tp,0.5*tp),(3.4*tp,2.5*tp),(3.6*tp,2.5*tp),(3.6*tp,0.5*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0*tp,6.35*tp),(0*tp,6.65*tp),(8*tp,6.65*tp),(8*tp,6.35*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.375*tp,1.5*tp),(0.375*tp,6.5*tp),(0.625*tp,6.5*tp),(0.625*tp,1.5*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7.4*tp,5.5*tp),(7.4*tp,6.5*tp),(7.6*tp,6.5*tp),(7.6*tp,5.5*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(1.5*tp,0.4*tp),(1.5*tp,0.6*tp),(3.4*tp,0.6*tp),(3.4*tp,2.5*tp),(3.6*tp,2.5*tp),(3.6*tp,0.4*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,0.125*tp),(7*tp,0.875*tp),(7.04*tp,0.875*tp),(7.04*tp,0.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,1.125*tp),(7*tp,1.875*tp),(7.04*tp,1.875*tp),(7.04*tp,1.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,2.125*tp),(7*tp,2.875*tp),(7.04*tp,2.875*tp),(7.04*tp,2.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,3.125*tp),(7*tp,3.875*tp),(7.04*tp,3.875*tp),(7.04*tp,3.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,4.125*tp),(7*tp,4.875*tp),(7.04*tp,4.875*tp),(7.04*tp,4.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,5.125*tp),(7*tp,5.875*tp),(7.04*tp,5.875*tp),(7.04*tp,5.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(6.125*tp,6*tp),(6.125*tp,6.04*tp),(6.875*tp,6.04*tp),(6.875*tp,6*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(5.125*tp,6*tp),(5.125*tp,6.04*tp),(5.875*tp,6.04*tp),(5.875*tp,6*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(4.125*tp,6*tp),(4.125*tp,6.04*tp),(4.875*tp,6.04*tp),(4.875*tp,6*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.125*tp,6*tp),(3.125*tp,6.04*tp),(3.875*tp,6.04*tp),(3.875*tp,6*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(2.125*tp,6*tp),(2.125*tp,6.04*tp),(2.875*tp,6.04*tp),(2.875*tp,6*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(1.125*tp,6*tp),(1.125*tp,6.04*tp),(1.875*tp,6.04*tp),(1.875*tp,6*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(1.125*tp,0.96*tp),(1.125*tp,1*tp),(1.875*tp,1*tp),(1.875*tp,0.96*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,5.125*tp),(0.96*tp,5.875*tp),(1*tp,5.875*tp),(1*tp,5.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,4.125*tp),(0.96*tp,4.875*tp),(1*tp,4.875*tp),(1*tp,4.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,3.125*tp),(0.96*tp,3.875*tp),(1*tp,3.875*tp),(1*tp,3.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,2.125*tp),(0.96*tp,2.875*tp),(1*tp,2.875*tp),(1*tp,2.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,1.125*tp),(0.96*tp,1.875*tp),(1*tp,1.875*tp),(1*tp,1.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.96*tp,0.125*tp),(3.96*tp,0.875*tp),(4*tp,0.875*tp),(4*tp,0.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.96*tp,1.125*tp),(3.96*tp,1.875*tp),(4*tp,1.875*tp),(4*tp,1.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.96*tp,2.125*tp),(3.96*tp,2.875*tp),(4*tp,2.875*tp),(4*tp,2.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3*tp,2.125*tp),(3*tp,2.875*tp),(3.04*tp,2.875*tp),(3.04*tp,2.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3*tp,1.125*tp),(3*tp,1.875*tp),(3.04*tp,1.875*tp),(3.04*tp,1.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.125*tp,2.96*tp),(3.125*tp,3*tp),(3.875*tp,3*tp),(3.875*tp,2.96*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(2.125*tp,0.96*tp),(2.125*tp,1*tp),(2.875*tp,1*tp),(2.875*tp,0.96*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7.125*tp,5*tp),(7.125*tp,5.04*tp),(7.875*tp,5.04*tp),(7.875*tp,5*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.125*tp,1*tp),(0.125*tp,1.04*tp),(0.875*tp,1.04*tp),(0.875*tp,1*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(1*tp,0.125*tp),(1*tp,0.875*tp),(1.04*tp,0.875*tp),(1.04*tp,0.125*tp)]),layer=sc.M0)

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.775*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,4.09*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,4.79*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.115*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,1.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(5.775*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(4.93*tp,0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(4.29*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(0.025*tp,1.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(0.93*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(0.03*tp,0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(1.845*tp,0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(5.93*tp,0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(6.93*tp,0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(3.015*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(5.055*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(3.835*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(6.125*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(6.735*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(6.77*tp,1.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(3.125*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(2.745*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(2.08*tp,4.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(1.93*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(0.845*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(2.125*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(1.775*tp,4.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(0.125*tp,4.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(0.025*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(3.735*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(3.735*tp,0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(7.835*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(7.835*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(4.77*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(4.09*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(5.09*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(7.735*tp,4.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(5.045*tp,3.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(4.775*tp,3.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(3.125*tp,0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m45,midpoint=(1.085*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(0.665*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(2.665*tp,2.095*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(1.665*tp,2.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(0.665*tp,4.085*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(1.665*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(2.665*tp,1.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(1.665*tp,1.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(1.665*tp,1.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(0.665*tp,1.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(0.665*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(0.665*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(1.665*tp,5.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(0.665*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(1.665*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m90,midpoint=(1.665*tp,0.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.m135,midpoint=(4.715*tp,2.665*tp))

        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(3.415*tp,3.415*tp),alias="via1")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(3.915*tp,1.415*tp),alias="via2")
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_175(),transformation=sc.r90,midpoint=(1.55*tp,4.5*tp),alias="bias1")
        elems += spira.SRef(sc.ls_ib_175(),transformation=sc.r90,midpoint=(7.455*tp,4.5*tp),alias="bias6")
        elems += spira.SRef(sc.ls_ib_175(),transformation=sc.r90,midpoint=(2.43*tp,1.5*tp),alias="bias5")
        elems += spira.SRef(sc.ls_ib_175(),transformation=sc.r90,midpoint=(6.44*tp,6.5*tp),alias="bias2")
        elems += spira.SRef(sc.ls_ib_142(),transformation=sc.r90,midpoint=(6.955*tp,5.5*tp),alias="bias4")
        elems += spira.SRef(sc.ls_ib_304(),transformation=sc.r90,midpoint=(1.135*tp,0.5*tp),alias="bias3")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_152_s(),midpoint=(4.5*tp,1.5*tp),alias="J10")
        elems += spira.SRef(sc.ls_jj_228_s(),transformation=sc.r180,midpoint=(4.5*tp,3.5*tp),alias="J7")
        elems += spira.SRef(sc.ls_jj_186_s(),transformation=sc.r90,midpoint=(3.5*tp,4*tp),alias="J6")
        elems += spira.SRef(sc.ls_jj_186_s(),transformation=sc.r180,midpoint=(3*tp,3.5*tp),alias="J3")
        elems += spira.SRef(sc.ls_jj_222_sg(),midpoint=(2.5*tp,3.5*tp),alias="J2")
        elems += spira.SRef(sc.ls_jj_222_sg(),transformation=sc.r270,midpoint=(3.5*tp,4.5*tp),alias="J5")
        elems += spira.SRef(sc.ls_jj_209_sg(),transformation=sc.r270,midpoint=(5.33*tp,4.45*tp),alias="J8")
        elems += spira.SRef(sc.ls_jj_160_sg(),transformation=sc.r180,midpoint=(5.5*tp,1.5*tp),alias="J11")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(3.5*tp,1.5*tp),alias="J9")
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r180,midpoint=(3.5*tp,5.5*tp),alias="J4")
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r270,midpoint=(1.5*tp,3.5*tp),alias="J1")
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r90,midpoint=(6.505*tp,3.5*tp),alias="J12")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 8):
                if (x in [1,2] and y in [1,2,3,4,5]) or (x in [4,5,6]):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                elif (x == 0 and y == 0) or (x == 3 and y in [4,5,6]) or (x == 7 and y != 5):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                else:
                    pass
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 8):
                if (x == 0 and y in [1,5]) or (x == 1 and y == 0) or (x == 3 and y == 2) or (x == 7 and y == 5):
                    elems += spira.SRef(sc.ls_tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
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