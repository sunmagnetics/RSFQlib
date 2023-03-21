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
    __name_prefix__ = "THmitll_SFQDC_v3p0"
    def create_elements(self, elems):
        M0M4M7strips = spira.SRef(M0M4M7_strips())
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        vias = spira.SRef(M0M6_connections())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        rs = spira.SRef(resistors())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M4M7strips, M0M5Strips, IXports, jjfill, vias, M4M5M6M7conns, ib, rs, jjs, ind, tblocks]

        # Text Labels
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(3.495*tp,3.495*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(2.515*tp,1.925*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M5 M6',position=(2.165*tp,2.15*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(1.53*tp,2.78*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.505*tp,4.205*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M5 M6',position=(1.13*tp,2.74*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.505*tp,4.21*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.495*tp,4.54*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(1.62*tp,1.89*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(3.83*tp,2.51*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.51*tp,3.55*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M5 M6',position=(1.135*tp,4.185*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PR1 M6 M4',position=(2.675*tp,2.42*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(3.905*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(3.87*tp,6.31*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RIB1',position=(0.505*tp,4.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.495*tp,5.08*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(1.62*tp,1.525*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(3.83*tp,1.43*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.505*tp,3.925*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.16*tp,3.03*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(1.53*tp,3.075*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(2.165*tp,1.83*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(2.515*tp,1.565*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(3.505*tp,3.79*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.505*tp,3.25*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.14*tp,3.85*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='R1',position=(2.84*tp,2.435*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.500*tp),(0.100*tp,3.600*tp),(0.200*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.400*tp),(3.800*tp,3.500*tp),(3.900*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.630*tp,3.410*tp),(0.630*tp,3.590*tp),(0.915*tp,3.590*tp),(0.915*tp,3.410*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.240*tp,2.6425*tp),(1.240*tp,2.9725*tp),(1.400*tp,2.9725*tp),(1.400*tp,2.6425*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.130*tp,5.505*tp),(1.130*tp,5.570*tp),(0.500*tp,5.570*tp),(0.500*tp,5.710*tp),(1.270*tp,5.710*tp),(1.270*tp,5.645*tp),(1.585*tp,5.645*tp),(1.585*tp,5.505*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,5.535*tp),(0.430*tp,6.300*tp),(0.570*tp,6.300*tp),(0.570*tp,5.535*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,4.705*tp),(0.430*tp,5.535*tp),(0.570*tp,5.535*tp),(0.570*tp,4.705*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,3.675*tp),(0.430*tp,4.275*tp),(0.570*tp,4.275*tp),(0.570*tp,3.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,4.305*tp),(1.430*tp,4.570*tp),(1.570*tp,4.570*tp),(1.570*tp,4.305*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.290*tp,3.500*tp),(2.290*tp,4.290*tp),(1.820*tp,4.290*tp),(1.820*tp,4.175*tp),(1.600*tp,4.175*tp),(1.600*tp,4.315*tp),(1.680*tp,4.315*tp),(1.680*tp,4.430*tp),(2.430*tp,4.430*tp),(2.430*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.400*tp),(3.900*tp,3.600*tp),(4.000*tp,3.600*tp),(4.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.085*tp,2.360*tp),(1.085*tp,2.680*tp),(1.175*tp,2.680*tp),(1.175*tp,2.360*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.545*tp,0.570*tp),(1.545*tp,1.235*tp),(1.685*tp,1.235*tp),(1.685*tp,0.710*tp),(2.305*tp,0.710*tp),(2.305*tp,0.570*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.545*tp,1.815*tp),(1.545*tp,2.425*tp),(2.1975*tp,2.425*tp),(2.1975*tp,2.230*tp),(2.0575*tp,2.230*tp),(2.0575*tp,2.285*tp),(1.685*tp,2.285*tp),(1.685*tp,1.815*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.4075*tp,2.015*tp),(2.4075*tp,2.100*tp),(2.255*tp,2.100*tp),(2.255*tp,2.210*tp),(2.5175*tp,2.210*tp),(2.5175*tp,2.015*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.705*tp,0.530*tp),(2.705*tp,0.670*tp),(3.895*tp,0.670*tp),(3.895*tp,0.530*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.4375*tp,2.500*tp),(3.4375*tp,3.400*tp),(3.5625*tp,3.400*tp),(3.5625*tp,2.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.440*tp,2.445*tp),(3.440*tp,2.585*tp),(3.895*tp,2.585*tp),(3.895*tp,2.445*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.800*tp,3.500*tp),(3.800*tp,3.550*tp),(3.610*tp,3.550*tp),(3.610*tp,3.650*tp),(3.900*tp,3.650*tp),(3.900*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.235*tp,3.965*tp),(1.235*tp,4.280*tp),(1.390*tp,4.280*tp),(1.390*tp,3.965*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.410*tp,1.535*tp),(3.410*tp,2.585*tp),(3.590*tp,2.585*tp),(3.590*tp,1.535*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.335*tp),(0.100*tp,3.500*tp),(0.200*tp,3.500*tp),(0.200*tp,3.435*tp),(0.370*tp,3.435*tp),(0.370*tp,3.335*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.745*tp,1.535*tp),(2.745*tp,1.780*tp),(2.595*tp,1.780*tp),(2.595*tp,1.900*tp),(2.865*tp,1.900*tp),(2.865*tp,1.655*tp),(3.590*tp,1.655*tp),(3.590*tp,1.535*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.950*tp,2.360*tp),(2.950*tp,2.680*tp),(3.090*tp,2.680*tp),(3.090*tp,2.360*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.420*tp,2.310*tp),(2.420*tp,2.610*tp),(2.625*tp,2.610*tp),(2.625*tp,2.310*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.135*tp,2.615*tp),(2.135*tp,2.715*tp),(2.365*tp,2.715*tp),(2.365*tp,2.615*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.760*tp,3.380*tp),(0.760*tp,3.680*tp),(1.2225*tp,3.680*tp),(1.2225*tp,3.380*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.295*tp,2.615*tp),(2.295*tp,3.500*tp),(2.435*tp,3.500*tp),(2.435*tp,2.615*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.0675*tp,2.430*tp),(2.0675*tp,2.715*tp),(2.2675*tp,2.715*tp),(2.2675*tp,2.430*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.130*tp,2.375*tp),(1.130*tp,2.485*tp),(2.155*tp,2.485*tp),(2.155*tp,2.375*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.150*tp,2.340*tp),(2.150*tp,2.510*tp),(2.485*tp,2.510*tp),(2.485*tp,2.340*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.015*tp,3.380*tp),(1.015*tp,4.2975*tp),(1.240*tp,4.2975*tp),(1.240*tp,3.380*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.0425*tp,2.200*tp),(2.0425*tp,2.500*tp),(2.2875*tp,2.500*tp),(2.2875*tp,2.200*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.0275*tp,2.595*tp),(1.0275*tp,3.380*tp),(1.2375*tp,3.380*tp),(1.2375*tp,2.595*tp)])

        return elems         
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(1.125*tp,4.040*tp),(1.125*tp,4.125*tp),(1.040*tp,4.125*tp),(1.040*tp,4.280*tp),(1.280*tp,4.280*tp),(1.280*tp,4.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.040*tp,3.720*tp),(1.040*tp,3.875*tp),(1.125*tp,3.875*tp),(1.125*tp,3.960*tp),(1.280*tp,3.960*tp),(1.280*tp,3.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.040*tp,2.720*tp),(1.040*tp,2.875*tp),(1.125*tp,2.875*tp),(1.125*tp,2.960*tp),(1.280*tp,2.960*tp),(1.280*tp,2.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.125*tp,3.040*tp),(1.125*tp,3.125*tp),(1.040*tp,3.125*tp),(1.040*tp,3.280*tp),(1.280*tp,3.280*tp),(1.280*tp,3.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(1.720*tp,4.040*tp),(1.720*tp,4.280*tp),(1.960*tp,4.280*tp),(1.960*tp,4.125*tp),(1.875*tp,4.125*tp),(1.875*tp,4.040*tp)])
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
        shape = spira.Shape(points=[(2.720*tp,1.720*tp),(2.720*tp,1.960*tp),(2.875*tp,1.960*tp),(2.875*tp,1.875*tp),(2.960*tp,1.875*tp),(2.960*tp,1.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(4.000*tp,6.650*tp),(4.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.345*tp,0.500*tp),(2.345*tp,6.500*tp),(2.645*tp,6.500*tp),(2.645*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(3.125*tp,6.000*tp),(3.125*tp,6.040*tp),(3.875*tp,6.040*tp),(3.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,6.000*tp),(0.125*tp,6.040*tp),(0.875*tp,6.040*tp),(0.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.000*tp,5.125*tp),(2.000*tp,5.875*tp),(2.040*tp,5.875*tp),(2.040*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.000*tp,4.125*tp),(2.000*tp,4.875*tp),(2.040*tp,4.875*tp),(2.040*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.000*tp,3.125*tp),(2.000*tp,3.875*tp),(2.040*tp,3.875*tp),(2.040*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.000*tp,2.125*tp),(2.000*tp,2.875*tp),(2.040*tp,2.875*tp),(2.040*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.000*tp,1.125*tp),(2.000*tp,1.875*tp),(2.040*tp,1.875*tp),(2.040*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.000*tp,0.125*tp),(2.000*tp,0.875*tp),(2.040*tp,0.875*tp),(2.040*tp,0.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.960*tp,0.125*tp),(2.960*tp,0.875*tp),(3.000*tp,0.875*tp),(3.000*tp,0.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.960*tp,1.125*tp),(2.960*tp,1.875*tp),(3.000*tp,1.875*tp),(3.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.960*tp,2.125*tp),(2.960*tp,2.875*tp),(3.000*tp,2.875*tp),(3.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.960*tp,3.125*tp),(2.960*tp,3.875*tp),(3.000*tp,3.875*tp),(3.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.960*tp,4.125*tp),(2.960*tp,4.875*tp),(3.000*tp,4.875*tp),(3.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.960*tp,5.125*tp),(2.960*tp,5.875*tp),(3.000*tp,5.875*tp),(3.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.630*tp,1.300*tp),(0.630*tp,1.700*tp),(1.145*tp,1.700*tp),(1.145*tp,1.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,0.110*tp),(0.300*tp,2.230*tp),(0.700*tp,2.230*tp),(0.700*tp,0.110*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.525*tp,0.300*tp),(0.525*tp,0.700*tp),(1.150*tp,0.700*tp),(1.150*tp,0.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.300*tp,4.770*tp),(3.300*tp,6.890*tp),(3.700*tp,6.890*tp),(3.700*tp,4.770*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.660*tp,6.300*tp),(2.660*tp,6.700*tp),(3.335*tp,6.700*tp),(3.335*tp,6.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.300*tp,5.200*tp),(2.300*tp,6.890*tp),(2.700*tp,6.890*tp),(2.700*tp,5.200*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.670*tp,5.300*tp),(2.670*tp,5.700*tp),(3.385*tp,5.700*tp),(3.385*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,6.060*tp),(1.300*tp,6.890*tp),(1.700*tp,6.890*tp),(1.700*tp,6.060*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.995*tp,3.450*tp),(3.995*tp,3.550*tp),(4.005*tp,3.550*tp),(4.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.480*tp,4.180*tp),(0.480*tp,4.230*tp),(0.535*tp,4.230*tp),(0.535*tp,4.180*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.470*tp,4.510*tp),(1.470*tp,4.560*tp),(1.525*tp,4.560*tp),(1.525*tp,4.510*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.595*tp,1.860*tp),(1.595*tp,1.920*tp),(1.655*tp,1.920*tp),(1.655*tp,1.860*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.805*tp,2.485*tp),(3.805*tp,2.535*tp),(3.860*tp,2.535*tp),(3.860*tp,2.485*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.620*tp,2.400*tp),(2.620*tp,2.455*tp),(2.685*tp,2.455*tp),(2.685*tp,2.400*tp)])
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.000*tp,6.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,4.97*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,5.400*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,5.83*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,6.26*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,6.69*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,5.400*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,5.83*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.26*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.69*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.000*tp,4.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.000*tp,6.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.000*tp,5.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.26*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.69*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.95*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,2.03*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.600*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.17*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.74*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.31*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.945*tp,1.500*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r90)

        return elems
        
class M0M6_connections(spira.Cell):
    __name_prefix__ = "M0M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.76*tp,3.415*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.215*tp,2.49*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.445*tp,3.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.315*tp,2.51*tp),transformation=ls.r270)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.26*tp,4.57*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.745*tp,4.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.345*tp,5.78*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.325*tp,4.935*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.94*tp,1.35*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.675*tp,0.115*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.585*tp,1.125*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.24*tp,3.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.700*tp,3.900*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.29*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.29*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.575*tp,2.44*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,2.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.44*tp,1.855*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.485*tp,4.32*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.875*tp,4.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.885*tp,2.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.075*tp,6.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.18*tp,5.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,5.295*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.185*tp,4.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.11*tp,0.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.205*tp,0.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.66*tp,0.96*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.955*tp,3.57*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.11*tp,3.575*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.02*tp,5.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.67*tp,0.265*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.26*tp,2.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.145*tp,1.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.67*tp,1.07*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.29*tp,1.67*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.300*tp,0.755*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.300*tp,1.23*tp),transformation=ls.r270)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_280(),midpoint=(0.505*tp,4.15*tp))
        elems += spira.SRef(bias.ib_220(),midpoint=(1.62*tp,1.945*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_150(),midpoint=(1.500*tp,5.63*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_080(),midpoint=(3.83*tp,2.565*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_325_sg(),midpoint=(0.500*tp,3.55*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_300_sg(),midpoint=(1.53*tp,2.775*tp))
        elems += spira.SRef(jj.jj_200_sg(),midpoint=(3.500*tp,3.51*tp))
        elems += spira.SRef(jj.jj_200_s(),midpoint=(1.135*tp,2.73*tp))
        elems += spira.SRef(jj.jj_175_sg(),midpoint=(1.500*tp,4.200*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_150_sg(),midpoint=(2.515*tp,1.92*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_150_s(),midpoint=(2.165*tp,2.15*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_150_s(),midpoint=(1.135*tp,4.175*tp),transformation=ls.r180)
        return elems
        
class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_5p74(),midpoint=(2.595*tp,2.43*tp),transformation=ls.r270)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 4):
                if ((x == 0 and y == 6) or (x == 2 and y == 0)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif ((x == 1 and y == 6) or (x == 2 and y in range(1, 7)) or (x == 3 and y == 6)):
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