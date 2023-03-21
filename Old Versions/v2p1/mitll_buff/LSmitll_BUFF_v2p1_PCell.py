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
L2_width = 0.135*tp*Scaling
L3_width = 0.13*tp*Scaling
L4_width = 0.135*tp*Scaling
L5_width = 0.25*tp*Scaling
LB_width = 0.14*tp*Scaling

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
        PB3N = spira.Port(name="PB3N",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name="PB3S",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias4
        PB4N = spira.Port(name="PB4N",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name="PB4S",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Ends
        PB1_4_end = spira.Port(name="PB1_4_end",midpoint=(2.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PB2_3_end = spira.Port(name="PB2_3_end",midpoint=(2.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
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
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(1.5*tp,3.8975*tp),(1.6*tp,3.8975*tp),(1.6*tp,4.25675*tp),(1.405*tp,4.2675*tp),
                                                       (1.405*tp,4.7225*tp),(1.6*tp,4.7225*tp),(1.6*tp,5.0925*tp),(1.5*tp,5.0925*tp)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PJ3,port2=PJ2,path=[(3.1025*tp,5.5*tp),(3.1025*tp,5.6*tp),(2.7325*tp,5.6*tp),(2.7325*tp,5.405*tp),
                                                       (2.2775*tp,5.405*tp),(2.2775*tp,5.6*tp),(1.9075*tp,5.6*tp),(1.9075*tp,5.5*tp)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PJ4,port2=PJ3,path=[(3.5*tp,3.8975*tp),(3.6*tp,3.8975*tp),(3.6*tp,4.25675*tp),(3.405*tp,4.2675*tp),
                                                       (3.405*tp,4.7225*tp),(3.6*tp,4.7225*tp),(3.6*tp,5.0925*tp),(3.5*tp,5.0925*tp)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PJ4,port2=PQ,path=[((PJ4.x+PQ.x)/2,(PJ4.y+PQ.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.height,layer=sc.M6)
        L5_post = spira.RoutePath(port1=PJ4,port2=PQ_post,path=[((PJ4.x+PQ_post.x)/2,(PJ4.y+PQ_post.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1N,path=[(PB1N.x,PJ1.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1S,port2=PB1_4_end,path=[(PB1S.x,PB1_4_end.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ2,port2=PB2S,path=[(PB2S.x,PJ2.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PB2_3_end,path=[(PB2N.x,PB2_3_end.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ3,port2=PB3S,path=[(PB3S.x,PJ3.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3N,port2=PB2_3_end,path=[(PB3N.x,PB2_3_end.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ4,port2=PB4N,path=[(PJ4.x,PB4N.x)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4S,port2=PB1_4_end,path=[(PB4S.x,PB1_4_end.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        elems += [L1, L1_post, L2, L3, L4, L5, L5_post,
                  LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2]
        # Text Labels
        elems += spira.Label(text="a",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.5*tp,3.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.5*tp,2.4075*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(1.505*tp,5.4975*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(0.5*tp,5.53*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(3.495*tp,5.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(4.5*tp,5.53*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(3.4875*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(2.495*tp,2.5075*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_out",position=(5*tp,6.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.175*tp,6.5025*tp),layer=spira.Layer(number=1,datatype=1))
        elems += spira.Label(text='GND',position=(0.4925*tp,6.9175*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='RB4',position=(3.2117*tp,3.5043*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(1.4878*tp,5.7862*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(3.509*tp,5.7962*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(0.4954*tp,5.8465*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(4.4983*tp,5.8683*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB1',position=(1.79*tp,3.495*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.5*tp,1.9125*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB4',position=(2.5*tp,2.035*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='a',position=(0.005*tp,3.4075*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q',position=(4.995*tp,3.4075*tp),layer=spira.Layer(number=60,datatype=1))
        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(4.9875*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(2.5075*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(2.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(4.9875*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(2.5075*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(2.4925*tp,0.0125*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(5*tp,3.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,5.53*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,2.502*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.5*tp,2.407*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,5.53*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(2.375*tp,0.5*tp),(2.375*tp,6.5*tp),(2.625*tp,6.5*tp),(2.625*tp,0.5*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,6.35*tp),(0*tp,6.65*tp),(5*tp,6.65*tp),(5*tp,6.35*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(2*tp,0.125*tp),(2*tp,5.875*tp),(2.04*tp,5.875*tp),(2.04*tp,0.125*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(4.125*tp,4.96*tp),(4.125*tp,5*tp),(4.875*tp,5*tp),(4.875*tp,4.96*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.125*tp,6*tp),(0.125*tp,6.04*tp),(1.875*tp,6.04*tp),(1.875*tp,6*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(3.125*tp,6*tp),(3.125*tp,6.04*tp),(4.875*tp,6.04*tp),(4.875*tp,6*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(2.96*tp,0.125*tp),(2.96*tp,5.875*tp),(3*tp,5.875*tp),(3*tp,0.125*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.28*tp,0.28*tp),(0.28*tp,0.72*tp),(0.72*tp,0.72*tp),(0.72*tp,0.28*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0.875*tp),(0*tp,1*tp),(0.125*tp,1*tp),(0.125*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0.875*tp),(0.875*tp,1*tp),(1*tp,1*tp),(1*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0*tp),(0.875*tp,0.125*tp),(1*tp,0.125*tp),(1*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0*tp),(0*tp,0.125*tp),(0.125*tp,0.125*tp),(0.125*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0*tp),(0*tp,0.125*tp),(0.125*tp,0.125*tp),(0.125*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0*tp),(0.875*tp,0.125*tp),(1*tp,0.125*tp),(1*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0.875*tp),(0.875*tp,1*tp),(1*tp,1*tp),(1*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0.875*tp),(0*tp,1*tp),(0.125*tp,1*tp),(0.125*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding 3um junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,3.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,0.5*tp))
        sys.stdout.write("Adding 1.5um junction fill.\n")
        for y in range(1, 7):
            for x in range(1, 5):
                elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(), midpoint=(0.0+x*tp,0.0+y*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.93*tp,1.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.835*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.93*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.93*tp,4.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.93*tp,4.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.93*tp,4.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.93*tp,1.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.93*tp,0.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.845*tp,0.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.93*tp,0.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.125*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.735*tp,5.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.93*tp,4.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.025*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.125*tp,1.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.735*tp,1.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.125*tp,5.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.805*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,6.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,5.055*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,4.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,3.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,6.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,6.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,5.055*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,6.835*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,2.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,2.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,5.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,6.735*tp),transformation=sc.m90)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(2.5*tp,1.55*tp),alias="bias4")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(1.5*tp,1.455*tp),alias="bias1")
        elems += spira.SRef(sc.ls_ib_235(),midpoint=(4.5*tp,5.475*tp),alias="bias3")
        elems += spira.SRef(sc.ls_ib_235(),midpoint=(0.5*tp,5.475*tp),alias="bias2")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(3.5*tp,5.5*tp),alias="J3")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(3.5*tp,3.5*tp),transformation=sc.r90,alias="J4")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,3.5*tp),transformation=sc.r270,alias="J1")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,5.5*tp),alias="J2")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 5):
                if (x != 2):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 5):
                if ((x == 2) and (y in [0,6])):
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