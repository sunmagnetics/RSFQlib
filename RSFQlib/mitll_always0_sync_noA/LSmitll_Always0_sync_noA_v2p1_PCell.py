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
L2_width = L1_width
L3_width = L1_width
L4_width = L1_width
L5_width = L1_width
L6_width = L1_width
LB_width = 0.14*tp*Scaling
class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_Always0_sync_v2p1"
    def create_elements(self, elems):
        R1 = spira.SRef(sc.ls_res_2(),transformation=sc.r270,midpoint=(0.73*tp,5.495*tp))
        R2 = spira.SRef(sc.ls_res_2(),midpoint=(1.5*tp,1.64*tp))
        M6Strips = spira.SRef(M6_strips())
        IXports = spira.SRef(IX_ports())
        M0tracks = spira.SRef(M0_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        M0blocks = spira.SRef(M0_blocks())
        tblocks = spira.SRef(trackblocks())
        elems += [R1, R2, M6Strips, IXports, M0tracks, jjfill, M4M5M6M7conns, bias, jjs, M0blocks, tblocks]
        # Bias Ports
        PB1N = spira.Port(name="PB1N",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name="PB1S",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name="PB2N",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name="PB2S",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1E = spira.Port(name="PR1E",midpoint=R1.ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1W = spira.Port(name="PR1W",midpoint=R1.ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PR2N = spira.Port(name="PR2N",midpoint=R2.ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR2S = spira.Port(name="PR2S",midpoint=R2.ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Pillar Ports
        PBP = spira.Port(name="PBP",midpoint=(0.5*tp,4.5*tp),process=spira.RDD.PROCESS.M6)
        # Junction Ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pins
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center,process=spira.RDD.PROCESS.M6)
        PCLK_end = spira.Port(name="PCLK_end",midpoint=(0.57*tp,5.495*tp),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_end = spira.Port(name="PQ_end",midpoint=(1.5*tp,1.55*tp),process=spira.RDD.PROCESS.M6)
        ## Inductors
        L1 = spira.RoutePath(port1=PCLK,port2=PJ1,path=[((PCLK.x+PJ1.x)/2,(PCLK.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PR1E,path=[((PJ1.x+PR1E.x)/2,(PJ1.y+PR1E.y)/2)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PR1W,port2=PCLK_end,path=[((PR1W.x+PCLK_end.x)/2,(PR1W.y+PCLK_end.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PQ,port2=PJ2,path=[(2.5*tp,PQ.y),(2.5*tp,PJ2.y)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PJ2,port2=PR2N,path=[((PJ2.x+PR2N.x)/2,(PJ2.y+PR2N.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        L6 = spira.RoutePath(port1=PR2S,port2=PQ_end,path=[((PR2S.x+PQ_end.x)/2,(PR2S.y+PQ_end.y)/2)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M6)
        elems += [L1, L2, L3, L4, L5, L6]
        
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1N,path=[(PB1N.x,PJ1.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1S,port2=PBP,path=[(PB1S.x,PBP.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ2,port2=PB2S,path=[(PB2S.x,PJ2.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PBP,path=[((PB2N.x+PBP.x)/2,(PB2N.y+PBP.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        elems += [LB1_1, LB1_2, LB2_1, LB2_2]
        # Text Labels
        elems += spira.Label(text='bias_out',position=(3*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='bias_in',position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='clk',position=(1.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text='q',position=(3*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='P1 M6 M4',position=(1.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text='J1 M6 M5',position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text='PR1 M6 M4',position=(1*tp,5.495*tp),layer=TEXT)
        elems += spira.Label(text='PB1 M6 M4',position=(2.5*tp,5.43*tp),layer=TEXT)
        elems += spira.Label(text='PB2 M6 M4',position=(0.5*tp,2.55*tp),layer=TEXT)
        elems += spira.Label(text='J2 M6 M5',position=(1.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text='PR2 M6 M4',position=(1.5*tp,1.91*tp),layer=TEXT)
        elems += spira.Label(text='P2 M6 M4',position=(3*tp,3.5*tp),layer=TEXT)

        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,4.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,4.5*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(1.5*tp,7.0*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(3.0*tp,3.5*tp),alias='Q')

        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.5*tp,1.91*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,2.55*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,5.432*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.0*tp,5.495*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M0,width=3.0*tp,height=0.3*tp,center=(1.5*tp,6.5*tp))
        elems += spira.Box(layer=sc.M0,width=2.75*tp,height=0.04*tp,center=(1.5*tp,6.02*tp))

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,3.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.41*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.81*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,4.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,5.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,4.09*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,2.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,4.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.57*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(1.155*tp,3.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(2.875*tp,4.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(2.875*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(1.875*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(1.265*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.265*tp,5.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(2.875*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(1.07*tp,1.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(2.07*tp,1.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(2.07*tp,0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(1.07*tp,0.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(2.155*tp,6.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(2.195*tp,3.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.875*tp,3.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.265*tp,3.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.265*tp,2.335*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),transformation=sc.r90,midpoint=(0.165*tp,4.335*tp))
        elems += spira.SRef(sc.ls_conn_M5M6M7(),midpoint=(1.465*tp,2.995*tp))
        elems += spira.SRef(sc.ls_conn_M5M6M7(),transformation=sc.m0,midpoint=(1.465*tp,5.005*tp))

        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(0.5*tp,2.495*tp),alias='bias2')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(2.5*tp,4.48*tp),alias='bias1')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,2.5*tp),alias='J2')
        elems += spira.SRef(sc.ls_jj_250_sg(),transformation=sc.r180,midpoint=(1.5*tp,5.5*tp),alias='J1')
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 3):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                if (x == 0 and y == 4):
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