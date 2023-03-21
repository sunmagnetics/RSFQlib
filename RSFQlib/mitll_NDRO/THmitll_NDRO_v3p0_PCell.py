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
    __name_prefix__ = "THmitll_NDRO_v3p0"
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
        elems += spira.Label(text='J3 M6 M5',position=(1.52*tp,4.585*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.555*tp,3.575*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(2.435*tp,6.47*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M6 M5',position=(2.445*tp,0.600*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P4 M6 M4',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(2.500*tp,7.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='b',position=(2.500*tp,7.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='clk',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M5 M6',position=(1.145*tp,4.57*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(2.56*tp,5.39*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M5 M6',position=(2.46*tp,5.765*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M5 M6',position=(2.44*tp,4.255*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(2.56*tp,2.615*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J11 M6 M5',position=(3.445*tp,3.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M5 M6',position=(2.535*tp,2.245*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB5 M6 M4',position=(2.115*tp,0.61*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(1.495*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.500*tp,3.18*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB6 M6 M4',position=(3.61*tp,4.03*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(2.055*tp,6.635*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.585*tp,4.93*tp),layer=spira.Layer(number=182,datatype=0))

        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(3.875*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(3.91*tp,6.315*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='q',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='b',position=(2.500*tp,7.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='clk',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RB3',position=(1.52*tp,4.29*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.84*tp,3.57*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(2.73*tp,6.475*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(2.725*tp,0.61*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB11',position=(3.15*tp,3.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(2.77*tp,5.755*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(2.27*tp,5.39*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.58*tp,5.31*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB6',position=(3.605*tp,4.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(1.585*tp,6.63*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(1.505*tp,3.200*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(1.67*tp,0.625*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.495*tp,2.72*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.845*tp,4.575*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(2.845*tp,4.245*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(2.27*tp,2.615*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(2.175*tp,2.255*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.400*tp),(0.100*tp,3.490*tp),(0.190*tp,3.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.410*tp),(3.810*tp,3.500*tp),(3.900*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.500*tp,6.800*tp),(2.400*tp,6.900*tp),(2.500*tp,6.900*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.250*tp,4.455*tp),(1.250*tp,4.685*tp),(1.410*tp,4.685*tp),(1.410*tp,4.455*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.335*tp,5.500*tp),(2.335*tp,5.675*tp),(2.675*tp,5.675*tp),(2.675*tp,5.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.515*tp,5.970*tp),(1.515*tp,6.335*tp),(1.155*tp,6.335*tp),(1.155*tp,6.475*tp),(1.655*tp,6.475*tp),(1.655*tp,5.970*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.435*tp,2.190*tp),(0.435*tp,2.425*tp),(1.500*tp,2.425*tp),(1.500*tp,2.285*tp),(0.575*tp,2.285*tp),(0.575*tp,2.190*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,1.705*tp),(1.430*tp,2.600*tp),(1.570*tp,2.600*tp),(1.570*tp,1.705*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.490*tp),(0.100*tp,3.690*tp),(0.450*tp,3.690*tp),(0.450*tp,3.600*tp),(0.190*tp,3.600*tp),(0.190*tp,3.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.540*tp,3.615*tp),(0.540*tp,4.330*tp),(0.710*tp,4.330*tp),(0.710*tp,3.615*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.625*tp,4.590*tp),(1.625*tp,4.690*tp),(2.390*tp,4.690*tp),(2.390*tp,4.590*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.5875*tp,6.600*tp),(2.5875*tp,6.800*tp),(2.500*tp,6.800*tp),(2.500*tp,6.900*tp),(2.6875*tp,6.900*tp),(2.6875*tp,6.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.570*tp,4.815*tp),(2.570*tp,5.045*tp),(2.305*tp,5.045*tp),(2.305*tp,5.270*tp),(2.395*tp,5.270*tp),(2.395*tp,5.135*tp),(2.660*tp,5.135*tp),(2.660*tp,4.815*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.440*tp,3.520*tp),(2.440*tp,4.175*tp),(2.570*tp,4.175*tp),(2.570*tp,3.520*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.4575*tp,2.720*tp),(2.4575*tp,3.520*tp),(2.5525*tp,3.520*tp),(2.5525*tp,2.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.810*tp,3.500*tp),(3.810*tp,3.520*tp),(3.550*tp,3.520*tp),(3.550*tp,3.610*tp),(3.900*tp,3.610*tp),(3.900*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.670*tp,2.5825*tp),(2.670*tp,2.6975*tp),(3.3225*tp,2.6975*tp),(3.3225*tp,3.385*tp),(3.4375*tp,3.385*tp),(3.4375*tp,2.5825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.415*tp,0.100*tp),(2.415*tp,0.490*tp),(2.585*tp,0.490*tp),(2.585*tp,0.100*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.415*tp,0.725*tp),(2.415*tp,1.570*tp),(2.575*tp,1.570*tp),(2.575*tp,0.725*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.420*tp,3.430*tp),(1.420*tp,3.570*tp),(1.930*tp,3.570*tp),(1.930*tp,3.590*tp),(2.565*tp,3.590*tp),(2.565*tp,3.450*tp),(2.070*tp,3.450*tp),(2.070*tp,3.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.320*tp,6.080*tp),(2.320*tp,6.360*tp),(2.410*tp,6.360*tp),(2.410*tp,6.170*tp),(2.570*tp,6.170*tp),(2.570*tp,6.080*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.400*tp),(3.900*tp,3.600*tp),(4.000*tp,3.600*tp),(4.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.400*tp,6.900*tp),(2.400*tp,7.000*tp),(2.600*tp,7.000*tp),(2.600*tp,6.900*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.400*tp,0.000*tp),(2.400*tp,0.100*tp),(2.600*tp,0.100*tp),(2.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.690*tp,6.335*tp),(0.690*tp,6.475*tp),(1.155*tp,6.475*tp),(1.155*tp,6.335*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.085*tp,6.405*tp),(1.085*tp,6.705*tp),(1.225*tp,6.705*tp),(1.225*tp,6.405*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.985*tp,6.420*tp),(1.985*tp,6.705*tp),(2.125*tp,6.705*tp),(2.125*tp,6.560*tp),(2.325*tp,6.560*tp),(2.325*tp,6.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.410*tp,4.675*tp),(1.410*tp,4.995*tp),(1.660*tp,4.995*tp),(1.660*tp,4.855*tp),(1.550*tp,4.855*tp),(1.550*tp,4.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.540*tp,4.865*tp),(3.540*tp,6.310*tp),(3.680*tp,6.310*tp),(3.680*tp,4.865*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.380*tp,3.620*tp),(3.380*tp,4.100*tp),(3.685*tp,4.100*tp),(3.685*tp,3.960*tp),(3.520*tp,3.960*tp),(3.520*tp,3.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,3.100*tp),(0.430*tp,3.480*tp),(0.570*tp,3.480*tp),(0.570*tp,3.100*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.145*tp,0.545*tp),(1.145*tp,0.685*tp),(1.430*tp,0.685*tp),(1.430*tp,1.300*tp),(1.570*tp,1.300*tp),(1.570*tp,0.545*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.035*tp,0.540*tp),(2.035*tp,0.680*tp),(2.325*tp,0.680*tp),(2.325*tp,0.540*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.315*tp,2.340*tp),(2.315*tp,2.500*tp),(2.615*tp,2.500*tp),(2.615*tp,2.340*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.625*tp,4.2825*tp),(0.625*tp,4.3825*tp),(0.900*tp,4.3825*tp),(0.900*tp,4.460*tp),(1.000*tp,4.460*tp),(1.000*tp,4.2825*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.540*tp,4.175*tp),(0.540*tp,4.3825*tp),(0.710*tp,4.3825*tp),(0.710*tp,4.175*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.3325*tp,4.360*tp),(2.3325*tp,4.430*tp),(2.305*tp,4.430*tp),(2.305*tp,4.700*tp),(2.405*tp,4.700*tp),(2.405*tp,4.530*tp),(2.4325*tp,4.530*tp),(2.4325*tp,4.360*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.590*tp,5.890*tp),(2.590*tp,6.015*tp),(2.415*tp,6.015*tp),(2.415*tp,6.105*tp),(2.680*tp,6.105*tp),(2.680*tp,5.890*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.555*tp,4.360*tp),(2.555*tp,4.880*tp),(2.655*tp,4.880*tp),(2.655*tp,4.360*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.415*tp,1.500*tp),(2.415*tp,2.215*tp),(2.575*tp,2.215*tp),(2.575*tp,1.500*tp)])

        return elems        
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(3.040*tp,5.720*tp),(3.040*tp,5.875*tp),(3.125*tp,5.875*tp),(3.125*tp,5.960*tp),(3.280*tp,5.960*tp),(3.280*tp,5.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.720*tp,5.720*tp),(2.720*tp,5.960*tp),(2.875*tp,5.960*tp),(2.875*tp,5.875*tp),(2.960*tp,5.875*tp),(2.960*tp,5.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(3.125*tp,4.040*tp),(3.125*tp,4.125*tp),(3.040*tp,4.125*tp),(3.040*tp,4.280*tp),(3.280*tp,4.280*tp),(3.280*tp,4.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.720*tp,4.040*tp),(2.720*tp,4.280*tp),(2.960*tp,4.280*tp),(2.960*tp,4.125*tp),(2.875*tp,4.125*tp),(2.875*tp,4.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.125*tp,2.040*tp),(2.125*tp,2.125*tp),(2.040*tp,2.125*tp),(2.040*tp,2.280*tp),(2.280*tp,2.280*tp),(2.280*tp,2.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.720*tp,2.040*tp),(1.720*tp,2.280*tp),(1.960*tp,2.280*tp),(1.960*tp,2.125*tp),(1.875*tp,2.125*tp),(1.875*tp,2.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(3.040*tp,5.720*tp),(3.040*tp,5.875*tp),(3.125*tp,5.875*tp),(3.125*tp,5.960*tp),(3.280*tp,5.960*tp),(3.280*tp,5.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.720*tp,5.720*tp),(2.720*tp,5.960*tp),(2.875*tp,5.960*tp),(2.875*tp,5.875*tp),(2.960*tp,5.875*tp),(2.960*tp,5.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(3.125*tp,4.040*tp),(3.125*tp,4.125*tp),(3.040*tp,4.125*tp),(3.040*tp,4.280*tp),(3.280*tp,4.280*tp),(3.280*tp,4.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.720*tp,4.040*tp),(2.720*tp,4.280*tp),(2.960*tp,4.280*tp),(2.960*tp,4.125*tp),(2.875*tp,4.125*tp),(2.875*tp,4.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.125*tp,2.040*tp),(2.125*tp,2.125*tp),(2.040*tp,2.125*tp),(2.040*tp,2.280*tp),(2.280*tp,2.280*tp),(2.280*tp,2.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(4.000*tp,6.650*tp),(4.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.350*tp,1.500*tp),(1.350*tp,6.500*tp),(1.650*tp,6.500*tp),(1.650*tp,1.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(3.125*tp,6.000*tp),(3.125*tp,6.040*tp),(3.875*tp,6.040*tp),(3.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,6.000*tp),(0.125*tp,6.040*tp),(0.875*tp,6.040*tp),(0.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,5.125*tp),(1.960*tp,5.875*tp),(2.000*tp,5.875*tp),(2.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,4.125*tp),(1.960*tp,4.875*tp),(2.000*tp,4.875*tp),(2.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,3.125*tp),(1.960*tp,3.875*tp),(2.000*tp,3.875*tp),(2.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,2.125*tp),(1.960*tp,2.875*tp),(2.000*tp,2.875*tp),(2.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,1.125*tp),(1.960*tp,1.875*tp),(2.000*tp,1.875*tp),(2.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,1.125*tp),(1.000*tp,1.875*tp),(1.040*tp,1.875*tp),(1.040*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,2.125*tp),(1.000*tp,2.875*tp),(1.040*tp,2.875*tp),(1.040*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,3.125*tp),(1.000*tp,3.875*tp),(1.040*tp,3.875*tp),(1.040*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,4.125*tp),(1.000*tp,4.875*tp),(1.040*tp,4.875*tp),(1.040*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,5.125*tp),(1.000*tp,5.875*tp),(1.040*tp,5.875*tp),(1.040*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,1.000*tp),(1.125*tp,1.040*tp),(1.875*tp,1.040*tp),(1.875*tp,1.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.2975*tp,0.105*tp),(0.2975*tp,1.795*tp),(0.700*tp,1.795*tp),(0.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.300*tp,0.105*tp),(3.300*tp,2.225*tp),(3.700*tp,2.225*tp),(3.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.105*tp,5.300*tp),(0.105*tp,5.700*tp),(0.945*tp,5.700*tp),(0.945*tp,5.300*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.995*tp,3.450*tp),(3.995*tp,3.550*tp),(4.005*tp,3.550*tp),(4.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.450*tp,6.995*tp),(2.450*tp,7.005*tp),(2.550*tp,7.005*tp),(2.550*tp,6.995*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.450*tp,-0.005*tp),(2.450*tp,0.005*tp),(2.550*tp,0.005*tp),(2.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.090*tp,0.580*tp),(2.090*tp,0.635*tp),(2.145*tp,0.635*tp),(2.145*tp,0.580*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.480*tp,3.145*tp),(0.480*tp,3.200*tp),(0.530*tp,3.200*tp),(0.530*tp,3.145*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.580*tp,4.005*tp),(3.580*tp,4.060*tp),(3.635*tp,4.060*tp),(3.635*tp,4.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.030*tp,6.605*tp),(2.030*tp,6.655*tp),(2.080*tp,6.655*tp),(2.080*tp,6.605*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.555*tp,4.900*tp),(1.555*tp,4.950*tp),(1.615*tp,4.950*tp),(1.615*tp,4.900*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.475*tp,3.475*tp),(1.475*tp,3.525*tp),(1.525*tp,3.525*tp),(1.525*tp,3.475*tp)])

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,0.305*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,0.735*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,1.165*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,1.595*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,2.025*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.305*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.735*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.165*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.595*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.74*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.31*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)

        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__ = "M0M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.415*tp,6.015*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.41*tp,1.415*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.71*tp,4.345*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.505*tp,4.895*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.235*tp,4.71*tp),transformation=ls.r270)

        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.83*tp,5.33*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.28*tp,2.355*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.84*tp,2.305*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.03*tp,1.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.97*tp,0.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.275*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.87*tp,2.36*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.275*tp,4.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.23*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.555*tp,4.81*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.42*tp,5.355*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.44*tp,5.805*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.44*tp,4.91*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.15*tp,4.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.655*tp,2.06*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.65*tp,6.035*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.125*tp,4.615*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.62*tp,3.805*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.08*tp,1.57*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.63*tp,0.265*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.09*tp,0.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.225*tp,1.56*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.29*tp,4.805*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.56*tp,3.200*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.300*tp,4.165*tp),transformation=ls.r270)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_175(),midpoint=(0.505*tp,2.22*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(2.11*tp,6.63*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_175(),midpoint=(3.61*tp,4.985*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(1.165*tp,0.61*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_158(),midpoint=(1.500*tp,3.56*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_139(),midpoint=(1.585*tp,6.100*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_258_sg(),midpoint=(2.55*tp,5.395*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_230_sg(),midpoint=(2.55*tp,2.61*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_201_sg(),midpoint=(1.52*tp,4.575*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_180_s(),midpoint=(1.15*tp,4.57*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_177_s(),midpoint=(2.54*tp,2.24*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_164_s(),midpoint=(2.445*tp,5.77*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_090_s(),midpoint=(2.44*tp,4.26*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.44*tp,3.500*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.44*tp,6.475*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.555*tp,3.57*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.44*tp,0.600*tp),transformation=ls.r270)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 4):
                if ((x in [0,3] and y == 6) or (x == 1 and y == 1)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif ((x == 2 and y == 6) or (x == 1 and y in range(1, 7))):
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