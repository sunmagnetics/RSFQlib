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
L2_width = 0.13*tp*Scaling
L3_width = 0.185*tp*Scaling
L4_width = 0.21*tp*Scaling
L5_width = L1_width
L6_width = L4_width
L7_width = L1_width
LB_width = 0.16*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_SPLIT_v2p1"
    def create_elements(self, elems):
        IXports = spira.SRef(IX_ports())
        M0tracks = spira.SRef(M0_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        M0blocks = spira.SRef(M0_blocks())
        tblocks = spira.SRef(trackblocks())
        elems += [IXports, M0tracks, jjfill, M4M5M6M7conns, bias, jjs, M0blocks, tblocks]
        # Ports for inductor connections
        # Bias1
        PB1N = spira.Port(name="PB1N",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name="PB1S",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias2
        PB2W = spira.Port(name="PB2W",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2E = spira.Port(name="PB2E",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias3
        PB3N = spira.Port(name="PB3N",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name="PB3S",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias4
        PB4W = spira.Port(name="PB4W",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4E = spira.Port(name="PB4E",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Ends
        PB1_3_end = spira.Port(name="PB1_3_end",midpoint=(1.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PB2_4_end = spira.Port(name="PB2_4_end",midpoint=(1.5*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # JJ1
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ2
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ3
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ4
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pins
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PQ0 = spira.Port(name="PQ0",midpoint=IXports.reference.elements['Q0'].center,process=spira.RDD.PROCESS.M6)
        PQ0_post = spira.Port(name="PQ0_post",midpoint=IXports.reference.elements['Q0'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PQ1 = spira.Port(name="PQ1",midpoint=IXports.reference.elements['Q1'].center,process=spira.RDD.PROCESS.M6)
        PQ1_post = spira.Port(name="PQ1_post",midpoint=IXports.reference.elements['Q1'].center+(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PN7 = spira.Port(name="PN7",midpoint=(PJ3.x,PJ2.y),process=spira.RDD.PROCESS.M6)
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(PJ2.x,PJ1.y)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PJ2,port2=PN7,path=[((PJ2.x+PN7.x)/2,(PJ2.y+PN7.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PJ3,port2=PN7,path=[((PJ3.x+PN7.x)/2,(PJ3.y+PN7.y)/2)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PQ0,port2=PJ3,path=[((PQ0.x+PJ3.x)/2,(PQ0.y+PJ3.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q0'].bbox_info.height,layer=sc.M6)
        L5_post = spira.RoutePath(port1=PQ0_post,port2=PJ3,path=[((PQ0_post.x+PJ3.x)/2,(PQ0_post.y+PJ3.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        L6 = spira.RoutePath(port1=PJ4,port2=PN7,path=[((PJ4.x+PN7.x)/2,(PJ4.y+PN7.y)/2)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M6)
        L7 = spira.RoutePath(port1=PQ1,port2=PJ4,path=[((PQ1.x+PJ4.x)/2,(PQ1.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q1'].bbox_info.width,layer=sc.M6)
        L7_post = spira.RoutePath(port1=PQ1_post,port2=PJ4,path=[((PQ1_post.x+PJ4.x)/2,(PQ1_post.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M6)
        
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1S,path=[((PJ1.x+PB1S.x)/2,(PJ1.y+PB1S.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1N,port2=PB1_3_end,path=[((PB1N.x+PB1_3_end.x)/2,(PB1N.y+PB1_3_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ2,port2=PB2E,path=[((PJ2.x+PB2E.x)/2,(PJ2.y+PB2E.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2W,port2=PB2_4_end,path=[(PB2_4_end.x,PB2W.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ3,port2=PB3S,path=[((PJ3.x+PB3S.x)/2,(PJ3.y+PB3S.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3N,port2=PB1_3_end,path=[(PB3N.x,PB1_3_end.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ4,port2=PB4E,path=[((PJ4.x+PB4E.x)/2,(PJ4.y+PB4E.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4W,port2=PB2_4_end,path=[((PB4W.x+PB2_4_end.x)/2,(PB4W.y+PB2_4_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        elems += [L1, L1_post, L2, L3, L4, L5, L5_post, 
                  L6, L7, L7_post] 
        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2,
                  LB4_1, LB4_2]
        # Text Labels
        elems += spira.Label(text='P3 M6 M4',position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text='PB4 M6 M4',position=(3.065*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='J4 M6 M5',position=(3.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='P2 M6 M4',position=(5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='PB3 M6 M4',position=(3.5*tp,4.54*tp),layer=TEXT)
        elems += spira.Label(text='J3 M6 M5',position=(3.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='PB2 M6 M4',position=(2.09*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text='J2 M6 M5',position=(2.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text='PB1 M6 M4',position=(1.5*tp,3.965*tp),layer=TEXT)
        elems += spira.Label(text='J1 M6 M5',position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='P1 M6 M4',position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='bias_in',position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='bias_out',position=(5*tp,6.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.152*tp,6.57*tp),layer=spira.Layer(number=1,datatype=1))
        elems += spira.Label(text='GND',position=(0.495*tp,6.849*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='a',position=(0.004*tp,3.406*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q0',position=(4.995*tp,3.407*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q1',position=(3.406*tp,0.006*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.503*tp,4.407*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(1.815*tp,2.509*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(3.495*tp,5.03*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB4',position=(2.635*tp,1.497*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB1',position=(1.505*tp,3.208*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(2.5*tp,2.202*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(3.206*tp,3.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB4',position=(3.788*tp,1.513*tp),layer=spira.Layer(number=52,datatype=1))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(5.0*tp,3.5*tp),alias='Q0')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,0.0*tp),alias='Q1')

        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(1.5*tp,3.965*tp))
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(2.09*tp,2.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(3.5*tp,4.545*tp))
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(3.065*tp,1.5*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M0,width=5.0*tp,height=0.3*tp,center=(2.5*tp,6.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.3*tp,height=5.0*tp,center=(1.5*tp,4.0*tp))

        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(1.02*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(1.98*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(0.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(1.5*tp,1.02*tp))
        elems += spira.Box(layer=sc.M0,width=2.75*tp,height=0.04*tp,center=(3.5*tp,6.02*tp))

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,4.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,4.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(-0.665*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(-0.665*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,5.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,4.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,2.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,2.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,4.04*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,4.855*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(0.93*tp,6.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(1.735*tp,4.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(1.125*tp,4.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.735*tp,4.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(1.93*tp,6.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.125*tp,0.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(0.93*tp,0.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(2.015*tp,4.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(1.015*tp,5.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(4.025*tp,4.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.735*tp,0.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(2.845*tp,4.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(1.93*tp,0.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.845*tp,5.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.735*tp,-0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(1.125*tp,2.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(0.93*tp,1.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.125*tp,4.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(4.015*tp,2.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.93*tp,6.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(2.93*tp,6.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.735*tp,2.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(0.845*tp,2.665*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r270,midpoint=(3.125*tp,-0.335*tp))

        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(3.5*tp,4.49*tp),alias="bias3")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(1.5*tp,3.91*tp),alias="bias1")
        elems += spira.SRef(sc.ls_ib_175(),transformation=sc.r90,midpoint=(3.12*tp,1.5*tp),alias="bias4")
        elems += spira.SRef(sc.ls_ib_280(),transformation=sc.r90,midpoint=(2.145*tp,2.5*tp),alias="bias2")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r90,midpoint=(3.5*tp,3.5*tp),alias="J3")
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r180,midpoint=(1.5*tp,3.5*tp),alias="J1")
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r270,midpoint=(3.5*tp,1.5*tp),alias="J4")
        elems += spira.SRef(sc.ls_jj_300_sg(),transformation=sc.r180,midpoint=(2.5*tp,2.5*tp),alias="J2")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 5):
                if (x == 1 and y > 0):
                    pass
                else:
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(-1, 7):
            for x in range(-1, 6):
                if (x == 1 and y in [1,4]):
                    elems += spira.SRef(sc.ls_tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif (x == -1 and y == 3) or (x == 3 and y == -1) or (x == 5 and y == 3):
                    elems += spira.SRef(sc.ls_tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(sc.ls_tr_M7(),midpoint=(0+x*tp,0+y*tp))
                elif (x in [-1,5]) or y == -1:
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