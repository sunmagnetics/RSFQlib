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
L3_width = 0.105*tp*Scaling
L4_width = 0.105*tp*Scaling
L5_width = 0.14*tp*Scaling
LB1_width = 0.14*tp*Scaling
LB2_width = 0.16*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_JTLT_v2p1"
    def create_elements(self, elems):
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        res = spira.SRef(resistors())
        tblocks = spira.SRef(trackblocks())
        elems += [M6M5Strips, IXports, jjfill, M4M5M6M7conns,
                  vias, bias, jjs, res, tblocks]
        # Bias ports
        PB1W = spira.Port(name='PB1W',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name='PB1E',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2W = spira.Port(name='PB2W',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2E = spira.Port(name='PB2E',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(3.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1W = spira.Port(name='PR1W',midpoint=res.reference.elements['R1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1E = spira.Port(name='PR1E',midpoint=res.reference.elements['R1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Junction ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center+(0,0.25*tp),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=(3.455*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN7 = spira.Port(name="PN7",midpoint=(PJ2.x,PB2W.y),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PA.x,PJ1.y)],width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(2.5*tp,PJ1.y),(2.5*tp,PJ2.y)],width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PJ2,port2=PN7,path=[(1.5*tp,3.18*tp),(1.6*tp,3.18*tp),(1.6*tp,2.98*tp),
                                                       (1.41*tp,2.98*tp),(1.41*tp,2.78*tp),(1.5*tp,2.78*tp)],width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PN7,port2=PJ3,path=[(1.5*tp,2.3*tp),(1.41*tp,2.3*tp),(1.41*tp,2.1*tp),
                                                       (1.6*tp,2.1*tp),(1.6*tp,1.9*tp),(1.5*tp,1.9*tp)],width=L4_width,layer=sc.M6)
        L5_1 = spira.RoutePath(port1=PJ3,port2=PR1W,path=[(PJ3.x,PR1W.y)],width=L5_width,layer=sc.M6)
        L5_2 = spira.RoutePath(port1=PR1E,port2=PQ,path=[(PQ.x,PR1E.y)],width=L5_width,layer=sc.M6)

        elems += [L1, L2, L3, L4, L5_1, L5_2]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1W,path=[(PJ1.x,PB1W.y)],width=LB1_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1E,port2=PV1,path=[(PV1.x,PB1E.y)],width=LB1_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PN7,port2=PB2W,path=[(PN7.x,PB2W.y)],width=LB1_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2E,port2=PV1,path=[(PV1.x,PB2E.y)],width=LB2_width,layer=sc.M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2]

        LBias = spira.RoutePath(port1=PV1,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=sc.M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="P2 M6 M4",position=(2.6235*tp,1.5005*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(1.5025*tp,1.4975*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(2.7165*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(1.5075*tp,3.5025*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.4925*tp,4.4925*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.9615*tp,5.5005*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0.5*tp,5.16*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(0.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(3.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(3.5*tp,7*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(3.5023*tp,6.8261*tp),layer=spira.Layer(number=50,datatype=1))
        elems += spira.Label(text='GND',position=(3.6312*tp,6.8403*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='RIB1',position=(2.6465*tp,5.4861*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(2.9859*tp,2.503*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RD',position=(2.7298*tp,1.5045*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB1',position=(1.5045*tp,4.1879*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(1.2004*tp,3.4995*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(1.2038*tp,1.4977*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='a',position=(0.5007*tp,5.5058*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q',position=(3.5024*tp,1.5016*tp),layer=spira.Layer(number=60,datatype=1))
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(3.9875*tp,1.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(3.9875*tp,1.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(3.23*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(2.81*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(2.39*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.97*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.55*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.13*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,0.71*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,1.13*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,1.55*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,1.97*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,2.39*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,2.81*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(2.39*tp,6.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.97*tp,6.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.55*tp,6.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.13*tp,6.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(0.71*tp,6.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,3.23*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(0.71*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(2.5*tp,6.29*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(1.5*tp,6.29*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(0.5*tp,5.16*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.619*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.717*tp,2.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.963*tp,5.5*tp))
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1.5*tp,6.155*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2.5*tp,6.155*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1.76*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,3.02*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.18*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,0.92*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.92*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.92*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,3.44*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.34*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.76*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.18*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.02*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.6*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.44*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.6*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.18*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1.34*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.34*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.76*tp,0.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,1.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,1.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.825*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,2.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,2.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.0725*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.7725*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,3.785*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,4.0725*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.255*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.975*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.985*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.9025*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.265*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.9025*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.195*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,4.795*tp),transformation=sc.m90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(3.415*tp,6.415*tp),alias='via1')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_112(),midpoint=(3.31*tp,5.5*tp),transformation=sc.r90,alias='bias1')
        elems += spira.SRef(sc.ls_ib_315(),midpoint=(3.26*tp,2.5*tp),transformation=sc.r90,alias='bias2')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_162_sg(),midpoint=(1.5*tp,4.5*tp),transformation=sc.r180,alias='J1')
        elems += spira.SRef(sc.ls_jj_200_sg(),midpoint=(1.5*tp,3.5*tp),transformation=sc.r90,alias='J2')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,1.5*tp),transformation=sc.r90,alias='J3')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_res_1p36(),midpoint=(2.875*tp,1.5*tp),transformation=sc.r90,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 4):
                if (x == 0 and y == 5) or (x == 3 and y == 1):
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