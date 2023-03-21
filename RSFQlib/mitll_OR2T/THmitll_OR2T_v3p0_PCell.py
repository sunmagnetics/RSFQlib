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
    __name_prefix__ = "THmitll_OR2T_v3p0"
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
        elems += spira.Label(text='PB6 M6 M4',position=(2.35*tp,2.765*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.500*tp,6.15*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(3.500*tp,6.15*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(0.500*tp,0.85*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P4 M6 M4',position=(3.500*tp,1.25*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.39*tp,5.53*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(1.725*tp,5.405*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(1.53*tp,4.055*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(0.385*tp,1.48*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(1.73*tp,1.61*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(1.53*tp,2.600*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(1.52*tp,2.945*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M6 M5',position=(2.52*tp,3.225*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J14 M6 M5',position=(3.25*tp,2.58*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M5 M6',position=(2.555*tp,3.59*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J13 M5 M6',position=(3.415*tp,2.94*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J11 M6 M5',position=(3.565*tp,5.58*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J12 M6 M5',position=(3.575*tp,4.395*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J15 M6 M5',position=(3.26*tp,1.55*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(1.78*tp,0.65*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(1.405*tp,0.43*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(1.405*tp,6.58*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.78*tp,6.35*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB5 M6 M4',position=(2.345*tp,4.28*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB7 M6 M4',position=(3.200*tp,4.65*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB8 M6 M4',position=(2.985*tp,1.355*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.53*tp,4.41*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(2.500*tp,6.965*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(2.500*tp,0.05*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='GND',position=(2.35*tp,6.95*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RIB6',position=(2.35*tp,2.300*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(3.500*tp,1.15*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.385*tp,5.25*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.995*tp,5.400*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.200*tp,4.05*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(0.385*tp,1.75*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(1.99*tp,1.605*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(1.255*tp,2.600*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(1.175*tp,2.95*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(2.86*tp,3.58*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(2.800*tp,3.225*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB11',position=(3.285*tp,5.575*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB12',position=(3.29*tp,4.385*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB13',position=(3.415*tp,3.27*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB14',position=(3.525*tp,2.575*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB15',position=(3.555*tp,1.55*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB8',position=(2.76*tp,1.345*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.085*tp,0.425*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(2.24*tp,0.64*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(2.33*tp,4.64*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB7',position=(2.845*tp,4.635*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(2.255*tp,6.35*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(1.925*tp,6.57*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.255*tp,4.400*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='a',position=(0.505*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='clk',position=(3.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='b',position=(0.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(3.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems

class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,6.060*tp),(0.280*tp,6.280*tp),(0.720*tp,6.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.280*tp,0.720*tp),(3.500*tp,0.940*tp),(3.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.500*tp,6.060*tp),(3.280*tp,6.280*tp),(3.720*tp,6.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.280*tp,0.720*tp),(0.500*tp,0.940*tp),(0.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.320*tp,5.250*tp),(1.320*tp,5.610*tp),(1.250*tp,5.610*tp),(1.250*tp,5.285*tp),(1.020*tp,5.285*tp),(1.020*tp,5.465*tp),(0.950*tp,5.465*tp),(0.950*tp,5.285*tp),(0.720*tp,5.285*tp),(0.720*tp,5.385*tp),(0.645*tp,5.385*tp),(0.645*tp,5.2925*tp),(0.485*tp,5.2925*tp),(0.485*tp,5.3725*tp),(0.565*tp,5.3725*tp),(0.565*tp,5.465*tp),(0.800*tp,5.465*tp),(0.800*tp,5.365*tp),(0.870*tp,5.365*tp),(0.870*tp,5.545*tp),(1.100*tp,5.545*tp),(1.100*tp,5.365*tp),(1.170*tp,5.365*tp),(1.170*tp,5.690*tp),(1.400*tp,5.690*tp),(1.400*tp,5.330*tp),(1.470*tp,5.330*tp),(1.470*tp,5.500*tp),(1.650*tp,5.500*tp),(1.650*tp,5.420*tp),(1.550*tp,5.420*tp),(1.550*tp,5.250*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.485*tp,5.535*tp),(0.485*tp,5.635*tp),(0.550*tp,5.635*tp),(0.550*tp,5.715*tp),(0.970*tp,5.715*tp),(0.970*tp,5.870*tp),(1.140*tp,5.870*tp),(1.140*tp,5.950*tp),(1.285*tp,5.950*tp),(1.285*tp,6.380*tp),(1.355*tp,6.380*tp),(1.355*tp,6.635*tp),(1.455*tp,6.635*tp),(1.455*tp,6.280*tp),(1.385*tp,6.280*tp),(1.385*tp,5.850*tp),(1.240*tp,5.850*tp),(1.240*tp,5.770*tp),(1.070*tp,5.770*tp),(1.070*tp,5.615*tp),(0.650*tp,5.615*tp),(0.650*tp,5.535*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.170*tp,1.310*tp),(1.170*tp,1.635*tp),(1.100*tp,1.635*tp),(1.100*tp,1.455*tp),(0.870*tp,1.455*tp),(0.870*tp,1.635*tp),(0.800*tp,1.635*tp),(0.800*tp,1.535*tp),(0.565*tp,1.535*tp),(0.565*tp,1.6275*tp),(0.485*tp,1.6275*tp),(0.485*tp,1.7075*tp),(0.645*tp,1.7075*tp),(0.645*tp,1.615*tp),(0.720*tp,1.615*tp),(0.720*tp,1.715*tp),(0.950*tp,1.715*tp),(0.950*tp,1.535*tp),(1.020*tp,1.535*tp),(1.020*tp,1.715*tp),(1.250*tp,1.715*tp),(1.250*tp,1.390*tp),(1.320*tp,1.390*tp),(1.320*tp,1.750*tp),(1.550*tp,1.750*tp),(1.550*tp,1.580*tp),(1.650*tp,1.580*tp),(1.650*tp,1.500*tp),(1.470*tp,1.500*tp),(1.470*tp,1.670*tp),(1.400*tp,1.670*tp),(1.400*tp,1.310*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.355*tp,0.365*tp),(1.355*tp,0.620*tp),(1.285*tp,0.620*tp),(1.285*tp,1.050*tp),(1.140*tp,1.050*tp),(1.140*tp,1.130*tp),(0.970*tp,1.130*tp),(0.970*tp,1.285*tp),(0.550*tp,1.285*tp),(0.550*tp,1.365*tp),(0.485*tp,1.365*tp),(0.485*tp,1.465*tp),(0.650*tp,1.465*tp),(0.650*tp,1.385*tp),(1.070*tp,1.385*tp),(1.070*tp,1.230*tp),(1.240*tp,1.230*tp),(1.240*tp,1.150*tp),(1.385*tp,1.150*tp),(1.385*tp,0.720*tp),(1.455*tp,0.720*tp),(1.455*tp,0.365*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.625*tp,1.695*tp),(1.625*tp,1.830*tp),(1.300*tp,1.830*tp),(1.300*tp,2.130*tp),(1.615*tp,2.130*tp),(1.615*tp,2.405*tp),(2.065*tp,2.405*tp),(2.065*tp,2.620*tp),(1.830*tp,2.620*tp),(1.830*tp,2.6175*tp),(1.620*tp,2.6175*tp),(1.620*tp,2.7075*tp),(1.740*tp,2.7075*tp),(1.740*tp,2.710*tp),(2.155*tp,2.710*tp),(2.155*tp,2.315*tp),(1.705*tp,2.315*tp),(1.705*tp,2.040*tp),(1.390*tp,2.040*tp),(1.390*tp,1.920*tp),(1.715*tp,1.920*tp),(1.715*tp,1.695*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.2975*tp,2.705*tp),(1.2975*tp,2.855*tp),(1.6275*tp,2.855*tp),(1.6275*tp,2.705*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.420*tp,1.670*tp),(3.420*tp,1.845*tp),(3.585*tp,1.845*tp),(3.585*tp,1.920*tp),(3.300*tp,1.920*tp),(3.300*tp,2.205*tp),(3.615*tp,2.205*tp),(3.615*tp,2.305*tp),(3.400*tp,2.305*tp),(3.400*tp,2.470*tp),(3.490*tp,2.470*tp),(3.490*tp,2.395*tp),(3.705*tp,2.395*tp),(3.705*tp,2.115*tp),(3.390*tp,2.115*tp),(3.390*tp,2.010*tp),(3.675*tp,2.010*tp),(3.675*tp,1.755*tp),(3.510*tp,1.755*tp),(3.510*tp,1.670*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.480*tp,2.285*tp),(2.480*tp,2.530*tp),(2.580*tp,2.530*tp),(2.580*tp,2.610*tp),(2.485*tp,2.610*tp),(2.485*tp,2.870*tp),(2.635*tp,2.870*tp),(2.635*tp,2.945*tp),(2.445*tp,2.945*tp),(2.445*tp,3.130*tp),(2.525*tp,3.130*tp),(2.525*tp,3.025*tp),(2.715*tp,3.025*tp),(2.715*tp,2.790*tp),(2.565*tp,2.790*tp),(2.565*tp,2.690*tp),(2.660*tp,2.690*tp),(2.660*tp,2.450*tp),(2.560*tp,2.450*tp),(2.560*tp,2.365*tp),(2.815*tp,2.365*tp),(2.815*tp,2.715*tp),(3.050*tp,2.715*tp),(3.050*tp,2.365*tp),(3.2475*tp,2.365*tp),(3.2475*tp,2.465*tp),(3.3275*tp,2.465*tp),(3.3275*tp,2.285*tp),(2.970*tp,2.285*tp),(2.970*tp,2.635*tp),(2.895*tp,2.635*tp),(2.895*tp,2.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.585*tp,3.850*tp),(3.585*tp,4.100*tp),(3.485*tp,4.100*tp),(3.485*tp,4.275*tp),(3.575*tp,4.275*tp),(3.575*tp,4.190*tp),(3.675*tp,4.190*tp),(3.675*tp,3.850*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.2825*tp,2.695*tp),(2.2825*tp,3.2025*tp),(2.405*tp,3.2025*tp),(2.405*tp,3.1125*tp),(2.3725*tp,3.1125*tp),(2.3725*tp,2.695*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.665*tp,4.2925*tp),(3.665*tp,4.3775*tp),(3.7975*tp,4.3775*tp),(3.7975*tp,4.6225*tp),(3.6125*tp,4.6225*tp),(3.6125*tp,4.9775*tp),(3.350*tp,4.9775*tp),(3.350*tp,5.0625*tp),(3.6975*tp,5.0625*tp),(3.6975*tp,4.7075*tp),(3.8825*tp,4.7075*tp),(3.8825*tp,4.2925*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.740*tp,4.290*tp),(1.740*tp,4.3875*tp),(1.620*tp,4.3875*tp),(1.620*tp,4.4775*tp),(1.830*tp,4.4775*tp),(1.830*tp,4.380*tp),(2.045*tp,4.380*tp),(2.045*tp,4.595*tp),(1.615*tp,4.595*tp),(1.615*tp,4.870*tp),(1.300*tp,4.870*tp),(1.300*tp,5.170*tp),(1.625*tp,5.170*tp),(1.625*tp,5.305*tp),(1.715*tp,5.305*tp),(1.715*tp,5.080*tp),(1.390*tp,5.080*tp),(1.390*tp,4.960*tp),(1.705*tp,4.960*tp),(1.705*tp,4.685*tp),(2.135*tp,4.685*tp),(2.135*tp,4.290*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.310*tp,5.620*tp),(0.310*tp,6.040*tp),(0.420*tp,6.040*tp),(0.420*tp,6.300*tp),(0.580*tp,6.300*tp),(0.580*tp,5.880*tp),(0.470*tp,5.880*tp),(0.470*tp,5.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.300*tp,4.125*tp),(1.300*tp,4.315*tp),(1.620*tp,4.315*tp),(1.620*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.500*tp,6.505*tp),(2.500*tp,6.645*tp),(2.860*tp,6.645*tp),(2.860*tp,6.505*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.500*tp,6.280*tp),(2.500*tp,6.420*tp),(2.845*tp,6.420*tp),(2.845*tp,6.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.290*tp,5.5775*tp),(2.290*tp,6.420*tp),(2.430*tp,6.420*tp),(2.430*tp,6.870*tp),(2.570*tp,6.870*tp),(2.570*tp,6.280*tp),(2.430*tp,6.280*tp),(2.430*tp,5.7175*tp),(2.460*tp,5.7175*tp),(2.460*tp,5.5775*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.650*tp,5.495*tp),(1.650*tp,5.580*tp),(1.565*tp,5.580*tp),(1.565*tp,6.4175*tp),(1.850*tp,6.4175*tp),(1.850*tp,6.2875*tp),(1.695*tp,6.2875*tp),(1.695*tp,5.710*tp),(1.780*tp,5.710*tp),(1.780*tp,5.495*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.450*tp,5.5775*tp),(2.450*tp,5.7175*tp),(2.715*tp,5.7175*tp),(2.715*tp,5.5775*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.550*tp,3.450*tp),(1.550*tp,3.550*tp),(2.100*tp,3.550*tp),(2.100*tp,3.845*tp),(2.140*tp,3.845*tp),(2.140*tp,4.035*tp),(2.370*tp,4.035*tp),(2.370*tp,3.935*tp),(2.240*tp,3.935*tp),(2.240*tp,3.745*tp),(2.200*tp,3.745*tp),(2.200*tp,3.450*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.575*tp,5.170*tp),(2.575*tp,5.7175*tp),(2.715*tp,5.7175*tp),(2.715*tp,5.170*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.565*tp,0.5825*tp),(1.565*tp,1.4225*tp),(1.650*tp,1.4225*tp),(1.650*tp,1.5075*tp),(1.780*tp,1.5075*tp),(1.780*tp,1.2925*tp),(1.695*tp,1.2925*tp),(1.695*tp,0.7125*tp),(1.850*tp,0.7125*tp),(1.850*tp,0.5825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.420*tp,0.720*tp),(3.420*tp,1.1075*tp),(3.580*tp,1.1075*tp),(3.580*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.420*tp,5.675*tp),(3.420*tp,6.280*tp),(3.580*tp,6.280*tp),(3.580*tp,5.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.285*tp,1.1825*tp),(3.285*tp,1.430*tp),(3.415*tp,1.430*tp),(3.415*tp,1.3125*tp),(3.575*tp,1.3125*tp),(3.575*tp,1.1825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.310*tp,2.690*tp),(3.310*tp,2.845*tp),(3.490*tp,2.845*tp),(3.490*tp,2.690*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.125*tp,4.5825*tp),(3.125*tp,4.7125*tp),(3.285*tp,4.7125*tp),(3.285*tp,5.045*tp),(3.415*tp,5.045*tp),(3.415*tp,4.5825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.305*tp,5.000*tp),(3.305*tp,5.225*tp),(3.605*tp,5.225*tp),(3.605*tp,5.300*tp),(3.340*tp,5.300*tp),(3.340*tp,5.475*tp),(3.430*tp,5.475*tp),(3.430*tp,5.390*tp),(3.695*tp,5.390*tp),(3.695*tp,5.135*tp),(3.395*tp,5.135*tp),(3.395*tp,5.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.915*tp,1.285*tp),(2.915*tp,1.620*tp),(3.150*tp,1.620*tp),(3.150*tp,1.480*tp),(3.055*tp,1.480*tp),(3.055*tp,1.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,0.135*tp),(2.430*tp,0.495*tp),(2.5775*tp,0.495*tp),(2.5775*tp,1.2825*tp),(2.020*tp,1.2825*tp),(2.020*tp,1.4225*tp),(2.7175*tp,1.4225*tp),(2.7175*tp,0.355*tp),(2.570*tp,0.355*tp),(2.570*tp,0.135*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.645*tp,0.355*tp),(2.645*tp,0.495*tp),(2.855*tp,0.495*tp),(2.855*tp,0.355*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.645*tp,0.5775*tp),(2.645*tp,0.7175*tp),(2.850*tp,0.7175*tp),(2.850*tp,0.5775*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.575*tp,1.355*tp),(2.575*tp,1.795*tp),(2.285*tp,1.795*tp),(2.285*tp,1.935*tp),(2.715*tp,1.935*tp),(2.715*tp,1.355*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.440*tp,3.325*tp),(2.440*tp,3.485*tp),(2.720*tp,3.485*tp),(2.720*tp,3.325*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.2825*tp,3.935*tp),(2.2825*tp,4.355*tp),(2.4125*tp,4.355*tp),(2.4125*tp,3.935*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.2825*tp,4.965*tp),(2.2825*tp,5.215*tp),(2.715*tp,5.215*tp),(2.715*tp,5.085*tp),(2.4125*tp,5.085*tp),(2.4125*tp,4.965*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.475*tp,4.580*tp),(2.475*tp,4.720*tp),(2.575*tp,4.720*tp),(2.575*tp,5.150*tp),(2.715*tp,5.150*tp),(2.715*tp,4.580*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,0.720*tp),(0.420*tp,0.980*tp),(0.310*tp,0.980*tp),(0.310*tp,1.400*tp),(0.470*tp,1.400*tp),(0.470*tp,1.140*tp),(0.580*tp,1.140*tp),(0.580*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.8175*tp,3.2825*tp),(1.8175*tp,3.4575*tp),(1.695*tp,3.4575*tp),(1.695*tp,3.5425*tp),(1.9025*tp,3.5425*tp),(1.9025*tp,3.3675*tp),(2.0175*tp,3.3675*tp),(2.0175*tp,3.7175*tp),(2.2975*tp,3.7175*tp),(2.2975*tp,3.5875*tp),(2.430*tp,3.5875*tp),(2.430*tp,3.5025*tp),(2.2125*tp,3.5025*tp),(2.2125*tp,3.6325*tp),(2.1025*tp,3.6325*tp),(2.1025*tp,3.2825*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.335*tp,3.640*tp),(3.335*tp,3.985*tp),(3.675*tp,3.985*tp),(3.675*tp,3.895*tp),(3.425*tp,3.895*tp),(3.425*tp,3.640*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.400*tp,6.715*tp),(2.400*tp,7.000*tp),(2.600*tp,7.000*tp),(2.600*tp,6.715*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.400*tp,0.000*tp),(2.400*tp,0.285*tp),(2.600*tp,0.285*tp),(2.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.2875*tp,3.055*tp),(1.2875*tp,3.945*tp),(1.7125*tp,3.945*tp),(1.7125*tp,3.055*tp)])
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.425*tp,height=0.890*tp,center=(1.500*tp,3.500*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(3.500*tp,6.150*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(0.500*tp,0.850*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(0.500*tp,6.150*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(3.500*tp,1.245*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(1.405*tp,6.575*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.050*tp,center=(1.7825*tp,6.350*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.050*tp,center=(1.405*tp,0.425*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.050*tp,center=(1.780*tp,0.650*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.050*tp,center=(2.345*tp,4.280*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.050*tp,center=(3.2025*tp,4.650*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.055*tp,center=(2.9875*tp,1.3475*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.060*tp,center=(2.3525*tp,2.755*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(1.040*tp,5.720*tp),(1.040*tp,5.875*tp),(1.125*tp,5.875*tp),(1.125*tp,5.960*tp),(1.280*tp,5.960*tp),(1.280*tp,5.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.125*tp,1.040*tp),(1.125*tp,1.125*tp),(1.040*tp,1.125*tp),(1.040*tp,1.280*tp),(1.280*tp,1.280*tp),(1.280*tp,1.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.125*tp,4.040*tp),(1.125*tp,4.125*tp),(1.040*tp,4.125*tp),(1.040*tp,4.280*tp),(1.280*tp,4.280*tp),(1.280*tp,4.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.040*tp,3.720*tp),(2.040*tp,3.875*tp),(2.125*tp,3.875*tp),(2.125*tp,3.960*tp),(2.280*tp,3.960*tp),(2.280*tp,3.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(0.720*tp,4.040*tp),(0.720*tp,4.280*tp),(0.960*tp,4.280*tp),(0.960*tp,4.125*tp),(0.875*tp,4.125*tp),(0.875*tp,4.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(3.125*tp,3.040*tp),(3.125*tp,3.125*tp),(3.040*tp,3.125*tp),(3.040*tp,3.280*tp),(3.280*tp,3.280*tp),(3.280*tp,3.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.720*tp,3.040*tp),(2.720*tp,3.280*tp),(2.960*tp,3.280*tp),(2.960*tp,3.125*tp),(2.875*tp,3.125*tp),(2.875*tp,3.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.040*tp,2.720*tp),(1.040*tp,2.875*tp),(1.125*tp,2.875*tp),(1.125*tp,2.960*tp),(1.280*tp,2.960*tp),(1.280*tp,2.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(0.720*tp,2.720*tp),(0.720*tp,2.960*tp),(0.875*tp,2.960*tp),(0.875*tp,2.875*tp),(0.960*tp,2.875*tp),(0.960*tp,2.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.325*tp,3.500*tp),transformation=ls.r270)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.33*tp,3.905*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.325*tp,2.955*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.38*tp,6.745*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.115*tp,0.35*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.445*tp,0.825*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.71*tp,4.145*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.12*tp,3.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.12*tp,6.32*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.86*tp,3.300*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.695*tp,5.83*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.795*tp,3.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.195*tp,6.600*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.56*tp,2.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.66*tp,2.735*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.58*tp,4.695*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.655*tp,4.41*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.21*tp,0.545*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.715*tp,0.26*tp),transformation=ls.r180)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.4175*tp,3.59*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(3.545*tp,4.005*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.415*tp,6.885*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.415*tp,0.285*tp),transformation=ls.r270)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_112(),midpoint=(1.35*tp,0.425*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_112(),midpoint=(1.35*tp,6.575*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_156(),midpoint=(1.725*tp,0.65*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_156(),midpoint=(1.725*tp,6.35*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_175(),midpoint=(2.035*tp,1.35*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_176(),midpoint=(2.35*tp,1.81*tp))
        elems += spira.SRef(bias.ib_210(),midpoint=(2.345*tp,4.225*tp))
        elems += spira.SRef(bias.ib_242(),midpoint=(2.485*tp,4.65*tp),transformation=ls.r270)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_125_s(),midpoint=(1.525*tp,4.055*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_125_s(),midpoint=(1.525*tp,2.945*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_128_sg(),midpoint=(1.725*tp,1.600*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_128_sg(),midpoint=(1.725*tp,5.400*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_144_s(),midpoint=(3.415*tp,2.94*tp))
        elems += spira.SRef(jj.jj_159_sg(),midpoint=(3.57*tp,4.385*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.385*tp,1.475*tp))
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(3.56*tp,5.575*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.385*tp,5.525*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_165_sg(),midpoint=(1.53*tp,4.405*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_165_sg(),midpoint=(1.53*tp,2.595*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_167_s(),midpoint=(2.55*tp,3.59*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_195_sg(),midpoint=(2.515*tp,3.23*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_209_sg(),midpoint=(3.245*tp,2.58*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.265*tp,1.545*tp),transformation=ls.r270)
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(3.500*tp,0.99*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 4):
                if (x in [0,3] and y in [0,6]):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(4.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(4.000*tp,7.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,7.000*tp),transformation=ls.r180)
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