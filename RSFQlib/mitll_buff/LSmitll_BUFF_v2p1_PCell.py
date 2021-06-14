
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

## Parameterization
# Trackpitch in microns
tp = 10

# Inductor widths
Scaling = (1+(tp-10)*0.25)
L1_width = 0.25*tp*Scaling
L2_width = 0.13*tp*Scaling
L3_width = 0.2*tp*Scaling
LJ3_width = 0.16*tp*Scaling
L4_width = 0.2*tp*Scaling
L5_width = 0.25*tp*Scaling
LB_width = 0.14*tp*Scaling
LB3_width = 0.16*tp*Scaling

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
    __name_prefix__ = "LSmitll_BUFF_v2p1"
    def create_elements(self, elems):
        IXports = spira.SRef(IX_ports())
        M6Strips = spira.SRef(M6_strips())
        M0tracks = spira.SRef(M0_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        M0blocks = spira.SRef(M0_blocks())
        tblocks = spira.SRef(trackblocks())
        elems += [IXports, M6Strips, M0tracks,
                  jjfill, M4M5M6M7conns, bias, jjs, M0blocks, tblocks]
        # Ports
        # Bias1
        PB1N = spira.Port(name="PB1N",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name="PB1S",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias2
        PB2N = spira.Port(name="PB2N",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name="PB2S",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias3
        PB3E = spira.Port(name="PB3E",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3W = spira.Port(name="PB3W",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias4
        PB4N = spira.Port(name="PB4N",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name="PB4S",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Ends
        PB1_4_end = spira.Port(name="PB1_4_end",midpoint=(0.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PB2_end = spira.Port(name="PB2_end",midpoint=(0.5*tp,4.5*tp),process=spira.RDD.PROCESS.M6)
        PB3_end = spira.Port(name="PB3_end",midpoint=(4.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        # JJ1
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ2
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ3
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ3_L = spira.Port(name="PJ3",midpoint=(4.5*tp,4.5*tp),process=spira.RDD.PROCESS.M6)
        # JJ4
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pins
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(1.5*tp,3.8975*tp),(1.6*tp,3.8975*tp),(1.6*tp,4.25675*tp),(1.405*tp,4.2675*tp),(1.405*tp,4.7225*tp),(1.6*tp,4.7225*tp),(1.6*tp,5.0925*tp),(1.5*tp,5.0925*tp)],start_straight=False,end_straight=False,width=L2_width,layer=M6)
        L3 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(2.5*tp,5.5*tp),(2.5*tp,6.5*tp),(3.5*tp,6.5*tp)],start_straight=False,end_straight=False,width=L3_width,layer=M6)
        LJ3 = spira.RoutePath(port1=PJ3,port2=PJ3_L,path=[(4.5*tp,5.5*tp)],start_straight=False,end_straight=False,width=LJ3_width,layer=M6)
        L4 = spira.RoutePath(port1=PJ3,port2=PJ4,path=[(3.5*tp,4.5*tp),(2.5*tp,4.5*tp),(2.5*tp,3.5*tp)],start_straight=False,end_straight=False,width=L4_width,layer=M6)
        L5 = spira.RoutePath(port1=PJ4,port2=PQ,path=[((PJ4.x+PQ.x)/2,(PJ4.y+PQ.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.height,layer=M6)
        L5_post = spira.RoutePath(port1=PJ4,port2=PQ_post,path=[((PJ4.x+PQ_post.x)/2,(PJ4.y+PQ_post.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=M6)
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1N,path=[((PJ1.x+PB1N.x)/2,(PJ1.y+PB1N.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=M6)
        LB1_2 = spira.RoutePath(port1=PB1S,port2=PB1_4_end,path=[(1.5*tp,0.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=M6)
        LB2_1 = spira.RoutePath(port1=PJ2,port2=PB2N,path=[(1.5*tp,6.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=M6)
        LB2_2 = spira.RoutePath(port1=PB2S,port2=PB2_end,path=[((PB2S.x+PB2_end.x)/2,(PB2S.y+PB2_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=M6)
        LB3_1 = spira.RoutePath(port1=PB3E,port2=PB3_end,path=[((PB3E.x+PB3_end.x)/2,(PB3E.y+PB3_end.y)/2)],start_straight=False,end_straight=False,width=LB3_width,layer=M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PB1_4_end,path=[((PB3W.x+PB1_4_end.x)/2,(PB3W.y+PB1_4_end.y)/2)],start_straight=False,end_straight=False,width=LB3_width,layer=M6)
        LB4_1 = spira.RoutePath(port1=PJ4,port2=PB4N,path=[(3.5*tp,2.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=M6)
        LB4_2 = spira.RoutePath(port1=PB4S,port2=PB1_4_end,path=[(2.5*tp,0.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=M6)
        elems += [L1, L1_post, L2, L3, L4, L5, L5_post,
                  LJ3, LB1_1, LB1_2, LB2_1,
                  LB2_2, LB3_1, LB3_2, LB4_1, LB4_2]
        # Text Labels
        elems += spira.Label(text="bias_out",position=(5*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(2.495*tp,2.5075*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(3.4875*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(3.96*tp,0.5025*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(3.495*tp,5.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(0.5*tp,6.5025*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(1.505*tp,5.4975*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.5*tp,2.4075*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.5*tp,3.5025*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(0*tp,3.5*tp),layer=TEXT)
        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(4.9875*tp,4.4925*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(4.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(4.9875*tp,0.4925*tp))
        elems += spira.Box(layer=M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,4.4925*tp))
        elems += spira.Box(layer=M6,width=0.315*tp,height=0.025*tp,center=(0.5*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(4.9875*tp,4.4925*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(4.4925*tp,0.0125*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(4.9875*tp,0.4925*tp))
        elems += spira.Box(layer=M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,4.4925*tp))
        elems += spira.Box(layer=M5,width=0.315*tp,height=0.025*tp,center=(0.5*tp,0.0125*tp))

        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(5*tp,3.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,6.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.5*tp,2.407*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,2.502*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.96*tp,0.5*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Box(layer=M0,width=5*tp,height=0.3*tp,center=(2.5*tp,6.5*tp))
        elems += spira.Box(layer=M0,width=0.25*tp,height=6.0*tp,center=(0.5*tp,3.5*tp))
        elems += spira.Box(layer=M0,width=0.2*tp,height=4.0*tp,center=(4.5*tp,2.5*tp))
        elems += spira.Box(layer=M0,width=0.04*tp,height=4.75*tp,center=(4.02*tp,2.5*tp))
        elems += spira.Box(layer=M0,width=0.75*tp,height=0.04*tp,center=(4.5*tp,4.98*tp))
        elems += spira.Box(layer=M0,width=3.75*tp,height=0.04*tp,center=(3.0*tp,6.02*tp))
        elems += spira.Box(layer=M0,width=0.04*tp,height=5.75*tp,center=(0.98*tp,3.0*tp))
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding 3um junction fill.\n")
        elems += spira.SRef(ls_FakeJJ_3umx3um(), midpoint=(0.5*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(), midpoint=(0.5*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(), midpoint=(3.5*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(), midpoint=(4.5*tp,1.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(), midpoint=(4.5*tp,2.5*tp))
        elems += spira.SRef(ls_FakeJJ_3umx3um(), midpoint=(4.5*tp,6.5*tp))
        sys.stdout.write("Adding 1.5um junction fill.\n")
        for y in range(1, 7):
            for x in range(1, 5):
                elems += spira.SRef(ls_FakeJJ_1p5umx1p5um(), midpoint=(0.0+x*tp,0.0+y*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        T90 = spira.Rotation(90)
        T180 = spira.Rotation(180)
        T270 = spira.Rotation(270)
        M45 = T270 + spira.Reflection(True)
        M90 = T180 + spira.Reflection(True)
        M135 = T90 + spira.Reflection(True)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,3.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,4.015*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.025*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.845*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.735*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.335*tp,1.93*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.335*tp,3.125*tp))

        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.805*tp,2.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.93*tp,1.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.735*tp,1.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.025*tp,0.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.93*tp,2.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.93*tp,1.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.125*tp,1.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.125*tp,2.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.835*tp,0.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.93*tp,6.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.735*tp,4.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.015*tp,4.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(4.835*tp,4.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.025*tp,4.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.93*tp,6.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.93*tp,4.335*tp),transformation=M45)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.93*tp,4.335*tp),transformation=M45)
        
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.665*tp,2.125*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(3.665*tp,6.735*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.125*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.665*tp,2.735*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.665*tp,6.735*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(1.665*tp,6.735*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.665*tp,6.735*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.735*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.665*tp,5.125*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.665*tp,4.015*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(0.665*tp,0.845*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.66*tp,4.735*tp),transformation=M90)
        elems += spira.SRef(ls_conn_M4M5M6M7(),midpoint=(2.665*tp,3.125*tp),transformation=M90)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(ls_ib_175(),midpoint=(2.5*tp,1.55*tp),alias="bias4")
        elems += spira.SRef(ls_ib_175(),midpoint=(1.5*tp,1.455*tp),alias="bias1")
        elems += spira.SRef(ls_ib_150(),midpoint=(0.5*tp,5.405*tp),alias="bias2")
        elems += spira.SRef(ls_ib_150(),midpoint=(4.015*tp,0.5*tp),transformation=spira.Rotation(90),alias="bias3")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(ls_jj_250_sg(),midpoint=(1.5*tp,3.5*tp),transformation=spira.Rotation(270),alias="J1")
        elems += spira.SRef(ls_jj_250_sg(),midpoint=(1.5*tp,5.5*tp),transformation=spira.Rotation(90),alias="J2")
        elems += spira.SRef(ls_jj_250_sg(),midpoint=(3.5*tp,5.5*tp),transformation=spira.Rotation(90),alias="J3")
        elems += spira.SRef(ls_jj_250_sg(),midpoint=(3.5*tp,3.5*tp),alias="J4")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 5):
                if (x in range(1,4) and y in range(0,6)):
                    elems += spira.SRef(ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                elif (x == 4 and y == 5):
                    elems += spira.SRef(ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 5):
                if ((x in [0,4]) and (y in [0,4])):
                    elems += spira.SRef(ls_tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(ls_tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(ls_tr_M7(),midpoint=(0+x*tp,0+y*tp))
        return elems

# 1.5um junction fill cell
class ls_FakeJJ_1p5umx1p5um(spira.Device):
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