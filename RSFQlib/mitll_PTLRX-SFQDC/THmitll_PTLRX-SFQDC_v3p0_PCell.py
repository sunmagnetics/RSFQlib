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
    __name_prefix__ = "THmitll_PTLRX-SFQDC_v3p0"
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
        elems += spira.Label(text='PB5 M6 M4',position=(3.61*tp,0.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M6 M5',position=(3.500*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M5 M6',position=(1.12*tp,4.205*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(1.48*tp,4.19*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M5 M6',position=(1.115*tp,2.765*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PR1 M6 M4',position=(2.515*tp,2.38*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M5 M6',position=(2.13*tp,2.135*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(3.500*tp,6.15*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(3.500*tp,5.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(1.500*tp,5.255*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(2.500*tp,5.79*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(0.500*tp,5.725*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(0.500*tp,3.57*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(1.900*tp,4.635*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(1.515*tp,2.775*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M6 M5',position=(2.49*tp,2.11*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(1.500*tp,1.595*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(2.500*tp,6.96*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(0.500*tp,6.965*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(1.500*tp,0.04*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='RIB5',position=(2.665*tp,0.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.14*tp,3.88*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(1.475*tp,3.905*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(1.15*tp,3.07*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='R1',position=(2.700*tp,2.39*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(2.145*tp,1.855*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(3.500*tp,5.23*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.505*tp,5.535*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(2.500*tp,6.195*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(0.500*tp,6.000*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(0.500*tp,3.27*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.34*tp,4.63*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(1.51*tp,3.085*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(2.500*tp,1.73*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(3.505*tp,3.795*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(1.500*tp,1.245*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='GND',position=(0.655*tp,6.96*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='q',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(3.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.400*tp),(3.800*tp,3.500*tp),(3.900*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.110*tp,4.375*tp),(2.200*tp,4.465*tp),(2.200*tp,4.375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.500*tp,6.060*tp),(3.280*tp,6.280*tp),(3.720*tp,6.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,0.230*tp),(1.430*tp,0.430*tp),(1.160*tp,0.430*tp),(1.160*tp,0.570*tp),(1.570*tp,0.570*tp),(1.570*tp,0.230*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.690*tp,1.5375*tp),(2.690*tp,1.8725*tp),(2.585*tp,1.8725*tp),(2.585*tp,2.0525*tp),(2.870*tp,2.0525*tp),(2.870*tp,1.7175*tp),(3.290*tp,1.7175*tp),(3.290*tp,2.575*tp),(3.570*tp,2.575*tp),(3.570*tp,2.395*tp),(3.470*tp,2.395*tp),(3.470*tp,1.5375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.540*tp,0.430*tp),(3.540*tp,1.070*tp),(3.570*tp,1.070*tp),(3.570*tp,2.435*tp),(3.500*tp,2.435*tp),(3.500*tp,2.575*tp),(3.710*tp,2.575*tp),(3.710*tp,0.930*tp),(3.680*tp,0.930*tp),(3.680*tp,0.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.400*tp),(3.900*tp,3.600*tp),(4.000*tp,3.600*tp),(4.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.800*tp,3.500*tp),(3.800*tp,3.600*tp),(3.610*tp,3.600*tp),(3.610*tp,3.700*tp),(3.900*tp,3.700*tp),(3.900*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,0.500*tp),(1.430*tp,0.915*tp),(1.570*tp,0.915*tp),(1.570*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.950*tp,5.400*tp),(2.950*tp,5.450*tp),(2.500*tp,5.450*tp),(2.500*tp,5.550*tp),(3.050*tp,5.550*tp),(3.050*tp,5.500*tp),(3.400*tp,5.500*tp),(3.400*tp,5.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.995*tp,5.300*tp),(1.995*tp,5.595*tp),(1.865*tp,5.595*tp),(1.865*tp,5.315*tp),(1.600*tp,5.315*tp),(1.600*tp,5.405*tp),(1.775*tp,5.405*tp),(1.775*tp,5.685*tp),(2.085*tp,5.685*tp),(2.085*tp,5.390*tp),(2.180*tp,5.390*tp),(2.180*tp,5.545*tp),(2.500*tp,5.545*tp),(2.500*tp,5.455*tp),(2.270*tp,5.455*tp),(2.270*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.530*tp,4.485*tp),(0.530*tp,4.715*tp),(1.100*tp,4.715*tp),(1.100*tp,4.485*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.2825*tp,4.615*tp),(1.2825*tp,4.945*tp),(1.440*tp,4.945*tp),(1.440*tp,4.845*tp),(1.3825*tp,4.845*tp),(1.3825*tp,4.615*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.510*tp,3.680*tp),(0.510*tp,4.715*tp),(0.630*tp,4.715*tp),(0.630*tp,3.680*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.615*tp,3.4475*tp),(0.615*tp,3.5525*tp),(0.910*tp,3.5525*tp),(0.910*tp,3.4475*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.285*tp,2.860*tp),(2.285*tp,4.375*tp),(2.485*tp,4.375*tp),(2.485*tp,2.860*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.215*tp,3.9525*tp),(1.215*tp,4.3025*tp),(1.370*tp,4.3025*tp),(1.370*tp,3.9525*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.390*tp,4.175*tp),(1.390*tp,4.375*tp),(1.600*tp,4.375*tp),(1.600*tp,4.175*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.190*tp,4.280*tp),(1.190*tp,4.545*tp),(1.4525*tp,4.545*tp),(1.4525*tp,4.680*tp),(1.970*tp,4.680*tp),(1.970*tp,4.580*tp),(1.5525*tp,4.580*tp),(1.5525*tp,4.445*tp),(1.290*tp,4.445*tp),(1.290*tp,4.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.590*tp,4.285*tp),(1.590*tp,4.375*tp),(2.395*tp,4.375*tp),(2.395*tp,4.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.225*tp,2.645*tp),(1.225*tp,2.985*tp),(1.380*tp,2.985*tp),(1.380*tp,2.645*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.100*tp,4.615*tp),(1.100*tp,4.715*tp),(1.3325*tp,4.715*tp),(1.3325*tp,4.615*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.390*tp,4.845*tp),(1.390*tp,5.145*tp),(1.590*tp,5.145*tp),(1.590*tp,4.845*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.280*tp,4.300*tp),(1.280*tp,4.305*tp),(1.360*tp,4.305*tp),(1.360*tp,4.300*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.200*tp,4.285*tp),(2.200*tp,4.465*tp),(2.485*tp,4.465*tp),(2.485*tp,4.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,1.525*tp),(1.430*tp,2.425*tp),(2.1575*tp,2.425*tp),(2.1575*tp,2.200*tp),(2.0175*tp,2.200*tp),(2.0175*tp,2.285*tp),(1.570*tp,2.285*tp),(1.570*tp,1.525*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.275*tp,2.315*tp),(2.275*tp,2.515*tp),(2.580*tp,2.515*tp),(2.580*tp,2.315*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.815*tp,2.310*tp),(2.815*tp,2.575*tp),(2.955*tp,2.575*tp),(2.955*tp,2.310*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.065*tp,2.365*tp),(1.065*tp,2.645*tp),(1.165*tp,2.645*tp),(1.165*tp,2.365*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.4075*tp,2.565*tp),(3.4075*tp,3.390*tp),(3.5925*tp,3.390*tp),(3.5925*tp,2.565*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.235*tp,2.0275*tp),(2.235*tp,2.1325*tp),(2.395*tp,2.1325*tp),(2.395*tp,2.0275*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.420*tp,5.600*tp),(3.420*tp,6.280*tp),(3.580*tp,6.280*tp),(3.580*tp,5.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,5.500*tp),(2.430*tp,5.855*tp),(2.570*tp,5.855*tp),(2.570*tp,5.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.295*tp,3.500*tp),(0.295*tp,5.030*tp),(0.430*tp,5.030*tp),(0.430*tp,5.790*tp),(0.570*tp,5.790*tp),(0.570*tp,4.890*tp),(0.435*tp,4.890*tp),(0.435*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,6.210*tp),(0.430*tp,6.570*tp),(0.570*tp,6.570*tp),(0.570*tp,6.210*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,4.560*tp),(2.430*tp,5.070*tp),(2.570*tp,5.070*tp),(2.570*tp,4.700*tp),(2.905*tp,4.700*tp),(2.905*tp,4.560*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,6.415*tp),(2.430*tp,6.770*tp),(2.570*tp,6.770*tp),(2.570*tp,6.415*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.400*tp,0.000*tp),(1.400*tp,0.400*tp),(1.600*tp,0.400*tp),(1.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.125*tp,2.625*tp),(2.125*tp,2.715*tp),(2.3275*tp,2.715*tp),(2.3275*tp,2.625*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.030*tp,2.380*tp),(1.030*tp,2.490*tp),(2.125*tp,2.490*tp),(2.125*tp,2.380*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.755*tp,3.290*tp),(0.755*tp,3.710*tp),(1.250*tp,3.710*tp),(1.250*tp,3.290*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.285*tp,2.625*tp),(2.285*tp,3.015*tp),(2.485*tp,3.015*tp),(2.485*tp,2.625*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.015*tp,2.435*tp),(2.015*tp,2.715*tp),(2.235*tp,2.715*tp),(2.235*tp,2.435*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.125*tp,2.345*tp),(2.125*tp,2.515*tp),(2.430*tp,2.515*tp),(2.430*tp,2.345*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,6.400*tp),(0.400*tp,7.000*tp),(0.600*tp,7.000*tp),(0.600*tp,6.400*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.400*tp,6.600*tp),(2.400*tp,7.000*tp),(2.600*tp,7.000*tp),(2.600*tp,6.600*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.400*tp,4.900*tp),(2.400*tp,6.600*tp),(2.600*tp,6.600*tp),(2.600*tp,4.900*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.9875*tp,2.620*tp),(0.9875*tp,3.500*tp),(1.250*tp,3.500*tp),(1.250*tp,2.620*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.180*tp,6.495*tp),(1.180*tp,6.700*tp),(1.355*tp,6.700*tp),(1.355*tp,6.495*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,0.105*tp),(0.300*tp,2.225*tp),(0.700*tp,2.225*tp),(0.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.965*tp,3.500*tp),(0.965*tp,4.300*tp),(1.240*tp,4.300*tp),(1.240*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.0025*tp,2.200*tp),(2.0025*tp,2.515*tp),(2.2575*tp,2.515*tp),(2.2575*tp,2.200*tp)])
        return elems        

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=2.120*tp,center=(0.500*tp,1.165*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.110*tp,center=(4.000*tp,3.500*tp),alias='Q')
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(3.500*tp,6.150*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(2.500*tp,5.790*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.055*tp,center=(0.4975*tp,5.7225*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(1.905*tp,4.630*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(1.500*tp,1.595*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(2.510*tp,2.380*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(3.610*tp,0.500*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(1.125*tp,3.040*tp),(1.125*tp,3.125*tp),(1.040*tp,3.125*tp),(1.040*tp,3.280*tp),(1.280*tp,3.280*tp),(1.280*tp,3.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.125*tp,4.040*tp),(1.125*tp,4.125*tp),(1.040*tp,4.125*tp),(1.040*tp,4.280*tp),(1.280*tp,4.280*tp),(1.280*tp,4.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.040*tp,2.720*tp),(1.040*tp,2.875*tp),(1.125*tp,2.875*tp),(1.125*tp,2.960*tp),(1.280*tp,2.960*tp),(1.280*tp,2.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(1.040*tp,3.720*tp),(1.040*tp,3.875*tp),(1.125*tp,3.875*tp),(1.125*tp,3.960*tp),(1.280*tp,3.960*tp),(1.280*tp,3.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.040*tp,1.720*tp),(2.040*tp,1.875*tp),(2.125*tp,1.875*tp),(2.125*tp,1.960*tp),(2.280*tp,1.960*tp),(2.280*tp,1.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.720*tp,1.720*tp),(2.720*tp,1.960*tp),(2.875*tp,1.960*tp),(2.875*tp,1.875*tp),(2.960*tp,1.875*tp),(2.960*tp,1.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.125*tp,2.040*tp),(2.125*tp,2.125*tp),(2.040*tp,2.125*tp),(2.040*tp,2.280*tp),(2.280*tp,2.280*tp),(2.280*tp,2.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.720*tp,1.720*tp),(2.720*tp,1.960*tp),(2.875*tp,1.960*tp),(2.875*tp,1.875*tp),(2.960*tp,1.875*tp),(2.960*tp,1.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.08*tp,6.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.695*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,2.025*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.595*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.165*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.735*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.305*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.700*tp,2.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.445*tp,1.095*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.18*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.44*tp,0.66*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.235*tp,3.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.945*tp,3.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.86*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.52*tp,4.32*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.86*tp,6.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.135*tp,6.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.88*tp,5.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.565*tp,6.06*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.96*tp,6.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.255*tp,6.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.88*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.97*tp,0.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.96*tp,1.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.285*tp,1.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.165*tp,3.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,2.38*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.555*tp,2.400*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.855*tp,3.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,6.35*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.18*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.865*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,5.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.845*tp,2.35*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.66*tp,0.27*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.89*tp,4.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.675*tp,0.27*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.665*tp,0.84*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.67*tp,1.165*tp),transformation=ls.r180)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.585*tp,4.915*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.925*tp,3.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.200*tp,2.51*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.47*tp,3.015*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.585*tp,0.385*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.585*tp,6.785*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.585*tp,6.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.26*tp,2.515*tp),transformation=ls.r270)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_064(),midpoint=(3.665*tp,0.500*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_167(),midpoint=(2.895*tp,4.63*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_212(),midpoint=(1.500*tp,1.65*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_229(),midpoint=(2.500*tp,6.54*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_292(),midpoint=(0.500*tp,6.33*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_122_sg(),midpoint=(2.49*tp,2.100*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_134_s(),midpoint=(1.12*tp,4.18*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(3.500*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_162_sg(),midpoint=(1.500*tp,5.25*tp))
        elems += spira.SRef(jj.jj_165_s(),midpoint=(2.13*tp,2.135*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_182_s(),midpoint=(1.12*tp,2.76*tp))
        elems += spira.SRef(jj.jj_198_sg(),midpoint=(1.48*tp,4.185*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_218_sg(),midpoint=(3.500*tp,3.500*tp))
        elems += spira.SRef(jj.jj_276_sg(),midpoint=(0.500*tp,3.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_315_sg(),midpoint=(1.51*tp,2.775*tp))
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_5p74(),midpoint=(2.455*tp,2.38*tp),transformation=ls.r270,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 4):
                if (x == 3 and y == 6):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(3.000*tp,6.000*tp),alias='A')
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