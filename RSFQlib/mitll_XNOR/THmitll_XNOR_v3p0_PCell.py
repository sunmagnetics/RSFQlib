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
    __name_prefix__ = "THmitll_XNOR_v3p0"
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
        elems += spira.Label(text='J13 M5 M6',position=(4.705*tp,2.145*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J18 M6 M5',position=(4.72*tp,2.465*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J14 M5 M6',position=(4.41*tp,1.695*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J17 M5 M6',position=(4.765*tp,1.765*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J12 M5 M6',position=(4.115*tp,2.400*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.505*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.535*tp,4.42*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(0.92*tp,4.42*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(1.56*tp,6.48*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(1.555*tp,5.625*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(1.56*tp,5.24*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M5 M6',position=(2.405*tp,4.18*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M5 M6',position=(1.500*tp,2.28*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(1.56*tp,2.63*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M6 M5',position=(1.43*tp,0.595*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J11 M6 M5',position=(2.505*tp,2.455*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J15 M6 M5',position=(2.500*tp,1.435*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J16 M6 M5',position=(3.500*tp,1.56*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J19 M6 M5',position=(5.435*tp,3.495*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB5 M6 M4',position=(3.355*tp,3.25*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB6 M6 M4',position=(3.59*tp,3.215*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB8 M6 M4',position=(4.355*tp,3.45*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P4 M6 M4',position=(6.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB7 M6 M4',position=(2.525*tp,0.39*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(0.500*tp,0.165*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.445*tp,3.145*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(1.500*tp,7.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(2.075*tp,6.59*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(2.645*tp,5.09*tp),layer=spira.Layer(number=182,datatype=0))

        
        # LVS Labels
        elems += spira.Label(text='RB13',position=(5.155*tp,2.15*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB18',position=(4.98*tp,2.46*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB14',position=(4.405*tp,1.355*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB17',position=(4.76*tp,1.405*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB12',position=(3.65*tp,2.400*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.45*tp,2.675*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(2.51*tp,6.59*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.645*tp,5.495*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(0.505*tp,0.77*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(3.355*tp,3.66*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB6',position=(3.58*tp,3.745*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB7',position=(3.13*tp,0.395*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB8',position=(4.36*tp,3.945*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.795*tp,3.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.535*tp,4.715*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.225*tp,4.425*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.255*tp,6.465*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(1.275*tp,5.615*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(1.26*tp,5.24*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(2.41*tp,3.86*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(1.26*tp,2.63*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(1.725*tp,0.595*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(1.500*tp,1.94*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB11',position=(2.505*tp,2.735*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB15',position=(2.505*tp,1.705*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB16',position=(3.495*tp,1.27*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB19',position=(5.445*tp,3.79*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='b',position=(1.500*tp,7.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='clk',position=(1.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(6.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='GND',position=(5.96*tp,6.33*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='VDD',position=(5.96*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M6,shape=[(1.500*tp,0.170*tp),(1.500*tp,0.270*tp),(1.600*tp,0.170*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.490*tp),(0.100*tp,3.600*tp),(0.210*tp,3.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.500*tp,6.785*tp),(1.400*tp,6.885*tp),(1.500*tp,6.885*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(5.900*tp,3.400*tp),(5.790*tp,3.510*tp),(5.900*tp,3.510*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.635*tp,2.220*tp),(4.635*tp,2.375*tp),(4.915*tp,2.375*tp),(4.915*tp,2.220*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.8425*tp,2.450*tp),(4.8425*tp,2.7125*tp),(5.2875*tp,2.7125*tp),(5.2875*tp,3.1375*tp),(5.3625*tp,3.1375*tp),(5.3625*tp,3.380*tp),(5.4575*tp,3.380*tp),(5.4575*tp,3.0425*tp),(5.3825*tp,3.0425*tp),(5.3825*tp,2.6175*tp),(4.9375*tp,2.6175*tp),(4.9375*tp,2.450*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.855*tp,1.305*tp),(2.855*tp,1.625*tp),(2.780*tp,1.625*tp),(2.780*tp,1.325*tp),(2.605*tp,1.325*tp),(2.605*tp,1.415*tp),(2.690*tp,1.415*tp),(2.690*tp,1.715*tp),(2.945*tp,1.715*tp),(2.945*tp,1.395*tp),(3.035*tp,1.395*tp),(3.035*tp,1.715*tp),(3.305*tp,1.715*tp),(3.305*tp,1.545*tp),(3.390*tp,1.545*tp),(3.390*tp,1.455*tp),(3.215*tp,1.455*tp),(3.215*tp,1.625*tp),(3.125*tp,1.625*tp),(3.125*tp,1.305*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.615*tp,2.355*tp),(2.615*tp,2.445*tp),(3.000*tp,2.445*tp),(3.000*tp,2.355*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.735*tp,2.290*tp),(1.735*tp,2.620*tp),(1.650*tp,2.620*tp),(1.650*tp,2.710*tp),(1.825*tp,2.710*tp),(1.825*tp,2.380*tp),(1.895*tp,2.380*tp),(1.895*tp,2.705*tp),(2.145*tp,2.705*tp),(2.145*tp,2.390*tp),(2.215*tp,2.390*tp),(2.215*tp,2.675*tp),(2.385*tp,2.675*tp),(2.385*tp,2.585*tp),(2.305*tp,2.585*tp),(2.305*tp,2.300*tp),(2.055*tp,2.300*tp),(2.055*tp,2.615*tp),(1.985*tp,2.615*tp),(1.985*tp,2.290*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.3975*tp,0.710*tp),(1.3975*tp,1.0525*tp),(1.4475*tp,1.0525*tp),(1.4475*tp,1.465*tp),(1.5525*tp,1.465*tp),(1.5525*tp,0.9475*tp),(1.5025*tp,0.9475*tp),(1.5025*tp,0.710*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,0.170*tp),(1.400*tp,0.485*tp),(1.500*tp,0.485*tp),(1.500*tp,0.170*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,0.000*tp),(1.400*tp,0.170*tp),(1.600*tp,0.170*tp),(1.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.520*tp,2.715*tp),(1.520*tp,2.960*tp),(1.590*tp,2.960*tp),(1.590*tp,3.090*tp),(1.520*tp,3.090*tp),(1.520*tp,3.410*tp),(2.595*tp,3.410*tp),(2.595*tp,4.135*tp),(2.500*tp,4.135*tp),(2.500*tp,4.255*tp),(2.715*tp,4.255*tp),(2.715*tp,3.290*tp),(1.640*tp,3.290*tp),(1.640*tp,3.210*tp),(1.710*tp,3.210*tp),(1.710*tp,2.840*tp),(1.640*tp,2.840*tp),(1.640*tp,2.715*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.550*tp,3.615*tp),(0.550*tp,3.805*tp),(0.330*tp,3.805*tp),(0.330*tp,4.105*tp),(0.500*tp,4.105*tp),(0.500*tp,4.320*tp),(0.590*tp,4.320*tp),(0.590*tp,4.015*tp),(0.420*tp,4.015*tp),(0.420*tp,3.895*tp),(0.640*tp,3.895*tp),(0.640*tp,3.615*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.615*tp,1.365*tp),(3.615*tp,1.465*tp),(3.925*tp,1.465*tp),(3.925*tp,1.485*tp),(4.025*tp,1.485*tp),(4.025*tp,1.365*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.6175*tp,1.825*tp),(4.6175*tp,2.075*tp),(4.9175*tp,2.075*tp),(4.9175*tp,1.825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.3325*tp,1.775*tp),(4.3325*tp,1.965*tp),(4.465*tp,1.965*tp),(4.465*tp,2.040*tp),(4.130*tp,2.040*tp),(4.130*tp,2.135*tp),(3.985*tp,2.135*tp),(3.985*tp,2.315*tp),(4.065*tp,2.315*tp),(4.065*tp,2.215*tp),(4.210*tp,2.215*tp),(4.210*tp,2.120*tp),(4.545*tp,2.120*tp),(4.545*tp,1.885*tp),(4.4125*tp,1.885*tp),(4.4125*tp,1.775*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.285*tp,2.195*tp),(4.285*tp,2.620*tp),(4.545*tp,2.620*tp),(4.545*tp,2.195*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.140*tp,2.290*tp),(4.140*tp,2.620*tp),(4.475*tp,2.620*tp),(4.475*tp,2.290*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,2.480*tp),(3.900*tp,2.585*tp),(3.520*tp,2.585*tp),(3.520*tp,3.275*tp),(3.650*tp,3.275*tp),(3.650*tp,2.715*tp),(4.030*tp,2.715*tp),(4.030*tp,2.480*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.400*tp),(0.100*tp,3.490*tp),(0.400*tp,3.490*tp),(0.400*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.375*tp,3.080*tp),(0.375*tp,3.380*tp),(0.515*tp,3.380*tp),(0.515*tp,3.080*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.375*tp,1.500*tp),(0.375*tp,2.320*tp),(0.515*tp,2.320*tp),(0.515*tp,1.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.400*tp,0.990*tp),(0.400*tp,1.500*tp),(0.600*tp,1.500*tp),(0.600*tp,0.990*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,0.095*tp),(0.430*tp,0.695*tp),(1.325*tp,0.695*tp),(1.325*tp,0.555*tp),(0.570*tp,0.555*tp),(0.570*tp,0.095*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.650*tp,4.305*tp),(0.650*tp,4.545*tp),(0.810*tp,4.545*tp),(0.810*tp,4.305*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.505*tp,5.720*tp),(1.505*tp,5.880*tp),(1.300*tp,5.880*tp),(1.300*tp,6.180*tp),(1.545*tp,6.180*tp),(1.545*tp,6.350*tp),(1.635*tp,6.350*tp),(1.635*tp,6.090*tp),(1.390*tp,6.090*tp),(1.390*tp,5.970*tp),(1.595*tp,5.970*tp),(1.595*tp,5.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,6.885*tp),(1.400*tp,7.000*tp),(1.600*tp,7.000*tp),(1.600*tp,6.885*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.500*tp,6.570*tp),(1.500*tp,6.885*tp),(1.600*tp,6.885*tp),(1.600*tp,6.570*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.330*tp,5.355*tp),(1.330*tp,5.505*tp),(1.670*tp,5.505*tp),(1.670*tp,5.355*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.575*tp,5.790*tp),(2.575*tp,6.425*tp),(3.290*tp,6.425*tp),(3.290*tp,6.285*tp),(2.715*tp,6.285*tp),(2.715*tp,5.790*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.665*tp,6.350*tp),(1.665*tp,6.490*tp),(2.000*tp,6.490*tp),(2.000*tp,6.660*tp),(2.140*tp,6.660*tp),(2.140*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.895*tp,6.520*tp),(2.895*tp,6.660*tp),(3.290*tp,6.660*tp),(3.290*tp,6.520*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.345*tp,4.415*tp),(2.345*tp,4.555*tp),(2.530*tp,4.555*tp),(2.530*tp,4.920*tp),(2.575*tp,4.920*tp),(2.575*tp,5.170*tp),(2.715*tp,5.170*tp),(2.715*tp,4.780*tp),(2.670*tp,4.780*tp),(2.670*tp,4.415*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,1.350*tp),(1.430*tp,1.450*tp),(2.400*tp,1.450*tp),(2.400*tp,1.350*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.455*tp,0.325*tp),(2.455*tp,1.320*tp),(2.595*tp,1.320*tp),(2.595*tp,0.325*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.725*tp,0.325*tp),(3.725*tp,0.455*tp),(5.280*tp,0.455*tp),(5.280*tp,0.325*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.405*tp,2.375*tp),(1.405*tp,2.520*tp),(1.605*tp,2.520*tp),(1.605*tp,2.375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.290*tp,2.600*tp),(3.290*tp,3.320*tp),(3.430*tp,3.320*tp),(3.430*tp,2.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.615*tp,2.585*tp),(2.615*tp,2.685*tp),(3.430*tp,2.685*tp),(3.430*tp,2.585*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(5.900*tp,3.400*tp),(5.900*tp,3.600*tp),(6.000*tp,3.600*tp),(6.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(5.550*tp,3.510*tp),(5.550*tp,3.600*tp),(5.900*tp,3.600*tp),(5.900*tp,3.510*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.300*tp,4.600*tp),(3.300*tp,6.295*tp),(3.500*tp,6.295*tp),(3.500*tp,4.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.290*tp,4.000*tp),(3.290*tp,4.600*tp),(3.430*tp,4.600*tp),(3.430*tp,4.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.515*tp,4.195*tp),(3.515*tp,4.530*tp),(3.290*tp,4.530*tp),(3.290*tp,4.670*tp),(3.655*tp,4.670*tp),(3.655*tp,4.195*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.285*tp,3.375*tp),(4.285*tp,3.670*tp),(5.335*tp,3.670*tp),(5.335*tp,3.530*tp),(4.425*tp,3.530*tp),(4.425*tp,3.375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.285*tp,4.275*tp),(4.285*tp,4.340*tp),(3.615*tp,4.340*tp),(3.615*tp,4.480*tp),(4.425*tp,4.480*tp),(4.425*tp,4.275*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.910*tp,1.455*tp),(3.910*tp,1.715*tp),(4.330*tp,1.715*tp),(4.330*tp,1.615*tp),(4.010*tp,1.615*tp),(4.010*tp,1.455*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.845*tp,2.335*tp),(2.845*tp,2.455*tp),(3.315*tp,2.455*tp),(3.315*tp,2.335*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.515*tp,4.615*tp),(1.515*tp,5.110*tp),(1.675*tp,5.110*tp),(1.675*tp,4.615*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.540*tp,4.3975*tp),(1.540*tp,4.5025*tp),(2.525*tp,4.5025*tp),(2.525*tp,4.3975*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.530*tp,1.535*tp),(4.530*tp,1.805*tp),(4.650*tp,1.805*tp),(4.650*tp,1.535*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.325*tp,2.0325*tp),(4.325*tp,2.350*tp),(4.515*tp,2.350*tp),(4.515*tp,2.0325*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.325*tp,1.9925*tp),(4.325*tp,2.2475*tp),(4.625*tp,2.2475*tp),(4.625*tp,1.9925*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.3825*tp,1.310*tp),(1.3825*tp,2.3925*tp),(1.6275*tp,2.3925*tp),(1.6275*tp,1.310*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.330*tp,4.485*tp),(2.330*tp,4.615*tp),(1.595*tp,4.615*tp),(1.595*tp,5.110*tp),(1.695*tp,5.110*tp),(1.695*tp,4.715*tp),(2.430*tp,4.715*tp),(2.430*tp,4.485*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.285*tp,4.270*tp),(2.285*tp,4.570*tp),(2.525*tp,4.570*tp),(2.525*tp,4.270*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.285*tp,4.520*tp),(2.285*tp,4.620*tp),(2.425*tp,4.620*tp),(2.425*tp,4.520*tp)])

        return elems
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(4.720*tp,1.720*tp),(4.720*tp,1.960*tp),(4.875*tp,1.960*tp),(4.875*tp,1.875*tp),(4.960*tp,1.875*tp),(4.960*tp,1.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(4.720*tp,1.040*tp),(4.720*tp,1.280*tp),(4.960*tp,1.280*tp),(4.960*tp,1.125*tp),(4.875*tp,1.125*tp),(4.875*tp,1.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(4.125*tp,2.040*tp),(4.125*tp,2.125*tp),(4.040*tp,2.125*tp),(4.040*tp,2.280*tp),(4.280*tp,2.280*tp),(4.280*tp,2.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(4.720*tp,2.040*tp),(4.720*tp,2.280*tp),(4.960*tp,2.280*tp),(4.960*tp,2.125*tp),(4.875*tp,2.125*tp),(4.875*tp,2.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(5.125*tp,2.040*tp),(5.125*tp,2.125*tp),(5.040*tp,2.125*tp),(5.040*tp,2.280*tp),(5.280*tp,2.280*tp),(5.280*tp,2.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.125*tp,5.040*tp),(1.125*tp,5.125*tp),(1.040*tp,5.125*tp),(1.040*tp,5.280*tp),(1.280*tp,5.280*tp),(1.280*tp,5.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(0.720*tp,5.040*tp),(0.720*tp,5.280*tp),(0.960*tp,5.280*tp),(0.960*tp,5.125*tp),(0.875*tp,5.125*tp),(0.875*tp,5.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,5.200*tp),(0.300*tp,6.890*tp),(0.700*tp,6.890*tp),(0.700*tp,5.200*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(5.300*tp,4.345*tp),(5.300*tp,6.895*tp),(5.700*tp,6.895*tp),(5.700*tp,4.345*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.000*tp,5.300*tp),(4.000*tp,5.700*tp),(5.300*tp,5.700*tp),(5.300*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.000*tp,6.300*tp),(4.000*tp,6.700*tp),(5.300*tp,6.700*tp),(5.300*tp,6.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(5.260*tp,4.345*tp),(5.260*tp,4.700*tp),(5.300*tp,4.700*tp),(5.300*tp,4.345*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.350*tp,1.500*tp),(0.350*tp,6.500*tp),(0.650*tp,6.500*tp),(0.650*tp,1.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(6.000*tp,6.650*tp),(6.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(5.350*tp,0.500*tp),(5.350*tp,6.500*tp),(5.650*tp,6.500*tp),(5.650*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(4.125*tp,6.000*tp),(4.125*tp,6.040*tp),(4.875*tp,6.040*tp),(4.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(3.125*tp,6.000*tp),(3.125*tp,6.040*tp),(3.875*tp,6.040*tp),(3.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,1.000*tp),(0.125*tp,1.040*tp),(0.875*tp,1.040*tp),(0.875*tp,1.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,1.125*tp),(0.960*tp,1.875*tp),(1.000*tp,1.875*tp),(1.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,2.125*tp),(0.960*tp,2.875*tp),(1.000*tp,2.875*tp),(1.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,3.125*tp),(0.960*tp,3.875*tp),(1.000*tp,3.875*tp),(1.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,4.125*tp),(0.960*tp,4.875*tp),(1.000*tp,4.875*tp),(1.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,5.125*tp),(0.960*tp,5.875*tp),(1.000*tp,5.875*tp),(1.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(5.000*tp,5.125*tp),(5.000*tp,5.875*tp),(5.040*tp,5.875*tp),(5.040*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(5.000*tp,4.125*tp),(5.000*tp,4.875*tp),(5.040*tp,4.875*tp),(5.040*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(5.000*tp,4.125*tp),(5.000*tp,4.875*tp),(5.040*tp,4.875*tp),(5.040*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(5.000*tp,3.125*tp),(5.000*tp,3.875*tp),(5.040*tp,3.875*tp),(5.040*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(5.000*tp,2.125*tp),(5.000*tp,2.875*tp),(5.040*tp,2.875*tp),(5.040*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(5.000*tp,1.125*tp),(5.000*tp,1.875*tp),(5.040*tp,1.875*tp),(5.040*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(5.000*tp,0.125*tp),(5.000*tp,0.875*tp),(5.040*tp,0.875*tp),(5.040*tp,0.125*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(1.450*tp,6.995*tp),(1.450*tp,7.005*tp),(1.550*tp,7.005*tp),(1.550*tp,6.995*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(5.995*tp,3.450*tp),(5.995*tp,3.550*tp),(6.005*tp,3.550*tp),(6.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.450*tp,-0.005*tp),(1.450*tp,0.005*tp),(1.550*tp,0.005*tp),(1.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.045*tp,6.565*tp),(2.045*tp,6.615*tp),(2.095*tp,6.615*tp),(2.095*tp,6.565*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.615*tp,5.070*tp),(2.615*tp,5.125*tp),(2.675*tp,5.125*tp),(2.675*tp,5.070*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.335*tp,3.225*tp),(3.335*tp,3.275*tp),(3.385*tp,3.275*tp),(3.385*tp,3.225*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.560*tp,3.180*tp),(3.560*tp,3.235*tp),(3.615*tp,3.235*tp),(3.615*tp,3.180*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(4.330*tp,3.420*tp),(4.330*tp,3.475*tp),(4.380*tp,3.475*tp),(4.380*tp,3.420*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.500*tp,0.365*tp),(2.500*tp,0.415*tp),(2.555*tp,0.415*tp),(2.555*tp,0.365*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.475*tp,0.140*tp),(0.475*tp,0.195*tp),(0.525*tp,0.195*tp),(0.525*tp,0.140*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.415*tp,3.120*tp),(0.415*tp,3.175*tp),(0.470*tp,3.175*tp),(0.470*tp,3.120*tp)])

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.06*tp,4.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.200*tp,5.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.63*tp,5.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.06*tp,5.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.200*tp,6.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.63*tp,6.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.06*tp,6.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.400*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.83*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.26*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.69*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,4.025*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.285*tp,5.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.500*tp,4.545*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.500*tp,4.975*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.500*tp,5.405*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.500*tp,5.835*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.500*tp,6.265*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.500*tp,6.695*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(5.500*tp,1.035*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(5.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(5.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(5.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(5.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,5.000*tp),transformation=ls.r90)


        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__ = "M0M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.845*tp,2.31*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.33*tp,4.400*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(4.495*tp,2.18*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.585*tp,1.48*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(3.91*tp,1.34*tp),transformation=ls.m45)

        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.89*tp,4.305*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.335*tp,0.115*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.78*tp,0.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.33*tp,0.115*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.295*tp,0.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.85*tp,0.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.41*tp,0.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(5.300*tp,1.785*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.385*tp,0.115*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.95*tp,0.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.87*tp,3.300*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.96*tp,5.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.33*tp,0.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.700*tp,3.125*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,2.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(5.700*tp,2.725*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.44*tp,4.83*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.96*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.44*tp,6.095*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(5.88*tp,1.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.735*tp,2.355*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.445*tp,2.93*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(5.47*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.835*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.700*tp,4.35*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.695*tp,3.785*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.23*tp,5.32*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.905*tp,3.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.18*tp,3.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.44*tp,1.87*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.17*tp,4.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.145*tp,4.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.11*tp,0.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.65*tp,3.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.145*tp,3.685*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.66*tp,6.88*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.11*tp,3.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.655*tp,3.02*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.17*tp,1.565*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(5.015*tp,1.665*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(5.745*tp,2.62*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.56*tp,2.13*tp),transformation=ls.r270)

        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_122(),midpoint=(3.85*tp,0.39*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_147(),midpoint=(3.585*tp,3.155*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(0.445*tp,2.195*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(4.355*tp,4.400*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(0.500*tp,1.12*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(2.015*tp,6.59*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_193(),midpoint=(3.36*tp,3.195*tp))
        elems += spira.SRef(bias.ib_207(),midpoint=(2.645*tp,5.04*tp))
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_072_s(),midpoint=(4.705*tp,2.145*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_077_s(),midpoint=(4.115*tp,2.395*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_083_sg(),midpoint=(4.725*tp,2.455*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_105_s(),midpoint=(4.755*tp,1.765*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_128_s(),midpoint=(1.505*tp,2.275*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_134_s(),midpoint=(4.415*tp,1.69*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_139_s(),midpoint=(2.405*tp,4.18*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_157_sg(),midpoint=(1.555*tp,2.62*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_163_sg(),midpoint=(2.500*tp,1.425*tp))
        elems += spira.SRef(jj.jj_212_s(),midpoint=(1.56*tp,5.24*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_212_s(),midpoint=(0.92*tp,4.425*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_215_sg(),midpoint=(3.500*tp,1.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_222_sg(),midpoint=(0.54*tp,4.42*tp))
        elems += spira.SRef(jj.jj_222_sg(),midpoint=(1.56*tp,5.615*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_243_sg(),midpoint=(2.505*tp,2.44*tp))
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(5.445*tp,3.49*tp))
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.56*tp,6.46*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.500*tp,3.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.44*tp,0.595*tp),transformation=ls.r270)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 6):
                if ((x == 0 and y == 1) or (x == 3 and y == 6) or (x == 5 and y == 0)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif ((x == 0 and y in range(2,7)) or (x in [1,2,4] and y == 6) or (x == 5 and y in range(1, 7))):
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