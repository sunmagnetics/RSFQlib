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
L2S_width = 0.2*tp*Scaling
L2NM5_width = 0.2*tp*Scaling
L2NM6_width = 0.2*tp*Scaling
L3_width = 0.16*tp*Scaling
L4W_width = 0.24*tp*Scaling
L4E_width = 0.24*tp*Scaling
L5N_width = 0.2*tp*Scaling
L5E_width = 0.2*tp*Scaling
L6_width = L1_width
L7S_width = L2S_width
L7NM5_width = L2NM5_width
L7NM6_width = L2NM6_width
L8_width = L3_width
L9E_width = L4W_width
L9W_width = L4E_width
L10N_width = L5N_width
L10E_width = L5E_width
L11_width = 0.25*tp*Scaling
LJ13_width = 0.16*tp*Scaling
L12_width = 0.09*tp*Scaling
LJ14_width = 0.16*tp*Scaling
L13_width = 0.3*tp*Scaling
L14_width = 0.3*tp*Scaling
L15_width = 0.25*tp*Scaling
LB_width = 0.14*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_AND2_v2p1"
    def create_elements(self, elems):
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        M0blocks = spira.SRef(M0_blocks())
        tblocks = spira.SRef(trackblocks())
        M0tracks = spira.SRef(M0_tracks())
        IXports = spira.SRef(IX_ports())
        M6Strips = spira.SRef(M6_strips())
        # Ports for inductor connections
        # Bias1
        PB1N = spira.Port(name="PB1N",midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name="PB1S",midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias2
        PB2W = spira.Port(name="PB2W",midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2E = spira.Port(name="PB2E",midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias3
        PB3N = spira.Port(name="PB3N",midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3S = spira.Port(name="PB3S",midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias4
        PB4W = spira.Port(name="PB4W",midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4E = spira.Port(name="PB4E",midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias5
        PB5W = spira.Port(name="PB5W",midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5E = spira.Port(name="PB5E",midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias6
        PB6W = spira.Port(name="PB6W",midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6E = spira.Port(name="PB6E",midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias7
        PB7W = spira.Port(name="PB7W",midpoint=bias.reference.elements['bias7'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7E = spira.Port(name="PB7E",midpoint=bias.reference.elements['bias7'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Ends
        PB1_end = spira.Port(name="PB1_end",midpoint=(3.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PB2_end = spira.Port(name="PB2_end",midpoint=(2.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
        PB3_end = spira.Port(name="PB3_end",midpoint=(6.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PB4_end = spira.Port(name="PB4_end",midpoint=(6.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
        # JJ1
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ2
        PJ2N = spira.Port(name="PJ2N",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ2S = spira.Port(name="PJ2S",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ3
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ4
        PJ4W = spira.Port(name="PJ4W",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ4E = spira.Port(name="PJ4E",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        # JJ5
        PJ5 = spira.Port(name="PJ5",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ6
        PJ6N = spira.Port(name="PJ6N",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ6E = spira.Port(name="PJ6E",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        # JJ7
        PJ7 = spira.Port(name="PJ7",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ8
        PJ8N = spira.Port(name="PJ8N",midpoint=jjs.reference.elements['J8'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ8S = spira.Port(name="PJ8S",midpoint=jjs.reference.elements['J8'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ9
        PJ9 = spira.Port(name="PJ9",midpoint=jjs.reference.elements['J9'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ10
        PJ10W = spira.Port(name="PJ10W",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ10E = spira.Port(name="PJ10E",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ11
        PJ11 = spira.Port(name="PJ11",midpoint=jjs.reference.elements['J11'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ12
        PJ12W = spira.Port(name="PJ12W",midpoint=jjs.reference.elements['J12'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M5)
        PJ12N = spira.Port(name="PJ12N",midpoint=jjs.reference.elements['J12'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # JJ13
        PJ13 = spira.Port(name="PJ13",midpoint=jjs.reference.elements['J13'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ13_L = spira.Port(name="PJ13_L",midpoint=(4.0*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        # JJ14
        PJ14 = spira.Port(name="PJ14",midpoint=jjs.reference.elements['J14'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ14_L = spira.Port(name="PJ14_L",midpoint=(5.0*tp,4.455*tp),process=spira.RDD.PROCESS.M6)
        # JJ15
        PJ15 = spira.Port(name="PJ15",midpoint=jjs.reference.elements['J15'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # VIA A
        PVAN = spira.Port(name="PVAN",midpoint=vias.reference.elements['viaA'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PVAS = spira.Port(name="PVAS",midpoint=vias.reference.elements['viaA'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        # VIA B
        PVBN = spira.Port(name="PVBN",midpoint=vias.reference.elements['viaB'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PVBS = spira.Port(name="PVBS",midpoint=vias.reference.elements['viaB'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        # VIA CLK
        PVCLKN = spira.Port(name="PVCLKN",midpoint=vias.reference.elements['viaCLK'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PVCLK = spira.Port(name="PVCLK",midpoint=vias.reference.elements['viaCLK'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        # VIA Q
        PVQ = spira.Port(name="PVQ",midpoint=vias.reference.elements['viaQ'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M5)
        PVQS = spira.Port(name="PVQS",midpoint=vias.reference.elements['viaQ'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pins
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center,process=spira.RDD.PROCESS.M6)
        PB_post = spira.Port(name="PB_post",midpoint=IXports.reference.elements['B'].center-(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        PQ_post = spira.Port(name="PQ_post",midpoint=IXports.reference.elements['Q'].center+(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center,process=spira.RDD.PROCESS.M6)
        PCLK_post = spira.Port(name="PCLK_post",midpoint=IXports.reference.elements['CLK'].center-(0,0.2*tp),process=spira.RDD.PROCESS.M6)
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[((PA.x+PJ1.x)/2,(PA.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['A'].bbox_info.height,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[((PA_post.x+PJ1.x)/2,(PA_post.y+PJ1.y)/2)],start_straight=False,end_straight=False,width=L1_width,layer=sc.M6)
        L2S = spira.RoutePath(port1=PJ1,port2=PJ2S,path=[((PJ1.x+PJ2S.x)/2,(PJ1.y+PJ2S.y)/2)],start_straight=False,end_straight=False,width=L2S_width,layer=sc.M6)
        L2NM5 = spira.RoutePath(port1=PJ2N,port2=PVAS,path=[((PJ2N.x+PVAS.x)/2,(PJ2N.y+PVAS.y)/2)],start_straight=False,end_straight=False,width=L2NM5_width,layer=sc.M5)
        L2NM6 = spira.RoutePath(port1=PVAN,port2=PJ3,path=[((PVAN.x+PJ3.x)/2,(PVAN.y+PJ3.y)/2)],start_straight=False,end_straight=False,width=L2NM6_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PJ3,port2=PJ5,path=[(3.5*tp,5.5*tp),(3.5*tp,4.5*tp),(2.5*tp,4.5*tp),(2.5*tp,3.5*tp)],start_straight=False,end_straight=False,width=L3_width,layer=sc.M6)
        L4W = spira.RoutePath(port1=PJ5,port2=PJ4W,path=[((PJ5.x+PJ4W.x)/2,PJ5.y),((PJ5.x+PJ4W.x)/2,PJ4W.y)],start_straight=False,end_straight=False,width=L4W_width,layer=sc.M6)
        L4E = spira.RoutePath(port1=PJ4E,port2=PVCLK,path=[((PJ4E.x+PVCLK.x)/2,PJ4E.y),((PJ4E.x+PVCLK.x)/2,PVCLK.y)],start_straight=False,end_straight=False,width=L4E_width,layer=sc.M5)
        L5N = spira.RoutePath(port1=PJ5,port2=PJ6N,path=[((PJ5.x+PJ6N.x)/2,(PJ5.y+PJ6N.y)/2)],start_straight=False,end_straight=False,width=L5N_width,layer=sc.M6)
        L5E = spira.RoutePath(port1=PJ6E,port2=PVQ,path=[((PJ6E.x+PVQ.x)/2,(PJ6E.y+PVQ.y)/2)],start_straight=False,end_straight=False,width=L5E_width,layer=sc.M5)
        L6 = spira.RoutePath(port1=PB,port2=PJ7,path=[((PB.x+PJ7.x)/2,(PB.y+PJ7.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['B'].bbox_info.height,layer=sc.M6)
        L6_post = spira.RoutePath(port1=PB_post,port2=PJ7,path=[((PB_post.x+PJ7.x)/2,(PB_post.y+PJ7.y)/2)],start_straight=False,end_straight=False,width=L6_width,layer=sc.M6)
        L7S = spira.RoutePath(port1=PJ7,port2=PJ8S,path=[((PJ7.x+PJ8S.x)/2,(PJ7.y+PJ8S.y)/2)],start_straight=False,end_straight=False,width=L7S_width,layer=sc.M6)
        L7NM5 = spira.RoutePath(port1=PJ8N,port2=PVBS,path=[((PJ8N.x+PVBS.x)/2,(PJ8N.y+PVBS.y)/2)],start_straight=False,end_straight=False,width=L7NM5_width,layer=sc.M5)
        L7NM6 = spira.RoutePath(port1=PVBN,port2=PJ9,path=[((PVBN.x+PJ9.x)/2,(PVBN.y+PJ9.y)/2)],start_straight=False,end_straight=False,width=L7NM6_width,layer=sc.M6)
        L8 = spira.RoutePath(port1=PJ9,port2=PJ11,path=[(5.5*tp,5.5*tp),(5.5*tp,4.5*tp),(6.5*tp,4.5*tp),(6.5*tp,3.5*tp)],start_straight=False,end_straight=False,width=L8_width,layer=sc.M6)
        L9E = spira.RoutePath(port1=PJ11,port2=PJ10E,path=[((PJ11.x+PJ10E.x)/2,PJ11.y),((PJ11.x+PJ10E.x)/2,PJ10E.y)],start_straight=False,end_straight=False,width=L9E_width,layer=sc.M6)
        L9W = spira.RoutePath(port1=PJ10W,port2=PVCLK,path=[((PJ10W.x+PVCLK.x)/2,PJ10W.y),((PJ10W.x+PVCLK.x)/2,PVCLK.y)],start_straight=False,end_straight=False,width=L9W_width,layer=sc.M5)
        L10N = spira.RoutePath(port1=PJ11,port2=PJ12N,path=[((PJ11.x+PJ12N.x)/2,(PJ11.y+PJ12N.y)/2)],start_straight=False,end_straight=False,width=L10N_width,layer=sc.M6)
        L10E = spira.RoutePath(port1=PJ12W,port2=PVQ,path=[((PJ12W.x+PVQ.x)/2,(PJ12W.y+PVQ.y)/2)],start_straight=False,end_straight=False,width=L10E_width,layer=sc.M5)
        L11 = spira.RoutePath(port1=PCLK,port2=PJ13,path=[((PCLK.x+PJ13.x)/2,(PCLK.y+PJ13.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['CLK'].bbox_info.width,layer=sc.M6)
        L11_post = spira.RoutePath(port1=PCLK_post,port2=PJ13,path=[((PCLK_post.x+PJ13.x)/2,(PCLK_post.y+PJ13.y)/2)],start_straight=False,end_straight=False,width=L11_width,layer=sc.M6)
        LJ13 = spira.RoutePath(port1=PJ13,port2=PJ13_L,path=[((PJ13.x+PJ13_L.x)/2,(PJ13.y+PJ13_L.y)/2)],start_straight=False,end_straight=False,width=LJ13_width,layer=sc.M6)
        L12 = spira.RoutePath(port1=PJ13,port2=PJ14,path=[(4.5*tp,5.19*tp),(4.4*tp,5.19*tp),(4.4*tp,4.98*tp),(4.6*tp,4.98*tp),(4.6*tp,4.75*tp),(4.5*tp,4.75*tp)],start_straight=False,end_straight=False,width=L12_width,layer=sc.M6)
        LJ14 = spira.RoutePath(port1=PJ14,port2=PJ14_L,path=[((PJ14.x+PJ14_L.x)/2,(PJ14.y+PJ14_L.y)/2)],start_straight=False,end_straight=False,width=LJ14_width,layer=sc.M6)
        L13 = spira.RoutePath(port1=PJ14,port2=PVCLKN,path=[((PJ14.x+PVCLKN.x)/2,(PJ14.y+PVCLKN.y)/2)],start_straight=False,end_straight=False,width=L13_width,layer=sc.M6)
        L14 = spira.RoutePath(port1=PVQS,port2=PJ15,path=[((PVQS.x+PJ15.x)/2,(PVQS.y+PJ15.y)/2)],start_straight=False,end_straight=False,width=L14_width,layer=sc.M6)
        L15 = spira.RoutePath(port1=PJ15,port2=PQ,path=[((PJ15.x+PQ.x)/2,(PJ15.y+PQ.y)/2)],start_straight=False,end_straight=False,width=IXports.reference.elements['Q'].bbox_info.width,layer=sc.M6)
        L15_post = spira.RoutePath(port1=PJ15,port2=PQ_post,path=[((PJ15.x+PQ_post.x)/2,(PJ15.y+PQ_post.y)/2)],start_straight=False,end_straight=False,width=L15_width,layer=sc.M6)
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1N,path=[((PJ1.x+PB1N.x)/2,(PJ1.y+PB1N.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1S,port2=PB5W,path=[(PB1S.x,PB5W.y)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB1_3 = spira.RoutePath(port1=PB5E,port2=PB1_end,path=[((PB5E.x+PB1_end.x)/2,(PB5E.y+PB1_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2W,path=[(0.5*tp,5.5*tp),(0.5*tp,6.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2E,port2=PB2_end,path=[((PB2E.x+PB2_end.x)/2,(PB2E.y+PB2_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ7,port2=PB3N,path=[((PJ7.x+PB3N.x)/2,(PJ7.y+PB3N.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PJ15,port2=PB7W,path=[((PJ15.x+PB7W.x)/2,(PJ15.y+PB7W.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_3 = spira.RoutePath(port1=PB3S,port2=PB6E,path=[(7.5*tp,1.5*tp),(8.5*tp,1.5*tp),(8.5*tp,0.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_4 = spira.RoutePath(port1=PB7E,port2=PB6E,path=[(8.5*tp,1.5*tp),(8.5*tp,0.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB3_5 = spira.RoutePath(port1=PB6W,port2=PB3_end,path=[((PB6W.x+PB3_end.x)/2,(PB6W.y+PB3_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ9,port2=PB4E,path=[(8.5*tp,5.5*tp),(8.5*tp,6.5*tp)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4W,port2=PB4_end,path=[((PB4W.x+PB4_end.x)/2,(PB4W.y+PB4_end.y)/2)],start_straight=False,end_straight=False,width=LB_width,layer=sc.M6)
        elems += [L1, L1_post, L2S, L2NM5, L2NM6, L3, L4W, L4E, L5N, L5E,
                  L6, L6_post, L7S, L7NM5, L7NM6, L8, L9E, L9W, L10N, L10E,
                  L11, L11_post, LJ13, L12, LJ14, L13, L14, L15, L15_post]
        elems += [LB1_1, LB1_2, LB1_3, LB2_1, LB2_2, LB3_1, 
                  LB3_2, LB3_3, LB3_4, LB3_5, LB4_1, LB4_2]
        elems += [jjfill, M4M5M6M7conns, vias, bias, jjs, 
                  M0blocks, tblocks, M0tracks, IXports, M6Strips]
        elems += spira.Box(layer=sc.M4,width=0.25*tp,height=0.56*tp,center=(4.0*tp,4.0*tp))
        elems += spira.Box(layer=sc.M4,width=0.25*tp,height=0.51*tp,center=(5.0*tp,3.975*tp))
        elems += spira.Box(layer=sc.M7,width=0.25*tp,height=0.56*tp,center=(4.0*tp,4.0*tp))
        elems += spira.Box(layer=sc.M7,width=0.25*tp,height=0.56*tp,center=(5.0*tp,4.0*tp))
        # Text Labels
        elems += spira.Label(text="PB6 M6 M4",position=(7.24*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(2.81*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text="J14 M6 M5",position=(4.5*tp,4.455*tp),layer=TEXT)
        elems += spira.Label(text="J13 M6 M5",position=(4.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="PB7 M6 M4",position=(5.17*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="J15 M6 M5",position=(4.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="J12 M6 M5",position=(5.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(3.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(5.0*tp,3.43*tp),layer=TEXT)
        elems += spira.Label(text="J11 M6 M5",position=(5.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(8.34*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="J9 M6 M5",position=(7.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(7.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(7.5*tp,3.0*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(7.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(4.0*tp,3.43*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(3.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.5*tp,3.0*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(0.66*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(1.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P4 M6 M4",position=(4.5*tp,0.0*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(4.5*tp,7.0*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(9.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(0.0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_out",position=(9.0*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="clk",position=(4.5*tp,7.0*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(0.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(9.0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(4.5*tp,0.0*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='RIB7',position=(5.6025*tp,1.5025*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB6',position=(7.68*tp,0.4975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB5',position=(2.215*tp,0.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB4',position=(7.7425*tp,6.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(7.4975*tp,2.5775*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(1.275*tp,6.505*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.5025*tp,2.5625*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB15',position=(4.17*tp,1.495*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB14',position=(4.1725*tp,4.4525*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB13',position=(4.8325*tp,5.5025*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB12',position=(5.88*tp,2.505*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB11',position=(5.5075*tp,3.845*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB10',position=(5*tp,3.7925*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB9',position=(7.5*tp,5.8175*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB8',position=(7.79*tp,4.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB7',position=(7.175*tp,3.4975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB6',position=(3.145*tp,2.4975*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB5',position=(3.5025*tp,3.8475*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB4',position=(3.9975*tp,3.765*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(1.4925*tp,5.8025*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(1.2*tp,4.5*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB1',position=(1.79*tp,3.5025*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='q',position=(4.4075*tp,0.005*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='b',position=(8.995*tp,3.4075*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='clk',position=(4.4075*tp,6.995*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='a',position=(0.005*tp,3.405*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='GND',position=(0.5025*tp,6.92*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='VDD',position=(0.235*tp,6.555*tp),layer=spira.Layer(number=1,datatype=1))
        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.04*tp,height=0.315*tp,center=(8.98*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.03*tp,center=(6.4925*tp,6.985*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.03*tp,center=(3.5075*tp,0.015*tp))
        elems += spira.Box(layer=sc.M6,width=0.035*tp,height=0.315*tp,center=(0.0175*tp,6.5075*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.03*tp,center=(2.5075*tp,6.985*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.03*tp,center=(6.5075*tp,0.015*tp))
        elems += spira.Box(layer=sc.M6,width=0.33*tp,height=0.03*tp,center=(8.5*tp,6.985*tp))
        elems += spira.Box(layer=sc.M5,width=0.04*tp,height=0.315*tp,center=(8.98*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.03*tp,center=(6.4925*tp,6.985*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.03*tp,center=(3.5075*tp,0.015*tp))
        elems += spira.Box(layer=sc.M5,width=0.035*tp,height=0.315*tp,center=(0.0175*tp,6.5075*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.03*tp,center=(2.5075*tp,6.985*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.03*tp,center=(6.5075*tp,0.015*tp))
        elems += spira.Box(layer=sc.M5,width=0.33*tp,height=0.03*tp,center=(8.5*tp,6.985*tp))

        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(4.5*tp,0.0*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.2*tp,height=0*tp,center=(4.5*tp,7.0*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(9.0*tp,3.5*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.173*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.81*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.238*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.5*tp,2.997*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(8.34*tp,6.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.66*tp,6.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.5*tp,2.997*tp))
        return elems

class M0_tracks(spira.Cell):
    __name_prefix__ = "M0_tracks"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=0.75*tp,center=(4.98*tp,5.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.2*tp,height=5.0*tp,center=(1.5*tp,4.0*tp))
        elems += spira.Box(layer=sc.M0,width=0.2*tp,height=5.0*tp,center=(7.5*tp,4.0*tp))
        elems += spira.Box(layer=sc.M0,width=9.0*tp,height=0.3*tp,center=(4.5*tp,6.5*tp))
        elems += spira.Polygon(shape=spira.Shape(
            points=[(3.4*tp,0.5*tp),(3.4*tp,5.5*tp),(4.0*tp,5.5*tp),
                    (4.0*tp,5.3*tp),(3.6*tp,5.3*tp),(3.6*tp,0.5*tp)]),layer=sc.M0)
        elems += spira.Polygon(shape=spira.Shape(
            points=[(5.0*tp,4.4*tp),(5.0*tp,4.6*tp),(5.6*tp,4.6*tp),
                    (5.6*tp,0.6*tp),(6.5*tp,0.6*tp),(6.5*tp,0.4*tp),
                    (5.4*tp,0.4*tp),(5.4*tp,4.4*tp)]),layer=sc.M0)
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(6.5*tp,0.98*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(1.02*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(1.5*tp,1.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(1.98*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(2.5*tp,6.06*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=5.75*tp,center=(3.02*tp,3.0*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=3.75*tp,center=(3.98*tp,2.0*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(4.5*tp,4.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=3.75*tp,center=(5.02*tp,2.0*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=3.75*tp,center=(5.98*tp,3.0*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(5.5*tp,4.98*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(7.5*tp,1.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(7.98*tp,3.5*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(0.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(2.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(5.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(6.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.75*tp,height=0.04*tp,center=(8.5*tp,6.02*tp))
        elems += spira.Box(layer=sc.M0,width=0.04*tp,height=4.75*tp,center=(7.02*tp,3.5*tp))
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding 3um junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(0.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(5.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(8.5*tp,2.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(3.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(3.0*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(0.5*tp,1.0*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(0.5*tp,2.0*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(0.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(2.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(3.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(0.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(), midpoint=(5.5*tp,6.5*tp))
        sys.stdout.write("Adding 1.5um junction fill.\n")
        for y in range(1, 7):
            for x in range(1, 9):
                if(x in [4, 5] and y == 4):
                    pass
                else:
                    elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(), midpoint=(0.0+x*tp,0.0+y*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,5.06*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,1.93*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,2.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,1.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,1.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,2.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.855*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,1.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,1.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.05*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.78*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,5.08*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,6.83*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.125*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.845*tp,0.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.435*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.125*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.075*tp,0.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.845*tp,1.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.015*tp,0.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.015*tp,1.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.82*tp,0.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.295*tp,4.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.735*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.445*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.125*tp,0.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.735*tp,0.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.125*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.735*tp,2.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.735*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.015*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.735*tp,6.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.735*tp,5.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.735*tp,1.335*tp),transformation=sc.m45)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,2.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,5.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,1.835*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,6.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,6.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.665*tp,3.065*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,5.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,5.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,4.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,6.835*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,3.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.66*tp,0.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,2.835*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.66*tp,0.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.66*tp,0.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.665*tp,0.025*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,0.845*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.665*tp,0.025*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.985*tp,6.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.91*tp,4.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.215*tp,4.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.91*tp,4.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.69*tp,4.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.215*tp,4.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.175*tp,6.665*tp),transformation=sc.m135)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(1.415*tp,4.915*tp),alias="viaA")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.415*tp,3.415*tp),alias="viaCLK")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.415*tp,2.415*tp),alias="viaQ")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(7.415*tp,4.915*tp),alias="viaB")
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(1.5*tp,2.045*tp),alias="bias1")
        elems += spira.SRef(sc.ls_ib_123(),midpoint=(0.605*tp,6.5*tp),transformation=sc.r270,alias="bias2")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(7.5*tp,2.045*tp),alias="bias3")
        elems += spira.SRef(sc.ls_ib_123(),midpoint=(7.0175*tp,6.5*tp),transformation=sc.r270,alias="bias4")
        elems += spira.SRef(sc.ls_ib_133(),midpoint=(2.865*tp,0.5*tp),transformation=sc.r90,alias="bias5")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(8.19*tp,0.5*tp),transformation=sc.r90,alias="bias6")
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(6.125*tp,1.5*tp),transformation=sc.r90,alias="bias7")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,3.5*tp),transformation=sc.r270,alias="J1")
        elems += spira.SRef(sc.ls_jj_201_s(),midpoint=(1.5*tp,4.5*tp),transformation=sc.r90,alias="J2")
        elems += spira.SRef(sc.ls_jj_191_sg(),midpoint=(1.5*tp,5.5*tp),alias="J3")
        elems += spira.SRef(sc.ls_jj_126_s(),midpoint=(4*tp,3.43*tp),alias="J4")
        elems += spira.SRef(sc.ls_jj_157_sg(),midpoint=(3.5*tp,3.5*tp),alias="J5")
        elems += spira.SRef(sc.ls_jj_119_s(),midpoint=(3.5*tp,2.5*tp),transformation=sc.r90,alias="J6")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(7.5*tp,3.5*tp),transformation=sc.r90,alias="J7")
        elems += spira.SRef(sc.ls_jj_201_s(),midpoint=(7.5*tp,4.5*tp),transformation=sc.r270,alias="J8")
        elems += spira.SRef(sc.ls_jj_191_sg(),midpoint=(7.5*tp,5.5*tp),alias="J9")
        elems += spira.SRef(sc.ls_jj_126_s(),midpoint=(5*tp,3.43*tp),alias="J10")
        elems += spira.SRef(sc.ls_jj_157_sg(),midpoint=(5.5*tp,3.5*tp),alias="J11")
        elems += spira.SRef(sc.ls_jj_119_s(),midpoint=(5.5*tp,2.5*tp),transformation=sc.r270,alias="J12")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(4.5*tp,5.5*tp),transformation=sc.r270,alias="J13")
        elems += spira.SRef(sc.ls_jj_206_sg(),midpoint=(4.5*tp,4.455*tp),transformation=sc.r90,alias="J14")
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(4.5*tp,1.5*tp),transformation=sc.r90,alias="J15")
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding M0 trackblocks.\n")
        for y in range(0, 6):
            for x in range(0, 9):
                if (x == 1 and y == 0) or (x == 5 and y == 5) or (x == 7 and y == 0):
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                elif (x == 4 and y in [4,5]) or (x == 6 and y == 0):
                    pass
                elif x in [0,2,4,6,8]:
                    elems += spira.SRef(sc.ls_tr_M0(), midpoint=(0+x*tp,0+y*tp))
                else:
                    pass
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 9):
                if (x == 1 and y == 1) or (x == 2 and y == 6) or (x == 3 and y == 0) or (x == 6 and y == 0) or (x == 6 and y == 6) or (x == 7 and y == 1):
                    elems += spira.SRef(sc.ls_tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 3 and y == 5) or (x == 4 and y == 4):
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter1(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter2(),midpoint=(0+x*tp,tp+y*tp), transformation=sc.r180)
                    elems += spira.SRef(sc.ls_tr_bias_pillar_half(),midpoint=(tp/2+x*tp,0+y*tp))
                elif (x == 4 and y == 5) or (x == 5 and y == 4):
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter1(),midpoint=(tp+x*tp,tp+y*tp), transformation=sc.r180)
                    elems += spira.SRef(sc.ls_tr_u_M4_quarter2(),midpoint=(tp+x*tp,0+y*tp))
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