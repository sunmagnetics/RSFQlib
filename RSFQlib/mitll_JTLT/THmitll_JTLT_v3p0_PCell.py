import sys
# Change this to the location that contains the subcells folder
subcell_path = '..\\..\\PCell_Subcells'
if subcell_path not in sys.path:
    sys.path.append(subcell_path)
import layer_setup as ls
import bias
import connectors as conns
import fill
import jj
import resistors as res
import trackblocks as tb
import os
import spira.all as spira
from spira.technologies.mit.process.database import RDD

IXPORT = spira.RDD.PLAYER.IXPORT
TEXT = spira.Layer(number=182)

## Parameterization
# Trackpitch in microns
tp = 10
ls.tp = tp

class PCELL(spira.PCell):
    __name_prefix__ = "THmitll_JTLT_v3p0"
    def create_elements(self, elems):
        M0M4M7strips = spira.SRef(M0M4M7_strips())
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        rs = spira.SRef(resistors())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M4M7strips, M6M5Strips, IXports, jjfill, M4M5M6M7conns, vias, ib, jjs, rs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text="J2 M6 M5",position=(0.420*tp,2.220*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(0.410*tp,3.515*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.500*tp,1.310*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(1.500*tp,1.695*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(0.500*tp,1.500*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.150*tp,3.500*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(0.500*tp,4.800*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.500*tp,6.960*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(0.500*tp,0.040*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='GND',position=(0.325*tp,6.950*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RB2',position=(0.860*tp,2.230*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.410*tp,3.790*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(1.500*tp,1.215*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.500*tp,1.985*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(0.505*tp,1.150*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.500*tp,5.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='a',position=(1.505*tp,3.505*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(1.505*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(1.280*tp,0.720*tp),(1.500*tp,0.940*tp),(1.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.280*tp,3.280*tp),(1.060*tp,3.500*tp),(1.280*tp,3.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.3525*tp,2.290*tp),(0.3525*tp,2.5225*tp),(0.8425*tp,2.5225*tp),(0.8425*tp,2.4725*tp),(0.9875*tp,2.4725*tp),(0.9875*tp,2.6125*tp),(0.6125*tp,2.6125*tp),(0.6125*tp,2.7525*tp),(0.3125*tp,2.7525*tp),(0.3125*tp,3.0425*tp),(0.6075*tp,3.0425*tp),(0.6075*tp,3.1575*tp),(0.2975*tp,3.1575*tp),(0.2975*tp,3.410*tp),(0.3825*tp,3.410*tp),(0.3825*tp,3.2425*tp),(0.6925*tp,3.2425*tp),(0.6925*tp,2.9575*tp),(0.3975*tp,2.9575*tp),(0.3975*tp,2.8375*tp),(0.6975*tp,2.8375*tp),(0.6975*tp,2.6975*tp),(1.0725*tp,2.6975*tp),(1.0725*tp,2.3875*tp),(0.7575*tp,2.3875*tp),(0.7575*tp,2.4375*tp),(0.4375*tp,2.4375*tp),(0.4375*tp,2.290*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.4375*tp,1.440*tp),(0.4375*tp,2.160*tp),(0.5625*tp,2.160*tp),(0.5625*tp,1.440*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.440*tp,1.445*tp),(0.440*tp,1.555*tp),(0.745*tp,1.555*tp),(0.745*tp,1.695*tp),(1.380*tp,1.695*tp),(1.380*tp,1.585*tp),(0.855*tp,1.585*tp),(0.855*tp,1.445*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.475*tp,3.620*tp),(0.475*tp,3.740*tp),(0.590*tp,3.740*tp),(0.590*tp,4.335*tp),(0.440*tp,4.335*tp),(0.440*tp,4.865*tp),(0.560*tp,4.865*tp),(0.560*tp,4.455*tp),(0.710*tp,4.455*tp),(0.710*tp,3.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.890*tp,3.420*tp),(0.890*tp,3.580*tp),(1.150*tp,3.580*tp),(1.150*tp,3.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.505*tp,3.4025*tp),(0.505*tp,3.4975*tp),(0.7025*tp,3.4975*tp),(0.7025*tp,3.5475*tp),(0.900*tp,3.5475*tp),(0.900*tp,3.4525*tp),(0.7975*tp,3.4525*tp),(0.7975*tp,3.4025*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,0.425*tp),(0.420*tp,0.895*tp),(0.580*tp,0.895*tp),(0.580*tp,0.425*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.420*tp,0.850*tp),(1.420*tp,1.170*tp),(1.580*tp,1.170*tp),(1.580*tp,0.850*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.420*tp,1.255*tp),(1.420*tp,1.575*tp),(1.580*tp,1.575*tp),(1.580*tp,1.255*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,6.115*tp),(0.420*tp,6.570*tp),(0.580*tp,6.570*tp),(0.580*tp,6.115*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,0.000*tp),(0.400*tp,0.585*tp),(0.600*tp,0.585*tp),(0.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,6.415*tp),(0.400*tp,7.000*tp),(0.600*tp,7.000*tp),(0.600*tp,6.415*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,3.910*tp),(1.300*tp,6.890*tp),(1.700*tp,6.890*tp),(1.700*tp,3.910*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.875*tp,5.300*tp),(0.875*tp,5.700*tp),(1.315*tp,5.700*tp),(1.315*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.875*tp,6.300*tp),(0.875*tp,6.700*tp),(1.315*tp,6.700*tp),(1.315*tp,6.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.875*tp,4.300*tp),(0.875*tp,4.700*tp),(1.310*tp,4.700*tp),(1.310*tp,4.300*tp)])
        return elems         
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(1.125*tp,2.040*tp),(1.125*tp,2.125*tp),(1.040*tp,2.125*tp),(1.040*tp,2.280*tp),(1.280*tp,2.280*tp),(1.280*tp,2.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape = spira.Shape(points=[(0.720*tp,2.040*tp),(0.720*tp,2.280*tp),(0.960*tp,2.280*tp),(0.960*tp,2.125*tp),(0.875*tp,2.125*tp),(0.875*tp,2.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=2.980*tp,center=(1.500*tp,5.400*tp))
        elems += spira.Box(layer=ls.M5,width=0.440*tp,height=0.400*tp,center=(1.095*tp,5.500*tp))
        elems += spira.Box(layer=ls.M5,width=0.440*tp,height=0.400*tp,center=(1.095*tp,6.500*tp))
        elems += spira.Box(layer=ls.M5,width=0.435*tp,height=0.400*tp,center=(1.0925*tp,4.500*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.1600*tp,center=(1.150*tp,3.500*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.0500*tp,height=0.0500*tp,center=(1.500*tp,1.310*tp))
        elems += spira.Box(layer=IXPORT,width=0.0500*tp,height=0.0500*tp,center=(0.5025*tp,1.500*tp))
        elems += spira.Box(layer=IXPORT,width=0.0500*tp,height=0.0500*tp,center=(0.505*tp,4.800*tp))
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.5*tp,4.11*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.5*tp,4.54*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.5*tp,4.97*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.5*tp,5.4*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.5*tp,5.83*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.5*tp,6.26*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.5*tp,6.69*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.075*tp,4.5*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.075*tp,5.5*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.075*tp,6.5*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.5*tp,2.92*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp),transformation=ls.r90)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.880*tp,2.290*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.270*tp,6.340*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,5.340*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,4.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.275*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.270*tp,0.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.860*tp,0.320*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.140*tp,0.320*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.560*tp,2.570*tp),transformation=ls.r180)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.415*tp,0.415*tp),alias='via2')
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.415*tp,6.415*tp),alias='via1')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_239(),midpoint=(0.500*tp,0.775*tp),alias='bias2')
        elems += spira.SRef(bias.ib_112(),midpoint=(0.500*tp,4.745*tp),alias='bias1')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_081_sg(),midpoint=(0.420*tp,2.225*tp),transformation=ls.r270,alias='J2')
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.500*tp,1.695*tp),alias='J3')
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.410*tp,3.510*tp),alias='J1')
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(1.500*tp,1.055*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 2):
                if (x == 1 and y in [0,3]):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,0.000*tp), alias='Q')
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,3.000*tp), alias='A')
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