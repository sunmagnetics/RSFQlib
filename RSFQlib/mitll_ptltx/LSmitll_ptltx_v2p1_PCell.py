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
L2_width = 0.115*tp*Scaling
L3_width = 0.16*tp*Scaling
LB_width = 0.16*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_PTLTX_v2p1"
    def create_elements(self, elems):
        M0strips = spira.SRef(M0_strips())
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        res = spira.SRef(resistors())
        M0blocks = spira.SRef(M0_blocks())
        tblocks = spira.SRef(trackblocks())
        elems += [M0strips, M6M5Strips, IXports, jjfill, M4M5M6M7conns,
                  bias, jjs, res, M0blocks, tblocks]
        # Bias ports
        PB1N = spira.Port(name='PB1N',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1S = spira.Port(name='PB1S',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2N = spira.Port(name='PB2N',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2S = spira.Port(name='PB2S',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBin1 = spira.Port(name='PBin1',midpoint=(0.5*tp,2.5*tp),process=spira.RDD.PROCESS.M6)
        PBin2 = spira.Port(name='PBin2',midpoint=(0.5*tp,6.5*tp),process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1N = spira.Port(name='PR1N',midpoint=res.reference.elements['R1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1S = spira.Port(name='PR1S',midpoint=res.reference.elements['R1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Junction ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center,process=spira.RDD.PROCESS.M6)
        PA_post = spira.Port(name="PA_post",midpoint=IXports.reference.elements['A'].center+(0.2*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PQ",midpoint=(2.5*tp,2.5*tp),process=spira.RDD.PROCESS.M6)
        
        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PA.x,PJ1.y)],width=IXports.reference.elements['A'].bbox_info.height,layer=sc.M6)
        L1_post = spira.RoutePath(port1=PA_post,port2=PJ1,path=[(PA_post.x,PJ1.y)],width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(PJ2.x,PJ1.y)],width=L2_width,layer=sc.M6)
        L3_1 = spira.RoutePath(port1=PJ2,port2=PR1S,path=[(PR1S.x,PJ2.y)],width=L3_width,layer=sc.M6)
        L3_2 = spira.RoutePath(port1=PR1N,port2=PQ,path=[(PR1N.x,PQ.y)],width=L3_width,layer=sc.M6)

        elems += [L1, L1_post, L2, L3_1, L3_2]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1S,path=[(PJ1.x,PB1S.y)],width=LB_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1N,port2=PBin2,path=[(PB1N.x,PBin2.y)],width=LB_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PJ2,port2=PB2S,path=[(PJ2.x,0.5*tp),(PB2S.x,0.5*tp)],width=LB_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2N,port2=PBin1,path=[(PB2N.x,PBin1.y)],width=LB_width,layer=sc.M6)

        elems += [LB1_1, LB1_2, LB2_1, LB2_2]

        #LBias = spira.RoutePath(port1=PV1,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=M5)

        #elems += LBias

        # Text Labels
        elems += spira.Label(text='Q',position=(2.5*tp,2.5*tp),layer=TEXT)
        elems += spira.Label(text='P2 M6 M4',position=(2.5*tp,1.72*tp),layer=TEXT)
        elems += spira.Label(text='PB2 M6 M4',position=(0.5*tp,0.605*tp),layer=TEXT)
        elems += spira.Label(text='J2 M6 M5',position=(1.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text='PB1 M6 M4',position=(1.5*tp,4.43*tp),layer=TEXT)
        elems += spira.Label(text='J1 M6 M5',position=(1.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='P1 M6 M4',position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='a',position=(0*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text='bias_out',position=(3*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text='bias_in',position=(0*tp,6.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='a',position=(0.006*tp,3.407*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q',position=(2.501*tp,2.501*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.509*tp,4.858*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(0.499*tp,1.031*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RD',position=(2.497*tp,1.813*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB1',position=(1.791*tp,3.503*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(1.209*tp,1.508*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='VDD',position=(2.836*tp,6.593*tp),layer=spira.Layer(number=1,datatype=1))
        elems += spira.Label(text='GND',position=(2.507*tp,6.84*tp),layer=spira.Layer(number=40,datatype=1))
        return elems

class M0_strips(spira.Cell):
    __name_prefix__ = "M0_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(0*tp,6.35*tp),(0*tp,6.65*tp),(3*tp,6.65*tp),(3*tp,6.35*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.4*tp,2.5*tp),(0.4*tp,6.5*tp),(0.6*tp,6.5*tp),(0.6*tp,2.5*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.125*tp,2*tp),(0.125*tp,2.04*tp),(0.875*tp,2.04*tp),(0.875*tp,2*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.96*tp,2.125*tp),(0.96*tp,5.875*tp),(1*tp,5.875*tp),(1*tp,2.125*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(1.125*tp,6*tp),(1.125*tp,6.04*tp),(2.875*tp,6.04*tp),(2.875*tp,6*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.28*tp,0.28*tp),(0.28*tp,0.72*tp),(0.72*tp,0.72*tp),(0.72*tp,0.28*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0.875*tp),(0*tp,1*tp),(0.125*tp,1*tp),(0.125*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0.875*tp),(0.875*tp,1*tp),(1*tp,1*tp),(1*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0*tp),(0.875*tp,0.125*tp),(1*tp,0.125*tp),(1*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0*tp),(0*tp,0.125*tp),(0.125*tp,0.125*tp),(0.125*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0.875*tp),(0*tp,1*tp),(0.125*tp,1*tp),(0.125*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0.875*tp),(0.875*tp,1*tp),(1*tp,1*tp),(1*tp,0.875*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0.875*tp,0*tp),(0.875*tp,0.125*tp),(1*tp,0.125*tp),(1*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        shape = spira.Shape(points=[(0*tp,0*tp),(0*tp,0.125*tp),(0.125*tp,0.125*tp),(0.125*tp,0*tp)])
        elems += spira.Polygon(shape,layer=sc.M0)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.33*tp,center=(2.9875*tp,2.5*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,0.5*tp))
        elems += spira.Box(layer=sc.M6,width=0.33*tp,height=0.025*tp,center=(0.5*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,2.5*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.33*tp,center=(2.9875*tp,1.5*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,6.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.33*tp,center=(2.9875*tp,2.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,0.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.33*tp,height=0.025*tp,center=(0.5*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,2.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.33*tp,center=(2.9875*tp,1.5*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.33*tp,center=(0.0125*tp,6.5*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(0.0*tp,3.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(1.5*tp,4.43*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.5*tp,1.72*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(0.5*tp,0.605*tp))
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,0.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,3.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,4.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,6.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(2.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5.5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,4.5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,6.835*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,2.845*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,6.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.665*tp,0.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,0.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,1.055*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.125*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,6.015*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,2.845*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,3.735*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,3.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,4.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.665*tp,5.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.665*tp,4.93*tp),transformation=sc.m90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.985*tp,2.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.875*tp,2.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.985*tp,0.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.875*tp,4.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.265*tp,4.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.265*tp,5.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.875*tp,5.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.945*tp,6.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,6.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,2.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.165*tp,0.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.975*tp,1.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.975*tp,2.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.155*tp,2.665*tp),transformation=sc.m135)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.265*tp,2.665*tp),transformation=sc.m135)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(1.5*tp,4.375*tp),alias='bias1')
        elems += spira.SRef(sc.ls_ib_175(),midpoint=(0.5*tp,0.55*tp),alias='bias2')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,1.5*tp),transformation=sc.r90,alias='J2')
        elems += spira.SRef(sc.ls_jj_250_sg(),midpoint=(1.5*tp,3.5*tp),transformation=sc.r270,alias='J1')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_res_1p36(),midpoint=(2.5*tp,1.665*tp),alias='R1')
        return elems

class M0_blocks(spira.Cell):
    __name_prefix__ = "M0_blocks"
    def create_elements(self, elems):
        for y in range(0,6):
            for x in range(0,3):
                if x == 0 and y not in [0,1]:
                    pass
                elif x == 2 and y == 2:
                    pass
                else:
                    elems += spira.SRef(sc.ls_tr_M0(),midpoint=(0+x*tp,0+y*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                if (x == 2 and y == 2):
                    elems += spira.SRef(sc.ls_tr_PTLconnection_M3M6(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 0 and y in [2, 6]):
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