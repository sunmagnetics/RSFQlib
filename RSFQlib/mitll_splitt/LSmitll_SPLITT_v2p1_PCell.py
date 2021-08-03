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
L1_width = 0.145*tp*Scaling
L2_width = 0.115*tp*Scaling
L3_width = 0.145*tp*Scaling
L4_width = 0.1*tp*Scaling
L5_width = 0.2*tp*Scaling
L6_width = 0.14*tp*Scaling
L7_width = 0.2*tp*Scaling
L8_width = 0.14*tp*Scaling
LB1_width = 0.14*tp*Scaling
LB2_width = 0.2*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_SPLITT_v2p1"
    def create_elements(self, elems):
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        M0M4M7tracks = spira.SRef(M0M4M7_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        res = spira.SRef(resistors())
        tblocks = spira.SRef(trackblocks())
        elems += [M6M5Strips, IXports, M0M4M7tracks, jjfill, M4M5M6M7conns,
                  vias, bias, jjs, res, tblocks]
        # Bias ports
        PB1W = spira.Port(name='PB1W',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name='PB1E',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name='PB2N',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name='PB2S',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3N = spira.Port(name='PB3N',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name='PB3S',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(4.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1N = spira.Port(name='PR1N',midpoint=res.reference.elements['R1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1S = spira.Port(name='PR1S',midpoint=res.reference.elements['R1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PR2N = spira.Port(name='PR2N',midpoint=res.reference.elements['R2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR2S = spira.Port(name='PR2S',midpoint=res.reference.elements['R2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Junction ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PQ0 = spira.Port(name="PQ0",midpoint=(1.5*tp,0.55375*tp),process=spira.RDD.PROCESS.M6)
        PQ1 = spira.Port(name="PQ1",midpoint=(3.5*tp,0.55375*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN5 = spira.Port(name="PN5",midpoint=(3.475*tp,PB1W.y),process=spira.RDD.PROCESS.M6)
        PN16 = spira.Port(name="PN16",midpoint=(2.5*tp,3.5*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PA.x,PJ1.y)],width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PN5,path=[(PN5.x,PJ1.y)],width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PN5,port2=PJ2,path=[(PN5.x,PJ2.y)],width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PJ2,port2=PN16,path=[(PJ2.x,4.215*tp),(2.4*tp,4.215*tp),
                                                        (2.4*tp,4.0*tp),(2.6*tp,4.0*tp),
                                                        (2.6*tp,3.8*tp),(PN16.x,3.8*tp)],width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PN16,port2=PJ3,path=[(PJ3.x,PN16.y)],width=L5_width,layer=sc.M6)
        L6_1 = spira.RoutePath(port1=PJ3,port2=PR2N,path=[(PJ3.x,PR2N.y)],width=L6_width,layer=sc.M6)
        L6_2 = spira.RoutePath(port1=PR2S,port2=PQ1,path=[(PR2S.x,PQ1.y)],width=L6_width,layer=sc.M6)
        L7 = spira.RoutePath(port1=PN16,port2=PJ4,path=[(PJ4.x,PN16.y)],width=L7_width,layer=sc.M6)
        L8_1 = spira.RoutePath(port1=PJ4,port2=PR1N,path=[(PJ4.x,PR1N.y)],width=L8_width,layer=sc.M6)
        L8_2 = spira.RoutePath(port1=PR1S,port2=PQ0,path=[(PR1S.x,PQ0.y)],width=L8_width,layer=sc.M6)

        elems += [L1, L2, L3, L4, L5, L6_1, L6_2, L7, L8_1, L8_2]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PN5,port2=PB1W,path=[(PN5.x,PB1W.y)],width=LB1_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1E,port2=PV1,path=[(PV1.x,PB1E.y)],width=LB1_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2S,path=[(PB2S.x,PJ3.y)],width=LB1_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PV1,path=[(PB2N.x,PV1.y)],width=LB1_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ4,port2=PB3S,path=[(PB3S.x,PJ4.y)],width=LB1_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3N,port2=PV1,path=[(PB3N.x,PV1.y)],width=LB1_width,layer=sc.M6)
        
        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2]

        LBias = spira.RoutePath(port1=PV1,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=sc.M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="P1 M6 M4",position=(1.8075*tp,5.4975*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(2.475*tp,5.505*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(3.7505*tp,5.1545*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(2.5125*tp,4.53*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(1.5*tp,2.495*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(0.5*tp,3.465*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(1.501*tp,1.357*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(3.5*tp,1.3525*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(3.5025*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(4.5025*tp,3.465*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="q0",position=(1.5*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text="q1",position=(3.5*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(4.5*tp,7*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='a',position=(1.498*tp,5.504*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q0',position=(1.51*tp,0.488*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q1',position=(3.505*tp,0.496*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='RIB1',position=(4.051*tp,5.154*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(4.498*tp,3.849*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(0.496*tp,3.859*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RD1',position=(1.498*tp,1.255*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RD2',position=(3.5*tp,1.255*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB1',position=(2.47*tp,5.818*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(2.194*tp,4.524*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(3.209*tp,2.501*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB4',position=(1.795*tp,2.496*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='VDD',position=(4.511*tp,6.838*tp),layer=spira.Layer(number=50,datatype=1))
        elems += spira.Label(text='GND',position=(4.639*tp,6.843*tp),layer=spira.Layer(number=40,datatype=1))
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9925*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9925*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.8075*tp,5.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.75*tp,5.155*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.5*tp,1.356*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.5*tp,1.356*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,3.465*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,3.465*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(3.72*tp,5.04*tp),(3.72*tp,5.28*tp),(4.28*tp,5.28*tp),(4.28*tp,5.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,0.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.34*tp,5.7375*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,4.78*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.0775*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.07*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.165*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.165*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.165*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.875*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.975*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.07*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.07*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.07*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.195*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.945*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.975*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.735*tp,5.63*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,4.055*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,3.735*tp),transformation=sc.m90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.415*tp,6.415*tp),alias='via1')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_185(),midpoint=(4.5*tp,3.41*tp),alias='bias2')
        elems += spira.SRef(sc.ls_ib_185(),midpoint=(0.5*tp,3.41*tp),alias='bias3')
        elems += spira.SRef(sc.ls_ib_255(),midpoint=(3.695*tp,5.155*tp),transformation=sc.r270,alias='bias1')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_160_sg(),midpoint=(2.47*tp,5.5*tp),alias='J1')
        elems += spira.SRef(sc.ls_jj_166_sg(),midpoint=(2.51*tp,4.525*tp),transformation=sc.r90,alias='J2')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(3.5*tp,2.5*tp),transformation=sc.r90,alias='J3')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,2.5*tp),transformation=sc.r270,alias='J4')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_res_1p36(),midpoint=(1.5*tp,1.1*tp),alias='R1')
        elems += spira.SRef(sc.ls_res_1p36(),midpoint=(3.5*tp,1.1*tp),alias='R2')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 5):
                if (x == 1 and y in [0,5]) or (x == 3 and y == 0):
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