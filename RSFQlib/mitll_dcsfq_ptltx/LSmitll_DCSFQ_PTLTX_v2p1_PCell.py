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
L1_width = 0.15*tp*Scaling
L2_width = 0.12*tp*Scaling
L3_width = 0.18*tp*Scaling
L4_width = 0.11*tp*Scaling
L5_width = 0.165*tp*Scaling
L6_width = 0.1*tp*Scaling
L7_width = 0.1647*tp*Scaling
L8_width = 0.15*tp*Scaling
LB_width = 0.15*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_DCSFQ_PTLTX_v2p1"
    def create_elements(self, elems):
        M6Strips = spira.SRef(M6_strips())
        IXports = spira.SRef(IX_ports())
        M0M4M7tracks = spira.SRef(M0M4M7_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        res = spira.SRef(resistors())
        tblocks = spira.SRef(trackblocks())
        elems += [M6Strips, IXports, M0M4M7tracks, jjfill, M4M5M6M7conns,
                  vias, bias, jjs, res, tblocks]
        # Bias ports
        PB1N = spira.Port(name='PB1N',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name='PB1S',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name='PB2N',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name='PB2S',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3N = spira.Port(name='PB3N',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name='PB3S',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4N = spira.Port(name='PB4N',midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name='PB4S',midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(4.5*tp,5.0*tp),process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1N = spira.Port(name='PR1N',midpoint=res.reference.elements['R1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1S = spira.Port(name='PR1S',midpoint=res.reference.elements['R1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Junction ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ5 = spira.Port(name="PJ5",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=(5.12*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)

        PGND = spira.Port(name="PGND",midpoint=(0.5*tp,0.9925*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PV1,path=[(PA.x,PV1.y)],width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PV1,port2=PGND,path=[(PV1.x,PGND.y)],width=L2_width,layer=sc.M5)
        L3 = spira.RoutePath(port1=PV1,port2=PJ1,path=[(PV1.x,PJ1.y)],width=L3_width,layer=sc.M5)
        L4 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(PJ1.x,PJ2.y)],width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(PJ2.x,1.5*tp),(PJ3.x,1.5*tp)],width=L5_width,layer=sc.M6)
        L6 = spira.RoutePath(port1=PJ3,port2=PJ4,path=[(PJ4.x,PJ3.y)],width=L6_width,layer=sc.M6)
        L7 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(PJ5.x,PJ4.y)],width=L7_width,layer=sc.M6)
        L8_1 = spira.RoutePath(port1=PJ5,port2=PR1N,path=[(PJ5.x,PR1N.y)],width=L8_width,layer=sc.M6)
        L8_2 = spira.RoutePath(port1=PR1S,port2=PQ,path=[(PR1S.x,PQ.y)],width=L8_width,layer=sc.M6)

        elems += [L1, L2, L3, L4, L5, L6, L7, L8_1, L8_2]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1S,path=[(PJ1.x,PB1S.y)],width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1N,port2=PV2,path=[(PB1N.x,PV2.y)],width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2S,path=[(PJ3.x,PB2S.y)],width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PV2,path=[(PB2N.x,PV2.y)],width=LB_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ4,port2=PB3S,path=[(PJ4.x,PB3S.y)],width=LB_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3N,port2=PV2,path=[(PB3N.x,PV2.y)],width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ5,port2=PB4S,path=[(PJ5.x,PB4S.y)],width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4N,port2=PV2,path=[(PB4N.x,PV2.y)],width=LB_width,layer=sc.M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2]

        LBias = spira.RoutePath(port1=PV2,port2=PBias,path=[(PBias.x,PBias.y)],width=LB_width,layer=sc.M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="J5 M6 M5",position=(4.5025*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(3.51*tp,3.505*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(4.5*tp,2.0375*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(5.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(3.5025*tp,3.8075*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(2.5025*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(1.4975*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M5 M6",position=(0.8625*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(2.5*tp,3.605*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0*tp,2.5125*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(0*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(5.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="bias",position=(4.5*tp,5*tp),layer=TEXT)
        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.015*tp,center=(5.5075*tp,4.9925*tp))
        elems += spira.Box(layer=sc.M6,width=0.015*tp,height=0.315*tp,center=(5.9925*tp,1.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.015*tp,height=0.315*tp,center=(5.9925*tp,2.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.015*tp,center=(5.5075*tp,4.9925*tp))
        elems += spira.Box(layer=sc.M5,width=0.015*tp,height=0.315*tp,center=(5.9925*tp,1.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.015*tp,height=0.315*tp,center=(5.9925*tp,2.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(2.5*tp,0.715*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(3.5*tp,1.555*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(3.5*tp,1.135*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(3.5*tp,0.715*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(0.5*tp,4.295*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(1.5*tp,0.715*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.25*tp,center=(3.29*tp,1.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(2.79*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(2.37*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.95*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.53*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.11*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(0.69*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(0.51*tp,4.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(3.21*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(3.63*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(4.05*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(4.47*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(4.89*tp,0.505*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(5.31*tp,0.505*tp))

        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,2.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(4.5*tp,2.0375*tp))
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(5.5*tp,2.5025*tp))
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(3.5025*tp,3.8075*tp))
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(1.5*tp,3.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.05*tp,height=0.05*tp,center=(2.5*tp,3.6025*tp))
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M4,width=0.25*tp,height=0.56*tp,center=(0.845*tp,3.0*tp))
        elems += spira.Box(layer=sc.M7,width=0.25*tp,height=0.56*tp,center=(0.845*tp,3.0*tp))
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3.155*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1.5*tp,0.85*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2.5*tp,0.85*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.84*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.72*tp,4.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.32*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.48*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.9*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.16*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.58*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.74*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.3*tp,4.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,4.085*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.42*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.52*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.26*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.1*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.68*tp,0.505*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,0.925*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,1.345*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,1.765*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.9075*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.2275*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.985*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.985*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.905*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.955*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.23*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.255*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.2125*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.275*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.96*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.6*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.665*tp,1.985*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,4.265*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,3.875*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,1.2325*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,1.265*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,2.265*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.665*tp,2.265*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.665*tp,4.985*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.1725*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.665*tp,1.155*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,1.215*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,4.875*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,4.875*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,2.875*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,4.875*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7_block(),midpoint=(3*tp,4*tp))
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(0.415*tp,2.415*tp),alias='via1')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.415*tp,4.415*tp),alias='via2')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_082(),midpoint=(5.5*tp,2.4475*tp),alias='bias4')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(2.5*tp,3.5475*tp),alias='bias2')
        elems += spira.SRef(sc.ls_ib_230(),midpoint=(3.5025*tp,3.7525*tp),alias='bias3')
        elems += spira.SRef(sc.ls_ib_275(),midpoint=(1.5*tp,3.445*tp),alias='bias1')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_162_sg(),midpoint=(4.5*tp,2.5*tp),transformation=sc.r90,alias='J5')
        elems += spira.SRef(sc.ls_jj_200_sg(),midpoint=(3.5001*tp,3.5*tp),transformation=sc.r90,alias='J4')
        elems += spira.SRef(sc.ls_jj_225_s(),midpoint=(0.865*tp,2.4975*tp),transformation=sc.r180,alias='J1')
        elems += spira.SRef(sc.ls_jj_225_sg(),midpoint=(1.5*tp,2.5*tp),alias='J2')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(2.5*tp,2.5*tp),transformation=sc.r90,alias='J3')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_res_1p36(),midpoint=(4.5*tp,1.7875*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 5):
            for x in range(0, 6):
                if (x == 5 and y == 1):
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