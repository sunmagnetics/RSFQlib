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
L2_width = 0.12*tp*Scaling
L3_width = 0.11*tp*Scaling
L4_width = 0.1*tp*Scaling
L5_width = 0.25*tp*Scaling
L6_width = 0.15*tp*Scaling
L7_width = 0.25*tp*Scaling
LB_width = 0.16*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_DFF_v2p1"
    def create_elements(self, elems):
        M6strips = spira.SRef(M6_strips())
        IXports = spira.SRef(IX_ports())
        M0tracks = spira.SRef(M0_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7connections = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        M0Blocks = spira.SRef(M0_blocks())
        trblocks = spira.SRef(trackblocks())
        elems += [M6strips, IXports, M0tracks, jjfill, 
                  M4M5M6M7connections, vias, bias, jjs, M0Blocks, trblocks]
        # Ports
        # B1
        PB1E = spira.Port(name="PB1E",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1W = spira.Port(name="PB1W",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # B2
        PB2E = spira.Port(name="PB2E",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2W = spira.Port(name="PB2W",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # B3
        PB3E = spira.Port(name="PB3E",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3W = spira.Port(name="PB3W",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # B4
        PB4N = spira.Port(name="PB4N",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name="PB4S",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # J1
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J2
        PJ2W = spira.Port(name="PJ2W",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ2S = spira.Port(name="PJ2S",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J3
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J4
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J5
        PJ5S = spira.Port(name="PJ5S",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ5W = spira.Port(name="PJ5W",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        # J6
        PJ6 = spira.Port(name="PJ6",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J7
        PJ7 = spira.Port(name="PJ7",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # PA
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        # PCLK
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center,process=spira.RDD.PROCESS.M6)
        PCLK_post = spira.Port(name="PCLK_post",midpoint=IXports.reference.elements['CLK'].center-(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        # PQ
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        # PVA
        PVAM6 = spira.Port(name="PVAM6",midpoint=vias.reference.elements['viaA'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PVAM5 = spira.Port(name="PVAM5",midpoint=vias.reference.elements['viaA'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        # PVCLK
        PVCLKM6 = spira.Port(name="PVCLKM6",midpoint=vias.reference.elements['viaCLK'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PVCLKM5 = spira.Port(name="PVCLKM5",midpoint=vias.reference.elements['viaCLK'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        # Bias ends
        PB1_3_end = spira.Port(name="PB1_3_end",midpoint=(0.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PB2_4_end = spira.Port(name="PB2_4_end",midpoint=(4.5*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2W = spira.RoutePath(port1=PJ1,port2=PVAM6,path=[((PJ1.x+PVAM6.x)/2,(PJ1.y+PVAM6.y)/2)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L2E = spira.RoutePath(port1=PVAM5,port2=PJ2W,path=[((PVAM5.x+PJ2W.x)/2,(PVAM5.y+PJ2W.y)/2)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M5)
        L2S = spira.RoutePath(port1=PJ2S,port2=PJ3,path=[((PJ2S.x+PJ3.x)/2,(PJ2S.y+PJ3.y)/2)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PJ3,port2=PJ4,path=[(3.5*tp,2.5*tp),(3.5*tp,2.9*tp),(3.6*tp,2.9*tp),(3.6*tp,3.3*tp),(3.4*tp,3.3*tp),(3.4*tp,3.7*tp),(3.6*tp,3.7*tp),(3.6*tp,4*tp),(3.5*tp,4*tp)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L4S = spira.RoutePath(port1=PJ4,port2=PJ5S,path=[(3.5*tp,4.8*tp),(3.615*tp,4.8*tp),(3.615*tp,5.0*tp),(3.415*tp,5.0*tp),(3.415*tp,5.2*tp),(3.5*tp,5.2*tp)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L4E = spira.RoutePath(port1=PJ5W,port2=PVCLKM5,path=[((PJ5W.x+PVCLKM5.x)/2,(PJ5W.y+PVCLKM5.y)/2)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M5)
        L4W = spira.RoutePath(port1=PVCLKM6,port2=PJ6,path=[((PVCLKM6.x+PJ6.x)/2,(PVCLKM6.y+PJ6.y)/2)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PCLK,port2=PJ6,path=[((PCLK.x+PJ6.x)/2,(PCLK.y+PJ6.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['CLK'].bbox_info.width,layer=sc.M6)
        L5_post = spira.RoutePath(port1=PCLK_post,port2=PJ6,path=[((PCLK_post.x+PJ6.x)/2,(PCLK_post.y+PJ6.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        L6 = spira.RoutePath(port1=PJ4,port2=PJ7,path=[(4.5*tp,4.5*tp)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M6)
        L7 = spira.RoutePath(port1=PJ7,port2=PQ,path=[((PJ7.x+PQ.x)/2,(PJ7.y+PQ.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.height,layer=sc.M6)
        L7_post = spira.RoutePath(port1=PJ7,port2=PQ_post,path=[((PJ7.x+PQ_post.x)/2,(PJ7.y+PQ_post.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M6)
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1E,path=[((PJ1.x+PB1E.x)/2,(PJ1.y+PB1E.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PB1_3_end,path=[(0.5*tp,4.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2W,path=[(2.5*tp,1.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2E,port2=PB2_4_end,path=[((PB2E.x+PB2_4_end.x)/2,(PB2E.y+PB2_4_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ6,port2=PB3E,path=[((PJ6.x+PB3E.x)/2,(PJ6.y+PB3E.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PB1_3_end,path=[((PB3W.x+PB1_3_end.x)/2,(PB3W.y+PB1_3_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ7,port2=PB4N,path=[((PJ7.x+PB4N.x)/2,(PJ7.y+PB4N.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4S,port2=PB2_4_end,path=[((PB4S.x+PB2_4_end.x)/2,(PB4S.y+PB2_4_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        elems += [L1, L1_post, L2W, L2E, L2S, L3, L4S, L4E, L4W, L5, L5_post, L6, L7, L7_post]
        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2]
        # Text Labels
        elems += spira.Label(text="bias_out",position=(6*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(2.5*tp,7.0*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(6.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(2.85*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(2.025*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(4.5*tp,2.905*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J2 M5 M6",position=(2.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(2.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(3.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="J5 M5 M6",position=(3.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(2.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(4.5*tp,3.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.1525*tp,6.5*tp),layer=spira.Layer(number=1,datatype=1))
        elems += spira.Label(text='GND',position=(0.4975*tp,6.84*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='RB1',position=(1.5*tp,3.2075*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(2.5*tp,3.815*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(2.1725*tp,2.505*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB4',position=(3.19*tp,4.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB5',position=(3.5025*tp,5.83*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB6',position=(2.5*tp,5.225*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB7',position=(4.205*tp,3.4975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.0175*tp,4.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(3.31*tp,1.4975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(1.57*tp,5.4975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB4',position=(4.5*tp,2.405*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='a',position=(0.005*tp,3.4075*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q',position=(5.995*tp,3.4075*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='clk',position=(2.4075*tp,6.995*tp),layer=spira.Layer(number=60,datatype=1))
        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.03*tp,height=0.315*tp,center=(0.015*tp,5.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.03*tp,height=0.315*tp,center=(0.015*tp,5.4925*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(2.5*tp,7.0*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(6.0*tp,3.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(2.025*tp,5.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(1.5*tp,4.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.045*tp,height=0.045*tp,center=(2.8525*tp,1.5025*tp))
        elems += spira.Box(layer=IXPORT,width=0.045*tp,height=0.045*tp,center=(4.5025*tp,2.9075*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M0,width=6*tp,height=0.3*tp,center=(3.0*tp,6.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.2*tp,height=1.0*tp,center=(0.5*tp,6.0*tp))
        elems += spira.Box(layer=sc.M0,width=0.2*tp,height=5.0*tp,center=(4.5*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(0.5*tp,5.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(0.98*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0,width=2.75*tp,height=0.04*tp,center=(2.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(4.02*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(4.5*tp,1.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(4.98*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(5.5*tp,6.02*tp))
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding 3um junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,6.53*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,1.5*tp))
        sys.stdout.write("Adding 1.5um junction fill.\n")
        for y in range(1, 7):
            for x in range(1, 6):
                elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(), midpoint=(0.0+x*tp,0.0+y*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.3350*tp,3.1250*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.3350*tp,5.1250*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.3350*tp,5.7350*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.3350*tp,5.0400*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.3350*tp,4.0300*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.3350*tp,4.8000*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.3350*tp,2.8250*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.3350*tp,0.9300*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.3350*tp,6.0150*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.3350*tp,0.9300*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.3350*tp,4.7650*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.3350*tp,3.7350*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.3350*tp,0.9300*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.3350*tp,0.9300*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.3350*tp,0.9300*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.3350*tp,0.9300*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.3350*tp,2.0550*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.3350*tp,1.7350*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.1650*tp,5.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.0700*tp,6.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.9850*tp,6.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.0700*tp,1.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.0700*tp,1.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.8750*tp,6.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.2650*tp,6.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.0700*tp,2.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.1550*tp,2.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.0700*tp,0.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.0700*tp,0.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.8750*tp,2.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.2650*tp,2.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.0700*tp,0.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.0700*tp,0.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.0700*tp,0.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.9050*tp,3.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.2300*tp,3.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.8750*tp,2.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.9100*tp,4.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.9100*tp,5.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.9100*tp,4.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.0700*tp,6.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.0700*tp,6.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.0700*tp,5.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.2650*tp,4.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.2650*tp,4.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.5900*tp,4.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.2200*tp,1.3350*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.6650*tp,1.9300*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.6650*tp,3.7350*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.6650*tp,3.1250*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.6650*tp,4.0550*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.6650*tp,1.9300*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.6650*tp,4.9300*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.6650*tp,2.8200*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.6650*tp,1.9300*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.6650*tp,5.9300*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.6650*tp,5.9300*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.6650*tp,5.9300*tp),transformation=sc.m90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(1.915*tp,3.415*tp),alias="viaA")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(2.915*tp,5.415*tp),alias="viaCLK")
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(1.555*tp,4.5*tp),transformation=sc.r90,alias="bias1")
        elems += spira.SRef(sc.ls_ib_173(),midpoint=(3.815*tp,1.5*tp),transformation=sc.r90,alias="bias2")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(2.08*tp,5.5*tp),transformation=sc.r90,alias="bias3")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(4.5*tp,1.955*tp),alias="bias4")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,3.5*tp),transformation=sc.r180,alias="J1")
        elems += spira.SRef(sc.ls_jj_161_s(),midpoint=(2.5*tp,3.5*tp),alias="J2")
        elems += spira.SRef(sc.ls_jj_154_sg(),midpoint=(2.5*tp,2.5*tp),transformation=sc.r90,alias="J3")
        elems += spira.SRef(sc.ls_jj_169_sg(),midpoint=(3.5*tp,4.5*tp),transformation=sc.r90,alias="J4")
        elems += spira.SRef(sc.ls_jj_138_s(),midpoint=(3.5*tp,5.5*tp),alias="J5")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(2.5*tp,5.5*tp),transformation=sc.r180,alias="J6")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(4.5*tp,3.5*tp),transformation=sc.r90,alias="J7")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 6):
                if (x == 4 and y == 0):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                elif (x == 0 and y == 5) or (x == 4):
                    pass
                else:
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 6):
                if ((x == 0 and y == 5) or (x == 4 and y == 1)):
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