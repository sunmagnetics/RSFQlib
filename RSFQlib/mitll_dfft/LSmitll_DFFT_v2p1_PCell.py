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
L1_width = 0.14*tp*Scaling
L2_width = 0.12*tp*Scaling
L3_width = 0.12*tp*Scaling
L4_width = 0.12*tp*Scaling
L5_width = 0.135*tp*Scaling
L6_width = 0.14*tp*Scaling
L7_width = 0.165*tp*Scaling
L8_width = 0.17*tp*Scaling
L9_width = 0.115*tp*Scaling
L10_width = 0.115*tp*Scaling
L11_width = 0.1*tp*Scaling
L12_width = 0.11*tp*Scaling
L13_width = 0.13*tp*Scaling
LB_width = 0.14*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_DFFT_v2p1"
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
        PB2W = spira.Port(name='PB2W',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2E = spira.Port(name='PB2E',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3W = spira.Port(name='PB3W',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3E = spira.Port(name='PB3E',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4N = spira.Port(name='PB4N',midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name='PB4S',midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(6.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1N = spira.Port(name='PR1N',midpoint=res.reference.elements['R1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1S = spira.Port(name='PR1S',midpoint=res.reference.elements['R1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Junction ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ5 = spira.Port(name="PJ5",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ6 = spira.Port(name="PJ6",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ7 = spira.Port(name="PJ7",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ8 = spira.Port(name="PJ8",midpoint=jjs.reference.elements['J8'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ9 = spira.Port(name="PJ9",midpoint=jjs.reference.elements['J9'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ10 = spira.Port(name="PJ10",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=(6.5*tp,1.545*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN5 = spira.Port(name="PN5",midpoint=(2.5*tp,3.09*tp),process=spira.RDD.PROCESS.M6)
        PN15 = spira.Port(name="PN15",midpoint=(2.5*tp,3.61*tp),process=spira.RDD.PROCESS.M6)
        PN23 = spira.Port(name="PN23",midpoint=(PJ10.x,PJ9.y),process=spira.RDD.PROCESS.M6)
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PJ1.x,PA.y)],width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PN5,path=[(PN5.x,PJ1.y)],width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PN5,port2=PJ2,path=[(PJ2.x,PN5.y)],width=L3_width,layer=sc.M6)
        L4_1 = spira.RoutePath(port1=PJ2,port2=PV1,path=[(PJ2.x,PV1.y)],width=L4_width,layer=sc.M6)
        L4_2 = spira.RoutePath(port1=PV1,port2=PJ3,path=[(PV1.x,PJ3.y)],width=L4_width,layer=sc.M5)
        L4_3 = spira.RoutePath(port1=PJ3,port2=PJ4,path=[(PJ3.x,PJ4.y)],width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PJ4,port2=PJ5,path=[(PJ5.x,PJ4.y)],width=L5_width,layer=sc.M6)
        L6 = spira.RoutePath(port1=PCLK,port2=PJ6,path=[(PCLK.x,PJ6.y)],width=L6_width,layer=sc.M6)
        L7 = spira.RoutePath(port1=PJ6,port2=PN15,path=[(PJ6.x,PN15.y)],width=L7_width,layer=sc.M6)
        L8 = spira.RoutePath(port1=PN15,port2=PJ7,path=[(PJ7.x,PN15.y)],width=L8_width,layer=sc.M6)
        L9_1 = spira.RoutePath(port1=PJ7,port2=PV2,path=[(PJ7.x,PV2.y)],width=L9_width,layer=sc.M6)
        L9_2 = spira.RoutePath(port1=PV2,port2=PJ8,path=[(PJ8.x,PV2.y)],width=L9_width,layer=sc.M5)
        L9_3 = spira.RoutePath(port1=PJ8,port2=PJ5,path=[(PJ8.x,PJ5.y)],width=L9_width,layer=sc.M6)
        L10 = spira.RoutePath(port1=PJ5,port2=PJ9,path=[(PJ9.x,PJ5.y)],width=L10_width,layer=sc.M6)
        L11 = spira.RoutePath(port1=PJ9,port2=PN23,path=[(PN23.x,PJ9.y)],width=L11_width,layer=sc.M6)
        L12 = spira.RoutePath(port1=PN23,port2=PJ10,path=[(PJ10.x,PN23.y)],width=L12_width,layer=sc.M6)
        L13_1 = spira.RoutePath(port1=PJ10,port2=PR1N,path=[(PR1N.x,PJ10.y)],width=L13_width,layer=sc.M6)
        L13_2 = spira.RoutePath(port1=PR1S,port2=PQ,path=[(PR1S.x,PQ.y)],width=L13_width,layer=sc.M6)

        elems += [L1, L2, L3, L4_1, L4_2, L4_3, L5, L6, L7, L8, L9_1, L9_2, L9_3, L10, L11, L12, L13_1, L13_2]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PN5,port2=PB1E,path=[(PB1E.x,PN5.y)],width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PV3,path=[(0.5*tp,PB1W.y),(0.5*tp,PV3.y)],width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ3,port2=PB2E,path=[(PJ3.x,PB2E.y)],width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2W,port2=PV3,path=[(0.5*tp,PB2W.y),(0.5*tp,PV3.y)],width=LB_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PN15,port2=PB3E,path=[(1.56*tp,PN15.y),(1.56*tp,PB3E.y)],width=LB_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PV3,path=[(0.5*tp,PB3W.y),(0.5*tp,PV3.y)],width=LB_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PN23,port2=PB4S,path=[(PN23.x,PB4S.y)],width=LB_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4N,port2=PV3,path=[(PB4N.x,PV3.y)],width=LB_width,layer=sc.M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2]

        LBias = spira.RoutePath(port1=PV3,port2=PBias,path=[(PBias.x,PBias.y)],width=LB_width,layer=sc.M6)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="bias",position=(6.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(6.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(1.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="clk",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(7.4985*tp,4.4015*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.815*tp,5.5025*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(2.515*tp,5.49*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(1.2225*tp,3.61*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(3.5*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(5.4975*tp,4.495*tp),layer=TEXT)
        elems += spira.Label(text="J8 M5 M6",position=(4.5025*tp,4.4925*tp),layer=TEXT)
        elems += spira.Label(text="J9 M6 M5",position=(6.5*tp,3.495*tp),layer=TEXT)
        elems += spira.Label(text="J3 M5 M6",position=(4.51*tp,2.495*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.2795*tp,2.4945*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(7.5*tp,2.495*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(3.505*tp,2.4775*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(6.497*tp,2.2525*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.8225*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(2.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(4.505*tp,1.4975*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(4.229*tp,0.501*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(6.5016*tp,6.8268*tp),layer=spira.Layer(number=50,datatype=1))
        elems += spira.Label(text='GND',position=(6.6306*tp,6.8413*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='RB1',position=(2.847*tp,1.4959*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(3.497*tp,2.1487*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(4.4876*tp,2.8441*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB4',position=(4.164*tp,1.5072*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB5',position=(5.503*tp,4.836*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB6',position=(2.8526*tp,5.4924*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB7',position=(3.4948*tp,4.8254*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB8',position=(4.5025*tp,4.8076*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB9',position=(6.4972*tp,3.1847*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB10',position=(7.5006*tp,2.1927*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RD',position=(6.5029*tp,2.1459*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.0112*tp,2.4925*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(3.9516*tp,0.4879*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(0.9605*tp,3.6037*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB4',position=(7.5026*tp,4.6687*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='a',position=(1.5023*tp,1.5017*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='clk',position=(1.4987*tp,5.5037*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q',position=(6.4999*tp,1.5023*tp),layer=spira.Layer(number=60,datatype=1))
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,2.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,2.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(7.9875*tp,6.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(3.5*tp,1.29*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(4.5*tp,3.71*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(3.5*tp,5.71*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(4.5*tp,5.71*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(5.5*tp,5.71*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(7.5*tp,1.13*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(7.5*tp,0.71*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(6.5*tp,5.29*tp))
        elems += spira.Box(layer=sc.M5,width=0.25*tp,height=0.02*tp,center=(6.5*tp,5.71*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(1.5*tp,4.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(6.23*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(5.81*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(5.39*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(4.97*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(4.5*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(4.13*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(7.09*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(6.67*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(6.25*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(5.83*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(5.41*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.25*tp,center=(7.51*tp,0.575*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(3.71*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.25*tp,center=(6.65*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(4.5*tp,3.5*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.815*tp,5.5075*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.82*tp,1.49875*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.28*tp,2.495*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.23*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.5*tp,2.256*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.5*tp,4.4*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.225*tp,3.61*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(2.72*tp,2.72*tp),(2.72*tp,2.96*tp),(3.28*tp,2.96*tp),(3.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(1.72*tp,3.04*tp),(1.72*tp,3.28*tp),(3.28*tp,3.28*tp),(3.28*tp,3.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(2.72*tp,3.72*tp),(2.72*tp,3.96*tp),(3.28*tp,3.96*tp),(3.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6.785*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3.5*tp,5.845*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6.5*tp,5.155*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5.5*tp,5.845*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6.5*tp,5.845*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4.5*tp,3.845*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4.5*tp,5.845*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7.645*tp,0.575*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3.505*tp,1.155*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.29*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.29*tp,3.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.76*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7.3*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.92*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.71*tp,3.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.44*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.18*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(4.34*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.6*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.46*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.71*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,1.34*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.88*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.62*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.04*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.2*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,0.92*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.02*tp,5.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.3325*tp,1.0125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.3275*tp,5.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.7725*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.3425*tp,1.85*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.3425*tp,2.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.2275*tp,3.28*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.6625*tp,3.28*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,1.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.155*tp,3.28*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.325*tp,1.065*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.165*tp,3.28*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.6425*tp,3.28*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,4.1075*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.3275*tp,4.7625*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.3275*tp,3.79*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.8825*tp,2.5*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.155*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.2375*tp,2.3325*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.89*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.8875*tp,3.3475*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.27*tp,3.3325*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.88*tp,3.33*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.235*tp,3.33*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.215*tp,2.345*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.875*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.245*tp,2.3225*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.915*tp,2.3225*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.215*tp,2.5*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.89*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.975*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.975*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.165*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.9325*tp,4.32*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.96*tp,2.3325*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.975*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.2075*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.2625*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.905*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.165*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=sc.r90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(3.915*tp,2.415*tp),alias='via1')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(3.915*tp,4.4125*tp),alias='via2')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(6.4175*tp,6.42*tp),alias='via3')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_235(),midpoint=(4.285*tp,0.5*tp),transformation=sc.r90,alias='bias2')
        elems += spira.SRef(sc.ls_ib_276(),midpoint=(1.335*tp,2.495*tp),transformation=sc.r90,alias='bias1')
        elems += spira.SRef(sc.ls_ib_284(),midpoint=(1.28*tp,3.61*tp),transformation=sc.r90,alias='bias3')
        elems += spira.SRef(sc.ls_ib_312(),midpoint=(7.5*tp,4.345*tp),alias='bias4')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_162_sg(),midpoint=(2.5*tp,5.5*tp),transformation=sc.r270,alias='J6')
        elems += spira.SRef(sc.ls_jj_162_sg(),midpoint=(2.5*tp,1.5*tp),transformation=sc.r270,alias='J1')
        elems += spira.SRef(sc.ls_jj_171_s(),midpoint=(4.5*tp,2.5*tp),alias='J3')
        elems += spira.SRef(sc.ls_jj_171_s(),midpoint=(4.5*tp,4.5*tp),alias='J8')
        elems += spira.SRef(sc.ls_jj_189_sg(),midpoint=(3.5*tp,2.5*tp),transformation=sc.r180,alias='J2')
        elems += spira.SRef(sc.ls_jj_198_sg(),midpoint=(3.5*tp,4.5*tp),alias='J7')
        elems += spira.SRef(sc.ls_jj_212_sg(),midpoint=(5.5*tp,4.5*tp),alias='J5')
        elems += spira.SRef(sc.ls_jj_212_sg(),midpoint=(6.5*tp,3.5*tp),transformation=sc.r180,alias='J9')
        elems += spira.SRef(sc.ls_jj_232_sg(),midpoint=(4.5*tp,1.5*tp),transformation=sc.r90,alias='J4')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(7.5*tp,2.5*tp),transformation=sc.r180,alias='J10')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_res_1p36(),midpoint=(6.5*tp,2*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 8):
                if (x == 1 and y in [1,5]) or (x == 6 and y == 1):
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