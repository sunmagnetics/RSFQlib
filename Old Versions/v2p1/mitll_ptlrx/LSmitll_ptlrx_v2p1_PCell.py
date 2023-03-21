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
L1_width = 0.16*tp*Scaling
L2_width = 0.095*tp*Scaling
L3_width = 0.22*tp*Scaling
L4_width = 0.25*tp*Scaling
LB1_width = 0.16*tp*Scaling
LB2_width = 0.2*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_PTLRX_v2p1"
    def create_elements(self, elems):
        M0strips = spira.SRef(M0_strips())
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        M0blocks = spira.SRef(M0_blocks())
        tblocks = spira.SRef(trackblocks())
        elems += [M0strips, M6M5Strips, IXports, jjfill, M4M5M6M7conns,
                  bias, jjs, M0blocks, tblocks]
        # Bias ports
        PB1N = spira.Port(name='PB1N',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name='PB1S',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name='PB2N',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name='PB2S',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3N = spira.Port(name='PB3N',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name='PB3S',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias IO Ports
        PBin = spira.Port(name='PBin',midpoint=(3.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PBout = spira.Port(name='PBout',midpoint=(3.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
        # Junction ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center+(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PJ1.x,PA.y)],width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(1.5*tp,4.1575*tp),(1.6*tp,4.1575*tp),(1.6*tp,3.9275*tp),
                                                       (1.4*tp,3.9275*tp),(1.4*tp,3.6975*tp),(1.6*tp,3.6975*tp),
                                                       (1.6*tp,3.4675*tp),(1.4*tp,3.4675*tp),(1.4*tp,3.2375*tp),
                                                       (1.6*tp,3.2375*tp),(1.6*tp,3.0075*tp),(1.5*tp,3.0075*tp)],width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(PJ2.x,1.5*tp),(PJ3.x,1.5*tp)],width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PJ3,port2=PQ,path=[(PJ3.x,PQ.y)],width=IXports.reference.elements['Q'].bbox_info.height,layer=sc.M6)
        L4_post = spira.RoutePath(port1=PJ3,port2=PQ_post,path=[(PJ3.x,PQ_post.y)],width=L4_width,layer=sc.M6)

        elems += [L1, L2, L3, L4, L4_post]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1S,path=[(PB1S.x,PJ1.y)],width=LB1_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1N,port2=PBout,path=[(PB1N.x,PBout.y)],width=LB2_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ2,port2=PB2N,path=[(PB2N.x,PJ2.y)],width=LB1_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2S,port2=PBin,path=[(PB2S.x,PBin.y)],width=LB1_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ3,port2=PB3S,path=[(PJ3.x,PB3S.y)],width=LB1_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3N,port2=PBout,path=[(PB3N.x,PBout.y)],width=LB1_width,layer=sc.M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2]

        # Text Labels
        elems += spira.Label(text='bias_out',position=(4*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='bias_in',position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='a',position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text='PB3 M6 M4',position=(2.5*tp,5*tp),layer=TEXT)
        elems += spira.Label(text='J3 M6 M5',position=(2.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='PB2 M6 M4',position=(0.5*tp,2.005*tp),layer=TEXT)
        elems += spira.Label(text='J2 M6 M5',position=(1.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text='PB1 M6 M4',position=(0.5*tp,5*tp),layer=TEXT)
        elems += spira.Label(text='J1 M6 M5',position=(1.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text='P1 M6 M4',position=(1.5*tp,5.14*tp),layer=TEXT)
        elems += spira.Label(text='P2 M6 M4',position=(4*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='q',position=(4*tp,3.5025*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.3336*tp,6.6186*tp),layer=spira.Layer(number=1,datatype=1))
        elems += spira.Label(text='GND',position=(0.4534*tp,6.7233*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='q',position=(3.9939*tp,3.4062*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='a',position=(1.5022*tp,5.4978*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='RIB1',position=(0.5026*tp,5.5082*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(0.4892*tp,1.4965*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(2.5071*tp,5.4586*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB1',position=(1.81*tp,4.4928*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(1.8067*tp,2.4912*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(2.1925*tp,3.502*tp),layer=spira.Layer(number=52,datatype=1))
        return elems

class M0_strips(spira.Cell):
    __name_prefix__ = "M0_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(3.4*tp,0.5*tp),(3.4*tp,6.5*tp),(3.6*tp,6.5*tp),(3.6*tp,0.5*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,6.35*tp),(0*tp,6.65*tp),(4*tp,6.65*tp),(4*tp,6.35*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,6*tp),(0*tp,6.04*tp),(3*tp,6.04*tp),(3*tp,6*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(3*tp,0.125*tp),(3*tp,6*tp),(3.04*tp,6*tp),(3.04*tp,0.125*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0*tp),(0*tp,0.125*tp),(0.125*tp,0.125*tp),(0.125*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0*tp),(0.875*tp,0.125*tp),(1*tp,0.125*tp),(1*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0.875*tp),(0.875*tp,1*tp),(1*tp,1*tp),(1*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0.875*tp),(0*tp,1*tp),(0.125*tp,1*tp),(0.125*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.28*tp,0.28*tp),(0.28*tp,0.72*tp),(0.72*tp,0.72*tp),(0.72*tp,0.28*tp)])
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

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(3.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(3.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(3.9875*tp,0.5*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(3.9875*tp,6.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(3.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(3.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(3.9875*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(3.9875*tp,6.5*tp))
        
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(4.0*tp,3.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(1.5*tp,5.14*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,5.0*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,2.004*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,5.0*tp))
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,3.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,1.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,4.055*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,4.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.055*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,2.805*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.055*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.985*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.975*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.975*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.245*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.155*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=sc.r90)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_141(),midpoint=(0.5*tp,0.945*tp),alias='bias2')
        elems += spira.SRef(sc.ls_ib_160(),midpoint=(0.5*tp,4.945*tp),alias='bias1')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(2.5*tp,4.945*tp),alias='bias3')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_162_sg(),midpoint=(1.5*tp,4.5*tp),transformation=sc.r270,alias="J1")
        elems += spira.SRef(sc.ls_jj_200_sg(),midpoint=(1.5*tp,2.5*tp),transformation=sc.r270,alias="J2")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(2.5*tp,3.5*tp),transformation=sc.r90,alias="J3")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        for y in range(0, 6):
            for x in range(0, 3):
                if (x == 1 and y == 5):
                    pass
                else:
                    elems += spira.SRef(sc.ls_tr_M0(),midpoint=(0+x*tp,0+y*tp))
        return elems


class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 4):
                if (x == 3 and y in [0,6]):
                    elems += spira.SRef(sc.ls_tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 1 and y == 5):
                    elems += spira.SRef(sc.ls_tr_PTLconnection_M3M6(),midpoint=(0+x*tp,0+y*tp))
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