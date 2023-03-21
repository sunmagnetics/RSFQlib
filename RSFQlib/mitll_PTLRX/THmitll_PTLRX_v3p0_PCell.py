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
    __name_prefix__ = "THmitll_PTLRX_v3p0"
    def create_elements(self, elems):
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        vias = spira.SRef(M5M6_connections())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M5Strips, IXports, jjfill, vias, M4M5M6M7conns, ib, jjs, ind, tblocks]
       
        # Text Labels
        elems += spira.Label(text='VDD',position=(1.500*tp,6.945*tp),layer=spira.Layer(number=50,datatype=1))
        elems += spira.Label(text='VDD',position=(0.500*tp,0.06*tp),layer=spira.Layer(number=50,datatype=1))
        elems += spira.Label(text='J3 M6 M5',position=(1.435*tp,3.47*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.500*tp,5.15*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(1.36*tp,4.59*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(1.575*tp,4.175*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.805*tp,4.595*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.385*tp,3.545*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(0.445*tp,2.645*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='GND',position=(1.345*tp,6.945*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='a',position=(0.500*tp,5.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(2.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RB3',position=(1.43*tp,3.18*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(1.36*tp,5.355*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(1.58*tp,4.665*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(0.445*tp,2.28*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.505*tp,4.595*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.38*tp,3.26*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(1.810*tp,3.510*tp),(1.900*tp,3.600*tp),(1.900*tp,3.510*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,5.060*tp),(0.280*tp,5.280*tp),(0.720*tp,5.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.510*tp,3.2225*tp),(1.510*tp,3.3125*tp),(1.6275*tp,3.3125*tp),(1.6275*tp,3.400*tp),(1.810*tp,3.400*tp),(1.810*tp,3.510*tp),(1.900*tp,3.510*tp),(1.900*tp,3.310*tp),(1.7175*tp,3.310*tp),(1.7175*tp,3.2225*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.770*tp,3.285*tp),(0.770*tp,3.580*tp),(0.660*tp,3.580*tp),(0.660*tp,3.515*tp),(0.485*tp,3.515*tp),(0.485*tp,3.595*tp),(0.580*tp,3.595*tp),(0.580*tp,3.660*tp),(0.850*tp,3.660*tp),(0.850*tp,3.365*tp),(0.925*tp,3.365*tp),(0.925*tp,3.710*tp),(1.210*tp,3.710*tp),(1.210*tp,3.370*tp),(1.310*tp,3.370*tp),(1.310*tp,3.290*tp),(1.130*tp,3.290*tp),(1.130*tp,3.630*tp),(1.005*tp,3.630*tp),(1.005*tp,3.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.330*tp,3.580*tp),(1.330*tp,4.245*tp),(1.645*tp,4.245*tp),(1.645*tp,4.105*tp),(1.470*tp,4.105*tp),(1.470*tp,3.580*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.410*tp,3.650*tp),(0.410*tp,3.815*tp),(0.615*tp,3.815*tp),(0.615*tp,3.890*tp),(0.285*tp,3.890*tp),(0.285*tp,4.415*tp),(0.540*tp,4.415*tp),(0.540*tp,4.125*tp),(0.635*tp,4.125*tp),(0.635*tp,4.485*tp),(0.715*tp,4.485*tp),(0.715*tp,4.045*tp),(0.460*tp,4.045*tp),(0.460*tp,4.335*tp),(0.365*tp,4.335*tp),(0.365*tp,3.970*tp),(0.695*tp,3.970*tp),(0.695*tp,3.735*tp),(0.490*tp,3.735*tp),(0.490*tp,3.650*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.900*tp,3.400*tp),(1.900*tp,3.600*tp),(2.000*tp,3.600*tp),(2.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,4.900*tp),(0.420*tp,5.280*tp),(0.580*tp,5.280*tp),(0.580*tp,4.900*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,4.695*tp),(0.575*tp,4.830*tp),(0.420*tp,4.830*tp),(0.420*tp,4.970*tp),(0.715*tp,4.970*tp),(0.715*tp,4.695*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.905*tp,4.520*tp),(0.905*tp,4.660*tp),(1.430*tp,4.660*tp),(1.430*tp,4.520*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,6.200*tp),(1.430*tp,6.570*tp),(1.570*tp,6.570*tp),(1.570*tp,6.200*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.290*tp,5.905*tp),(1.290*tp,6.270*tp),(1.500*tp,6.270*tp),(1.500*tp,6.130*tp),(1.430*tp,6.130*tp),(1.430*tp,5.905*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.375*tp,2.575*tp),(0.375*tp,2.715*tp),(0.555*tp,2.715*tp),(0.555*tp,3.2975*tp),(0.490*tp,3.2975*tp),(0.490*tp,3.4375*tp),(0.695*tp,3.4375*tp),(0.695*tp,2.575*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,0.430*tp),(0.430*tp,0.835*tp),(0.380*tp,0.835*tp),(0.380*tp,1.925*tp),(0.520*tp,1.925*tp),(0.520*tp,0.975*tp),(0.570*tp,0.975*tp),(0.570*tp,0.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.505*tp,5.005*tp),(1.505*tp,6.130*tp),(1.500*tp,6.130*tp),(1.500*tp,6.270*tp),(1.645*tp,6.270*tp),(1.645*tp,5.005*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.400*tp,6.400*tp),(1.400*tp,7.000*tp),(1.600*tp,7.000*tp),(1.600*tp,6.400*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,0.000*tp),(0.400*tp,0.600*tp),(0.600*tp,0.600*tp),(0.600*tp,0.000*tp)])

        return elems             

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,6.070*tp),(0.300*tp,6.900*tp),(0.700*tp,6.900*tp),(0.700*tp,6.070*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,0.110*tp),(1.300*tp,2.230*tp),(1.700*tp,2.230*tp),(1.700*tp,0.110*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.870*tp,0.300*tp),(0.870*tp,0.700*tp),(1.390*tp,0.700*tp),(1.390*tp,0.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.870*tp,1.300*tp),(0.870*tp,1.700*tp),(1.390*tp,1.700*tp),(1.390*tp,1.300*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(1.995*tp,3.450*tp),(1.995*tp,3.550*tp),(2.005*tp,3.550*tp),(2.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.420*tp,5.145*tp),(0.420*tp,5.155*tp),(0.580*tp,5.155*tp),(0.580*tp,5.145*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.425*tp,2.620*tp),(0.425*tp,2.670*tp),(0.480*tp,2.670*tp),(0.480*tp,2.620*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.550*tp,4.150*tp),(1.550*tp,4.200*tp),(1.605*tp,4.200*tp),(1.605*tp,4.150*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.335*tp,4.565*tp),(1.335*tp,4.620*tp),(1.390*tp,4.620*tp),(1.390*tp,4.565*tp)])
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.27*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.700*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,0.31*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,0.74*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.17*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.600*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,2.03*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.07*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.07*tp,0.500*tp),transformation=ls.r90)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.745*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.255*tp,2.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.885*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.07*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.885*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.965*tp,6.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.28*tp,6.38*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,1.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,2.38*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.21*tp,2.365*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.53*tp,2.415*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.94*tp,2.445*tp),transformation=ls.r180)
        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__="M5M6_connections"           
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.585*tp,6.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.585*tp,0.585*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_200(),midpoint=(0.45*tp,2.700*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(1.575*tp,5.13*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_112(),midpoint=(1.36*tp,6.025*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.43*tp,3.475*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_200_sg(),midpoint=(0.385*tp,3.54*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.800*tp,4.59*tp),transformation=ls.r90)

        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 2):
                if (x == 0 and y == 5):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTL_conn(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r180)
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