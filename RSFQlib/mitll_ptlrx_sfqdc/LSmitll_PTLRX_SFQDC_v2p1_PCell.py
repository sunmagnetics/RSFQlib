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
L2_width = 0.2*tp*Scaling
L3_width = 0.165*tp*Scaling
L4_width = 0.1*tp*Scaling
L5_width = 0.13*tp*Scaling
L6_width = 0.145*tp*Scaling
L7_width = 0.25*tp*Scaling
L9_width = 0.13*tp*Scaling
L10_width = 0.1*tp*Scaling
L11_width = 0.2*tp*Scaling
L12_width = 0.155*tp*Scaling
L14_width = 0.3*tp*Scaling
L15_width = 0.18*tp*Scaling
L16_width = 0.16*tp*Scaling
L17_width = 0.115*tp*Scaling
L18_width = 0.2*tp*Scaling
LB1_width = 0.14*tp*Scaling
LB2_width = 0.2*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_PTLRX_SFQDC_v2p1"
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
        PB4N = spira.Port(name='PB4N',midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4S = spira.Port(name='PB4S',midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5W = spira.Port(name='PB5W',midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5E = spira.Port(name='PB5E',midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(8.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1W = spira.Port(name='PR1W',midpoint=res.reference.elements['R1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1E = spira.Port(name='PR1E',midpoint=res.reference.elements['R1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
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
        PJ11 = spira.Port(name="PJ11",midpoint=jjs.reference.elements['J11'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=IXports.reference.elements['Q'].center,process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN5 = spira.Port(name="PN5",midpoint=(2.5*tp,4.5*tp),process=spira.RDD.PROCESS.M6)
        PN33 = spira.Port(name="PN33",midpoint=(8.5*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        PGND = spira.Port(name="PGND",midpoint=(6.2375*tp,3.5*tp),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PA.x,PJ1.y)],width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PN5,path=[(3.495*tp,PJ1.y),(3.495*tp,PN5.y)],width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PN5,port2=PJ2,path=[(PN5.x,3.5*tp),(PJ2.x,3.5*tp)],width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PJ2,port2=PJ3,path=[(1.91*tp,PJ2.y),(1.91*tp,2.6025*tp),(2.41*tp,2.6025*tp),
                                                       (2.41*tp,2.3925*tp),(3.045*tp,2.3925*tp),(3.045*tp,PJ3.y)],width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PJ3,port2=PJ4,path=[(PJ3.x,PJ4.y)],width=L5_width,layer=sc.M6)
        L6 = spira.RoutePath(port1=PJ4,port2=PV1,path=[(PJ4.x,PV1.y)],width=L6_width,layer=sc.M6)
        L7_1 = spira.RoutePath(port1=PV1,port2=PJ5,path=[(PV1.x,PJ5.y)],width=L7_width,layer=sc.M5)
        L7_2 = spira.RoutePath(port1=PJ5,port2=PJ6,path=[(PJ5.x,PJ6.y)],width=L7_width,layer=sc.M6)
        L9 = spira.RoutePath(port1=PJ6,port2=PV2,path=[(PV2.x,PJ6.y)],width=L9_width,layer=sc.M6)
        L10_1 = spira.RoutePath(port1=PV1,port2=PJ7,path=[(PV1.x,(PV1.y+PJ7.y)/2),(PJ7.x,(PV1.y+PJ7.y)/2)],width=L10_width,layer=sc.M5)
        L10_2 = spira.RoutePath(port1=PJ7,port2=PJ8,path=[((PJ7.x+PJ8.x)/2,PJ7.y),((PJ7.x+PJ8.x)/2,PJ8.y)],width=L10_width,layer=sc.M6)
        L11 = spira.RoutePath(port1=PJ8,port2=PV2,path=[(PJ8.x,2.8625*tp),(PV2.x,2.8625*tp)],width=L11_width,layer=sc.M6)
        L12 = spira.RoutePath(port1=PV2,port2=PR1E,path=[(PV2.x,PR1E.y)],width=L12_width,layer=sc.M6)
        L14 = spira.RoutePath(port1=PV2,port2=PJ9,path=[(PV2.x,PJ9.y)],width=L14_width,layer=sc.M5)
        L15 = spira.RoutePath(port1=PJ9,port2=PJ10,path=[(PJ10.x,PJ9.y)],width=L15_width,layer=sc.M6)
        L16 = spira.RoutePath(port1=PJ10,port2=PN33,path=[(PN33.x,PJ10.y)],width=L16_width,layer=sc.M6)
        L17 = spira.RoutePath(port1=PN33,port2=PJ11,path=[(PN33.x,PJ11.y)],width=L17_width,layer=sc.M6)
        L18 = spira.RoutePath(port1=PJ11,port2=PQ,path=[(PJ11.x,PQ.y)],width=L18_width,layer=sc.M6)


        elems += [L1, L2, L3, L4, L5, L6, L7_1, L7_2, L9, 
                  L10_1, L10_2, L11, L12, L14, L15, L16, L17, L18]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PN5,port2=PB1E,path=[(PN5.x,PB1E.y)],width=LB1_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PV3,path=[(0.5*tp,PB1W.y),(0.5*tp,PV3.y)],width=LB2_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ4,port2=PB2N,path=[(PJ4.x,PB2N.y)],width=LB1_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2S,port2=PV3,path=[(PB2S.x,0.5*tp),(0.5*tp,0.5*tp),(0.5*tp,PV3.y)],width=LB2_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ6,port2=PB3S,path=[(PB3S.x,PJ6.y)],width=LB1_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3N,port2=PV3,path=[(PB3N.x,PV3.y)],width=LB2_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ9,port2=PB4S,path=[(PJ9.x,4.1225*tp),(PB4S.x,4.1225*tp)],width=LB1_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4N,port2=PV3,path=[(PB4N.x,PV3.y)],width=LB2_width,layer=sc.M6)
        LB5_1 = spira.RoutePath(port1=PN33,port2=PB5E,path=[(PB5E.x,PN33.y)],width=LB1_width,layer=sc.M6)
        LB5_2 = spira.RoutePath(port1=PB5W,port2=PV3,path=[(0.5*tp,PB5W.y),(0.5*tp,PV3.y)],width=LB2_width,layer=sc.M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2, LB3_1, LB3_2, LB4_1, LB4_2, LB5_1, LB5_2]

        LGND = spira.RoutePath(port1=PR1W,port2=PGND,path=[(PGND.x,PGND.y)],width=L12_width,layer=sc.M6)
        LBias = spira.RoutePath(port1=PV3,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=sc.M5)

        elems += [LGND, LBias]

        # Text Labels
        elems += spira.Label(text="P2 M6 M4",position=(10*tp,3.4975*tp),layer=TEXT)
        elems += spira.Label(text="J11 M6 M5",position=(9.5*tp,1.495*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(7.4975*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(8.17*tp,3.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(8.5*tp,5.5025*tp),layer=TEXT)
        elems += spira.Label(text="J9 M5 M6",position=(7.49*tp,3.5025*tp),layer=TEXT)
        elems += spira.Label(text="PR1 M6 M4",position=(6.715*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(5.5*tp,3.14*tp),layer=TEXT)
        elems += spira.Label(text="J7 M5 M6",position=(5*tp,3.1375*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(4.5*tp,5*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(5*tp,4.4675*tp),layer=TEXT)
        elems += spira.Label(text="J5 M5 M6",position=(5*tp,4*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(4.5*tp,1.425*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(4.4975*tp,3.5025*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(3.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(1.5*tp,2.5025*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.94*tp,4.5*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(2.5*tp,5.5025*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.825*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="bias_in",position=(8.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(10*tp,3.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(8.5179*tp,6.8551*tp),layer=spira.Layer(number=50,datatype=1))
        elems += spira.Label(text='GND',position=(8.6309*tp,6.8705*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='q',position=(9.9941*tp,3.408*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='a',position=(1.5003*tp,5.4999*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='R1',position=(6.5317*tp,3.5054*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.4698*tp,4.5049*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(4.5002*tp,1.1309*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(4.4969*tp,5.525*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB4',position=(8.5105*tp,5.874*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB5',position=(6.5696*tp,0.5041*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB1',position=(2.5045*tp,5.8558*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(1.499*tp,2.1224*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(3.5087*tp,2.1589*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB4',position=(4.5049*tp,3.8045*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB5',position=(5.3231*tp,4.0008*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB6',position=(5.001*tp,4.7755*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB7',position=(4.992*tp,2.8419*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB8',position=(5.5035*tp,3.4447*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB9',position=(7.4882*tp,3.1803*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB10',position=(8.1714*tp,3.1903*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB11',position=(9.5054*tp,1.2063*tp),layer=spira.Layer(number=52,datatype=1))
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(9.9875*tp,1.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(9.9875*tp,1.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(0.0125*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))

        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.1*tp,center=(3.71*tp,1.425*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.1*tp,center=(1.29*tp,1.425*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(2.29*tp,1.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(2.71*tp,1.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.25*tp,center=(7.71*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.25*tp,center=(5.29*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.25*tp,center=(9.55*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.25*tp,center=(8.29*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.25*tp,center=(6.71*tp,1.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.25*tp,center=(5.29*tp,1.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(9.13*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(8.71*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(9.49*tp,6.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(9.49*tp,5.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.02*tp,height=0.4*tp,center=(9.49*tp,4.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(8.5*tp,0.59*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(6.5*tp,1.45*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(6.5*tp,1.87*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,1.87*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,1.45*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(2.5*tp,1.48*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(7.5*tp,5.59*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(7.5*tp,5.17*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(6.5*tp,5.59*tp))
        elems += spira.Box(layer=sc.M5,width=0.4*tp,height=0.02*tp,center=(5.5*tp,5.59*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(10*tp,3.5*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.825*tp,5.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.715*tp,3.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,5.0*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(8.5*tp,5.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.497*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(4.5*tp,1.427*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.94*tp,4.5*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(4.815*tp,3.72*tp),(4.815*tp,3.96*tp),(5.28*tp,3.96*tp),(5.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.815*tp,4.04*tp),(4.815*tp,4.28*tp),(5.28*tp,4.28*tp),(5.28*tp,4.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.815*tp,3.04*tp),(4.815*tp,3.28*tp),(5.28*tp,3.28*tp),(5.28*tp,3.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.815*tp,2.72*tp),(4.815*tp,2.96*tp),(5.28*tp,2.96*tp),(5.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(7.04*tp,3.72*tp),(7.04*tp,4.28*tp),(7.28*tp,4.28*tp),(7.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(7.04*tp,2.72*tp),(7.04*tp,3.28*tp),(7.28*tp,3.28*tp),(7.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(7.72*tp,4.04*tp),(7.72*tp,4.28*tp),(8.28*tp,4.28*tp),(8.28*tp,4.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(5.72*tp,2.72*tp),(5.72*tp,2.96*tp),(6.28*tp,2.96*tp),(6.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(6.72*tp,2.72*tp),(6.72*tp,2.96*tp),(6.96*tp,2.96*tp),(6.96*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(8.04*tp,2.72*tp),(8.04*tp,3.28*tp),(8.28*tp,3.28*tp),(8.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.875*tp,4.72*tp),(4.875*tp,4.8775*tp),(5.125*tp,4.8775*tp),(5.125*tp,4.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3.845*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1.155*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5.155*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7.845*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9.685*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8.155*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5.155*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6.845*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(8.5*tp,0.8*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.5*tp,1.275*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(1.5*tp,1.275*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.92*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.28*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.08*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,2.08*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.5*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.28*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,4.96*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,5.38*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.7*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,5.38*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,5.38*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.7*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,5.8*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(7.5*tp,5.8*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,1.69*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(8.5*tp,0.38*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.34*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(8.92*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,2.08*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6*tp,1.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,1.27*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.7*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,1.24*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,1.24*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,1.66*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,1.66*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(9.28*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(5.5*tp,5.8*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.9175*tp,4.4025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,4.4025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,4.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,4.2025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,3.785*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,4.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.7725*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,4.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,2.42*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,2.42*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,3.0625*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.775*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,2.78*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,2.0525*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.8825*tp,2.42*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.8325*tp,2.42*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.155*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.555*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.215*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.9125*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.9025*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.915*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.9325*tp,3.34*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.255*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.255*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.9175*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.2475*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.975*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.915*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.925*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.255*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.915*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.24*tp,3.34*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.665*tp,3.765*tp),transformation=sc.m90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(8.415*tp,6.415*tp),alias='via3')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.915*tp,3.415*tp),alias='via1')
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(7.0325*tp,3.415*tp),alias='via2')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_080(),midpoint=(5.53*tp,0.5*tp),transformation=sc.r270,alias='bias5')
        elems += spira.SRef(sc.ls_ib_150(),midpoint=(4.5*tp,4.945*tp),alias='bias3')
        elems += spira.SRef(sc.ls_ib_155(),midpoint=(1.995*tp,4.5*tp),transformation=sc.r90,alias='bias1')
        elems += spira.SRef(sc.ls_ib_220(),midpoint=(8.5*tp,5.445*tp),alias='bias4')
        elems += spira.SRef(sc.ls_ib_280(),midpoint=(4.5*tp,0.795*tp),alias='bias2')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_100_sg(),midpoint=(1.5*tp,2.5*tp),transformation=sc.r180,alias='J2')
        elems += spira.SRef(sc.ls_jj_100_sg(),midpoint=(3.5*tp,2.5*tp),transformation=sc.r180,alias='J3')
        elems += spira.SRef(sc.ls_jj_100_sg(),midpoint=(2.5*tp,5.5*tp),alias='J1')
        elems += spira.SRef(sc.ls_jj_150_s(),midpoint=(7.49*tp,3.5*tp),transformation=sc.r180,alias='J9')
        elems += spira.SRef(sc.ls_jj_150_s(),midpoint=(5*tp,4*tp),transformation=sc.r270,alias='J5')
        elems += spira.SRef(sc.ls_jj_150_sg(),midpoint=(8.17*tp,3.5*tp),transformation=sc.r180,alias='J10')
        elems += spira.SRef(sc.ls_jj_175_sg(),midpoint=(5*tp,4.465*tp),alias='J6')
        elems += spira.SRef(sc.ls_jj_200_s(),midpoint=(5*tp,3.14*tp),transformation=sc.r180,alias='J7')
        elems += spira.SRef(sc.ls_jj_200_sg(),midpoint=(9.5*tp,1.5*tp),transformation=sc.r180,alias='J11')
        elems += spira.SRef(sc.ls_jj_300_sg(),midpoint=(5.5*tp,3.135*tp),alias='J8')
        elems += spira.SRef(sc.ls_jj_325_sg(),midpoint=(4.5*tp,3.5*tp),alias='J4')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_res_5p74(),midpoint=(6.77*tp,3.5*tp),transformation=sc.r90,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 10):
                if (x == 1 and y ==5):
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