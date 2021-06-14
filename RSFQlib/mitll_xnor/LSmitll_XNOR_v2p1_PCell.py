
import gdspy
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
L2_width = 0.105*tp*Scaling
L3_1_width = 0.265*tp*Scaling
L3_2_width = 0.3*tp*Scaling
L4_width = 0.12*tp*Scaling
L5_width = L1_width
L6_width = L2_width
L7_width = 0.22*tp*Scaling
L8_width = 0.13*tp*Scaling
L9_1_width = 0.3*tp*Scaling
L9_2_width = 0.25*tp*Scaling
L10_width = L1_width
L11_width = 0.175*tp*Scaling
L12_width = 0.1*tp*Scaling
L13_width = 0.3*tp*Scaling
L14_width = 0.18*tp*Scaling
L15_width = 0.22*tp*Scaling
L16_width = 0.195*tp*Scaling
L17_width = 0.125*tp*Scaling
L18_1_width = 0.16*tp*Scaling
L18_2_width = 0.2*tp*Scaling
L19_width = 0.13*tp*Scaling
L20_1_width = 0.22*tp*Scaling
L20_2_width = 0.3*tp*Scaling
L21_width = 0.29*tp*Scaling
L22_width = 0.35*tp*Scaling
L23_width = 0.3*tp*Scaling
L24_width = 0.28*tp*Scaling
L25_width = L1_width
LB1_width = 0.14*tp*Scaling
LB2_width = 0.16*tp*Scaling
LB3_width = 0.18*tp*Scaling


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
    __name_prefix__ = "LSmitll_NOT_v2p1"
    def create_elements(self, elems):
        M1M4M7blocks = spira.SRef(M1M4M7_blocks())
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
        elems += [M1M4M7blocks, M6Strips, IXports, M0tracks, jjfill, M4M5M6M7conns, vias, bias, jjs, M0blocks, tblocks]
        # Ports for inductor connections
        # Bias1
        PB1N = spira.Port(name="PB1N",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name="PB1S",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias2
        PB2W = spira.Port(name="PB2W",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2E = spira.Port(name="PB2E",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias3
        PB3W = spira.Port(name="PB3W",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3E = spira.Port(name="PB3E",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias4
        PB4W = spira.Port(name="PB4W",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4E = spira.Port(name="PB4E",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias5
        PB5N = spira.Port(name="PB5N",midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5S = spira.Port(name="PB5S",midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias6
        PB6N = spira.Port(name="PB6N",midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6S = spira.Port(name="PB6S",midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias7
        PB7E = spira.Port(name="PB7E",midpoint=bias.reference.elements['bias7'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7W = spira.Port(name="PB7W",midpoint=bias.reference.elements['bias7'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias8
        PB8N = spira.Port(name="PB8N",midpoint=bias.reference.elements['bias8'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB8S = spira.Port(name="PB8S",midpoint=bias.reference.elements['bias8'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias9
        PB9E = spira.Port(name="PB9E",midpoint=bias.reference.elements['bias9'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB9W = spira.Port(name="PB9W",midpoint=bias.reference.elements['bias9'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias10
        PB10N = spira.Port(name="PB10N",midpoint=bias.reference.elements['bias10'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB10S = spira.Port(name="PB10S",midpoint=bias.reference.elements['bias10'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # VIA
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV4 = spira.Port(name="PV4",midpoint=vias.reference.elements['via4'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Junctions
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
        # Pins
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center,process=spira.RDD.PROCESS.M6)
        PB_post = spira.Port(name="PB_post",midpoint=IXports.reference.elements['B'].center+(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center,process=spira.RDD.PROCESS.M6)
        PCLK_post = spira.Port(name="PCLK_post",midpoint=IXports.reference.elements['CLK'].center-(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PN25 = spira.Port(name="PN25",midpoint=(6.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PN30 = spira.Port(name="PN30",midpoint=(5.5*tp,3.5*tp),process=spira.RDD.PROCESS.M6)
        PN35 = spira.Port(name="PN35",midpoint=(6.5*tp,3.0*tp),process=spira.RDD.PROCESS.M6)
        # Bias pillars
        PBP1 = spira.Port(name="PBP1",midpoint=(0.5*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        PBP2 = spira.Port(name="PBP2",midpoint=(0.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
        PBP3 = spira.Port(name="PBP3",midpoint=(2.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PBP4 = spira.Port(name="PBP4",midpoint=(2.5*tp,4.5*tp),process=spira.RDD.PROCESS.M6)
        PBP5 = spira.Port(name="PBP5",midpoint=(4.5*tp,2.5*tp),process=spira.RDD.PROCESS.M6)
        PBP6 = spira.Port(name="PBP6",midpoint=(4.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
        PBP7 = spira.Port(name="PBP7",midpoint=(5.5*tp,2.5*tp),process=spira.RDD.PROCESS.M6)
        PBP8 = spira.Port(name="PBP8",midpoint=(9.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PBP9 = spira.Port(name="PBP9",midpoint=(9.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
        ## Inductors
        #L = spira.RoutePath(port1=,port2=,path=[((.x+.x)/2,(.y+.y)/2)],start_straight=False,end_straight=False,width=L_width,layer=M6)
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(1.5*tp,3.2075*tp),(1.6*tp,3.2075*tp),(1.6*tp,3.0*tp),(1.4*tp,3.0*tp),(1.4*tp,2.8*tp),(1.5*tp,2.8*tp)],start_straight=False,end_straight=False,width=L2_width,layer=M6)
        L3_1 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[((PJ2.x+PJ3.x)/2,(PJ2.y+PJ3.y)/2)],start_straight=False,end_straight=False,width=L3_1_width,layer=M6)
        L3_2 = spira.RoutePath(port1=PJ3,port2=PV1,path=[((PJ3.x+PV1.x)/2,(PJ3.y+PV1.y)/2)],start_straight=False,end_straight=False,width=L3_2_width,layer=M5)
        L4 = spira.RoutePath(port1=PV1,port2=PV2,path=[(PV1.x,PV2.y)],start_straight=False,end_straight=False,width=L4_width,layer=M6)
        L5 = spira.RoutePath(port1=PB,port2=PJ4,path=[((PB.x+PJ4.x)/2,(PB.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['B'].bbox_info.width,layer=M6)
        L5_post = spira.RoutePath(port1=PB_post,port2=PJ4,path=[((PB_post.x+PJ4.x)/2,(PB_post.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=M6)
        L6 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(3.792*tp,1.5*tp),(3.7925*tp,1.6*tp),(4.0*tp,1.6*tp),(4.0*tp,1.4*tp),(4.2*tp,1.4*tp),(4.2*tp,1.5*tp)],start_straight=False,end_straight=False,width=L6_width,layer=M6)
        L7_1 = spira.RoutePath(port1=PJ5,port2=PJ6,path=[((PJ5.x+PJ6.x)/2,(PJ5.y+PJ6.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=M6)
        L7_2 = spira.RoutePath(port1=PJ6,port2=PBP5,path=[((PJ6.x+PBP5.x)/2,(PJ6.y+PBP5.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=M5)
        L8 = spira.RoutePath(port1=PBP5,port2=PV2,path=[(PV2.x,PBP5.y)],start_straight=False,end_straight=False,width=L8_width,layer=M6)
        L9_1 = spira.RoutePath(port1=PV2,port2=PJ7,path=[((PV2.x+PJ7.x)/2,(PV2.y+PJ7.y)/2)],start_straight=False,end_straight=False,width=L9_1_width,layer=M5)
        L9_2 = spira.RoutePath(port1=PJ7,port2=PJ8,path=[((PJ7.x+PJ8.x)/2,(PJ7.y+PJ8.y)/2)],start_straight=False,end_straight=False,width=L9_2_width,layer=M6)
        L10 = spira.RoutePath(port1=PCLK,port2=PJ9,path=[((PCLK.x+PJ9.x)/2,(PCLK.y+PJ9.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['CLK'].bbox_info.width,layer=M6)
        L10_post = spira.RoutePath(port1=PCLK_post,port2=PJ9,path=[((PCLK_post.x+PJ9.x)/2,(PCLK_post.y+PJ9.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=M6)
        L11 = spira.RoutePath(port1=PJ9,port2=PJ10,path=[(4.5*tp,PJ9.y),(4.5*tp,PJ10.y)],start_straight=False,end_straight=False,width=L11_width,layer=M6)
        L12 = spira.RoutePath(port1=PJ10,port2=PV3,path=[((PJ10.x+PV3.x)/2,(PJ10.y+PV3.y)/2)],start_straight=False,end_straight=False,width=L12_width,layer=M6)
        L13_1 = spira.RoutePath(port1=PV3,port2=PJ11,path=[((PV3.x+PJ11.x)/2,(PV3.y+PJ11.y)/2)],start_straight=False,end_straight=False,width=L13_width,layer=M5)
        L13_2 = spira.RoutePath(port1=PJ11,port2=PJ8,path=[(PJ8.x,PJ11.y)],start_straight=False,end_straight=False,width=L13_width,layer=M6)
        L14 = spira.RoutePath(port1=PV3,port2=PJ12,path=[(PJ12.x,PV3.y)],start_straight=False,end_straight=False,width=L14_width,layer=M6)
        L15 = spira.RoutePath(port1=PJ12,port2=PN25,path=[(PN25.x,PJ12.y)],start_straight=False,end_straight=False,width=L15_width,layer=M6)
        L16 = spira.RoutePath(port1=PN25,port2=PJ13,path=[((PN25.x+PJ13.x)/2,(PN25.y+PJ13.y)/2)],start_straight=False,end_straight=False,width=L16_width,layer=M6)
        L17 = spira.RoutePath(port1=PJ13,port2=PV4,path=[((PJ13.x+PV4.x)/2,(PJ13.y+PV4.y)/2)],start_straight=False,end_straight=False,width=L17_width,layer=M6)
        L18_1 = spira.RoutePath(port1=PJ14,port2=PJ8,path=[((PJ14.x+PJ8.x)/2,(PJ14.y+PJ8.y)/2)],start_straight=False,end_straight=False,width=L18_1_width,layer=M6)
        L18_2 = spira.RoutePath(port1=PJ14,port2=PN30,path=[((PJ14.x+PN30.x)/2,(PJ14.y+PN30.y)/2)],start_straight=False,end_straight=False,width=L18_2_width,layer=M5)
        L19 = spira.RoutePath(port1=PV4,port2=PBP7,path=[(PV4.x,PBP7.y)],start_straight=False,end_straight=False,width=L19_width,layer=M5)
        L20_1 = spira.RoutePath(port1=PN30,port2=PJ15,path=[((PN30.x+PJ15.x)/2,(PN30.y+PJ15.y)/2)],start_straight=False,end_straight=False,width=L20_1_width,layer=M5)
        L20_2 = spira.RoutePath(port1=PJ15,port2=PN35,path=[((PJ15.x+PN35.x)/2,(PJ15.y+PN35.y)/2)],start_straight=False,end_straight=False,width=L20_2_width,layer=M6)
        L21_1 = spira.RoutePath(port1=PN35,port2=PJ16,path=[((PN35.x+PJ16.x)/2,(PN35.y+PJ16.y)/2)],start_straight=False,end_straight=False,width=L21_width,layer=M6)
        L21_2 = spira.RoutePath(port1=PJ16,port2=PV4,path=[((PJ16.x+PV4.x)/2,(PJ16.y+PV4.y)/2)],start_straight=False,end_straight=False,width=L21_width,layer=M5)
        L22 = spira.RoutePath(port1=PBP7,port2=PN30,path=[((PBP7.x+PN30.x)/2,(PBP7.y+PN30.y)/2)],start_straight=False,end_straight=False,width=L22_width,layer=M5)
        L23 = spira.RoutePath(port1=PJ17,port2=PN35,path=[((PJ17.x+PN35.x)/2,(PJ17.y+PN35.y)/2)],start_straight=False,end_straight=False,width=L23_width,layer=M6)
        L24 = spira.RoutePath(port1=PJ17,port2=PJ18,path=[(PJ18.x,PJ17.y)],start_straight=False,end_straight=False,width=L24_width,layer=M6)
        L25 = spira.RoutePath(port1=PQ,port2=PJ18,path=[((PQ.x+PJ18.x)/2,(PQ.y+PJ18.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.height,layer=M6)
        L25_post = spira.RoutePath(port1=PQ_post,port2=PJ18,path=[((PQ_post.x+PJ18.x)/2,(PQ_post.y+PJ18.y)/2)],start_straight=False,end_straight=False,width=L25_width,layer=M6)
        elems += [L1, L1_post, L2, L3_1, L3_2, L4, L5, L5_post, L6, L7_1, L7_2, 
                  L8, L9_1, L9_2, L10, L10_post, L11, L12, L13_1, L13_2, L14,
                  L15, L16, L17, L18_1, L18_2, L19, L20_1, L20_2, L21_1, L21_2,
                  L22, L23, L24, L25, L25_post]

        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1S,path=[(PJ1.x,PB1S.y)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1N,port2=PBP2,path=[((PB1N.x+PBP2.x)/2,(PB1N.y+PBP2.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PV1,port2=PB2E,path=[((PV1.x+PB2E.x)/2,(PV1.y+PB2E.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2W,port2=PBP1,path=[(PB2W.x,PBP1.y)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB3_1 = spira.RoutePath(port1=PJ4,port2=PB3E,path=[((PJ4.x+PB3E.x)/2,(PJ4.y+PB3E.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PBP1,path=[((PB3W.x+PBP1.x)/2,(PB3W.y+PBP1.y)/2)],start_straight=False,end_straight=False,width=LB2_width,layer=M6)
        LB4_1 = spira.RoutePath(port1=PBP1,port2=PB4W,path=[((PBP1.x+PB4W.x)/2,(PBP1.y+PB4W.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB4_2 = spira.RoutePath(port1=PB4E,port2=PBP3,path=[((PB4E.x+PBP3.x)/2,(PB4E.y+PBP3.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB5_1 = spira.RoutePath(port1=PJ9,port2=PB5S,path=[((PJ9.x+PB5S.x)/2,(PJ9.y+PB5S.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB5_2 = spira.RoutePath(port1=PB5N,port2=PBP2,path=[(PB5N.x,PBP2.y)],start_straight=False,end_straight=False,width=LB3_width,layer=M6)
        LB6_1 = spira.RoutePath(port1=PJ10,port2=PB6S,path=[((PJ10.x+PB6S.x)/2,(PJ10.y+PB6S.y)/2)],start_straight=False,end_straight=False,width=LB2_width,layer=M6)
        LB6_2 = spira.RoutePath(port1=PB6N,port2=PBP6,path=[(PB6N.x,PBP6.y)],start_straight=False,end_straight=False,width=LB2_width,layer=M6)
        LB7_1 = spira.RoutePath(port1=PN25,port2=PB7W,path=[(PB7W.x,PN25.y)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB7_2 = spira.RoutePath(port1=PB7E,port2=PBP9,path=[((PB7E.x+PBP9.x)/2,(PB7E.y+PBP9.y)/2)],start_straight=False,end_straight=False,width=LB2_width,layer=M6)
        LB8_1 = spira.RoutePath(port1=PBP2,port2=PB8N,path=[(PB8N.x,PBP2.y)],start_straight=False,end_straight=False,width=LB3_width,layer=M6)
        LB8_2 = spira.RoutePath(port1=PB8S,port2=PBP4,path=[(PB8S.x,5.0*tp),(PBP4.x,5.0*tp)],start_straight=False,end_straight=False,width=LB3_width,layer=M6)
        LB9_1 = spira.RoutePath(port1=PJ17,port2=PB9W,path=[(PB9W.x,PJ17.y)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB9_2 = spira.RoutePath(port1=PB9E,port2=PBP8,path=[((PB9E.x+PBP8.x)/2,(PB9E.y+PBP8.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB10_1 = spira.RoutePath(port1=PJ18,port2=PB10S,path=[((PJ18.x+PB10S.x)/2,(PJ18.y+PB10S.y)/2)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        LB10_2 = spira.RoutePath(port1=PB10N,port2=PBP9,path=[(PB10N.x,PBP9.y)],start_straight=False,end_straight=False,width=LB1_width,layer=M6)
        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2,
                  LB5_1, LB5_2, LB6_1, LB6_2, LB7_1, LB7_2, LB8_1, LB8_2,
                  LB9_1, LB9_2, LB10_1, LB10_2]
        # Text Labels
        elems += spira.Label(text='bias_out',position=(10*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='bias_in',position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='J18 M6 M5',position=(8.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='J17 M6 M5',position=(6.5*tp,1.95*tp),layer=TEXT)
        elems += spira.Label(text='J16 M5 M6',position=(7*tp,3.005*tp),layer=TEXT)
        elems += spira.Label(text='J15 M5 M6',position=(6.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='J14 M6 M5',position=(5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='J13 M6 M5',position=(7.505*tp,5.495*tp),layer=TEXT)
        elems += spira.Label(text='J12 M6 M5',position=(6*tp,4.495*tp),layer=TEXT)
        elems += spira.Label(text='J11 M5 M6',position=(4.5525*tp,4*tp),layer=TEXT)
        elems += spira.Label(text='J10 M6 M5',position=(5*tp,4.495*tp),layer=TEXT)
        elems += spira.Label(text='J9 M6 M5',position=(3.495*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text='J8 M6 M5',position=(4.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='J7 M5 M6',position=(4*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='J6 M6 M5',position=(4.5*tp,2*tp),layer=TEXT)
        elems += spira.Label(text='J5 M6 M5',position=(4.505*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='J4 M6 M5',position=(3.5*tp,1.495*tp),layer=TEXT)
        elems += spira.Label(text='J3 M6 M5',position=(2*tp,2.49*tp),layer=TEXT)
        elems += spira.Label(text='J2 M6 M5',position=(1.505*tp,2.49*tp),layer=TEXT)
        elems += spira.Label(text='J1 M6 M5',position=(1.505*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='PB10 M6 M4',position=(8.5*tp,5*tp),layer=TEXT)
        elems += spira.Label(text='PB9 M6 M4',position=(5.5*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text='PB8 M6 M4',position=(1.505*tp,5.265*tp),layer=TEXT)
        elems += spira.Label(text='PB7 M6 M4',position=(5.5*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='PB6 M6 M4',position=(5*tp,5.485*tp),layer=TEXT)
        elems += spira.Label(text='PB5 M6 M4',position=(2.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text='PB4 M6 M4',position=(1.52*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text='PB3 M6 M4',position=(3.19*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='PB2 M6 M4',position=(2.5*tp,1.825*tp),layer=TEXT)
        elems += spira.Label(text='PB1 M6 M4',position=(0.495*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text='P4 M6 M4',position=(10*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='P3 M6 M4',position=(3.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text='P2 M6 M4',position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text='P1 M6 M4',position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='q',position=(10*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='clk',position=(3.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text='b',position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text='a',position=(0*tp,3.5*tp),layer=TEXT)

        return elems

class M1M4M7_blocks(spira.Cell):
    __name_prefix__ = "M1M4M7_blocks"
    def create_elements(self, elems):
        elems += spira.Polygon(spira.Shape(points=[(5.04*tp,3.72*tp),(5.04*tp,3.875*tp),(5.28*tp,3.875*tp),(5.28*tp,3.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(5.04*tp,3.72*tp),(5.04*tp,3.875*tp),(5.28*tp,3.875*tp),(5.28*tp,3.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(7.72*tp,1.72*tp),(7.72*tp,1.96*tp),(8.28*tp,1.96*tp),(8.28*tp,1.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(7.72*tp,2.04*tp),(7.72*tp,2.16*tp),(8.28*tp,2.16*tp),(8.28*tp,2.04*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,2.04*tp),(6.72*tp,2.16*tp),(7.28*tp,2.16*tp),(7.28*tp,2.04*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,3.72*tp),(4.72*tp,4.28*tp),(4.96*tp,4.28*tp),(4.96*tp,3.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,4.72*tp),(5.72*tp,4.96*tp),(6.28*tp,4.96*tp),(6.28*tp,4.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(1.72*tp,4.875*tp),(1.72*tp,5.125*tp),(2.28*tp,5.125*tp),(2.28*tp,4.875*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,1.72*tp),(5.72*tp,1.96*tp),(6.28*tp,1.96*tp),(6.28*tp,1.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,1.72*tp),(6.72*tp,1.96*tp),(7.28*tp,1.96*tp),(7.28*tp,1.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(5.875*tp,4.72*tp),(5.875*tp,5.28*tp),(6.125*tp,5.28*tp),(6.125*tp,4.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,4.72*tp),(4.875*tp,5.28*tp),(5.125*tp,5.28*tp),(5.125*tp,4.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,5.72*tp),(4.875*tp,6.28*tp),(5.125*tp,6.28*tp),(5.125*tp,5.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(5.875*tp,4*tp),(5.875*tp,4.28*tp),(6.125*tp,4.28*tp),(6.125*tp,4*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,3.875*tp),(5.72*tp,4.125*tp),(6*tp,4.125*tp),(6*tp,3.875*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,3.875*tp),(4.72*tp,4.125*tp),(5.28*tp,4.125*tp),(5.28*tp,3.875*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,4.125*tp),(4.875*tp,4.28*tp),(5.125*tp,4.28*tp),(5.125*tp,4.125*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(3.72*tp,3.875*tp),(3.72*tp,4.125*tp),(4.28*tp,4.125*tp),(4.28*tp,3.875*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(4.8725*tp,2.8225*tp),(4.8725*tp,3.28*tp),(5.125*tp,3.28*tp),(5.125*tp,2.8225*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,1.86*tp),(4.72*tp,2.14*tp),(4.96*tp,2.14*tp),(4.96*tp,1.86*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(1.86*tp,2.72*tp),(1.86*tp,2.96*tp),(2.14*tp,2.96*tp),(2.14*tp,2.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(3.86*tp,3.04*tp),(3.86*tp,3.28*tp),(4.14*tp,3.28*tp),(4.14*tp,3.04*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(1.72*tp,1.72*tp),(1.72*tp,1.96*tp),(2.28*tp,1.96*tp),(2.28*tp,1.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,2.72*tp),(6.72*tp,3.28*tp),(7.28*tp,3.28*tp),(7.28*tp,2.72*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(6.8725*tp,3*tp),(6.8725*tp,3.28*tp),(7.1275*tp,3.28*tp),(7.1275*tp,3*tp)]),layer=M1)
        elems += spira.Polygon(spira.Shape(points=[(5.04*tp,3.72*tp),(5.04*tp,3.875*tp),(5.28*tp,3.875*tp),(5.28*tp,3.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(5.04*tp,3.72*tp),(5.04*tp,3.875*tp),(5.28*tp,3.875*tp),(5.28*tp,3.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(7.72*tp,1.72*tp),(7.72*tp,1.96*tp),(8.28*tp,1.96*tp),(8.28*tp,1.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(7.72*tp,2.04*tp),(7.72*tp,2.16*tp),(8.28*tp,2.16*tp),(8.28*tp,2.04*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,2.04*tp),(6.72*tp,2.16*tp),(7.28*tp,2.16*tp),(7.28*tp,2.04*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,3.72*tp),(4.72*tp,4.28*tp),(4.96*tp,4.28*tp),(4.96*tp,3.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,4.72*tp),(5.72*tp,4.96*tp),(6.28*tp,4.96*tp),(6.28*tp,4.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(1.72*tp,4.875*tp),(1.72*tp,5.125*tp),(2.28*tp,5.125*tp),(2.28*tp,4.875*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,1.72*tp),(5.72*tp,1.96*tp),(6.28*tp,1.96*tp),(6.28*tp,1.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,1.72*tp),(6.72*tp,1.96*tp),(7.28*tp,1.96*tp),(7.28*tp,1.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(5.875*tp,4.72*tp),(5.875*tp,5.28*tp),(6.125*tp,5.28*tp),(6.125*tp,4.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,4.72*tp),(4.875*tp,5.28*tp),(5.125*tp,5.28*tp),(5.125*tp,4.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,5.72*tp),(4.875*tp,6.28*tp),(5.125*tp,6.28*tp),(5.125*tp,5.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(5.875*tp,4*tp),(5.875*tp,4.28*tp),(6.125*tp,4.28*tp),(6.125*tp,4*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,3.875*tp),(5.72*tp,4.125*tp),(6*tp,4.125*tp),(6*tp,3.875*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,3.875*tp),(4.72*tp,4.125*tp),(5.28*tp,4.125*tp),(5.28*tp,3.875*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,4.125*tp),(4.875*tp,4.28*tp),(5.125*tp,4.28*tp),(5.125*tp,4.125*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(3.72*tp,3.875*tp),(3.72*tp,4.125*tp),(4.28*tp,4.125*tp),(4.28*tp,3.875*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(4.8725*tp,2.8225*tp),(4.8725*tp,3.28*tp),(5.125*tp,3.28*tp),(5.125*tp,2.8225*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,1.86*tp),(4.72*tp,2.14*tp),(4.96*tp,2.14*tp),(4.96*tp,1.86*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(1.86*tp,2.72*tp),(1.86*tp,2.96*tp),(2.14*tp,2.96*tp),(2.14*tp,2.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(3.86*tp,3.04*tp),(3.86*tp,3.28*tp),(4.14*tp,3.28*tp),(4.14*tp,3.04*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(1.72*tp,1.72*tp),(1.72*tp,1.96*tp),(2.28*tp,1.96*tp),(2.28*tp,1.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,2.72*tp),(6.72*tp,3.28*tp),(7.28*tp,3.28*tp),(7.28*tp,2.72*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(6.8725*tp,3*tp),(6.8725*tp,3.28*tp),(7.1275*tp,3.28*tp),(7.1275*tp,3*tp)]),layer=M4)
        elems += spira.Polygon(spira.Shape(points=[(5.04*tp,3.72*tp),(5.04*tp,3.875*tp),(5.28*tp,3.875*tp),(5.28*tp,3.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(5.04*tp,3.72*tp),(5.04*tp,3.875*tp),(5.28*tp,3.875*tp),(5.28*tp,3.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(7.72*tp,1.72*tp),(7.72*tp,1.96*tp),(8.28*tp,1.96*tp),(8.28*tp,1.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(7.72*tp,2.04*tp),(7.72*tp,2.16*tp),(8.28*tp,2.16*tp),(8.28*tp,2.04*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,2.04*tp),(6.72*tp,2.16*tp),(7.28*tp,2.16*tp),(7.28*tp,2.04*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,3.72*tp),(4.72*tp,4.28*tp),(4.96*tp,4.28*tp),(4.96*tp,3.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,4.72*tp),(5.72*tp,4.96*tp),(6.28*tp,4.96*tp),(6.28*tp,4.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(1.72*tp,4.875*tp),(1.72*tp,5.125*tp),(2.28*tp,5.125*tp),(2.28*tp,4.875*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,1.72*tp),(5.72*tp,1.96*tp),(6.28*tp,1.96*tp),(6.28*tp,1.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,1.72*tp),(6.72*tp,1.96*tp),(7.28*tp,1.96*tp),(7.28*tp,1.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(5.875*tp,4.72*tp),(5.875*tp,5.28*tp),(6.125*tp,5.28*tp),(6.125*tp,4.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,4.72*tp),(4.875*tp,5.28*tp),(5.125*tp,5.28*tp),(5.125*tp,4.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,5.72*tp),(4.875*tp,6.28*tp),(5.125*tp,6.28*tp),(5.125*tp,5.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(5.875*tp,4*tp),(5.875*tp,4.28*tp),(6.125*tp,4.28*tp),(6.125*tp,4*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,3.875*tp),(5.72*tp,4.125*tp),(6*tp,4.125*tp),(6*tp,3.875*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,3.875*tp),(4.72*tp,4.125*tp),(5.28*tp,4.125*tp),(5.28*tp,3.875*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,4.125*tp),(4.875*tp,4.28*tp),(5.125*tp,4.28*tp),(5.125*tp,4.125*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(3.72*tp,3.875*tp),(3.72*tp,4.125*tp),(4.28*tp,4.125*tp),(4.28*tp,3.875*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(4.8725*tp,2.8225*tp),(4.8725*tp,3.28*tp),(5.125*tp,3.28*tp),(5.125*tp,2.8225*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,1.86*tp),(4.72*tp,2.14*tp),(4.96*tp,2.14*tp),(4.96*tp,1.86*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(1.86*tp,2.72*tp),(1.86*tp,2.96*tp),(2.14*tp,2.96*tp),(2.14*tp,2.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(3.86*tp,3.04*tp),(3.86*tp,3.28*tp),(4.14*tp,3.28*tp),(4.14*tp,3.04*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(1.72*tp,1.72*tp),(1.72*tp,1.96*tp),(2.28*tp,1.96*tp),(2.28*tp,1.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,2.72*tp),(6.72*tp,3.28*tp),(7.28*tp,3.28*tp),(7.28*tp,2.72*tp)]),layer=M7)
        elems += spira.Polygon(spira.Shape(points=[(6.8725*tp,3*tp),(6.8725*tp,3.28*tp),(7.1275*tp,3.28*tp),(7.1275*tp,3*tp)]),layer=M7)
        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(9.9875*tp,6.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,6.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,4.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,1.4925*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(0.5075*tp,6.9875*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(2.5075*tp,0.0125*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(4.5075*tp,6.9875*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(9.5075*tp,6.9875*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(9.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(9.9875*tp,6.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,6.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,4.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,1.4925*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(0.5075*tp,6.9875*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(2.5075*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(4.5075*tp,6.9875*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(9.5075*tp,6.9875*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(9.4925*tp,0.0125*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,0.0*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(10.0*tp,3.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,7.0*tp),alias='CLK')

        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,1.825*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.52*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.19*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.5*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(8.5*tp,5.0*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.502*tp,6.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.0005*tp,5.4845*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,5.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.5*tp,5.265*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,4.5*tp))

        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Polygon(spira.Shape(points=[(2.5*tp,0.435*tp),(2.5*tp,0.635*tp),(4.38*tp,0.635*tp),(4.38*tp,2.505*tp),(4.58*tp,2.505*tp),(4.58*tp,0.435*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.41*tp,2.5*tp),(5.41*tp,4.41*tp),(2.5*tp,4.41*tp),(2.5*tp,4.59*tp),(5.59*tp,4.59*tp),(5.59*tp,2.5*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(0*tp,6.35*tp),(0*tp,6.65*tp),(10*tp,6.65*tp),(10*tp,6.35*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(9.4*tp,0.5*tp),(9.4*tp,6.5*tp),(9.6*tp,6.5*tp),(9.6*tp,0.5*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(0.35*tp,1.5*tp),(0.35*tp,6.5*tp),(0.65*tp,6.5*tp),(0.65*tp,1.5*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(2.28*tp,4.96*tp),(2.28*tp,5*tp),(5.875*tp,5*tp),(5.875*tp,4.96*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(2*tp,4.125*tp),(2*tp,4.875*tp),(2.04*tp,4.875*tp),(2.04*tp,4.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(2.125*tp,4*tp),(2.125*tp,4.04*tp),(4.72*tp,4.04*tp),(4.72*tp,4*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.04*tp,3.72*tp),(5.04*tp,3.875*tp),(5.28*tp,3.875*tp),(5.28*tp,3.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.04*tp,3.72*tp),(5.04*tp,3.875*tp),(5.28*tp,3.875*tp),(5.28*tp,3.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(7.72*tp,2.04*tp),(7.72*tp,2.16*tp),(8.28*tp,2.16*tp),(8.28*tp,2.04*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,2.04*tp),(6.72*tp,2.16*tp),(7.28*tp,2.16*tp),(7.28*tp,2.04*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,2.72*tp),(6.72*tp,3.28*tp),(7.28*tp,3.28*tp),(7.28*tp,2.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,3.72*tp),(4.72*tp,4.28*tp),(4.96*tp,4.28*tp),(4.96*tp,3.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,4.72*tp),(5.72*tp,4.96*tp),(6.28*tp,4.96*tp),(6.28*tp,4.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(1.72*tp,4.875*tp),(1.72*tp,5.125*tp),(2.28*tp,5.125*tp),(2.28*tp,4.875*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,1.72*tp),(5.72*tp,1.96*tp),(6.28*tp,1.96*tp),(6.28*tp,1.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(6.72*tp,1.72*tp),(6.72*tp,1.96*tp),(7.28*tp,1.96*tp),(7.28*tp,1.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(7.72*tp,1.72*tp),(7.72*tp,1.96*tp),(8.28*tp,1.96*tp),(8.28*tp,1.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.875*tp,4.72*tp),(5.875*tp,5.28*tp),(6.125*tp,5.28*tp),(6.125*tp,4.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,4.72*tp),(4.875*tp,5.28*tp),(5.125*tp,5.28*tp),(5.125*tp,4.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,5.72*tp),(4.875*tp,6.125*tp),(5.125*tp,6.125*tp),(5.125*tp,5.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.875*tp,4*tp),(5.875*tp,4.28*tp),(6.125*tp,4.28*tp),(6.125*tp,4*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.72*tp,3.875*tp),(5.72*tp,4.125*tp),(6*tp,4.125*tp),(6*tp,3.875*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,3.875*tp),(4.72*tp,4.125*tp),(5.28*tp,4.125*tp),(5.28*tp,3.875*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,4.125*tp),(4.875*tp,4.28*tp),(5.125*tp,4.28*tp),(5.125*tp,4.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.875*tp,4.125*tp),(4.875*tp,4.28*tp),(5.125*tp,4.28*tp),(5.125*tp,4.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(3.72*tp,3.875*tp),(3.72*tp,4.125*tp),(4.28*tp,4.125*tp),(4.28*tp,3.875*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.8725*tp,2.8225*tp),(4.8725*tp,3.28*tp),(5.125*tp,3.28*tp),(5.125*tp,2.8225*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,1.86*tp),(4.72*tp,2.14*tp),(4.96*tp,2.14*tp),(4.96*tp,1.86*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(1.86*tp,2.72*tp),(1.86*tp,2.96*tp),(2.14*tp,2.96*tp),(2.14*tp,2.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(1.72*tp,1.72*tp),(1.72*tp,1.96*tp),(2.28*tp,1.96*tp),(2.28*tp,1.72*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(3.86*tp,3.04*tp),(3.86*tp,3.28*tp),(4.14*tp,3.28*tp),(4.14*tp,3.04*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(6.8725*tp,3*tp),(6.8725*tp,3.28*tp),(7.1275*tp,3.28*tp),(7.1275*tp,3*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(9*tp,0.125*tp),(9*tp,5.875*tp),(9.04*tp,5.875*tp),(9.04*tp,0.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(1.125*tp,6*tp),(1.125*tp,6.04*tp),(8.875*tp,6.04*tp),(8.875*tp,6*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(0.96*tp,1.125*tp),(0.96*tp,5.875*tp),(1*tp,5.875*tp),(1*tp,1.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(0.125*tp,1*tp),(0.125*tp,1.04*tp),(0.875*tp,1.04*tp),(0.875*tp,1*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(2*tp,0.125*tp),(2*tp,0.875*tp),(2.04*tp,0.875*tp),(2.04*tp,0.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(2.125*tp,0.96*tp),(2.125*tp,1*tp),(3.875*tp,1*tp),(3.875*tp,0.96*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4*tp,1.125*tp),(4*tp,2.875*tp),(4.04*tp,2.875*tp),(4.04*tp,1.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.125*tp,2.96*tp),(4.125*tp,3*tp),(4.8725*tp,3*tp),(4.8725*tp,2.96*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(4.96*tp,0.125*tp),(4.96*tp,2.8225*tp),(5*tp,2.8225*tp),(5*tp,0.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5*tp,2.125*tp),(5*tp,2.8225*tp),(5.04*tp,2.8225*tp),(5.04*tp,2.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.125*tp,2*tp),(5.125*tp,2.04*tp),(5.875*tp,2.04*tp),(5.875*tp,2*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.96*tp,2.125*tp),(5.96*tp,2.875*tp),(6*tp,2.875*tp),(6*tp,2.125*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5.96*tp,3.085*tp),(5.96*tp,3.875*tp),(6*tp,3.875*tp),(6*tp,3.085*tp)]),layer=M0)
        elems += spira.Polygon(spira.Shape(points=[(5*tp,3.28*tp),(5*tp,3.875*tp),(5.04*tp,3.875*tp),(5.04*tp,3.28*tp)]),layer=M0)
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,5.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(9*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.34*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(3.76*tp,4.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,2*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.86*tp,1.48*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.815*tp,1.48*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.58*tp,1.48*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.48*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,3.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,0.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(9.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(5.195*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(3.07*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(6.985*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(1.265*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(8.265*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(8.875*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(4.945*tp,1.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(0.165*tp,1.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(1.875*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(7.265*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(2.195*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(7.945*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(9.975*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(8.875*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(8.265*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(7.875*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(8.265*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(8.875*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(0.165*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(2.155*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(1.875*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(0.265*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(5.07*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(7.345*tp,3.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(2.985*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(4.265*tp,4.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(2.985*tp,0.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(7.915*tp,2.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(0.875*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(3.875*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(4.155*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(3.265*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(2.945*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(5.235*tp,1.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(0.265*tp,5.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r90,midpoint=(0.165*tp,6.335*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r270,midpoint=(3.125*tp,0.665*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=r270,midpoint=(3.735*tp,0.665*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(2.665*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,1.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(4.665*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(4.665*tp,6.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(2.665*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(2.665*tp,0.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,4.08*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(4.665*tp,6.835*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,6.835*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(0.665*tp,3.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(2.665*tp,1.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(1.665*tp,2.06*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(2.665*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(2.665*tp,5.185*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(2.665*tp,4.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(3.665*tp,3.925*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(6.665*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(5.665*tp,5.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(5.665*tp,4.785*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(9.665*tp,6.835*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(5.665*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(9.665*tp,6.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(6.665*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(7.665*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(8.665*tp,6.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),transformation=m90,midpoint=(6.665*tp,6.125*tp))
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(3.415*tp,3.415*tp),alias="via2")
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(7.415*tp,2.915*tp),alias="via4")
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(2.415*tp,2.405*tp),alias="via1")
        elems += spira.SRef(ls_conn_M5M6(),midpoint=(4.915*tp,3.915*tp),alias="via3")
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_051(),transformation=r90,midpoint=(8.53*tp,0.5*tp),alias="bias9")
        elems += spira.SRef(ls_ib_056(),transformation=r90,midpoint=(8.27*tp,6.5*tp),alias="bias7")
        elems += spira.SRef(ls_ib_153(),transformation=r90,midpoint=(2.555*tp,1.825*tp),alias="bias2")
        elems += spira.SRef(ls_ib_153(),transformation=r270,midpoint=(0.445*tp,0.5*tp),alias="bias4")
        elems += spira.SRef(ls_ib_175(),midpoint=(0.5*tp,4.445*tp),alias="bias1")
        elems += spira.SRef(ls_ib_175(),midpoint=(8.5*tp,4.945*tp),alias="bias10")
        elems += spira.SRef(ls_ib_175(),midpoint=(2.5*tp,5.445*tp),alias="bias5")
        elems += spira.SRef(ls_ib_175(),transformation=r90,midpoint=(3.245*tp,1.5*tp),alias="bias3")
        elems += spira.SRef(ls_ib_248(),midpoint=(1.5*tp,5.21*tp),alias="bias8")
        elems += spira.SRef(ls_ib_260(),midpoint=(5*tp,5.43*tp),alias="bias6")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_095_s(),midpoint=(6.5*tp,3.5*tp),alias="J15")
        elems += spira.SRef(ls_jj_140_sg(),transformation=r180,midpoint=(6.5*tp,1.95*tp),alias="J17")
        elems += spira.SRef(ls_jj_144_s(),midpoint=(7*tp,3*tp),alias="J16")
        elems += spira.SRef(ls_jj_144_s(),transformation=r90,midpoint=(4.555*tp,4*tp),alias="J11")
        elems += spira.SRef(ls_jj_163_s(),transformation=r180,midpoint=(5*tp,3.5*tp),alias="J14")
        elems += spira.SRef(ls_jj_231_s(),transformation=r180,midpoint=(4*tp,3.5*tp),alias="J7")
        elems += spira.SRef(ls_jj_234_s(),midpoint=(2*tp,2.49*tp),alias="J3")
        elems += spira.SRef(ls_jj_234_s(),transformation=r270,midpoint=(4.5*tp,2*tp),alias="J6")
        elems += spira.SRef(ls_jj_250_sg(),midpoint=(3.5*tp,1.5*tp),alias="J4")
        elems += spira.SRef(ls_jj_250_sg(),transformation=r90,midpoint=(8.5*tp,3.5*tp),alias="J18")
        elems += spira.SRef(ls_jj_250_sg(),transformation=r180,midpoint=(3.5*tp,5.5*tp),alias="J9")
        elems += spira.SRef(ls_jj_250_sg(),transformation=r270,midpoint=(1.5*tp,3.5*tp),alias="J1")
        elems += spira.SRef(ls_jj_258_sg(),transformation=r270,midpoint=(5*tp,4.5*tp),alias="J10")
        elems += spira.SRef(ls_jj_260_sg(),midpoint=(6*tp,4.49*tp),alias="J12")
        elems += spira.SRef(ls_jj_266_sg(),transformation=r90,midpoint=(1.5*tp,2.49*tp),alias="J2")
        elems += spira.SRef(ls_jj_266_sg(),transformation=r180,midpoint=(4.5*tp,1.5*tp),alias="J5")
        elems += spira.SRef(ls_jj_271_sg(),midpoint=(7.5*tp,5.5*tp),alias="J13")
        elems += spira.SRef(ls_jj_315_sg(),transformation=r180,midpoint=(4.5*tp,3.5*tp),alias="J8")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 9):
                if (x == 0 and y != 0) or (x in [2,3,4] and y in [0,4]) or (x == 4 and y in [1,2]) or (x == 5 and y in [2,3,4]):
                    pass
                else:
                    elems += spira.SRef(ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 10):
                if (x == 0 and y in [1,6]) or (x == 2 and y in [0,4]) or (x == 4 and y in [2,6]) or (x == 5 and y == 2) or (x  == 9 and y in [0,6]):
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

# Bias 51A cell
class ls_ib_051(spira.Cell):
    __name_prefix__ = 'ls_ib_051'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=3.0825*tp,center=(0.0,1.54125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,3.03*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,3.02875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,3.02875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 56A cell
class ls_ib_056(spira.Cell):
    __name_prefix__ = 'ls_ib_056'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=2.8225*tp,center=(0.0,1.41125*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,2.768*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,2.76875*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,2.76875*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 153uA cell
class ls_ib_153(spira.Cell):
    __name_prefix__ = 'ls_ib_153'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=1.13*tp,center=(0.0,0.565*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,1.075*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,1.07625*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,1.07625*tp),process=spira.RDD.PROCESS.M6)
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

# Bias 248uA cell
class ls_ib_248(spira.Cell):
    __name_prefix__ = 'ls_ib_248'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.755*tp,center=(0.0,0.3775*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.701*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.70125*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.70125*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# Bias 260uA cell
class ls_ib_260(spira.Cell):
    __name_prefix__ = 'ls_ib_260'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=0.115*tp,height=0.7275*tp,center=(0.0,0.36375*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.055*tp))
        elems += spira.Box(layer=C5R,width=0.052*tp,height=0.052*tp,center=(0.0,0.673*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.05375*tp))
        elems += spira.Box(layer=M6,width=0.125*tp,height=0.1275*tp,center=(0.0,0.67375*tp))

        return elems
    def create_ports(self, ports):
        ports += spira.Port(name="PN",midpoint=(0.0,0.67375*tp),process=spira.RDD.PROCESS.M6)
        ports += spira.Port(name="PS",midpoint=(0.0,0.05375*tp),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 95uA shunted cell
class ls_jj_095_s(spira.Cell):
    __name_prefix__ = 'ls_jj_095_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=5.475,center=(0.0,3.7375))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,5.94))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.53))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,6.6875))
        elems += spira.Box(layer=M6,width=1.9,height=3.125,center=(0.0,0.6125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,7.35))
        elems += spira.Box(layer=M5,width=1.75,height=5.95,center=(0.0,5.25))
        elems += spira.Box(layer=M5,width=2.2,height=3.375,center=(0.0,0.5875))
        elems += spira.Circle(layer=J5,box_size=(1.15, 1.15))
        elems += spira.Circle(layer=C5J,box_size=(0.84, 0.84))

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

# JJ 144uA shunted cell
class ls_jj_144_s(spira.Cell):
    __name_prefix__ = 'ls_jj_144_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=4.15,center=(0.0,3.225))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,4.76))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.68))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,5.5125))
        elems += spira.Box(layer=M6,width=2.15,height=3.4,center=(0.0,0.625))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,6.175))
        elems += spira.Box(layer=M5,width=1.75,height=4.625,center=(0.0,4.7375))
        elems += spira.Box(layer=M5,width=2.45,height=3.65,center=(0.0,0.6))
        elems += spira.Circle(layer=J5,box_size=(1.4, 1.4))
        elems += spira.Circle(layer=C5J,box_size=(1.1, 1.1))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 163uA shunted cell
class ls_jj_163_s(spira.Cell):
    __name_prefix__ = 'ls_jj_163_s'
    def create_elements(self, elems):
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

# JJ 231uA shunted cell
class ls_jj_231_s(spira.Cell):
    __name_prefix__ = 'ls_jj_231_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=R5,width=1.15,height=3.2,center=(0.0,2.9))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.84))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.95))
        elems += spira.Box(layer=M6,width=2.5,height=3.725,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.7125))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.375))
        elems += spira.Box(layer=M5,width=2.8,height=3.975,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.675,center=(0.0,4.4125))
        elems += spira.Circle(layer=J5,box_size=(1.75, 1.75))
        elems += spira.Circle(layer=C5J,box_size=(1.46, 1.46))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 234uA shunted cell
class ls_jj_234_s(spira.Cell):
    __name_prefix__ = 'ls_jj_234_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.35))
        elems += spira.Box(layer=M6,width=2.5,height=3.725,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6875))
        elems += spira.Box(layer=M5,width=2.8,height=3.975,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.65,center=(0.0,4.4))
        elems += spira.Box(layer=R5,width=1.15,height=3.175,center=(0.0,2.8875))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,1.84))
        elems += spira.Box(layer=C5R,width=0.52,height=0.52,center=(0.0,3.94))
        elems += spira.Circle(layer=J5,box_size=(1.76, 1.76))
        elems += spira.Circle(layer=C5J,box_size=(1.46, 1.46))

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

# JJ 258uA shunted and grounded cell
class ls_jj_258_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_258_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,4.95))
        elems += spira.Box(layer=M6,width=2.6,height=3.825,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6125))
        elems += spira.Box(layer=M5,width=2.9,height=4.075,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.525,center=(0.0,4.3875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.925))
        elems += spira.Box(layer=R5,width=1.1,height=3.05,center=(0.0,2.875))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,1.88))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,3.87))
        elems += spira.Circle(layer=J5,box_size=(1.85, 1.85))
        elems += spira.Circle(layer=C5J,box_size=(1.54, 1.54))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 260uA shunted and grounded cell
class ls_jj_260_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_260_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.0))
        elems += spira.Box(layer=M6,width=2.6,height=3.85,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6625))
        elems += spira.Box(layer=M5,width=2.9,height=4.1,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.425))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.925))
        elems += spira.Box(layer=R5,width=1.15,height=3.075,center=(0.0,2.9125))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,1.91))
        elems += spira.Box(layer=C5R,width=0.58,height=0.52,center=(0.0,3.92))
        elems += spira.Circle(layer=J5,box_size=(1.86, 1.86))
        elems += spira.Circle(layer=C5J,box_size=(1.56, 1.56))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 266uA shunted and grounded cell
class ls_jj_266_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_266_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.0))
        elems += spira.Box(layer=M6,width=2.65,height=3.875,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.45,height=2.75,center=(0.0,4.675))
        elems += spira.Box(layer=M5,width=2.95,height=4.125,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.425))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.95))
        elems += spira.Box(layer=R5,width=1.15,height=3.05,center=(0.0,2.925))
        elems += spira.Box(layer=C5R,width=0.6,height=0.52,center=(0.0,1.92))
        elems += spira.Box(layer=C5R,width=0.6,height=0.52,center=(0.0,3.93))
        elems += spira.Circle(layer=J5,box_size=(1.88, 1.88))
        elems += spira.Circle(layer=C5J,box_size=(1.79, 1.79))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 271uA shunted and grounded cell
class ls_jj_271_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_271_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.0))
        elems += spira.Box(layer=M6,width=2.65,height=3.9,center=(0.0,0.625))
        elems += spira.Box(layer=M6,width=1.45,height=2.775,center=(0.0,4.6875))
        elems += spira.Box(layer=M5,width=2.95,height=4.15,center=(0.0,0.6))
        elems += spira.Box(layer=M5,width=1.75,height=3.55,center=(0.0,4.45))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,2.95))
        elems += spira.Box(layer=R5,width=1.25,height=3.075,center=(0.0,2.9375))
        elems += spira.Box(layer=C5R,width=0.62,height=0.52,center=(0.0,1.93))
        elems += spira.Box(layer=C5R,width=0.62,height=0.52,center=(0.0,3.94))
        elems += spira.Circle(layer=J5,box_size=(1.89, 1.89))
        elems += spira.Circle(layer=C5J,box_size=(1.6, 1.6))
        elems += spira.Box(layer=I5,width=0.7,height=0.7,center=(0.0,5.35))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0,0),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 315uA shunted and grounded cell
class ls_jj_315_sg(spira.Cell):
    __name_prefix__ = 'ls_jj_315_sg'
    def create_elements(self, elems):
        elems += spira.SRef(ls_conn_M5M6M7(), (-0.35,5.05))
        elems += spira.Box(layer=M6,width=2.8,height=4.025,center=(0.0,0.6125))
        elems += spira.Box(layer=M6,width=1.55,height=2.775,center=(0.0,4.7125))
        elems += spira.Box(layer=M5,width=3.1,height=4.275,center=(0.0,0.5875))
        elems += spira.Box(layer=M5,width=1.75,height=3.525,center=(0.0,4.4875))
        elems += spira.Box(layer=I4,width=1,height=1,center=(0.0,3.025))
        elems += spira.Box(layer=R5,width=1.35,height=3.05,center=(0.0,2.975))
        elems += spira.Box(layer=C5R,width=0.8,height=0.52,center=(0.0,1.98))
        elems += spira.Box(layer=C5R,width=0.8,height=0.52,center=(0.0,3.97))
        elems += spira.Circle(layer=J5,box_size=(2.04, 2.04))
        elems += spira.Circle(layer=C5J,box_size=(1.74, 1.74))

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