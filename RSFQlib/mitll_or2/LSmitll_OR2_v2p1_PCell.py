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
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(PJ1.x,2.56*tp),(PJ2.x,2.56*tp)],start_straight=False,end_straight=False,width=L2_width,layer=M6)
        L3_1 = spira.RoutePath(port1=PJ2,port2=PJ3M6,path=[((PJ2.x+PJ3M6.x)/2,(PJ2.y+PJ3M6.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=M6)
        L3_2 = spira.RoutePath(port1=PJ3M5,port2=PV1M5,path=[((PJ3M5.x+PV1M5.x)/2,(PJ3M5.y+PV1M5.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=M5)
        L4 = spira.RoutePath(port1=PB,port2=PJ4,path=[((PB.x+PJ4.x)/2,(PB.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['B'].bbox_info.width,layer=M6)
        L4_post = spira.RoutePath(port1=PB_post,port2=PJ4,path=[((PB_post.x+PJ4.x)/2,(PB_post.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=L4_width,layer=M6)
        L5 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(2.56*tp,PJ4.y),(2.56*tp,PJ5.y)],start_straight=False,end_straight=False,width=L5_width,layer=M6)
        L6_1 = spira.RoutePath(port1=PJ5,port2=PJ6M6,path=[((PJ5.x+PJ6M6.x)/2,(PJ5.y+PJ6M6.y)/2)],start_straight=False,end_straight=False,width=L6_width,layer=M6)
        L6_2 = spira.RoutePath(port1=PJ6M5,port2=PV1M5,path=[((PJ6M5.x+PV1M5.x)/2,(PJ6M5.y+PV1M5.y)/2)],start_straight=False,end_straight=False,width=L6_width,layer=M5)
        L6_3 = spira.RoutePath(port1=PV1M6,port2=PL6,path=[((PV1M6.x+PL6.x)/2,(PV1M6.y+PL6.y)/2)],start_straight=False,end_straight=False,width=LB2_width,layer=M6)
        L7_1 = spira.RoutePath(port1=PV1M5,port2=PJ7M5,path=[((PV1M5.x+PJ7M5.x)/2,(PV1M5.y+PJ7M5.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=M5)
        L7_2 = spira.RoutePath(port1=PJ7M6,port2=PJ8,path=[(PJ7M6.x,PJ8.y)],start_straight=False,end_straight=False,width=L7_width,layer=M6)
        L8 = spira.RoutePath(port1=PJ8,port2=PJ11,path=[(PJ8.x,4.14*tp),(5.4*tp,4.14*tp),(5.4*tp,3.74*tp),(5.6*tp,3.74*tp),(5.6*tp,3.34*tp),(5.4*tp,3.34*tp),(5.4*tp,2.94*tp),
                                                        (5.6*tp,2.94*tp),(5.6*tp,2.54*tp),(5.4*tp,2.54*tp),(5.4*tp,2.14*tp),(5.6*tp,2.14*tp),(5.6*tp,1.84*tp),(5.5*tp,1.84*tp)],start_straight=False,end_straight=False,width=L8_width,layer=M6)
        L9 = spira.RoutePath(port1=PCLK,port2=PJ9,path=[((PCLK.x+PJ9.x)/2,(PCLK.y+PJ9.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['CLK'].bbox_info.width,layer=M6)
        L9_post = spira.RoutePath(port1=PCLK_post,port2=PJ9,path=[((PCLK_post.x+PJ9.x)/2,(PCLK_post.y+PJ9.y)/2)],start_straight=False,end_straight=False,width=L9_width,layer=M6)
        L10_1 = spira.RoutePath(port1=PJ9,port2=PV2M6,path=[((PJ9.x+PV2M6.x)/2,(PJ9.y+PV2M6.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=M6)
        L10_2 = spira.RoutePath(port1=PV2M5,port2=PJ10M5,path=[((PV2M5.x+PJ10M5.x)/2,(PV2M5.y+PJ10M5.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=M5)
        L10_3 = spira.RoutePath(port1=PJ10M6,port2=PJ11,path=[((PJ10M6.x+PJ11.x)/2,(PJ10M6.y+PJ11.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=M6)
        L11 = spira.RoutePath(port1=PJ11,port2=PJ12,path=[(PJ12.x,PJ11.y)],start_straight=False,end_straight=False,width=L11_width,layer=M6)
        L12 = spira.RoutePath(port1=PQ,port2=PJ12,path=[((PQ.x+PJ12.x)/2,(PQ.y+PJ12.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.height,layer=M6)
        L12_post = spira.RoutePath(port1=PQ_post,port2=PJ12,path=[((PQ_post.x+PJ12.x)/2,(PQ_post.y+PJ12.y)/2)],start_straight=False,end_straight=False,width=L12_width,layer=M6)
        
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1E,path=[((PJ1.x+PB1E.x)/2,(PJ1.y+PB1E.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PB1_end,path=[(PB1_end.x,PB1W.y)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PJ4,port2=PB2W,path=[(4.5*tp,PJ4.y),(4.5*tp,PB2W.y)],start_straight=False,end_straight=False,width=LB2_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2E,port2=PB2_4_6_end,path=[(PB2_4_6_end.x,PB2E.y)],start_straight=False,end_straight=False,width=LB2_width,layer=M6)
        LB3_1 = spira.RoutePath(port1=PB5_end,port2=PB3W,path=[(PB5_end.x,PB3W.y)],start_straight=False,end_straight=False,width=LB2_width,layer=M6)
        LB3_2 = spira.RoutePath(port1=PB3E,port2=PB3_end,path=[((PB3E.x+PB3_end.x)/2,(PB3E.y+PB3_end.y)/2)],start_straight=False,end_straight=False,width=LB2_width,layer=M6)
        LB4_1 = spira.RoutePath(port1=PJ8,port2=PB4W,path=[(PJ8.x,PB4W.y)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB4_2 = spira.RoutePath(port1=PB4E,port2=PB2_4_6_end,path=[((PB4E.x+PB2_4_6_end.x)/2,(PB4E.y+PB2_4_6_end.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB5_1 = spira.RoutePath(port1=PJ9,port2=PB5E,path=[((PJ9.x+PB5E.x)/2,(PJ9.y+PB5E.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB5_2 = spira.RoutePath(port1=PB5W,port2=PB5_end,path=[((PB5W.x+PB5_end.x)/2,(PB5W.y+PB5_end.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB6_1 = spira.RoutePath(port1=PJ12,port2=PB6W,path=[((PJ12.x+PB6W.x)/2,(PJ12.y+PB6W.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB6_2 = spira.RoutePath(port1=PB6E,port2=PB2_4_6_end,path=[(PB2_4_6_end.x,PB6E.y)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        elems += [L1, L1_post, L2, L3_1, L3_2, L4, L4_post, 
                  L5, L6_1, L6_2, L6_3, L7_1, L7_2, L8, L9, 
                  L9_post, L10_1, L10_2, L10_3, L11, L12, L12_post] 
        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2,
                  LB4_1, LB4_2, LB5_1, LB5_2, LB6_1, LB6_2]
        elems += spira.Box(layer=M4,width=0.56*tp,height=0.27*tp,center=(3*tp,4*tp))
        elems += spira.Box(layer=M4,width=0.27*tp,height=0.56*tp,center=(3*tp,3*tp))
        elems += spira.Box(layer=M7,width=0.56*tp,height=0.27*tp,center=(3*tp,4*tp))
        elems += spira.Box(layer=M7,width=0.27*tp,height=0.56*tp,center=(3*tp,3*tp))
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

        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.015*tp,1.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.015*tp,0.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,6.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,5.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,5.4925*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(1.5075*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.015*tp,1.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.015*tp,0.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,6.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,5.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,5.4925*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(1.5075*tp,0.0125*tp))
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
        elems += spira.Polygon(shape=spira.Shape(points=[(3.4*tp,0.5*tp),(3.4*tp,2.5*tp),(3.6*tp,2.5*tp),(3.6*tp,0.5*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0*tp,6.35*tp),(0*tp,6.65*tp),(8*tp,6.65*tp),(8*tp,6.35*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.375*tp,1.5*tp),(0.375*tp,6.5*tp),(0.625*tp,6.5*tp),(0.625*tp,1.5*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7.4*tp,5.5*tp),(7.4*tp,6.5*tp),(7.6*tp,6.5*tp),(7.6*tp,5.5*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(1.5*tp,0.4*tp),(1.5*tp,0.6*tp),(3.4*tp,0.6*tp),(3.4*tp,2.5*tp),(3.6*tp,2.5*tp),(3.6*tp,0.4*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,0.125*tp),(7*tp,0.875*tp),(7.04*tp,0.875*tp),(7.04*tp,0.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,1.125*tp),(7*tp,1.875*tp),(7.04*tp,1.875*tp),(7.04*tp,1.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,2.125*tp),(7*tp,2.875*tp),(7.04*tp,2.875*tp),(7.04*tp,2.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,3.125*tp),(7*tp,3.875*tp),(7.04*tp,3.875*tp),(7.04*tp,3.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,4.125*tp),(7*tp,4.875*tp),(7.04*tp,4.875*tp),(7.04*tp,4.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7*tp,5.125*tp),(7*tp,5.875*tp),(7.04*tp,5.875*tp),(7.04*tp,5.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(6.125*tp,6*tp),(6.125*tp,6.04*tp),(6.875*tp,6.04*tp),(6.875*tp,6*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(5.125*tp,6*tp),(5.125*tp,6.04*tp),(5.875*tp,6.04*tp),(5.875*tp,6*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(4.125*tp,6*tp),(4.125*tp,6.04*tp),(4.875*tp,6.04*tp),(4.875*tp,6*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.125*tp,6*tp),(3.125*tp,6.04*tp),(3.875*tp,6.04*tp),(3.875*tp,6*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(2.125*tp,6*tp),(2.125*tp,6.04*tp),(2.875*tp,6.04*tp),(2.875*tp,6*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(1.125*tp,6*tp),(1.125*tp,6.04*tp),(1.875*tp,6.04*tp),(1.875*tp,6*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(1.125*tp,0.96*tp),(1.125*tp,1*tp),(1.875*tp,1*tp),(1.875*tp,0.96*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,5.125*tp),(0.96*tp,5.875*tp),(1*tp,5.875*tp),(1*tp,5.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,4.125*tp),(0.96*tp,4.875*tp),(1*tp,4.875*tp),(1*tp,4.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,3.125*tp),(0.96*tp,3.875*tp),(1*tp,3.875*tp),(1*tp,3.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,2.125*tp),(0.96*tp,2.875*tp),(1*tp,2.875*tp),(1*tp,2.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.96*tp,1.125*tp),(0.96*tp,1.875*tp),(1*tp,1.875*tp),(1*tp,1.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.96*tp,0.125*tp),(3.96*tp,0.875*tp),(4*tp,0.875*tp),(4*tp,0.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.96*tp,1.125*tp),(3.96*tp,1.875*tp),(4*tp,1.875*tp),(4*tp,1.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.96*tp,2.125*tp),(3.96*tp,2.875*tp),(4*tp,2.875*tp),(4*tp,2.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3*tp,2.125*tp),(3*tp,2.875*tp),(3.04*tp,2.875*tp),(3.04*tp,2.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3*tp,1.125*tp),(3*tp,1.875*tp),(3.04*tp,1.875*tp),(3.04*tp,1.125*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(3.125*tp,2.96*tp),(3.125*tp,3*tp),(3.875*tp,3*tp),(3.875*tp,2.96*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(2.125*tp,0.96*tp),(2.125*tp,1*tp),(2.875*tp,1*tp),(2.875*tp,0.96*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(7.125*tp,5*tp),(7.125*tp,5.04*tp),(7.875*tp,5.04*tp),(7.875*tp,5*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(0.125*tp,1*tp),(0.125*tp,1.04*tp),(0.875*tp,1.04*tp),(0.875*tp,1*tp)]),layer=M0)
        elems += spira.Polygon(shape=spira.Shape(points=[(1*tp,0.125*tp),(1*tp,0.875*tp),(1.04*tp,0.875*tp),(1.04*tp,0.125*tp)]),layer=M0)

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,6.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,6.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,6.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.775*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,4.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,4.09*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,4.79*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.115*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,3.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(5.775*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(4.93*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(4.29*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(0.025*tp,1.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(0.93*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(0.03*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(1.845*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(5.93*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(6.93*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(3.015*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(5.055*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(3.835*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(6.125*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(6.735*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(6.77*tp,1.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(3.125*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(2.745*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(2.08*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(1.93*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(0.845*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(2.125*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(1.775*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(0.125*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(0.025*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(3.735*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(3.735*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(7.835*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(7.835*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(4.77*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(4.09*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(5.09*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(7.735*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(5.045*tp,3.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(4.775*tp,3.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(3.125*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m45,midpoint=(1.085*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,5.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(2.665*tp,2.095*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,2.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,4.085*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,4.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(2.665*tp,1.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,1.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,1.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,5.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,3.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,0.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m135,midpoint=(4.715*tp,2.665*tp))

        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(3.415*tp,3.415*tp),alias="via1")
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(3.915*tp,1.415*tp),alias="via2")
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_175(),transformation=r90,midpoint=(1.55*tp,4.5*tp),alias="bias1")
        elems += spira.SRef(ls_ib_175(),transformation=r90,midpoint=(7.455*tp,4.5*tp),alias="bias6")
        elems += spira.SRef(ls_ib_175(),transformation=r90,midpoint=(2.43*tp,1.5*tp),alias="bias5")
        elems += spira.SRef(ls_ib_175(),transformation=r90,midpoint=(6.44*tp,6.5*tp),alias="bias2")
        elems += spira.SRef(ls_ib_142(),transformation=r90,midpoint=(6.955*tp,5.5*tp),alias="bias4")
        elems += spira.SRef(ls_ib_304(),transformation=r90,midpoint=(1.135*tp,0.5*tp),alias="bias3")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_152_s(),midpoint=(4.5*tp,1.5*tp),alias="J10")
        elems += spira.SRef(ls_jj_228_s(),transformation=r180,midpoint=(4.5*tp,3.5*tp),alias="J7")
        elems += spira.SRef(ls_jj_186_s(),transformation=r90,midpoint=(3.5*tp,4*tp),alias="J6")
        elems += spira.SRef(ls_jj_186_s(),transformation=r180,midpoint=(3*tp,3.5*tp),alias="J3")
        elems += spira.SRef(ls_jj_222_sg(),midpoint=(2.5*tp,3.5*tp),alias="J2")
        elems += spira.SRef(ls_jj_222_sg(),transformation=r270,midpoint=(3.5*tp,4.5*tp),alias="J5")
        elems += spira.SRef(ls_jj_209_sg(),transformation=r270,midpoint=(5.33*tp,4.45*tp),alias="J8")
        elems += spira.SRef(ls_jj_160_sg(),transformation=r180,midpoint=(5.5*tp,1.5*tp),alias="J11")
        elems += spira.SRef(ls_jj_250_sg(),midpoint=(3.5*tp,1.5*tp),alias="J9")
        elems += spira.SRef(ls_jj_250_sg(),transformation=r180,midpoint=(3.5*tp,5.5*tp),alias="J4")
        elems += spira.SRef(ls_jj_250_sg(),transformation=r270,midpoint=(1.5*tp,3.5*tp),alias="J1")
        elems += spira.SRef(ls_jj_250_sg(),transformation=r90,midpoint=(6.505*tp,3.5*tp),alias="J12")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 8):
                if (x in [1,2] and y in [1,2,3,4,5]) or (x in [4,5,6]):
                    elems += spira.SRef(ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                elif (x == 0 and y == 0) or (x == 3 and y in [4,5,6]) or (x == 7 and y != 5):
                    elems += spira.SRef(ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
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
                    elems += spira.SRef(ls_tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(ls_tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(ls_tr_M7(),midpoint=(0+x*tp,0+y*tp))
        return elems

# 1.5um junction fill cell
class ls_FakeJJ_1p5x1p5um(spira.Device):
    __name_prefix__ = 'ls_FakeJJ_1p5x1p5um'
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

# Bias 142uA cell
class ls_ib_142(spira.Cell):
    __name_prefix__ = 'ls_ib_142'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,1.15125*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.205*tp,center=(0.0,0.6025*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.151*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.15125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 175uA cell
class ls_ib_175(spira.Cell):
    __name_prefix__ = 'ls_ib_175'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.005*tp,center=(0.0,0.5025*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.952*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,0.95125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.95125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 304uA cell
class ls_ib_304(spira.Cell):
    __name_prefix__ = 'ls_ib_304'
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.125*tp,center=(0.0,0.59*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.6425*tp,center=(0.0,0.32125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.59*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.68*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 152uA shunted cell
class ls_jj_152_s(spira.Cell):
    __name_prefix__ = 'ls_jj_152_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=4.5,center=(0.0,4.65))
        elems += spira.Box(layer=M5,width=2.5,height=3.65,center=(0.0,0.575))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.3625))
        elems += spira.Box(layer=M6,width=2.2,height=3.4,center=(0.0,0.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.025))
        elems += spira.Box(layer=R5,width=1.15,height=4,center=(0.0,3.15))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.62))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.68))
        elems += spira.Circle(layer=C5J,box_size=(1.14, 1.14))
        elems += spira.Circle(layer=J5,box_size=(1.43, 1.43))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 160uA shunted and grounded cell
class ls_jj_160_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_160_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,7.7))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,8.05))
        elems += spira.Box(layer=M6,width=1.8,height=3.05,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,7.3875))
        elems += spira.Box(layer=M5,width=2.1,height=3.3,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=5.5875,center=(0.0,6.675))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.525))
        elems += spira.Box(layer=R5,width=1.15,height=6.2,center=(0.0,4.075))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.51))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,6.64))
        elems += spira.Circle(layer=J5,box_size=(1.06, 1.06))
        elems += spira.Circle(layer=C5J,box_size=(0.76, 0.76))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 186uA shunted cell
class ls_jj_186_s(spira.Cell):
    __name_prefix__ = 'ls_jj_186_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=4.05,center=(0.0,4.525))
        elems += spira.Box(layer=M5,width=2.65,height=3.825,center=(0.0,0.5875))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,5.025))
        elems += spira.Box(layer=M6,width=2.35,height=3.575,center=(0.0,0.6125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.675))
        elems += spira.Box(layer=R5,width=1.15,height=3.55,center=(0.0,3.025))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.28))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.77))
        elems += spira.Circle(layer=C5J,box_size=(1.28, 1.28))
        elems += spira.Circle(layer=J5,box_size=(1.58, 1.58))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 209uA shunted and grounded cell
class ls_jj_209_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_209_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.2))
        elems += spira.Box(layer=M5,width=1.75,height=3.85,center=(0.0,4.475))
        elems += spira.Box(layer=M5,width=2.7,height=3.9,center=(0.0,0.6))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.8625))
        elems += spira.Box(layer=M6,width=2.4,height=3.65,center=(0.0,0.625))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.825))
        elems += spira.Box(layer=R5,width=1.15,height=3.375,center=(0.0,2.9625))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.1))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.82))
        elems += spira.Circle(layer=C5J,box_size=(1.38, 1.38))
        elems += spira.Circle(layer=J5,box_size=(1.67, 1.67))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 222uA shunted and grounded cell
class ls_jj_222_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_222_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.1))
        elems += spira.Box(layer=M5,width=1.75,height=3.725,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.75,height=3.925,center=(0.0,0.5875))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.75))
        elems += spira.Box(layer=M6,width=2.45,height=3.675,center=(0.0,0.6125))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.85))
        elems += spira.Box(layer=R5,width=1.15,height=3.25,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.82))
        elems += spira.Circle(layer=C5J,box_size=(1.42, 1.42))
        elems += spira.Circle(layer=J5,box_size=(1.72, 1.72))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 228uA shunted cell
class ls_jj_228_s(spira.Cell):
    __name_prefix__ = 'ls_jj_228_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=M5,width=1.75,height=3.675,center=(0.0,4.4125))
        elems += spira.Box(layer=M5,width=2.8,height=3.975,center=(0.0,0.5875))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7125))
        elems += spira.Box(layer=M6,width=2.5,height=3.725,center=(0.0,0.6125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.375))
        elems += spira.Box(layer=R5,width=1.15,height=3.2,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.97))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.83))
        elems += spira.Circle(layer=J5,box_size=(1.74, 1.74))
        elems += spira.Circle(layer=C5J,box_size=(1.44, 1.44))

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

# M0 Track block fill cell
class ls_tr_M0(spira.Cell):
    __name_prefix__ = 'ls_tr_M0'
    def create_elements(self, elems):
        elems += spira.Polygon(shape=lowerHalf, layer=M0)
        elems += spira.Polygon(shape=upperHalf, layer=M0)
        elems += spira.Polygon(shape=middleCross, layer=M0)

        return elems

# M7 Track block fill cell
class ls_tr_M7(spira.Cell):
    __name_prefix__ = 'ls_tr_M7'
    def create_elements(self, elems):
        elems += spira.Polygon(shape=lowerHalf, layer=M7)
        elems += spira.Polygon(shape=upperHalf, layer=M7)
        elems += spira.Polygon(shape=middleCross, layer=M7)

        return elems

# Track block with bias pillar cell
class ls_tr_bias_pillar_M0M6(spira.Cell):
    __name_prefix__ = 'ls_tr_bias_pillar_M0M6'
    def create_elements(self, elems):
        # Common shapes
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

        elems += spira.Box(layer=M0,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I0,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.61*tp))
        elems += spira.Box(layer=I0,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.39*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Polygon(shape=top, layer=M1)
        elems += spira.Polygon(shape=bot, layer=M1)
        elems += spira.Box(layer=M1,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=I1,width=0.12*tp,height=0.12*tp,center=(0.61*tp,0.61*tp))
        elems += spira.Box(layer=I1,width=0.12*tp,height=0.12*tp,center=(0.39*tp,0.39*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.44*tp,height=0.44*tp,center=(0.5*tp,0.5*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
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
class ls_tr_u_M4_alt(spira.Cell):
    __name_prefix__ = 'ls_tr_u_M4_alt'
    def create_elements(self, elems):
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M0,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.935*tp))
        elems += spira.Box(layer=I0,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.065*tp))
        elems += spira.Polygon(shape=lowerHalf, layer=M1)
        elems += spira.Polygon(shape=upperHalf, layer=M1)
        elems += spira.Polygon(shape=middleCross, layer=M1)
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.935*tp,0.935*tp))
        elems += spira.Box(layer=I1,width=0.06*tp,height=0.06*tp,center=(0.065*tp,0.065*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.9375*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.9375*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.9375*tp,0.0625*tp))
        elems += spira.Box(layer=M2,width=0.125*tp,height=0.125*tp,center=(0.0625*tp,0.0625*tp))
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