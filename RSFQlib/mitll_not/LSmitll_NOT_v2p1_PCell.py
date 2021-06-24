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
L2_width = 0.15*tp*Scaling
L3_width = 0.25*tp*Scaling
L4_width = L1_width
L5_width = 0.28*tp*Scaling
L6_width = 0.28*tp*Scaling
L7_width = 0.165*tp*Scaling
L8_width = 0.205*tp*Scaling
L9_width = 0.15*tp*Scaling
L10_width = L6_width
L11_width = 0.215*tp*Scaling
L12_width = L1_width
LB_width = 0.14*tp*Scaling
LR1_width = 0.14*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_NOT_v2p1"
    def create_elements(self, elems):
        resistor = spira.SRef(sc.ls_res_4(),midpoint=(5.215*tp,4.73*tp),transformation=sc.r90,alias='R1')
        M6Strips = spira.SRef(M6_strips())
        IXports = spira.SRef(IX_ports())
        M0tracks = spira.SRef(M0_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        M0blocks = spira.SRef(M0_blocks())
        tblocks = spira.SRef(trackblocks())
        elems += [M6Strips, IXports, M0tracks, jjfill, M4M5M6M7conns, vias, bias, jjs, M0blocks, tblocks, resistor]
        # Ports for inductor connections
        # Bias1
        PB1W = spira.Port(name="PB1W",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name="PB1E",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias2
        PB2N = spira.Port(name="PB2N",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name="PB2S",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias3
        PB3E = spira.Port(name="PB3E",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3W = spira.Port(name="PB3W",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias4
        PB4N = spira.Port(name="PB4N",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name="PB4S",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias5
        PB5W = spira.Port(name="PB5W",midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5E = spira.Port(name="PB5E",midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Ends
        PB2_end = spira.Port(name="PB2_end",midpoint=(1.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PB3_end = spira.Port(name="PB3_end",midpoint=(1.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PR1_end = spira.Port(name="PR1_end",midpoint=(5.5*tp,4.73*tp),process=spira.RDD.PROCESS.M6)
        # Resistor
        PR1W = spira.Port(name="PR1W",midpoint=resistor.ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1E = spira.Port(name="PR1E",midpoint=resistor.ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # VIA
        PVW = spira.Port(name="PVW",midpoint=vias.reference.elements['via'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        PVE = spira.Port(name="PVE",midpoint=vias.reference.elements['via'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ1
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ2
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ3
        PJ3N = spira.Port(name="PJ3N",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ3W = spira.Port(name="PJ3W",midpoint=(PJ3N.x,PJ2.y),process=spira.RDD.PROCESS.M6)
        # JJ4
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ5
        PJ5W = spira.Port(name="PJ5W",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ5E = spira.Port(name="PJ5E",midpoint=(PJ5W.x,PVW.y),process=spira.RDD.PROCESS.M6)
        # JJ6
        PJ6 = spira.Port(name="PJ6",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ6L = spira.Port(name="PJ6L",midpoint=(PJ3N.x,PJ5W.y),process=spira.RDD.PROCESS.M6)
        # JJ7
        PJ7W = spira.Port(name="PJ7W",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ7E = spira.Port(name="PJ7E",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ8
        PJ8 = spira.Port(name="PJ8",midpoint=jjs.reference.elements['J8'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ9
        PJ9 = spira.Port(name="PJ9",midpoint=jjs.reference.elements['J9'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pins
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center+(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center,process=spira.RDD.PROCESS.M6)
        PCLK_post = spira.Port(name="PCLK_post",midpoint=IXports.reference.elements['CLK'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PN12 = spira.Port(name="PN12",midpoint=(PVE.x,PR1W.y),process=spira.RDD.PROCESS.M6)
        ## Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[((PJ1.x+PJ2.x)/2,(PJ1.y+PJ2.y)/2)],start_straight=False,end_straight=False,width=L2_width,layer=sc.M6)
        L3_1 = spira.RoutePath(port1=PJ2,port2=PJ3W,path=[((PJ2.x+PJ3W.x)/2,(PJ2.y+PJ3W.y)/2)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L3_2 = spira.RoutePath(port1=PJ3N,port2=PJ7W,path=[(PJ6L.x,PJ6L.y)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M5)
        L4 = spira.RoutePath(port1=PCLK,port2=PJ4,path=[((PCLK.x+PJ4.x)/2,(PCLK.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['CLK'].bbox_info.height,layer=sc.M6)
        L4_post = spira.RoutePath(port1=PCLK_post,port2=PJ4,path=[((PCLK_post.x+PJ4.x)/2,(PCLK_post.y+PJ4.y)/2)],start_straight=False,end_straight=False,width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PJ4,port2=PVE,path=[((PJ4.x+PVE.x)/2,(PJ4.y+PVE.y)/2)],start_straight=False,end_straight=False,width=L5_width,layer=sc.M6)
        L6_1 = spira.RoutePath(port1=PVW,port2=PJ5E,path=[((PVW.x+PJ5E.x)/2,(PVW.y+PJ5E.y)/2)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M5)
        L6_2 = spira.RoutePath(port1=PJ5W,port2=PJ8,path=[((PJ5W.x+PJ8.x)/2,(PJ5W.y+PJ8.y)/2)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M6)
        L7 = spira.RoutePath(port1=PVE,port2=PN12,path=[((PVE.x+PN12.x)/2,(PVE.y+PN12.y)/2)],start_straight=False,end_straight=False,width=L7_width,layer=sc.M6)
        L8 = spira.RoutePath(port1=PN12,port2=PJ6,path=[((PN12.x+PJ6.x)/2,(PN12.y+PJ6.y)/2)],start_straight=False,end_straight=False,width=L8_width,layer=sc.M6)
        L9 = spira.RoutePath(port1=PJ6,port2=PJ6L,path=[(2.5*tp,5.5*tp)],start_straight=False,end_straight=False,width=L9_width,layer=sc.M6)
        L10 = spira.RoutePath(port1=PJ7E,port2=PJ8,path=[((PJ7E.x+PJ8.x)/2,(PJ7E.y+PJ8.y)/2)],start_straight=False,end_straight=False,width=L10_width,layer=sc.M6)
        L11 = spira.RoutePath(port1=PJ8,port2=PJ9,path=[((PJ8.x+PJ9.x)/2,(PJ8.y+PJ9.y)/2)],start_straight=False,end_straight=False,width=L11_width,layer=sc.M6)
        L12 = spira.RoutePath(port1=PJ9,port2=PQ,path=[((PJ9.x+PQ.x)/2,(PJ9.y+PQ.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.width,layer=sc.M6)
        L12_post = spira.RoutePath(port1=PJ9,port2=PQ_post,path=[((PJ9.x+PQ_post.x)/2,(PJ9.y+PQ_post.y)/2)],start_straight=False,end_straight=False,width=L12_width,layer=sc.M6)
        LB1 = spira.RoutePath(port1=PJ1,port2=PB1E,path=[((PJ1.x+PB1E.x)/2,(PJ1.y+PB1E.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ2,port2=PB2N,path=[(0.5*tp,2.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2S,port2=PB2_end,path=[(0.5*tp,0.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PB1W,port2=PB3W,path=[(0.5*tp,4.5*tp),(0.5*tp,6.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3E,port2=PB3_end,path=[(1.5*tp,6.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ4,port2=PB4N,path=[((PJ4.x+PB4N.x)/2,(PJ4.y+PB4N.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4S,port2=PB5E,path=[(5.5*tp,1.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB5 = spira.RoutePath(port1=PJ9,port2=PB5W,path=[((PJ9.x+PB5W.x)/2,(PJ9.y+PB5W.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LR1_1 = spira.RoutePath(port1=PN12,port2=PR1W,path=[((PN12.x+PR1W.x)/2,(PN12.y+PR1W.y)/2)],start_straight=False,end_straight=False,width=LR1_width,layer=sc.M6)
        LR1_2 = spira.RoutePath(port1=PR1E,port2=PR1_end,path=[((PR1E.x+PR1_end.x)/2,(PR1E.y+PR1_end.y)/2)],start_straight=False,end_straight=False,width=LR1_width,layer=sc.M6)
        elems += [L1, L1_post, L2, L3_1, L3_2, L4, L4_post, 
                  L5, L6_1, L6_2, L7, L8, L9, L9, L10, L11, L12, L12_post] 
        elems += [LB1, LB2_1, LB2_2, LB3_1, LB3_2,
                  LB4_1, LB4_2, LB5, LR1_1, LR1_2]
        elems += spira.Polygon(spira.Shape(points=[(3.04*tp,3.72*tp),(3.04*tp,4.28*tp),(3.28*tp,4.28*tp),(3.28*tp,3.72*tp)]),layer=sc.M1)
        elems += spira.Polygon(spira.Shape(points=[(3.72*tp,3.72*tp),(3.72*tp,4.28*tp),(3.96*tp,4.28*tp),(3.96*tp,3.72*tp)]),layer=sc.M1)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,4.72*tp),(4.72*tp,4.96*tp),(5.28*tp,4.96*tp),(5.28*tp,4.72*tp)]),layer=sc.M1)
        elems += spira.Polygon(spira.Shape(points=[(3.04*tp,3.72*tp),(3.04*tp,4.28*tp),(3.28*tp,4.28*tp),(3.28*tp,3.72*tp)]),layer=sc.M4)
        elems += spira.Polygon(spira.Shape(points=[(3.72*tp,3.72*tp),(3.72*tp,4.28*tp),(3.96*tp,4.28*tp),(3.96*tp,3.72*tp)]),layer=sc.M4)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,4.72*tp),(4.72*tp,4.96*tp),(5.28*tp,4.96*tp),(5.28*tp,4.72*tp)]),layer=sc.M4)
        elems += spira.Polygon(spira.Shape(points=[(3.04*tp,3.72*tp),(3.04*tp,4.28*tp),(3.28*tp,4.28*tp),(3.28*tp,3.72*tp)]),layer=sc.M7)
        elems += spira.Polygon(spira.Shape(points=[(3.72*tp,3.72*tp),(3.72*tp,4.28*tp),(3.96*tp,4.28*tp),(3.96*tp,3.72*tp)]),layer=sc.M7)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,4.72*tp),(4.72*tp,4.96*tp),(5.28*tp,4.96*tp),(5.28*tp,4.72*tp)]),layer=sc.M7)
        # Text Labels
        elems += spira.Label(text='P3 M6 M4',position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text='q',position=(3.5*tp,0*tp),layer=TEXT)
        elems += spira.Label(text='PB5 M6 M4',position=(4.0*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='J9 M6 M5',position=(3.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='J8 M6 M5',position=(3.5*tp,3.475*tp),layer=TEXT)
        elems += spira.Label(text='J7 M5 M6 ',position=(3.115*tp,3.475*tp),layer=TEXT)
        elems += spira.Label(text='J5 M5 M6',position=(3.885*tp,3.475*tp),layer=TEXT)
        elems += spira.Label(text='PB4 M6 M4',position=(5.5*tp,3.0*tp),layer=TEXT)
        elems += spira.Label(text='J4 M6 M5',position=(5.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='P2 M6 M4',position=(7.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='clk',position=(7.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='PR1 M6 M4',position=(4.885*tp,4.73*tp),layer=TEXT)
        elems += spira.Label(text='J6 M6 M5',position=(4.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text='PB3 M6 M4',position=(1.28*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='J3 M6 M5',position=(2.5*tp,2.56*tp),layer=TEXT)
        elems += spira.Label(text='PB2 M6 M4',position=(0.5*tp,2.4*tp),layer=TEXT)
        elems += spira.Label(text='J2 M6 M5',position=(1.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text='PB1 M6 M4',position=(1.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text='J1 M6 M5',position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='P1 M6 M4',position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='a',position=(0*tp,3.5*tp),layer=TEXT)

        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,4.5*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,4.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,5.5*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(3.5*tp,0.0*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(7.0*tp,3.5*tp),alias='CLK')

        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.5*tp,3.002*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.887*tp,4.73*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.28*tp,6.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,2.401*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.497*tp,4.5*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Polygon(spira.Shape(points=[(0*tp,6.35*tp),(0*tp,6.65*tp),(7*tp,6.65*tp),(7*tp,6.35*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(0.375*tp,0.375*tp),(0.375*tp,6.5*tp),(0.625*tp,6.5*tp),(0.625*tp,0.625*tp),(1.5*tp,0.625*tp),(1.5*tp,0.375*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(5.375*tp,1.5*tp),(5.375*tp,6.5*tp),(5.625*tp,6.5*tp),(5.625*tp,1.5*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(2.4*tp,3.5*tp),(2.4*tp,5.4*tp),(1.5*tp,5.4*tp),(1.5*tp,5.6*tp),(2.6*tp,5.6*tp),(2.6*tp,3.5*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(6.125*tp,6*tp),(6.125*tp,6.04*tp),(6.875*tp,6.04*tp),(6.875*tp,6*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(5.96*tp,1.125*tp),(5.96*tp,5.875*tp),(6*tp,5.875*tp),(6*tp,1.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(5.125*tp,1*tp),(5.125*tp,1.04*tp),(5.875*tp,1.04*tp),(5.875*tp,1*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(5*tp,1.125*tp),(5*tp,5.875*tp),(5.04*tp,5.875*tp),(5.04*tp,1.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(3.125*tp,6*tp),(3.125*tp,6.04*tp),(4.875*tp,6.04*tp),(4.875*tp,6*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(2.96*tp,3.125*tp),(2.96*tp,5.875*tp),(3*tp,5.875*tp),(3*tp,3.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(2.125*tp,3*tp),(2.125*tp,3.04*tp),(2.875*tp,3.04*tp),(2.875*tp,3*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(2*tp,3.125*tp),(2*tp,4.875*tp),(2.04*tp,4.875*tp),(2.04*tp,3.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(1.125*tp,5*tp),(1.125*tp,5.04*tp),(1.875*tp,5.04*tp),(1.875*tp,5*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(0.96*tp,1.125*tp),(0.96*tp,4.875*tp),(1*tp,4.875*tp),(1*tp,1.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(1.125*tp,0.96*tp),(1.125*tp,1*tp),(1.875*tp,1*tp),(1.875*tp,0.96*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(1.96*tp,0.125*tp),(1.96*tp,0.875*tp),(2*tp,0.875*tp),(2*tp,0.125*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(3.04*tp,3.72*tp),(3.04*tp,4.28*tp),(3.28*tp,4.28*tp),(3.28*tp,3.72*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(3.72*tp,3.72*tp),(3.72*tp,4.28*tp),(3.96*tp,4.28*tp),(3.96*tp,3.72*tp)]),layer=sc.M0)
        elems += spira.Polygon(spira.Shape(points=[(4.72*tp,4.72*tp),(4.72*tp,4.96*tp),(5.28*tp,4.96*tp),(5.28*tp,4.72*tp)]),layer=sc.M0)
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,0.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.325*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.325*tp,4.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.84*tp,4.34*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.325*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.325*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,3.045*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.325*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.325*tp,4.805*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.775*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.325*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.43*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.325*tp,5.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.325*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.325*tp,0.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.325*tp,5.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.325*tp,5.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.07*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.945*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.185*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.91*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.07*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.935*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.955*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.565*tp,4.565*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.93*tp,1.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.125*tp,0.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.93*tp,0.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.125*tp,2.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.735*tp,0.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.93*tp,4.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.93*tp,5.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.93*tp,5.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.93*tp,6.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.93*tp,6.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.93*tp,6.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.93*tp,1.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.93*tp,0.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.93*tp,6.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.845*tp,0.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.125*tp,0.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.125*tp,1.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.735*tp,1.665*tp),transformation=sc.r270)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,5.015*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,6.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,4.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,4.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,2.805*tp),transformation=sc.m90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.415*tp,3.415*tp),alias='via')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_257(),midpoint=(1.335*tp,6.5*tp),transformation=sc.r90,alias='bias3')
        elems += spira.SRef(sc.ls_ib_087(),midpoint=(0.5*tp,0.59*tp),alias='bias2')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(5.5*tp,2.05*tp),alias='bias4')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(3.945*tp,1.5*tp),transformation=sc.r270,alias='bias5')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(0.545*tp,4.5*tp),transformation=sc.r270,alias='bias1')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_138_s(),midpoint=(3.115*tp,3.475*tp),alias='J7')
        elems += spira.SRef(sc.ls_jj_134_s(),midpoint=(3.885*tp,3.475*tp),alias='J5')
        elems += spira.SRef(sc.ls_jj_107_s(),midpoint=(2.5*tp,2.56*tp),transformation=sc.r180,alias='J3')
        elems += spira.SRef(sc.ls_jj_080_sg(),midpoint=(3.5*tp,3.475*tp),alias='J8')
        elems += spira.SRef(sc.ls_jj_303_sg(),midpoint=(4.5*tp,5.5*tp),alias='J6')
        elems += spira.SRef(sc.ls_jj_257_sg(),midpoint=(1.5*tp,2.5*tp),transformation=sc.r180,alias='J2')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,3.5*tp),transformation=sc.r270,alias='J1')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(5.5*tp,3.5*tp),alias='J4')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(3.5*tp,1.5*tp),transformation=sc.r90,alias='J9')
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(1, 7):
                if (x == 1 and y in [1,2,3,4]) or (x == 2 and y in [0,1,2]):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                elif (x in [3,4,6]) or (x == 5 and y == 0):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                else:
                    pass
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 7):
                if (x == 1 and y in [0,5]) or (x == 0 and y == 5) or (x == 2 and y == 3) or (x == 5 and y == 1):
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