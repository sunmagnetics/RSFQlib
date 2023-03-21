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
    __name_prefix__ = "THmitll_DFF_v3p0"
    def create_elements(self, elems):
        M0M4M7Strips = spira.SRef(M0M4M7_strips())
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M4M7Strips, M0M5Strips, IXports, jjfill, M4M5M6M7conns, vias, ib, jjs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.595*tp,3.555*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.435*tp,4.635*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M5 M6',position=(1.105*tp,4.495*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.48*tp,4.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(1.54*tp,2.495*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M5 M6',position=(1.92*tp,2.535*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='clk',position=(3.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(3.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(2.365*tp,3.435*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.500*tp,4.82*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(2.400*tp,4.31*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(0.525*tp,0.18*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(1.44*tp,0.600*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(2.92*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(2.915*tp,6.325*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RB1',position=(0.595*tp,3.27*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.435*tp,5.100*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.105*tp,4.825*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.755*tp,4.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.500*tp,5.19*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(1.92*tp,2.225*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.255*tp,2.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(1.73*tp,0.605*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(2.08*tp,3.435*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.400*tp,4.755*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(0.52*tp,0.71*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='clk',position=(3.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.500*tp),(0.100*tp,3.595*tp),(0.195*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.500*tp,0.125*tp),(1.500*tp,0.225*tp),(1.600*tp,0.125*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.850*tp,3.400*tp),(2.740*tp,3.510*tp),(2.850*tp,3.510*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.3125*tp),(0.100*tp,3.500*tp),(0.195*tp,3.500*tp),(0.195*tp,3.4075*tp),(0.475*tp,3.4075*tp),(0.475*tp,3.3125*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.290*tp,3.580*tp),(0.290*tp,4.700*tp),(0.510*tp,4.700*tp),(0.510*tp,4.560*tp),(0.430*tp,4.560*tp),(0.430*tp,3.580*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,4.615*tp),(1.430*tp,4.890*tp),(1.570*tp,4.890*tp),(1.570*tp,4.615*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.200*tp,4.375*tp),(1.200*tp,4.625*tp),(1.380*tp,4.625*tp),(1.380*tp,4.375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.600*tp,3.675*tp),(0.600*tp,4.495*tp),(0.830*tp,4.495*tp),(0.830*tp,4.395*tp),(0.700*tp,4.395*tp),(0.700*tp,3.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.360*tp,3.580*tp),(0.360*tp,3.690*tp),(0.490*tp,3.690*tp),(0.490*tp,3.580*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.645*tp,2.400*tp),(1.645*tp,2.600*tp),(1.820*tp,2.600*tp),(1.820*tp,2.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.340*tp,2.440*tp),(2.340*tp,3.320*tp),(2.440*tp,3.320*tp),(2.440*tp,2.440*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.330*tp,3.540*tp),(2.330*tp,4.380*tp),(2.470*tp,4.380*tp),(2.470*tp,3.540*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.850*tp,3.400*tp),(2.850*tp,3.600*tp),(3.000*tp,3.600*tp),(3.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.480*tp,3.340*tp),(2.480*tp,3.430*tp),(2.575*tp,3.430*tp),(2.575*tp,3.600*tp),(2.850*tp,3.600*tp),(2.850*tp,3.510*tp),(2.665*tp,3.510*tp),(2.665*tp,3.340*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.455*tp,0.110*tp),(0.455*tp,0.710*tp),(1.320*tp,0.710*tp),(1.320*tp,0.570*tp),(0.595*tp,0.570*tp),(0.595*tp,0.110*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,0.000*tp),(1.400*tp,0.125*tp),(1.600*tp,0.125*tp),(1.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.310*tp,0.125*tp),(1.310*tp,0.485*tp),(1.410*tp,0.485*tp),(1.410*tp,0.225*tp),(1.500*tp,0.225*tp),(1.500*tp,0.125*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.455*tp,1.000*tp),(0.455*tp,1.300*tp),(0.595*tp,1.300*tp),(0.595*tp,1.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,5.450*tp),(1.430*tp,6.300*tp),(1.570*tp,6.300*tp),(1.570*tp,5.450*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.360*tp,5.460*tp),(0.360*tp,5.600*tp),(1.575*tp,5.600*tp),(1.575*tp,5.460*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.330*tp,5.130*tp),(2.330*tp,5.460*tp),(1.425*tp,5.460*tp),(1.425*tp,5.600*tp),(2.470*tp,5.600*tp),(2.470*tp,5.130*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.305*tp,2.605*tp),(1.305*tp,2.865*tp),(1.625*tp,2.865*tp),(1.625*tp,3.005*tp),(1.290*tp,3.005*tp),(1.290*tp,3.345*tp),(1.545*tp,3.345*tp),(1.545*tp,3.715*tp),(1.285*tp,3.715*tp),(1.285*tp,3.995*tp),(1.625*tp,3.995*tp),(1.625*tp,4.155*tp),(1.355*tp,4.155*tp),(1.355*tp,4.390*tp),(1.445*tp,4.390*tp),(1.445*tp,4.245*tp),(1.715*tp,4.245*tp),(1.715*tp,3.905*tp),(1.375*tp,3.905*tp),(1.375*tp,3.805*tp),(1.635*tp,3.805*tp),(1.635*tp,3.255*tp),(1.380*tp,3.255*tp),(1.380*tp,3.095*tp),(1.715*tp,3.095*tp),(1.715*tp,2.775*tp),(1.395*tp,2.775*tp),(1.395*tp,2.605*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.370*tp,0.710*tp),(1.370*tp,2.050*tp),(1.530*tp,2.050*tp),(1.530*tp,2.390*tp),(1.630*tp,2.390*tp),(1.630*tp,1.950*tp),(1.470*tp,1.950*tp),(1.470*tp,0.710*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.760*tp,4.380*tp),(0.760*tp,4.715*tp),(1.000*tp,4.715*tp),(1.000*tp,4.605*tp),(0.870*tp,4.605*tp),(0.870*tp,4.380*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.030*tp,2.455*tp),(2.030*tp,2.545*tp),(2.470*tp,2.545*tp),(2.470*tp,2.455*tp)])

        return elems             
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(1.125*tp,5.040*tp),(1.125*tp,5.125*tp),(1.040*tp,5.125*tp),(1.040*tp,5.280*tp),(1.280*tp,5.280*tp),(1.280*tp,5.040*tp),(1.125*tp,5.040*tp),(1.125*tp,5.125*tp),(1.040*tp,5.125*tp),(1.040*tp,5.280*tp),(1.280*tp,5.280*tp),(1.280*tp,5.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.040*tp,4.720*tp),(1.040*tp,4.875*tp),(1.125*tp,4.875*tp),(1.125*tp,4.960*tp),(1.280*tp,4.960*tp),(1.280*tp,4.720*tp),(1.040*tp,4.720*tp),(1.040*tp,4.875*tp),(1.125*tp,4.875*tp),(1.125*tp,4.960*tp),(1.280*tp,4.960*tp),(1.280*tp,4.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.720*tp,1.720*tp),(1.720*tp,1.960*tp),(1.875*tp,1.960*tp),(1.875*tp,1.875*tp),(1.960*tp,1.875*tp),(1.960*tp,1.720*tp),(1.720*tp,1.720*tp),(1.720*tp,1.960*tp),(1.875*tp,1.960*tp),(1.875*tp,1.875*tp),(1.960*tp,1.875*tp),(1.960*tp,1.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.720*tp,2.040*tp),(1.720*tp,2.280*tp),(1.960*tp,2.280*tp),(1.960*tp,2.125*tp),(1.875*tp,2.125*tp),(1.875*tp,2.040*tp),(1.720*tp,2.040*tp),(1.720*tp,2.280*tp),(1.960*tp,2.280*tp),(1.960*tp,2.125*tp),(1.875*tp,2.125*tp),(1.875*tp,2.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        return elems

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(3.000*tp,6.650*tp),(3.000*tp,6.350*tp),(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(3.000*tp,6.650*tp),(3.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.350*tp,1.500*tp),(0.350*tp,6.500*tp),(0.650*tp,6.500*tp),(0.650*tp,1.500*tp),(0.350*tp,1.500*tp),(0.350*tp,6.500*tp),(0.650*tp,6.500*tp),(0.650*tp,1.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp),(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp),(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,5.125*tp),(0.960*tp,5.875*tp),(1.000*tp,5.875*tp),(1.000*tp,5.125*tp),(0.960*tp,5.125*tp),(0.960*tp,5.875*tp),(1.000*tp,5.875*tp),(1.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,4.125*tp),(0.960*tp,4.875*tp),(1.000*tp,4.875*tp),(1.000*tp,4.125*tp),(0.960*tp,4.125*tp),(0.960*tp,4.875*tp),(1.000*tp,4.875*tp),(1.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,3.125*tp),(0.960*tp,3.875*tp),(1.000*tp,3.875*tp),(1.000*tp,3.125*tp),(0.960*tp,3.125*tp),(0.960*tp,3.875*tp),(1.000*tp,3.875*tp),(1.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,2.125*tp),(0.960*tp,2.875*tp),(1.000*tp,2.875*tp),(1.000*tp,2.125*tp),(0.960*tp,2.125*tp),(0.960*tp,2.875*tp),(1.000*tp,2.875*tp),(1.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,1.125*tp),(0.960*tp,1.875*tp),(1.000*tp,1.875*tp),(1.000*tp,1.125*tp),(0.960*tp,1.125*tp),(0.960*tp,1.875*tp),(1.000*tp,1.875*tp),(1.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,1.000*tp),(0.125*tp,1.040*tp),(0.875*tp,1.040*tp),(0.875*tp,1.000*tp),(0.125*tp,1.000*tp),(0.125*tp,1.040*tp),(0.875*tp,1.040*tp),(0.875*tp,1.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.300*tp,6.060*tp),(2.300*tp,6.890*tp),(2.700*tp,6.890*tp),(2.700*tp,6.060*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.300*tp,0.730*tp),(2.300*tp,1.990*tp),(2.700*tp,1.990*tp),(2.700*tp,0.730*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.860*tp,1.300*tp),(1.860*tp,1.700*tp),(2.325*tp,1.700*tp),(2.325*tp,1.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,6.060*tp),(0.300*tp,6.890*tp),(0.700*tp,6.890*tp),(0.700*tp,6.060*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.995*tp,3.450*tp),(2.995*tp,3.550*tp),(3.005*tp,3.550*tp),(3.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.450*tp,-0.005*tp),(1.450*tp,0.005*tp),(1.550*tp,0.005*tp),(1.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.410*tp,4.605*tp),(0.410*tp,4.655*tp),(0.470*tp,4.655*tp),(0.470*tp,4.605*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.470*tp,4.790*tp),(1.470*tp,4.845*tp),(1.525*tp,4.845*tp),(1.525*tp,4.790*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.375*tp,4.280*tp),(2.375*tp,4.330*tp),(2.425*tp,4.330*tp),(2.425*tp,4.280*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.495*tp,0.150*tp),(0.495*tp,0.210*tp),(0.555*tp,0.210*tp),(0.555*tp,0.150*tp)])
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.26*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.69*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.085*tp,1.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.69*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.26*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.06*tp,1.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,1.79*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,1.36*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,0.93*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.300*tp,2.13*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.38*tp,2.645*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.905*tp,3.425*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.79*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.865*tp,2.355*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.88*tp,0.285*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.875*tp,5.300*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.27*tp,0.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,2.29*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.035*tp,6.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.075*tp,6.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.725*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.775*tp,2.43*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.67*tp,2.04*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.13*tp,0.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.66*tp,5.895*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.66*tp,5.900*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.47*tp,0.44*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.195*tp,0.62*tp),transformation=ls.r270)
        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.87*tp,4.55*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.475*tp,2.585*tp),transformation=ls.r180)
        
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_222(),midpoint=(1.500*tp,5.59*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(2.400*tp,4.25*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(0.44*tp,4.575*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(0.525*tp,1.13*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.37*tp,3.435*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.595*tp,3.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.44*tp,0.600*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_232_sg(),midpoint=(1.475*tp,4.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_202_sg(),midpoint=(1.54*tp,2.495*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_169_s(),midpoint=(1.915*tp,2.535*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_167_s(),midpoint=(1.105*tp,4.49*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                if ((x == 0 and y in [2,3,4,5,6]) or (x == 2 and y == 6)):
                    elems += spira.SRef(tb.tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
                elif ((x == 0 and y == 1) or (x == 1 and y == 6)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
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