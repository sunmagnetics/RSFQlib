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
    __name_prefix__ = "THmitll_OR2_v3p0"
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
        elems += spira.Label(text='P2 M6 M4',position=(2.500*tp,7.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P4 M6 M4',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='clk',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='b',position=(2.500*tp,7.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.700*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.965*tp,4.585*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.32*tp,4.595*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(2.28*tp,4.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(1.92*tp,4.595*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M5 M6',position=(1.44*tp,2.76*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(1.49*tp,2.365*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M6 M5',position=(3.19*tp,1.58*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M6 M5',position=(2.43*tp,0.615*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J11 M5 M6',position=(3.265*tp,1.21*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J12 M6 M5',position=(3.36*tp,3.49*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(1.365*tp,5.025*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.65*tp,5.595*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB6 M6 M4',position=(3.385*tp,4.53*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.375*tp,2.805*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(0.655*tp,2.405*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB5 M6 M4',position=(1.865*tp,0.645*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(2.445*tp,6.385*tp),layer=spira.Layer(number=182,datatype=0))

        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(3.905*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(3.900*tp,6.315*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='clk',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='b',position=(2.500*tp,7.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RIB2',position=(1.655*tp,6.07*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.375*tp,2.37*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(1.365*tp,5.29*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(0.655*tp,1.89*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB6',position=(3.385*tp,4.98*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(1.42*tp,0.635*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB12',position=(3.055*tp,3.49*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB11',position=(3.265*tp,0.875*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(3.465*tp,1.57*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(2.72*tp,0.605*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(1.495*tp,2.065*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(1.735*tp,2.76*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(1.92*tp,4.26*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.31*tp,4.27*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.685*tp,4.600*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.995*tp,3.51*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(2.565*tp,4.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(2.735*tp,6.405*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M6,shape=[(3.860*tp,3.560*tp),(3.900*tp,3.600*tp),(3.900*tp,3.560*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.400*tp),(3.860*tp,3.440*tp),(3.900*tp,3.440*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.440*tp,6.860*tp),(2.400*tp,6.900*tp),(2.440*tp,6.900*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.560*tp,6.860*tp),(2.560*tp,6.900*tp),(2.600*tp,6.900*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.400*tp),(0.100*tp,3.415*tp),(0.115*tp,3.415*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.585*tp),(0.100*tp,3.600*tp),(0.115*tp,3.585*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.500*tp,0.100*tp),(2.500*tp,0.200*tp),(2.600*tp,0.100*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.455*tp,0.730*tp),(2.455*tp,1.265*tp),(2.555*tp,1.265*tp),(2.555*tp,0.730*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.440*tp,6.505*tp),(2.440*tp,6.900*tp),(2.560*tp,6.900*tp),(2.560*tp,6.505*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.295*tp,1.680*tp),(3.295*tp,1.980*tp),(3.330*tp,1.980*tp),(3.330*tp,3.380*tp),(3.450*tp,3.380*tp),(3.450*tp,1.860*tp),(3.415*tp,1.860*tp),(3.415*tp,1.680*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.285*tp,0.100*tp),(2.285*tp,0.395*tp),(2.480*tp,0.395*tp),(2.480*tp,0.495*tp),(2.580*tp,0.495*tp),(2.580*tp,0.295*tp),(2.385*tp,0.295*tp),(2.385*tp,0.200*tp),(2.500*tp,0.200*tp),(2.500*tp,0.100*tp),(2.400*tp,0.100*tp),(2.400*tp,0.100*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.570*tp,0.685*tp),(0.570*tp,1.485*tp),(0.710*tp,1.485*tp),(0.710*tp,0.685*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.700*tp,0.575*tp),(0.700*tp,0.715*tp),(1.040*tp,0.715*tp),(1.040*tp,0.575*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.300*tp,0.710*tp),(0.300*tp,1.985*tp),(0.440*tp,1.985*tp),(0.440*tp,0.710*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.295*tp,2.725*tp),(0.295*tp,2.865*tp),(0.5725*tp,2.865*tp),(0.5725*tp,3.400*tp),(0.7125*tp,3.400*tp),(0.7125*tp,2.725*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.560*tp,5.520*tp),(1.560*tp,5.660*tp),(2.320*tp,5.660*tp),(2.320*tp,6.280*tp),(2.460*tp,6.280*tp),(2.460*tp,5.520*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.695*tp,6.420*tp),(0.695*tp,6.560*tp),(1.745*tp,6.560*tp),(1.745*tp,6.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.295*tp,5.515*tp),(1.295*tp,6.490*tp),(1.435*tp,6.490*tp),(1.435*tp,5.515*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.310*tp,3.610*tp),(3.310*tp,4.600*tp),(3.450*tp,4.600*tp),(3.450*tp,3.610*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.315*tp,5.355*tp),(3.315*tp,6.310*tp),(3.455*tp,6.310*tp),(3.455*tp,5.355*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.400*tp),(3.900*tp,3.600*tp),(4.000*tp,3.600*tp),(4.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.400*tp,0.000*tp),(2.400*tp,0.100*tp),(2.600*tp,0.100*tp),(2.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.020*tp,4.390*tp),(2.020*tp,4.610*tp),(2.180*tp,4.610*tp),(2.180*tp,4.390*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.070*tp,4.475*tp),(1.070*tp,4.695*tp),(1.220*tp,4.695*tp),(1.220*tp,4.475*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.540*tp,4.445*tp),(1.540*tp,4.950*tp),(1.295*tp,4.950*tp),(1.295*tp,5.090*tp),(1.680*tp,5.090*tp),(1.680*tp,4.445*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.305*tp,4.595*tp),(2.305*tp,4.925*tp),(2.570*tp,4.925*tp),(2.570*tp,6.280*tp),(2.690*tp,6.280*tp),(2.690*tp,4.805*tp),(2.425*tp,4.805*tp),(2.425*tp,4.595*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.375*tp,2.465*tp),(1.375*tp,2.640*tp),(1.595*tp,2.640*tp),(1.595*tp,2.465*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,2.330*tp),(0.575*tp,2.470*tp),(1.380*tp,2.470*tp),(1.380*tp,2.330*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.415*tp),(0.100*tp,3.585*tp),(0.590*tp,3.585*tp),(0.590*tp,3.415*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.465*tp,3.440*tp),(3.465*tp,3.560*tp),(4.000*tp,3.560*tp),(4.000*tp,3.440*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.795*tp,0.575*tp),(1.795*tp,0.715*tp),(2.315*tp,0.715*tp),(2.315*tp,0.575*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.165*tp,1.295*tp),(3.165*tp,1.470*tp),(3.365*tp,1.470*tp),(3.365*tp,1.295*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.400*tp,6.900*tp),(2.400*tp,7.000*tp),(2.600*tp,7.000*tp),(2.600*tp,6.900*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.625*tp,3.620*tp),(0.625*tp,3.725*tp),(0.305*tp,3.725*tp),(0.305*tp,3.995*tp),(0.345*tp,3.995*tp),(0.345*tp,4.095*tp),(0.305*tp,4.095*tp),(0.305*tp,4.380*tp),(0.785*tp,4.380*tp),(0.785*tp,4.490*tp),(0.875*tp,4.490*tp),(0.875*tp,4.290*tp),(0.395*tp,4.290*tp),(0.395*tp,4.185*tp),(0.435*tp,4.185*tp),(0.435*tp,3.905*tp),(0.395*tp,3.905*tp),(0.395*tp,3.815*tp),(0.715*tp,3.815*tp),(0.715*tp,3.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.320*tp,1.520*tp),(2.320*tp,1.805*tp),(2.610*tp,1.805*tp),(2.610*tp,1.940*tp),(2.300*tp,1.940*tp),(2.300*tp,2.230*tp),(2.570*tp,2.230*tp),(2.570*tp,2.345*tp),(2.075*tp,2.345*tp),(2.075*tp,2.405*tp),(1.945*tp,2.405*tp),(1.945*tp,2.345*tp),(1.575*tp,2.345*tp),(1.575*tp,2.435*tp),(1.855*tp,2.435*tp),(1.855*tp,2.495*tp),(2.165*tp,2.495*tp),(2.165*tp,2.435*tp),(2.660*tp,2.435*tp),(2.660*tp,2.140*tp),(2.390*tp,2.140*tp),(2.390*tp,2.030*tp),(2.700*tp,2.030*tp),(2.700*tp,1.715*tp),(2.410*tp,1.715*tp),(2.410*tp,1.610*tp),(3.080*tp,1.610*tp),(3.080*tp,1.520*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.485*tp,1.150*tp),(2.485*tp,1.250*tp),(3.165*tp,1.250*tp),(3.165*tp,1.150*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.280*tp,4.355*tp),(1.280*tp,4.715*tp),(1.980*tp,4.715*tp),(1.980*tp,4.355*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.455*tp,2.860*tp),(1.455*tp,3.255*tp),(1.515*tp,3.255*tp),(1.515*tp,4.565*tp),(1.705*tp,4.565*tp),(1.705*tp,3.065*tp),(1.645*tp,3.065*tp),(1.645*tp,2.860*tp)])
        return elems
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(2.720*tp,1.040*tp),(2.720*tp,1.280*tp),(2.960*tp,1.280*tp),(2.960*tp,1.125*tp),(2.875*tp,1.125*tp),(2.875*tp,1.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.125*tp,4.040*tp),(1.125*tp,4.125*tp),(1.040*tp,4.125*tp),(1.040*tp,4.280*tp),(1.280*tp,4.280*tp),(1.280*tp,4.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.720*tp,4.040*tp),(1.720*tp,4.280*tp),(1.960*tp,4.280*tp),(1.960*tp,4.125*tp),(1.875*tp,4.125*tp),(1.875*tp,4.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.040*tp,3.720*tp),(1.040*tp,3.875*tp),(1.125*tp,3.875*tp),(1.125*tp,3.960*tp),(1.280*tp,3.960*tp),(1.280*tp,3.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.720*tp,3.720*tp),(1.720*tp,3.960*tp),(1.875*tp,3.960*tp),(1.875*tp,3.875*tp),(1.960*tp,3.875*tp),(1.960*tp,3.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.720*tp,2.720*tp),(1.720*tp,2.960*tp),(1.875*tp,2.960*tp),(1.875*tp,2.875*tp),(1.960*tp,2.875*tp),(1.960*tp,2.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.040*tp,2.720*tp),(2.040*tp,2.875*tp),(2.125*tp,2.875*tp),(2.125*tp,2.960*tp),(2.280*tp,2.960*tp),(2.280*tp,2.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(3.125*tp,1.040*tp),(3.125*tp,1.125*tp),(3.040*tp,1.125*tp),(3.040*tp,1.280*tp),(3.280*tp,1.280*tp),(3.280*tp,1.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(3.040*tp,0.720*tp),(3.040*tp,0.875*tp),(3.125*tp,0.875*tp),(3.125*tp,0.960*tp),(3.280*tp,0.960*tp),(3.280*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,5.300*tp),(0.300*tp,6.125*tp),(0.700*tp,6.125*tp),(0.700*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(4.000*tp,6.650*tp),(4.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.350*tp,0.500*tp),(0.350*tp,6.500*tp),(0.650*tp,6.500*tp),(0.650*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(3.125*tp,6.000*tp),(3.125*tp,6.040*tp),(3.875*tp,6.040*tp),(3.875*tp,6.000*tp)])
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
        elems += spira.Polygon(layer=IXPORT,shape=[(3.995*tp,3.450*tp),(3.995*tp,3.550*tp),(4.005*tp,3.550*tp),(4.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.450*tp,-0.005*tp),(2.450*tp,0.005*tp),(2.550*tp,0.005*tp),(2.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.450*tp,6.995*tp),(2.450*tp,7.005*tp),(2.550*tp,7.005*tp),(2.550*tp,6.995*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.625*tp,5.565*tp),(1.625*tp,5.620*tp),(1.680*tp,5.620*tp),(1.680*tp,5.565*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.340*tp,4.995*tp),(1.340*tp,5.045*tp),(1.395*tp,5.045*tp),(1.395*tp,4.995*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.360*tp,4.500*tp),(3.360*tp,4.550*tp),(3.405*tp,4.550*tp),(3.405*tp,4.500*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.350*tp,2.775*tp),(0.350*tp,2.830*tp),(0.405*tp,2.830*tp),(0.405*tp,2.775*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.625*tp,2.380*tp),(0.625*tp,2.435*tp),(0.680*tp,2.435*tp),(0.680*tp,2.380*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.835*tp,0.625*tp),(1.835*tp,0.670*tp),(1.900*tp,0.670*tp),(1.900*tp,0.625*tp)])

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.000*tp,1.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.01*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,3.03*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.925*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.02*tp,3.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp))

        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__ = "M0M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.425*tp,1.11*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.525*tp,4.415*tp))

        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.33*tp,0.12*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.88*tp,0.305*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.785*tp,0.305*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.84*tp,1.43*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.83*tp,2.425*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.355*tp,3.825*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.58*tp,4.815*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.69*tp,0.86*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.700*tp,4.81*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.88*tp,5.29*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.700*tp,5.765*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.88*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.54*tp,3.36*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.055*tp,5.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.07*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.065*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.700*tp,3.87*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.695*tp,2.81*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.695*tp,1.86*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.875*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.66*tp,6.875*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.64*tp,0.265*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.665*tp,4.255*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.655*tp,1.53*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.86*tp,0.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.655*tp,2.700*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_158(),midpoint=(0.65*tp,1.36*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(0.375*tp,1.85*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(1.65*tp,6.545*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(3.385*tp,5.48*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(0.91*tp,0.645*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_283(),midpoint=(1.365*tp,4.965*tp))
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_144_s(),midpoint=(3.265*tp,1.21*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_148_s(),midpoint=(1.315*tp,4.595*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_148_s(),midpoint=(1.925*tp,4.595*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_167_sg(),midpoint=(0.965*tp,4.585*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_167_sg(),midpoint=(2.28*tp,4.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_176_sg(),midpoint=(3.19*tp,1.575*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_227_s(),midpoint=(1.445*tp,2.755*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_236_sg(),midpoint=(1.49*tp,2.355*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.355*tp,3.49*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.43*tp,0.61*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.700*tp,3.505*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.445*tp,6.39*tp),transformation=ls.r270)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 4):
                if ((x == 0 and y in [0,6]) or (x == 3 and y == 6)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif ((x in [1,2] and y == 6) or (x == 0 and y in range(1, 6))):
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