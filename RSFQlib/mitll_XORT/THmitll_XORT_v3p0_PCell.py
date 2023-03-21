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
    __name_prefix__ = "THmitll_XORT_v3p0"
    def create_elements(self, elems):
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
        elems += [M6M5Strips, IXports, jjfill, M4M5M6M7conns,
                  vias, ib, jjs, rs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text='PB1 M6 M4',position=(1.68*tp,5.345*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(3.315*tp,5.35*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(2.505*tp,4.155*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(2.355*tp,1.46*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB5 M6 M4',position=(2.645*tp,1.605*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(0.85*tp,0.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P4 M6 M4',position=(3.500*tp,1.275*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(4.15*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.85*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(1.425*tp,6.48*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.52*tp,5.42*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(0.545*tp,4.565*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(0.925*tp,4.56*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(3.58*tp,6.475*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(4.48*tp,5.42*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(4.455*tp,4.565*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(4.07*tp,4.57*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M6 M5',position=(2.855*tp,2.58*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J11 M6 M5',position=(1.42*tp,0.52*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J12 M6 M5',position=(0.535*tp,1.565*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J14 M6 M5',position=(3.425*tp,1.57*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J13 M5 M6',position=(2.155*tp,2.575*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M5 M6',position=(2.500*tp,2.585*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='a',position=(0.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='b',position=(4.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(3.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='clk',position=(0.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='VDD',position=(2.500*tp,6.965*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(2.500*tp,0.04*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='GND',position=(2.345*tp,6.96*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RIB1',position=(2.055*tp,5.35*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(3.015*tp,5.35*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.495*tp,4.39*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(2.345*tp,1.15*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(2.645*tp,1.14*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(1.695*tp,6.475*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.515*tp,5.685*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(0.545*tp,4.27*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.215*tp,4.565*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(3.28*tp,6.48*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(4.48*tp,5.695*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(4.45*tp,4.27*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(3.77*tp,4.56*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(2.495*tp,2.265*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(3.13*tp,2.575*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB13',position=(1.85*tp,2.565*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB11',position=(1.685*tp,0.53*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB12',position=(0.535*tp,1.27*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB14',position=(3.735*tp,1.575*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(3.500*tp,1.18*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(3.280*tp,0.720*tp),(3.500*tp,0.940*tp),(3.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.720*tp,0.280*tp),(0.720*tp,0.720*tp),(0.940*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.280*tp,6.280*tp),(4.060*tp,6.500*tp),(4.280*tp,6.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.720*tp,6.280*tp),(0.720*tp,6.720*tp),(0.940*tp,6.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.420*tp,0.720*tp),(3.420*tp,1.1375*tp),(3.580*tp,1.1375*tp),(3.580*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.430*tp,1.2075*tp),(3.430*tp,1.455*tp),(3.570*tp,1.455*tp),(3.570*tp,1.2075*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.575*tp,1.530*tp),(2.575*tp,1.670*tp),(3.325*tp,1.670*tp),(3.325*tp,1.530*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.720*tp,0.420*tp),(0.720*tp,0.580*tp),(1.320*tp,0.580*tp),(1.320*tp,0.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,0.330*tp),(2.430*tp,0.645*tp),(2.575*tp,0.645*tp),(2.575*tp,0.770*tp),(2.715*tp,0.770*tp),(2.715*tp,0.505*tp),(2.570*tp,0.505*tp),(2.570*tp,0.330*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.285*tp,0.505*tp),(2.285*tp,0.870*tp),(2.425*tp,0.870*tp),(2.425*tp,0.645*tp),(2.500*tp,0.645*tp),(2.500*tp,0.505*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.420*tp,1.390*tp),(1.420*tp,1.530*tp),(2.420*tp,1.530*tp),(2.420*tp,1.390*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,0.620*tp),(1.430*tp,0.940*tp),(1.360*tp,0.940*tp),(1.360*tp,1.530*tp),(1.480*tp,1.530*tp),(1.480*tp,1.060*tp),(1.550*tp,1.060*tp),(1.550*tp,0.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,1.675*tp),(0.430*tp,2.675*tp),(0.705*tp,2.675*tp),(0.705*tp,2.475*tp),(0.630*tp,2.475*tp),(0.630*tp,1.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.250*tp,2.4675*tp),(2.250*tp,2.6825*tp),(2.400*tp,2.6825*tp),(2.400*tp,2.4675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.600*tp,2.465*tp),(2.600*tp,2.685*tp),(2.755*tp,2.685*tp),(2.755*tp,2.465*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.545*tp,1.680*tp),(3.545*tp,1.795*tp),(3.290*tp,1.795*tp),(3.290*tp,2.105*tp),(3.615*tp,2.105*tp),(3.615*tp,2.290*tp),(2.935*tp,2.290*tp),(2.935*tp,2.470*tp),(3.025*tp,2.470*tp),(3.025*tp,2.380*tp),(3.705*tp,2.380*tp),(3.705*tp,2.015*tp),(3.380*tp,2.015*tp),(3.380*tp,1.885*tp),(3.635*tp,1.885*tp),(3.635*tp,1.680*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.680*tp,6.420*tp),(3.680*tp,6.580*tp),(4.280*tp,6.580*tp),(4.280*tp,6.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.720*tp,6.420*tp),(0.720*tp,6.580*tp),(1.325*tp,6.580*tp),(1.325*tp,6.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,4.530*tp),(2.430*tp,6.570*tp),(2.570*tp,6.570*tp),(2.570*tp,4.530*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.305*tp,5.280*tp),(2.305*tp,5.420*tp),(2.695*tp,5.420*tp),(2.695*tp,5.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,3.095*tp),(2.430*tp,4.225*tp),(2.570*tp,4.225*tp),(2.570*tp,3.095*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.665*tp,4.445*tp),(0.665*tp,4.685*tp),(0.810*tp,4.685*tp),(0.810*tp,4.445*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.185*tp,4.445*tp),(4.185*tp,4.685*tp),(4.330*tp,4.685*tp),(4.330*tp,4.445*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.505*tp,4.675*tp),(0.505*tp,4.775*tp),(0.290*tp,4.775*tp),(0.290*tp,5.040*tp),(0.625*tp,5.040*tp),(0.625*tp,5.125*tp),(0.410*tp,5.125*tp),(0.410*tp,5.325*tp),(0.500*tp,5.325*tp),(0.500*tp,5.215*tp),(0.715*tp,5.215*tp),(0.715*tp,4.950*tp),(0.380*tp,4.950*tp),(0.380*tp,4.865*tp),(0.595*tp,4.865*tp),(0.595*tp,4.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.485*tp,4.680*tp),(4.485*tp,4.780*tp),(4.305*tp,4.780*tp),(4.305*tp,5.045*tp),(4.625*tp,5.045*tp),(4.625*tp,5.130*tp),(4.385*tp,5.130*tp),(4.385*tp,5.330*tp),(4.475*tp,5.330*tp),(4.475*tp,5.220*tp),(4.715*tp,5.220*tp),(4.715*tp,4.955*tp),(4.395*tp,4.955*tp),(4.395*tp,4.870*tp),(4.575*tp,4.870*tp),(4.575*tp,4.680*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.250*tp,5.285*tp),(3.250*tp,5.670*tp),(3.450*tp,5.670*tp),(3.450*tp,5.530*tp),(3.390*tp,5.530*tp),(3.390*tp,5.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.645*tp,1.360*tp),(0.645*tp,1.450*tp),(0.785*tp,1.450*tp),(0.785*tp,1.695*tp),(1.110*tp,1.695*tp),(1.110*tp,1.505*tp),(1.420*tp,1.505*tp),(1.420*tp,1.415*tp),(1.020*tp,1.415*tp),(1.020*tp,1.605*tp),(0.875*tp,1.605*tp),(0.875*tp,1.360*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.715*tp,5.320*tp),(0.715*tp,5.555*tp),(0.605*tp,5.555*tp),(0.605*tp,5.645*tp),(0.805*tp,5.645*tp),(0.805*tp,5.410*tp),(0.960*tp,5.410*tp),(0.960*tp,5.700*tp),(1.345*tp,5.700*tp),(1.345*tp,5.645*tp),(1.550*tp,5.645*tp),(1.550*tp,5.555*tp),(1.255*tp,5.555*tp),(1.255*tp,5.610*tp),(1.050*tp,5.610*tp),(1.050*tp,5.320*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.610*tp,5.285*tp),(1.610*tp,5.530*tp),(1.550*tp,5.530*tp),(1.550*tp,5.670*tp),(1.750*tp,5.670*tp),(1.750*tp,5.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.950*tp,5.320*tp),(3.950*tp,5.610*tp),(3.745*tp,5.610*tp),(3.745*tp,5.555*tp),(3.450*tp,5.555*tp),(3.450*tp,5.645*tp),(3.655*tp,5.645*tp),(3.655*tp,5.700*tp),(4.040*tp,5.700*tp),(4.040*tp,5.410*tp),(4.195*tp,5.410*tp),(4.195*tp,5.640*tp),(4.395*tp,5.640*tp),(4.395*tp,5.550*tp),(4.285*tp,5.550*tp),(4.285*tp,5.320*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.405*tp,5.530*tp),(3.405*tp,5.945*tp),(3.555*tp,5.945*tp),(3.555*tp,6.100*tp),(3.370*tp,6.100*tp),(3.370*tp,6.375*tp),(3.460*tp,6.375*tp),(3.460*tp,6.190*tp),(3.645*tp,6.190*tp),(3.645*tp,5.855*tp),(3.495*tp,5.855*tp),(3.495*tp,5.530*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.505*tp,5.530*tp),(1.505*tp,5.855*tp),(1.350*tp,5.855*tp),(1.350*tp,6.190*tp),(1.530*tp,6.190*tp),(1.530*tp,6.375*tp),(1.620*tp,6.375*tp),(1.620*tp,6.100*tp),(1.440*tp,6.100*tp),(1.440*tp,5.945*tp),(1.595*tp,5.945*tp),(1.595*tp,5.530*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.400*tp,6.400*tp),(2.400*tp,7.000*tp),(2.600*tp,7.000*tp),(2.600*tp,6.400*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.400*tp,0.000*tp),(2.400*tp,0.500*tp),(2.600*tp,0.500*tp),(2.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.550*tp,2.450*tp),(0.550*tp,2.700*tp),(2.2725*tp,2.700*tp),(2.2725*tp,2.450*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.375*tp,2.695*tp),(2.375*tp,3.200*tp),(2.625*tp,3.200*tp),(2.625*tp,2.695*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.415*tp,3.110*tp),(2.415*tp,3.200*tp),(2.625*tp,3.200*tp),(2.625*tp,3.380*tp),(2.955*tp,3.380*tp),(2.955*tp,3.425*tp),(3.565*tp,3.425*tp),(3.565*tp,3.525*tp),(3.400*tp,3.525*tp),(3.400*tp,3.805*tp),(3.565*tp,3.805*tp),(3.565*tp,3.905*tp),(3.310*tp,3.905*tp),(3.310*tp,4.185*tp),(3.605*tp,4.185*tp),(3.605*tp,4.285*tp),(3.455*tp,4.285*tp),(3.455*tp,4.480*tp),(3.545*tp,4.480*tp),(3.545*tp,4.375*tp),(3.695*tp,4.375*tp),(3.695*tp,4.095*tp),(3.400*tp,4.095*tp),(3.400*tp,3.995*tp),(3.655*tp,3.995*tp),(3.655*tp,3.715*tp),(3.490*tp,3.715*tp),(3.490*tp,3.615*tp),(3.655*tp,3.615*tp),(3.655*tp,3.335*tp),(3.045*tp,3.335*tp),(3.045*tp,3.290*tp),(2.715*tp,3.290*tp),(2.715*tp,3.110*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.285*tp,3.110*tp),(2.285*tp,3.290*tp),(1.955*tp,3.290*tp),(1.955*tp,3.335*tp),(1.345*tp,3.335*tp),(1.345*tp,3.615*tp),(1.505*tp,3.615*tp),(1.505*tp,3.715*tp),(1.345*tp,3.715*tp),(1.345*tp,3.995*tp),(1.605*tp,3.995*tp),(1.605*tp,4.095*tp),(1.300*tp,4.095*tp),(1.300*tp,4.375*tp),(1.455*tp,4.375*tp),(1.455*tp,4.480*tp),(1.545*tp,4.480*tp),(1.545*tp,4.285*tp),(1.390*tp,4.285*tp),(1.390*tp,4.185*tp),(1.695*tp,4.185*tp),(1.695*tp,3.905*tp),(1.435*tp,3.905*tp),(1.435*tp,3.805*tp),(1.595*tp,3.805*tp),(1.595*tp,3.525*tp),(1.435*tp,3.525*tp),(1.435*tp,3.425*tp),(2.045*tp,3.425*tp),(2.045*tp,3.380*tp),(2.375*tp,3.380*tp),(2.375*tp,3.200*tp),(2.585*tp,3.200*tp),(2.585*tp,3.110*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.300*tp,0.105*tp),(4.300*tp,3.515*tp),(4.700*tp,3.515*tp),(4.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.870*tp,0.300*tp),(3.870*tp,0.700*tp),(4.300*tp,0.700*tp),(4.300*tp,0.300*tp)])
        return elems        

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=3.410*tp,center=(4.500*tp,1.810*tp))
        elems += spira.Box(layer=ls.M5,width=0.430*tp,height=0.400*tp,center=(4.085*tp,0.500*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.160*tp,center=(0.850*tp,0.500*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.160*tp,center=(4.150*tp,6.500*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.160*tp,center=(0.850*tp,6.500*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.055*tp,center=(2.645*tp,1.6025*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(2.355*tp,1.460*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.050*tp,center=(3.500*tp,1.270*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.050*tp,center=(2.500*tp,4.155*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.050*tp,center=(1.6825*tp,5.350*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.050*tp,center=(3.320*tp,5.350*tp))
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,4.965*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,4.985*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,3.32*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.87*tp,4.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.13*tp,4.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.995*tp,3.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.005*tp,3.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,3.315*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,2.885*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,2.455*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,2.025*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,1.595*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,1.165*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,0.735*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,0.305*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.07*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,4.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.34*tp,3.645*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.505*tp,5.300*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.85*tp,0.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.165*tp,5.295*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.33*tp,3.655*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.34*tp,2.85*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.91*tp,5.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.345*tp,2.19*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.345*tp,1.91*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.35*tp,1.635*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.44*tp,2.895*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.875*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.700*tp,2.895*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,2.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.325*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.815*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.875*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.115*tp,0.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.165*tp,3.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.16*tp,3.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.15*tp,2.625*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.66*tp,0.26*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.09*tp,5.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.665*tp,6.875*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.66*tp,6.875*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.300*tp,3.13*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.56*tp,3.12*tp),transformation=ls.r270)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.415*tp,0.315*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.415*tp,3.03*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.585*tp,6.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.72*tp,2.66*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_373(),midpoint=(2.500*tp,4.655*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_245(),midpoint=(2.355*tp,1.515*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_230(),midpoint=(3.375*tp,5.35*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_230(),midpoint=(2.43*tp,5.35*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_175(),midpoint=(2.645*tp,0.65*tp))
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.44*tp,1.57*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_245_sg(),midpoint=(4.455*tp,4.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_245_sg(),midpoint=(0.545*tp,4.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_222_s(),midpoint=(4.07*tp,4.565*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_222_s(),midpoint=(0.93*tp,4.565*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_216_sg(),midpoint=(0.535*tp,1.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(3.575*tp,6.475*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(1.425*tp,6.475*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(1.425*tp,0.525*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_156_s(),midpoint=(2.500*tp,2.575*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_152_sg(),midpoint=(2.855*tp,2.575*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_147_s(),midpoint=(2.15*tp,2.575*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_125_sg(),midpoint=(4.485*tp,5.415*tp))
        elems += spira.SRef(jj.jj_125_sg(),midpoint=(0.515*tp,5.42*tp))
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(3.500*tp,1.02*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 5):
                if ((x == 0 and y in [0,6]) or (x == 3 and y == 0) or (x == 4 and y == 6)):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,7.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(4.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(5.000*tp,7.000*tp),transformation=ls.r180)
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