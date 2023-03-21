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
    __name_prefix__ = "THmitll_NDROT_v3p0"
    def create_elements(self, elems):
        M6M5Strips = spira.SRef(M6M5_strips())
        IXports = spira.SRef(IX_ports())
        M0M4M7tracks = spira.SRef(M0M4M7_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        rs = spira.SRef(resistors())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M6M5Strips, IXports, M0M4M7tracks, jjfill, M4M5M6M7conns,
                  vias, ib, jjs, rs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text='P2 M6 M4',position=(4.15*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.85*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(1.695*tp,5.645*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.07*tp,4.38*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(2.500*tp,3.525*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(3.31*tp,5.645*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB5 M6 M4',position=(3.925*tp,4.38*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB6 M6 M4',position=(3.295*tp,2.355*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB7 M6 M4',position=(1.13*tp,0.65*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB8 M6 M4',position=(4.355*tp,1.625*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P4 M6 M4',position=(3.500*tp,1.265*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(0.500*tp,2.15*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(1.265*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.505*tp,5.445*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(0.76*tp,4.43*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(1.55*tp,3.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(3.735*tp,6.49*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(4.495*tp,5.44*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(4.24*tp,4.43*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M6 M5',position=(3.445*tp,3.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J12 M6 M5',position=(2.56*tp,1.62*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J13 M6 M5',position=(0.505*tp,1.56*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J14 M6 M5',position=(1.59*tp,0.805*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J16 M6 M5',position=(3.495*tp,1.565*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J15 M5 M6',position=(2.500*tp,1.28*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J11 M5 M6',position=(2.500*tp,2.445*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M5 M6',position=(1.18*tp,3.585*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M5 M6',position=(3.825*tp,3.585*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(2.500*tp,6.96*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(0.500*tp,0.04*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(4.500*tp,0.04*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='GND',position=(2.36*tp,6.96*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RB1',position=(1.54*tp,6.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.505*tp,5.71*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(0.46*tp,4.43*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(0.865*tp,3.59*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(1.54*tp,3.795*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(3.44*tp,3.795*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(4.11*tp,3.58*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(4.52*tp,4.43*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(4.500*tp,5.71*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(3.46*tp,6.49*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB11',position=(2.505*tp,2.825*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB12',position=(2.275*tp,1.62*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB15',position=(2.500*tp,0.92*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB16',position=(3.500*tp,1.865*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB14',position=(1.585*tp,0.53*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB13',position=(0.500*tp,1.285*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB7',position=(0.835*tp,0.655*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB8',position=(4.345*tp,1.200*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB6',position=(3.885*tp,2.365*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(3.315*tp,4.385*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.505*tp,3.91*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.800*tp,4.38*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(1.98*tp,5.66*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(3.015*tp,5.655*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(3.495*tp,1.175*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='a',position=(0.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='b',position=(4.505*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(3.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='clk',position=(0.500*tp,2.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(3.280*tp,0.720*tp),(3.500*tp,0.940*tp),(3.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,2.060*tp),(0.280*tp,2.280*tp),(0.720*tp,2.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.720*tp,6.280*tp),(0.720*tp,6.720*tp),(0.940*tp,6.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.280*tp,6.280*tp),(4.060*tp,6.500*tp),(4.280*tp,6.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.420*tp,0.720*tp),(3.420*tp,1.1325*tp),(3.580*tp,1.1325*tp),(3.580*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.430*tp,1.2025*tp),(3.430*tp,1.445*tp),(3.570*tp,1.445*tp),(3.570*tp,1.2025*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.615*tp,1.555*tp),(3.615*tp,1.695*tp),(4.420*tp,1.695*tp),(4.420*tp,1.555*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.430*tp,0.230*tp),(4.430*tp,0.660*tp),(4.285*tp,0.660*tp),(4.285*tp,0.800*tp),(4.570*tp,0.800*tp),(4.570*tp,0.230*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.500*tp,0.570*tp),(4.500*tp,1.270*tp),(4.520*tp,1.270*tp),(4.520*tp,2.070*tp),(4.565*tp,2.070*tp),(4.565*tp,2.425*tp),(4.705*tp,2.425*tp),(4.705*tp,1.930*tp),(4.660*tp,1.930*tp),(4.660*tp,1.130*tp),(4.640*tp,1.130*tp),(4.640*tp,0.570*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.720*tp,6.420*tp),(0.720*tp,6.580*tp),(1.170*tp,6.580*tp),(1.170*tp,6.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.830*tp,6.420*tp),(3.830*tp,6.580*tp),(4.280*tp,6.580*tp),(4.280*tp,6.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,4.160*tp),(2.430*tp,6.570*tp),(2.570*tp,6.570*tp),(2.570*tp,4.160*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.200*tp,4.310*tp),(2.200*tp,4.450*tp),(2.795*tp,4.450*tp),(2.795*tp,4.310*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.220*tp,5.575*tp),(2.220*tp,5.715*tp),(2.780*tp,5.715*tp),(2.780*tp,5.575*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.555*tp,5.490*tp),(3.555*tp,5.855*tp),(3.520*tp,5.855*tp),(3.520*tp,6.245*tp),(3.605*tp,6.245*tp),(3.605*tp,6.400*tp),(3.695*tp,6.400*tp),(3.695*tp,6.155*tp),(3.610*tp,6.155*tp),(3.610*tp,5.945*tp),(3.645*tp,5.945*tp),(3.645*tp,5.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.355*tp,5.490*tp),(1.355*tp,5.945*tp),(1.385*tp,5.945*tp),(1.385*tp,6.155*tp),(1.305*tp,6.155*tp),(1.305*tp,6.400*tp),(1.395*tp,6.400*tp),(1.395*tp,6.245*tp),(1.475*tp,6.245*tp),(1.475*tp,5.855*tp),(1.445*tp,5.855*tp),(1.445*tp,5.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.355*tp,5.490*tp),(1.355*tp,5.630*tp),(1.630*tp,5.630*tp),(1.630*tp,5.710*tp),(1.770*tp,5.710*tp),(1.770*tp,5.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.600*tp,0.900*tp),(1.600*tp,1.030*tp),(1.475*tp,1.030*tp),(1.475*tp,1.290*tp),(1.600*tp,1.290*tp),(1.600*tp,1.405*tp),(1.335*tp,1.405*tp),(1.335*tp,1.495*tp),(1.690*tp,1.495*tp),(1.690*tp,1.200*tp),(1.565*tp,1.200*tp),(1.565*tp,1.120*tp),(1.690*tp,1.120*tp),(1.690*tp,0.900*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.235*tp,5.490*tp),(3.235*tp,5.710*tp),(3.375*tp,5.710*tp),(3.375*tp,5.630*tp),(3.645*tp,5.630*tp),(3.645*tp,5.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.600*tp,1.405*tp),(0.600*tp,1.495*tp),(0.755*tp,1.495*tp),(0.755*tp,1.645*tp),(1.120*tp,1.645*tp),(1.120*tp,1.495*tp),(1.335*tp,1.495*tp),(1.335*tp,1.405*tp),(1.030*tp,1.405*tp),(1.030*tp,1.555*tp),(0.845*tp,1.555*tp),(0.845*tp,1.405*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.850*tp,4.310*tp),(3.850*tp,4.450*tp),(4.130*tp,4.450*tp),(4.130*tp,4.310*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.865*tp,4.310*tp),(0.865*tp,4.450*tp),(1.145*tp,4.450*tp),(1.145*tp,4.310*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.280*tp,3.4725*tp),(1.280*tp,3.6975*tp),(1.425*tp,3.6975*tp),(1.425*tp,3.4725*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.575*tp,3.4725*tp),(3.575*tp,3.6975*tp),(3.720*tp,3.6975*tp),(3.720*tp,3.4725*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.300*tp,3.770*tp),(4.300*tp,4.150*tp),(4.385*tp,4.150*tp),(4.385*tp,4.315*tp),(4.475*tp,4.315*tp),(4.475*tp,4.060*tp),(4.390*tp,4.060*tp),(4.390*tp,3.770*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.555*tp,2.525*tp),(1.555*tp,3.385*tp),(1.675*tp,3.385*tp),(1.675*tp,2.645*tp),(2.280*tp,2.645*tp),(2.280*tp,2.525*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.720*tp,2.525*tp),(2.720*tp,2.645*tp),(3.330*tp,2.645*tp),(3.330*tp,3.385*tp),(3.450*tp,3.385*tp),(3.450*tp,2.525*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,3.465*tp),(2.430*tp,3.575*tp),(1.670*tp,3.575*tp),(1.670*tp,3.715*tp),(2.570*tp,3.715*tp),(2.570*tp,3.465*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.420*tp,2.020*tp),(2.420*tp,2.365*tp),(2.580*tp,2.365*tp),(2.580*tp,2.020*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.4525*tp,1.720*tp),(2.4525*tp,2.020*tp),(2.5475*tp,2.020*tp),(2.5475*tp,1.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.420*tp,1.9625*tp),(2.420*tp,2.0775*tp),(2.7575*tp,2.0775*tp),(2.7575*tp,2.4125*tp),(3.355*tp,2.4125*tp),(3.355*tp,2.2975*tp),(2.8725*tp,2.2975*tp),(2.8725*tp,1.9625*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.4025*tp,1.365*tp),(2.4025*tp,1.510*tp),(2.5975*tp,1.510*tp),(2.5975*tp,1.365*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.600*tp,5.445*tp),(0.600*tp,5.535*tp),(0.680*tp,5.535*tp),(0.680*tp,5.710*tp),(0.940*tp,5.710*tp),(0.940*tp,5.605*tp),(1.020*tp,5.605*tp),(1.020*tp,5.710*tp),(1.270*tp,5.710*tp),(1.270*tp,5.605*tp),(1.400*tp,5.605*tp),(1.400*tp,5.515*tp),(1.180*tp,5.515*tp),(1.180*tp,5.620*tp),(1.110*tp,5.620*tp),(1.110*tp,5.515*tp),(0.850*tp,5.515*tp),(0.850*tp,5.620*tp),(0.770*tp,5.620*tp),(0.770*tp,5.445*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.690*tp,0.580*tp),(1.690*tp,0.680*tp),(2.260*tp,0.680*tp),(2.260*tp,0.580*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,1.660*tp),(0.420*tp,2.280*tp),(0.580*tp,2.280*tp),(0.580*tp,1.660*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,0.230*tp),(0.430*tp,0.710*tp),(0.570*tp,0.710*tp),(0.570*tp,0.230*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.0675*tp,0.595*tp),(1.0675*tp,0.695*tp),(1.285*tp,0.695*tp),(1.285*tp,1.450*tp),(1.385*tp,1.450*tp),(1.385*tp,0.595*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.7425*tp,1.2825*tp),(2.7425*tp,1.6325*tp),(2.660*tp,1.6325*tp),(2.660*tp,1.7175*tp),(2.8275*tp,1.7175*tp),(2.8275*tp,1.3675*tp),(2.9025*tp,1.3675*tp),(2.9025*tp,1.7175*tp),(3.1425*tp,1.7175*tp),(3.1425*tp,1.4775*tp),(3.2125*tp,1.4775*tp),(3.2125*tp,1.6675*tp),(3.390*tp,1.6675*tp),(3.390*tp,1.5825*tp),(3.2975*tp,1.5825*tp),(3.2975*tp,1.3925*tp),(3.0575*tp,1.3925*tp),(3.0575*tp,1.6325*tp),(2.9875*tp,1.6325*tp),(2.9875*tp,1.2825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.610*tp,3.770*tp),(0.610*tp,4.060*tp),(0.525*tp,4.060*tp),(0.525*tp,4.315*tp),(0.615*tp,4.315*tp),(0.615*tp,4.150*tp),(0.700*tp,4.150*tp),(0.700*tp,3.770*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.230*tp,5.440*tp),(4.230*tp,5.620*tp),(4.150*tp,5.620*tp),(4.150*tp,5.515*tp),(3.890*tp,5.515*tp),(3.890*tp,5.620*tp),(3.820*tp,5.620*tp),(3.820*tp,5.515*tp),(3.600*tp,5.515*tp),(3.600*tp,5.605*tp),(3.730*tp,5.605*tp),(3.730*tp,5.710*tp),(3.980*tp,5.710*tp),(3.980*tp,5.605*tp),(4.060*tp,5.605*tp),(4.060*tp,5.710*tp),(4.320*tp,5.710*tp),(4.320*tp,5.530*tp),(4.400*tp,5.530*tp),(4.400*tp,5.440*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.590*tp,4.530*tp),(0.590*tp,4.745*tp),(0.295*tp,4.745*tp),(0.295*tp,5.025*tp),(0.605*tp,5.025*tp),(0.605*tp,5.145*tp),(0.395*tp,5.145*tp),(0.395*tp,5.350*tp),(0.485*tp,5.350*tp),(0.485*tp,5.235*tp),(0.695*tp,5.235*tp),(0.695*tp,4.935*tp),(0.385*tp,4.935*tp),(0.385*tp,4.835*tp),(0.680*tp,4.835*tp),(0.680*tp,4.530*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.320*tp,4.530*tp),(4.320*tp,4.835*tp),(4.615*tp,4.835*tp),(4.615*tp,4.935*tp),(4.305*tp,4.935*tp),(4.305*tp,5.235*tp),(4.515*tp,5.235*tp),(4.515*tp,5.350*tp),(4.605*tp,5.350*tp),(4.605*tp,5.145*tp),(4.395*tp,5.145*tp),(4.395*tp,5.025*tp),(4.705*tp,5.025*tp),(4.705*tp,4.745*tp),(4.410*tp,4.745*tp),(4.410*tp,4.530*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.400*tp,0.000*tp),(4.400*tp,0.400*tp),(4.600*tp,0.400*tp),(4.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.400*tp,6.400*tp),(2.400*tp,7.000*tp),(2.600*tp,7.000*tp),(2.600*tp,6.400*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.545*tp,3.635*tp),(0.545*tp,3.890*tp),(0.715*tp,3.890*tp),(0.715*tp,3.635*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.285*tp,3.635*tp),(4.285*tp,3.890*tp),(4.455*tp,3.890*tp),(4.455*tp,3.635*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.600*tp,2.515*tp),(2.600*tp,2.655*tp),(2.875*tp,2.655*tp),(2.875*tp,2.515*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.125*tp,2.515*tp),(2.125*tp,2.655*tp),(2.400*tp,2.655*tp),(2.400*tp,2.515*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.105*tp,0.570*tp),(2.105*tp,0.690*tp),(2.420*tp,0.690*tp),(2.420*tp,0.570*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,0.000*tp),(0.400*tp,0.400*tp),(0.600*tp,0.400*tp),(0.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,4.540*tp),(1.300*tp,5.365*tp),(1.700*tp,5.365*tp),(1.700*tp,4.540*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.300*tp,4.540*tp),(3.300*tp,5.365*tp),(3.700*tp,5.365*tp),(3.700*tp,4.540*tp)])
        return elems        

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=0.830*tp,center=(0.500*tp,4.950*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(0.420*tp,2.145*tp),(0.420*tp,2.155*tp),(0.580*tp,2.155*tp),(0.580*tp,2.145*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.845*tp,6.420*tp),(0.845*tp,6.580*tp),(0.855*tp,6.580*tp),(0.855*tp,6.420*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(4.145*tp,6.420*tp),(4.145*tp,6.580*tp),(4.155*tp,6.580*tp),(4.155*tp,6.420*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.105*tp,0.620*tp),(1.105*tp,0.670*tp),(1.160*tp,0.670*tp),(1.160*tp,0.620*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(4.330*tp,1.600*tp),(4.330*tp,1.650*tp),(4.380*tp,1.650*tp),(4.380*tp,1.600*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.475*tp,1.240*tp),(3.475*tp,1.290*tp),(3.530*tp,1.290*tp),(3.530*tp,1.240*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.265*tp,2.330*tp),(3.265*tp,2.380*tp),(3.320*tp,2.380*tp),(3.320*tp,2.330*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.475*tp,3.500*tp),(2.475*tp,3.555*tp),(2.530*tp,3.555*tp),(2.530*tp,3.500*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.045*tp,4.350*tp),(1.045*tp,4.405*tp),(1.100*tp,4.405*tp),(1.100*tp,4.350*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.900*tp,4.355*tp),(3.900*tp,4.405*tp),(3.955*tp,4.405*tp),(3.955*tp,4.355*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.280*tp,5.620*tp),(3.280*tp,5.670*tp),(3.340*tp,5.670*tp),(3.340*tp,5.620*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.670*tp,5.620*tp),(1.670*tp,5.670*tp),(1.725*tp,5.670*tp),(1.725*tp,5.620*tp)])
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(1.720*tp,3.720*tp),(1.720*tp,3.960*tp),(1.875*tp,3.960*tp),(1.875*tp,3.875*tp),(1.960*tp,3.875*tp),(1.960*tp,3.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.040*tp,3.720*tp),(2.040*tp,3.875*tp),(2.125*tp,3.875*tp),(2.125*tp,3.960*tp),(2.280*tp,3.960*tp),(2.280*tp,3.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.125*tp,3.040*tp),(2.125*tp,3.125*tp),(2.040*tp,3.125*tp),(2.040*tp,3.280*tp),(2.280*tp,3.280*tp),(2.280*tp,3.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.720*tp,3.040*tp),(1.720*tp,3.280*tp),(1.960*tp,3.280*tp),(1.960*tp,3.125*tp),(1.875*tp,3.125*tp),(1.875*tp,3.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.720*tp,1.040*tp),(2.720*tp,1.280*tp),(2.960*tp,1.280*tp),(2.960*tp,1.125*tp),(2.875*tp,1.125*tp),(2.875*tp,1.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.720*tp,0.720*tp),(2.720*tp,0.960*tp),(2.875*tp,0.960*tp),(2.875*tp,0.875*tp),(2.960*tp,0.875*tp),(2.960*tp,0.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.025*tp,2.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,4.74*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,5.165*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.485*tp,3.045*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,4.74*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.165*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.93*tp,3.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.97*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.79*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.565*tp,2.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.96*tp,0.300*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.635*tp,2.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.385*tp,3.24*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.13*tp,2.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.335*tp,2.93*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.48*tp,2.095*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.44*tp,2.835*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.255*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.255*tp,0.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.88*tp,3.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.44*tp,1.785*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.700*tp,3.86*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.88*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.88*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.27*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.44*tp,5.835*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.700*tp,5.835*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.700*tp,2.835*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.44*tp,3.86*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.87*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.88*tp,1.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,3.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.125*tp,0.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.000*tp,2.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.16*tp,0.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.165*tp,1.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.165*tp,0.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.165*tp,5.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.665*tp,0.26*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.665*tp,6.88*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.165*tp,5.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.155*tp,5.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.165*tp,3.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.165*tp,4.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.665*tp,6.88*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.165*tp,4.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.165*tp,5.445*tp),transformation=ls.r180)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.125*tp,2.500*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.705*tp,2.500*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.415*tp,6.415*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(4.415*tp,0.215*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(4.455*tp,3.72*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.275*tp,0.715*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.715*tp,3.89*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.415*tp,0.385*tp),transformation=ls.r270)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_268(),midpoint=(2.655*tp,5.645*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_268(),midpoint=(1.64*tp,5.645*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_254(),midpoint=(0.445*tp,0.645*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_225(),midpoint=(2.500*tp,3.475*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(4.355*tp,1.68*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_129(),midpoint=(2.67*tp,4.38*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_129(),midpoint=(1.015*tp,4.38*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_115(),midpoint=(4.69*tp,2.355*tp),transformation=ls.r90)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_254_sg(),midpoint=(1.55*tp,3.505*tp))
        elems += spira.SRef(jj.jj_254_sg(),midpoint=(3.45*tp,3.500*tp))
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.500*tp,1.565*tp))
        elems += spira.SRef(jj.jj_215_sg(),midpoint=(0.755*tp,4.43*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_215_sg(),midpoint=(4.245*tp,4.43*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_173_s(),midpoint=(1.175*tp,3.585*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_173_s(),midpoint=(3.825*tp,3.585*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(3.735*tp,6.49*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(1.59*tp,0.800*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.500*tp,1.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(1.265*tp,6.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_157_sg(),midpoint=(2.56*tp,1.615*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_145_sg(),midpoint=(0.500*tp,5.44*tp))
        elems += spira.SRef(jj.jj_145_sg(),midpoint=(4.500*tp,5.44*tp))
        elems += spira.SRef(jj.jj_108_s(),midpoint=(2.500*tp,1.275*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_074_s(),midpoint=(2.500*tp,2.445*tp))
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(3.500*tp,1.32*tp),transformation=ls.r180,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 5):
                if ((x == 0 and y in [2,6]) or (x == 3 and y == 0) or (x == 4 and y == 6)):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,7.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(5.000*tp,7.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(4.000*tp,1.000*tp),transformation=ls.r180)
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