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
    __name_prefix__ = "THmitll_PTLTX_v3p0"
    def create_elements(self, elems):
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        vias = spira.SRef(M5M6_connections())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        rs = spira.SRef(resistors())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M5Strips, IXports, jjfill, vias, M4M5M6M7conns, ib, jjs, rs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text='P2 M6 M4',position=(1.500*tp,2.235*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.615*tp,3.565*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(1.56*tp,2.535*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.36*tp,3.885*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.505*tp,4.36*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='q',position=(1.500*tp,1.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RIB1',position=(0.365*tp,4.37*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.025*tp,4.365*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.255*tp,2.53*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.615*tp,3.275*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(1.505*tp,2.135*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='GND',position=(0.355*tp,6.94*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='VDD',position=(0.500*tp,6.96*tp),layer=spira.Layer(number=50,datatype=0))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(1.280*tp,1.720*tp),(1.500*tp,1.940*tp),(1.720*tp,1.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.500*tp),(0.100*tp,3.600*tp),(0.200*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.420*tp,1.850*tp),(1.420*tp,2.0975*tp),(1.580*tp,2.0975*tp),(1.580*tp,1.850*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,2.1675*tp),(1.430*tp,2.415*tp),(1.570*tp,2.415*tp),(1.570*tp,2.1675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.300*tp),(0.100*tp,3.500*tp),(0.200*tp,3.500*tp),(0.200*tp,3.400*tp),(0.300*tp,3.400*tp),(0.300*tp,3.570*tp),(0.500*tp,3.570*tp),(0.500*tp,3.470*tp),(0.400*tp,3.470*tp),(0.400*tp,3.300*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.290*tp,4.720*tp),(0.290*tp,5.205*tp),(0.500*tp,5.205*tp),(0.500*tp,5.065*tp),(0.430*tp,5.065*tp),(0.430*tp,4.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.535*tp,4.295*tp),(0.535*tp,5.065*tp),(0.500*tp,5.065*tp),(0.500*tp,5.205*tp),(0.675*tp,5.205*tp),(0.675*tp,4.295*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.5475*tp,2.650*tp),(1.5475*tp,4.290*tp),(1.425*tp,4.290*tp),(1.425*tp,4.430*tp),(1.6875*tp,4.430*tp),(1.6875*tp,2.650*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.310*tp,2.650*tp),(1.310*tp,3.460*tp),(1.020*tp,3.460*tp),(1.020*tp,3.350*tp),(0.730*tp,3.350*tp),(0.730*tp,3.450*tp),(0.920*tp,3.450*tp),(0.920*tp,3.560*tp),(1.410*tp,3.560*tp),(1.410*tp,2.650*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.540*tp,3.680*tp),(0.540*tp,3.815*tp),(0.285*tp,3.815*tp),(0.285*tp,3.955*tp),(0.680*tp,3.955*tp),(0.680*tp,3.680*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.390*tp,5.135*tp),(0.390*tp,6.070*tp),(0.430*tp,6.070*tp),(0.430*tp,6.570*tp),(0.570*tp,6.570*tp),(0.570*tp,5.930*tp),(0.530*tp,5.930*tp),(0.530*tp,5.135*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,6.400*tp),(0.400*tp,7.000*tp),(0.600*tp,7.000*tp),(0.600*tp,6.400*tp)])

        return elems         
        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,0.105*tp),(0.300*tp,2.225*tp),(0.700*tp,2.225*tp),(0.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.575*tp,0.295*tp),(0.575*tp,0.695*tp),(1.555*tp,0.695*tp),(1.555*tp,0.295*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.290*tp,0.695*tp),(1.290*tp,0.775*tp),(1.555*tp,0.775*tp),(1.555*tp,0.695*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,4.770*tp),(1.300*tp,6.890*tp),(1.700*tp,6.890*tp),(1.700*tp,4.770*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.875*tp,6.300*tp),(0.875*tp,6.700*tp),(1.335*tp,6.700*tp),(1.335*tp,6.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.875*tp,5.300*tp),(0.875*tp,5.700*tp),(1.345*tp,5.700*tp),(1.345*tp,5.300*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.475*tp,2.205*tp),(1.475*tp,2.255*tp),(1.525*tp,2.255*tp),(1.525*tp,2.205*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.335*tp,3.860*tp),(0.335*tp,3.915*tp),(0.390*tp,3.915*tp),(0.390*tp,3.860*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.475*tp,4.335*tp),(1.475*tp,4.385*tp),(1.530*tp,4.385*tp),(1.530*tp,4.335*tp)])
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.305*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.735*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.165*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.595*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,2.025*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.075*tp,6.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.075*tp,5.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.49*tp,0.925*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.355*tp,0.495*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.925*tp,0.495*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,4.97*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.400*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.83*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.26*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.69*tp),transformation=ls.r90)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.76*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,2.385*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.28*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,6.36*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.44*tp,3.805*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.56*tp,2.495*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.88*tp,0.29*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.81*tp,4.65*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.14*tp,4.695*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.145*tp,1.57*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.675*tp,2.665*tp),transformation=ls.r270)
        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__="M5M6_connections"           
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.585*tp,6.585*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_175(),midpoint=(0.36*tp,4.84*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(0.55*tp,4.36*tp),transformation=ls.r270)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.56*tp,2.53*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.615*tp,3.56*tp),transformation=ls.r180)
        return elems
        
class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(1.500*tp,2.285*tp),transformation=ls.r180)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 2):
                if (x == 1 and y == 1):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTL_conn(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r180)
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