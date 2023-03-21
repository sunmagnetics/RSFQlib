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
    __name_prefix__ = "THmitll_MERGE_v3p0"
    def create_elements(self, elems):
        M0M4M7strips = spira.SRef(M0M4M7_strips())
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        vias = spira.SRef(M5M6_connections())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M4M7strips, M0M5Strips, IXports, jjfill, vias, M4M5M6M7conns, ib, jjs, ind, tblocks]

        # Text Labels
        elems += spira.Label(text='J1 M6 M5',position=(0.71*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(2.305*tp,3.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(1.44*tp,0.715*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(2.105*tp,2.57*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(2.48*tp,2.635*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(0.900*tp,2.56*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.515*tp,2.635*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(0.545*tp,1.825*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(1.500*tp,3.100*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(2.77*tp,4.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.225*tp,4.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(3.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='b',position=(3.000*tp,3.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(2.92*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(2.925*tp,6.315*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='q',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='b',position=(3.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RB1',position=(0.99*tp,3.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(2.005*tp,3.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(1.75*tp,0.725*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(2.105*tp,2.21*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(2.48*tp,2.33*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(0.900*tp,2.195*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.525*tp,2.33*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.675*tp,4.495*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(2.33*tp,4.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(1.495*tp,3.455*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(0.495*tp,1.305*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.150*tp,3.400*tp),(0.150*tp,3.500*tp),(0.250*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.850*tp,3.400*tp),(2.750*tp,3.500*tp),(2.850*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,0.300*tp),(1.350*tp,0.350*tp),(1.400*tp,0.350*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.600*tp,0.300*tp),(1.600*tp,0.350*tp),(1.650*tp,0.350*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.420*tp,3.890*tp),(1.420*tp,6.295*tp),(1.580*tp,6.295*tp),(1.580*tp,3.890*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.150*tp,3.600*tp),(0.150*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.290*tp,3.620*tp),(2.290*tp,4.565*tp),(2.850*tp,4.565*tp),(2.850*tp,4.435*tp),(2.420*tp,4.435*tp),(2.420*tp,3.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.580*tp,3.620*tp),(0.580*tp,4.435*tp),(0.150*tp,4.435*tp),(0.150*tp,4.565*tp),(0.710*tp,4.565*tp),(0.710*tp,3.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.355*tp,2.700*tp),(0.355*tp,3.130*tp),(0.610*tp,3.130*tp),(0.610*tp,3.380*tp),(0.700*tp,3.380*tp),(0.700*tp,3.040*tp),(0.445*tp,3.040*tp),(0.445*tp,2.700*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.335*tp,3.370*tp),(0.335*tp,3.500*tp),(0.150*tp,3.500*tp),(0.150*tp,3.600*tp),(0.435*tp,3.600*tp),(0.435*tp,3.470*tp),(0.620*tp,3.470*tp),(0.620*tp,3.370*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,0.000*tp),(1.400*tp,0.350*tp),(1.600*tp,0.350*tp),(1.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.380*tp,3.370*tp),(2.380*tp,3.470*tp),(2.565*tp,3.470*tp),(2.565*tp,3.600*tp),(2.850*tp,3.600*tp),(2.850*tp,3.500*tp),(2.665*tp,3.500*tp),(2.665*tp,3.370*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.850*tp,3.400*tp),(2.850*tp,3.600*tp),(3.000*tp,3.600*tp),(3.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.315*tp,0.800*tp),(1.315*tp,1.295*tp),(0.440*tp,1.295*tp),(0.440*tp,1.885*tp),(0.560*tp,1.885*tp),(0.560*tp,1.415*tp),(1.435*tp,1.415*tp),(1.435*tp,0.800*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.350*tp,0.350*tp),(1.350*tp,0.660*tp),(1.650*tp,0.660*tp),(1.650*tp,0.350*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.555*tp,2.700*tp),(2.555*tp,3.040*tp),(2.305*tp,3.040*tp),(2.305*tp,3.380*tp),(2.395*tp,3.380*tp),(2.395*tp,3.130*tp),(2.645*tp,3.130*tp),(2.645*tp,2.700*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.5375*tp,0.800*tp),(1.5375*tp,2.0375*tp),(1.4375*tp,2.0375*tp),(1.4375*tp,2.500*tp),(1.5625*tp,2.500*tp),(1.5625*tp,2.1625*tp),(1.6625*tp,2.1625*tp),(1.6625*tp,0.800*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.190*tp,2.3825*tp),(2.190*tp,2.6625*tp),(2.350*tp,2.6625*tp),(2.350*tp,2.3825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.650*tp,2.3825*tp),(0.650*tp,2.6625*tp),(0.810*tp,2.6625*tp),(0.810*tp,2.3825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,0.695*tp),(0.430*tp,0.990*tp),(0.570*tp,0.990*tp),(0.570*tp,0.695*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.045*tp,4.430*tp),(1.045*tp,4.570*tp),(1.950*tp,4.570*tp),(1.950*tp,4.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,2.500*tp),(1.430*tp,3.170*tp),(1.570*tp,3.170*tp),(1.570*tp,2.500*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.120*tp,2.290*tp),(1.120*tp,2.710*tp),(1.880*tp,2.710*tp),(1.880*tp,2.290*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.865*tp,2.350*tp),(0.865*tp,2.650*tp),(1.500*tp,2.650*tp),(1.500*tp,2.350*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.500*tp,2.350*tp),(1.500*tp,2.650*tp),(2.135*tp,2.650*tp),(2.135*tp,2.350*tp)])

        return elems         
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(1.720*tp,0.720*tp),(1.720*tp,0.960*tp),(1.875*tp,0.960*tp),(1.875*tp,0.875*tp),(1.960*tp,0.875*tp),(1.960*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.040*tp,0.720*tp),(2.040*tp,0.875*tp),(2.125*tp,0.875*tp),(2.125*tp,0.960*tp),(2.280*tp,0.960*tp),(2.280*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(0.720*tp,2.040*tp),(0.720*tp,2.280*tp),(0.960*tp,2.280*tp),(0.960*tp,2.125*tp),(0.875*tp,2.125*tp),(0.875*tp,2.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.040*tp,1.720*tp),(2.040*tp,1.875*tp),(2.125*tp,1.875*tp),(2.125*tp,1.960*tp),(2.280*tp,1.960*tp),(2.280*tp,1.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.125*tp,2.040*tp),(2.125*tp,2.125*tp),(2.040*tp,2.125*tp),(2.040*tp,2.280*tp),(2.280*tp,2.280*tp),(2.280*tp,2.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(0.720*tp,1.720*tp),(0.720*tp,1.960*tp),(0.875*tp,1.960*tp),(0.875*tp,1.875*tp),(0.960*tp,1.875*tp),(0.960*tp,1.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M5,shape=[(2.300*tp,5.200*tp),(2.300*tp,6.890*tp),(2.700*tp,6.890*tp),(2.700*tp,5.200*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,5.200*tp),(0.300*tp,6.890*tp),(0.700*tp,6.890*tp),(0.700*tp,5.200*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.300*tp,0.110*tp),(2.300*tp,1.370*tp),(2.700*tp,1.370*tp),(2.700*tp,0.110*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(3.000*tp,6.650*tp),(3.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.350*tp,0.500*tp),(0.350*tp,6.500*tp),(0.650*tp,6.500*tp),(0.650*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,5.125*tp),(0.960*tp,5.875*tp),(1.000*tp,5.875*tp),(1.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,4.125*tp),(0.960*tp,4.875*tp),(1.000*tp,4.875*tp),(1.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,3.125*tp),(0.960*tp,3.875*tp),(1.000*tp,3.875*tp),(1.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,2.125*tp),(0.960*tp,2.875*tp),(1.000*tp,2.875*tp),(1.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,1.125*tp),(0.960*tp,1.875*tp),(1.000*tp,1.875*tp),(1.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,0.125*tp),(0.960*tp,0.875*tp),(1.000*tp,0.875*tp),(1.000*tp,0.125*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.995*tp,3.450*tp),(2.995*tp,3.550*tp),(3.005*tp,3.550*tp),(3.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.450*tp,-0.005*tp),(1.450*tp,0.005*tp),(1.550*tp,0.005*tp),(1.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.200*tp,4.475*tp),(0.200*tp,4.530*tp),(0.255*tp,4.530*tp),(0.255*tp,4.475*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.740*tp,4.470*tp),(2.740*tp,4.530*tp),(2.800*tp,4.530*tp),(2.800*tp,4.470*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.470*tp,3.070*tp),(1.470*tp,3.125*tp),(1.530*tp,3.125*tp),(1.530*tp,3.070*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.520*tp,1.795*tp),(0.520*tp,1.845*tp),(0.570*tp,1.845*tp),(0.570*tp,1.795*tp)])
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,5.400*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,5.83*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.26*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.69*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.400*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.83*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.26*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.69*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,0.31*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,0.74*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,1.17*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.155*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.92*tp,1.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.57*tp,4.735*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.57*tp,4.735*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.695*tp,3.93*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.445*tp,3.89*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.085*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.86*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.985*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.28*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.200*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.66*tp,1.64*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.99*tp,1.685*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.43*tp,1.685*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.14*tp,0.46*tp),transformation=ls.r180)
        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__="M5M6_connections"           
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.585*tp,2.535*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_183(),midpoint=(1.500*tp,4.015*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(0.500*tp,0.865*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(0.17*tp,4.500*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_175(),midpoint=(1.82*tp,4.500*tp),transformation=ls.r270)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_301_sg(),midpoint=(0.525*tp,2.64*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_301_sg(),midpoint=(2.475*tp,2.64*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_118_s(),midpoint=(2.100*tp,2.57*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_118_s(),midpoint=(0.900*tp,2.57*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.295*tp,3.500*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.705*tp,3.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.44*tp,0.715*tp),transformation=ls.r270)

        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                if ((x == 0 and y == 0) or (x == 1 and y == 6)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif ((x == 0 and y in range(1,7)) or (x == 2 and y == 6)):
                    elems += spira.SRef(tb.tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(tb.tr_u_M4_NPTL(),midpoint=(0+x*tp,0+y*tp))
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