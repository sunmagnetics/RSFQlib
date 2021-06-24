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
L2_width = 0.16*tp*Scaling
L3M6_width = 0.23*tp*Scaling
L3M5_width = 0.22*tp*Scaling
L4_width = L1_width
L5_width = L2_width
L6M6_width = L3M6_width
L6M5_width = L3M5_width
L7_width = 0.145*tp*Scaling
L8_width = 0.1*tp*Scaling
L9_width = L1_width
LB_width = 0.14*tp*Scaling
LB3_width = 0.16*tp*Scaling
LJ1_width = 0.14*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_MERGE_v2p1"
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
        PB1W = spira.Port(name="PB1W",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name="PB1E",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # B2
        PB2N = spira.Port(name="PB2N",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name="PB2S",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # B3
        PB3N = spira.Port(name="PB3N",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name="PB3S",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # B4
        PB4W = spira.Port(name="PB4W",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4E = spira.Port(name="PB4E",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # B5
        PB5W = spira.Port(name="PB5W",midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5E = spira.Port(name="PB5E",midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # J1
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ1L = spira.Port(name="PJ1L",midpoint=(2.5*tp,3.5*tp),process=spira.RDD.PROCESS.M6)
        # J2
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J3
        PJ3E = spira.Port(name="PJ3E",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ3W = spira.Port(name="PJ3W",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J4
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J5
        PJ5 = spira.Port(name="PJ5",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J6
        PJ6E = spira.Port(name="PJ6E",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ6W = spira.Port(name="PJ6W",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        # J7
        PJ7 = spira.Port(name="PJ7",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # J8
        PJ8 = spira.Port(name="PJ8",midpoint=jjs.reference.elements['J8'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # PA
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        # PB
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center,process=spira.RDD.PROCESS.M6)
        PB_post = spira.Port(name="PB_post",midpoint=IXports.reference.elements['B'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        # PQ
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center-(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        # PVA
        PVAM6 = spira.Port(name="PVAM6",midpoint=vias.reference.elements['viaA'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PVAM5 = spira.Port(name="PVAM5",midpoint=vias.reference.elements['viaA'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        # Bias ends
        PB1_end = spira.Port(name="PB1_end",midpoint=(0.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PB4_end = spira.Port(name="PB4_end",midpoint=(0.5*tp,4.5*tp),process=spira.RDD.PROCESS.M6)
        PB2_5_end = spira.Port(name="PB2_5_end",midpoint=(5.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        ## Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(1.5*tp,2.5*tp)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L3W = spira.RoutePath(port1=PJ2,port2=PJ3W,path=[((PJ2.x+PJ3W.x)/2,(PJ2.y+PJ3W.y)/2)],start_straight=False,end_straight=False,width=L3M6_width,layer=sc.M6)
        L3E = spira.RoutePath(port1=PJ3E,port2=PVAM5,path=[((PJ3E.x+PVAM5.x)/2,(PJ3E.y+PVAM5.y)/2)],start_straight=False,end_straight=False,width=L3M5_width,layer=sc.M5)
        L4 = spira.RoutePath(port1=PB,port2=PJ4,path=[((PB.x+PJ4.x)/2,(PB.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['B'].bbox_info.height,layer=sc.M6)
        L4_post = spira.RoutePath(port1=PB_post,port2=PJ4,path=[((PB_post.x+PJ4.x)/2,(PB_post.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(5.5*tp,2.5*tp)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        L6W = spira.RoutePath(port1=PJ6W,port2=PVAM5,path=[((PJ6W.x+PVAM5.x)/2,(PJ6W.y+PVAM5.y)/2)],start_straight=False,end_straight=False,width=L6M5_width,layer=sc.M5)
        L6E = spira.RoutePath(port1=PJ5,port2=PJ6E,path=[((PJ5.x+PJ6E.x)/2,(PJ5.y+PJ6E.y)/2)],start_straight=False,end_straight=False,width=L6M6_width,layer=sc.M6)
        L7 = spira.RoutePath(port1=PJ7,port2=PVAM6,path=[(3.5*tp,4.5*tp)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M6)
        L8 = spira.RoutePath(port1=PJ8,port2=PJ7,path=[(2.5*tp,5.5*tp)],start_straight=False,end_straight=False,width=L8_width,layer=sc.M6)
        L9 = spira.RoutePath(port1=PJ8,port2=PQ,path=[((PJ8.x+PQ.x)/2,(PJ8.y+PQ.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.width,layer=sc.M6)
        L9_post = spira.RoutePath(port1=PJ8,port2=PQ_post,path=[((PJ8.x+PQ_post.x)/2,(PJ8.y+PQ_post.y)/2)],start_straight=False,end_straight=False,width=L9_width,layer=sc.M6)
        LJ1 = spira.RoutePath(port1=PJ1,port2=PJ1L,path=[((PJ1.x+PJ1L.x)/2,(PJ1.y+PJ1L.y)/2)],start_straight=False,end_straight=False,width=LJ1_width,layer=sc.M6)
        LB1_1 = spira.RoutePath(port1=PB1_end,port2=PB1W,path=[((PB1_end.x+PB1W.x)/2,(PB1_end.y+PB1W.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1E,port2=PB3S,path=[(2.5*tp,0.5*tp),(2.5*tp,1.51375*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ4,port2=PB2S,path=[((PJ4.x+PB2S.x)/2,(PJ4.y+PB2S.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PB5E,path=[(5.5*tp,5.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3 = spira.RoutePath(port1=PVAM6,port2=PB3N,path=[((PVAM6.x+PB3N.x)/2,(PVAM6.y+PB3N.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ7,port2=PB4E,path=[((PJ7.x+PB4E.x)/2,(PJ7.y+PB4E.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4W,port2=PB4_end,path=[((PB4W.x+PB4_end.x)/2,(PB4W.y+PB4_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB5 = spira.RoutePath(port1=PJ8,port2=PB5W,path=[((PJ8.x+PB5W.x)/2,(PJ8.y+PB5W.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        elems += [L1, L1_post, L2, L3W, L3E, L4, L4_post, L5, L6W, L6E, L7, L8, L9, L9_post]
        elems += [LJ1, LB1_1, LB1_2, LB2_1, LB2_2, LB3, LB4_1, LB4_2, LB5]
        elems += spira.Box(layer=sc.M4,width=0.27*tp,height=0.425*tp,center=(3.0*tp,2.9325*tp))
        elems += spira.Box(layer=sc.M4,width=0.27*tp,height=0.425*tp,center=(4.0*tp,2.9325*tp))
        elems += spira.Box(layer=sc.M7,width=0.27*tp,height=0.425*tp,center=(3.0*tp,2.9325*tp))
        elems += spira.Box(layer=sc.M7,width=0.27*tp,height=0.425*tp,center=(4.0*tp,2.9325*tp))
        ## Text Labels
        elems += spira.Label(text="bias_out",position=(7*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="Q",position=(3.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(7.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(0.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.188*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(5.497*tp,4.053*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(3.5*tp,2.145*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(1.857*tp,4.502*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(4.008*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(2.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(3.0*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(5.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(4.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(4.0*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(2.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(3.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(7.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(3.5*tp,7.0*tp),layer=TEXT)
        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,0.5*tp))
        elems += spira.Box(layer=sc.M6,width=0.33*tp,height=0.025*tp,center=(0.5*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M5,width=0.33*tp,height=0.025*tp,center=(0.5*tp,0.0125*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,7.0*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(7.0*tp,3.5*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.005*tp,5.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.857*tp,4.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.5*tp,4.053*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(3.5*tp,2.145*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.188*tp,0.5*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M0,width=7*tp,height=0.3*tp,center=(3.5*tp,6.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.25*tp,height=2.0*tp,center=(0.5*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.25*tp,height=1.0*tp,center=(5.5*tp,6.0*tp))

        elems += spira.Polygon(shape=spira.Shape([(2.5*tp,1.375*tp),(3.625*tp,1.375*tp),(3.625*tp,6.5*tp),(3.375*tp,6.5*tp),(3.375*tp,1.625*tp),(2.5*tp,1.625*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape([(0.5*tp,0.375*tp),(1.625*tp,0.375*tp),(1.625*tp,3.375*tp),(2.5*tp,3.375*tp),(2.5*tp,3.625*tp),(1.375*tp,3.625*tp),(1.375*tp,0.625*tp),(0.5*tp,0.625*tp)]),layer=sc.M0)

        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(0.5*tp,0.98*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(2.5*tp,1.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(3.5*tp,1.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(2.5*tp,1.98*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(2.5*tp,3.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(1.5*tp,3.98*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(2.5*tp,3.98*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(0.5*tp,4.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(5.5*tp,5.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(1.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(2.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(4.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(6.5*tp,6.02*tp))

        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(0.98*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(0.98*tp,4.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(1.02*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(1.02*tp,2.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(1.02*tp,1.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(1.98*tp,2.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(1.98*tp,0.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(3.02*tp,2.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(3.02*tp,4.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(3.02*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(3.98*tp,1.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(3.98*tp,2.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(3.98*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(3.98*tp,4.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(3.98*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(5.02*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(5.98*tp,5.5*tp))
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding 3um junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,3.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2.5*tp))
        sys.stdout.write("Adding 1.5um junction fill.\n")
        for y in range(1, 7):
            for x in range(1, 7):
                if (x in [3,4] and y == 3) :
                    pass
                else:
                    elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(), midpoint=(0.0+x*tp,0.0+y*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,4.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,2.805*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,2.815*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,1.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,2.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.205*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.155*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.07*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.07*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.07*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.07*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.07*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.155*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.07*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.07*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.265*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.07*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.195*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.945*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.07*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.07*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.07*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.07*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.155*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.07*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.215*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.98*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.155*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,1.835*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.665*tp,5.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,0.025*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,0.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,0.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,2.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,2.805*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.665*tp,2.815*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,1.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,0.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,5.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,0.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,0.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.665*tp,0.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.665*tp,0.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,0.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,5.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,5.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,5.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,4.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,3.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,5.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.665*tp,1.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,4.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.735*tp),transformation=sc.m90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(3.415*tp,2.415*tp),alias="viaA")
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(2.14*tp,0.5*tp),transformation=sc.r90,alias="bias1")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(5.5*tp,5.005*tp),transformation=sc.r180,alias="bias2")
        elems += spira.SRef(sc.ls_ib_254(),midpoint=(3.5*tp,2.2*tp),transformation=sc.r180,alias="bias3")
        elems += spira.SRef(sc.ls_ib_192(),midpoint=(0.98*tp,4.5*tp),transformation=sc.r270,alias="bias4")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(3.95*tp,5.5*tp),transformation=sc.r270,alias="bias5")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,3.5*tp),alias="J1")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(2.5*tp,2.5*tp),transformation=sc.r180,alias="J2")
        elems += spira.SRef(sc.ls_jj_192_s(),midpoint=(3.0*tp,2.5*tp),alias="J3")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(5.5*tp,3.5*tp),transformation=sc.r90,alias="J4")
        elems += spira.SRef(sc.ls_jj_192_s(),midpoint=(4.0*tp,2.5*tp),alias="J6")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(4.5*tp,2.5*tp),transformation=sc.r180,alias="J5")
        elems += spira.SRef(sc.ls_jj_253_sg(),midpoint=(2.5*tp,4.5*tp),transformation=sc.r180,alias="J7")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(3.5*tp,5.5*tp),transformation=sc.r180,alias="J8")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 7):
                if (x > 3 and y < 5):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                elif (x == 0 and y in [1,2,3]) or (x == 1 and y in [4,5]) or (x == 2 and y in [0,2,4,5]) or (x == 3 and y == 0) or (x == 4 and y == 5) or (x == 6 and y ==5):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 7):
                if ((x == 0 and y in [0,4]) or (x == 2 and y in [1,3]) or (x == 5 and y == 5)):
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