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
    __name_prefix__ = "THmitll_AND2T_v3p0"
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
        elems += spira.Label(text='PB2 M6 M4',position=(0.645*tp,5.545*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(2.355*tp,1.415*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB6 M6 M4',position=(0.61*tp,2.35*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(3.63*tp,6.535*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(0.500*tp,0.85*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P4 M6 M4',position=(4.500*tp,3.26*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(4.500*tp,1.15*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(1.85*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(2.500*tp,6.495*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(3.44*tp,5.615*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M5 M6',position=(1.48*tp,5.63*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(1.585*tp,5.275*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(2.385*tp,3.685*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(2.000*tp,3.675*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M5 M6',position=(3.595*tp,3.74*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J14 M5 M6',position=(3.59*tp,3.42*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J13 M6 M5',position=(2.000*tp,3.325*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J12 M6 M5',position=(2.38*tp,3.325*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J11 M6 M5',position=(2.68*tp,1.595*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M5 M6',position=(2.75*tp,1.245*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M6 M5',position=(3.62*tp,1.445*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(4.205*tp,0.415*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J15 M6 M5',position=(0.800*tp,1.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J16 M6 M5',position=(0.615*tp,3.44*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J17 M6 M5',position=(4.265*tp,3.575*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB7 M6 M4',position=(4.500*tp,4.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(3.24*tp,0.355*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB5 M6 M4',position=(1.36*tp,1.85*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='RIB1',position=(3.925*tp,6.54*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(4.500*tp,3.16*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(2.505*tp,6.22*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(3.715*tp,5.62*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.805*tp,5.635*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.58*tp,4.975*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(2.385*tp,3.97*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(1.69*tp,3.68*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(3.595*tp,4.12*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB14',position=(3.595*tp,3.045*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB13',position=(1.66*tp,3.335*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB12',position=(2.38*tp,3.02*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB17',position=(4.565*tp,3.575*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB15',position=(0.495*tp,1.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB16',position=(0.605*tp,3.72*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB11',position=(2.94*tp,1.595*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(2.745*tp,0.89*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(3.61*tp,1.73*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(4.49*tp,0.41*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.915*tp,0.355*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(2.355*tp,0.84*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(1.355*tp,1.200*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB6',position=(0.96*tp,2.355*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(0.645*tp,6.135*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB7',position=(4.505*tp,5.01*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='clk',position=(0.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(4.500*tp,2.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='b',position=(4.500*tp,1.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(1.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='GND',position=(0.34*tp,6.96*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='VDD',position=(1.500*tp,0.04*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(0.500*tp,6.965*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(4.500*tp,6.96*tp),layer=spira.Layer(number=50,datatype=0))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.280*tp,0.720*tp),(0.500*tp,0.940*tp),(0.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.720*tp,6.280*tp),(1.720*tp,6.720*tp),(1.940*tp,6.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.280*tp,2.720*tp),(4.500*tp,2.940*tp),(4.720*tp,2.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.500*tp,1.060*tp),(4.280*tp,1.280*tp),(4.720*tp,1.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.590*tp,3.4775*tp),(3.590*tp,3.6725*tp),(4.150*tp,3.6725*tp),(4.150*tp,3.4775*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.625*tp,1.605*tp),(0.625*tp,1.755*tp),(0.285*tp,1.755*tp),(0.285*tp,2.325*tp),(0.110*tp,2.325*tp),(0.110*tp,2.710*tp),(0.395*tp,2.710*tp),(0.395*tp,2.935*tp),(0.285*tp,2.935*tp),(0.285*tp,3.250*tp),(0.335*tp,3.250*tp),(0.335*tp,3.4275*tp),(0.510*tp,3.4275*tp),(0.510*tp,3.3375*tp),(0.425*tp,3.3375*tp),(0.425*tp,3.160*tp),(0.375*tp,3.160*tp),(0.375*tp,3.025*tp),(0.485*tp,3.025*tp),(0.485*tp,2.620*tp),(0.200*tp,2.620*tp),(0.200*tp,2.415*tp),(0.375*tp,2.415*tp),(0.375*tp,1.845*tp),(0.715*tp,1.845*tp),(0.715*tp,1.605*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.600*tp,6.350*tp),(2.600*tp,6.440*tp),(2.905*tp,6.440*tp),(2.905*tp,6.605*tp),(3.410*tp,6.605*tp),(3.410*tp,6.515*tp),(2.995*tp,6.515*tp),(2.995*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.490*tp,3.3025*tp),(2.490*tp,3.4375*tp),(2.860*tp,3.4375*tp),(2.860*tp,3.3025*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.505*tp,0.375*tp),(3.505*tp,0.545*tp),(3.765*tp,0.545*tp),(3.765*tp,0.625*tp),(3.515*tp,0.625*tp),(3.515*tp,0.960*tp),(3.625*tp,0.960*tp),(3.625*tp,1.105*tp),(3.505*tp,1.105*tp),(3.505*tp,1.335*tp),(3.595*tp,1.335*tp),(3.595*tp,1.195*tp),(3.715*tp,1.195*tp),(3.715*tp,0.870*tp),(3.605*tp,0.870*tp),(3.605*tp,0.715*tp),(3.855*tp,0.715*tp),(3.855*tp,0.455*tp),(3.595*tp,0.455*tp),(3.595*tp,0.375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.305*tp,0.910*tp),(3.305*tp,1.4225*tp),(3.515*tp,1.4225*tp),(3.515*tp,1.3225*tp),(3.405*tp,1.3225*tp),(3.405*tp,0.910*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.565*tp,1.695*tp),(2.565*tp,1.875*tp),(2.625*tp,1.875*tp),(2.625*tp,1.955*tp),(2.525*tp,1.955*tp),(2.525*tp,2.295*tp),(2.620*tp,2.295*tp),(2.620*tp,2.485*tp),(2.345*tp,2.485*tp),(2.345*tp,2.285*tp),(1.970*tp,2.285*tp),(1.970*tp,2.545*tp),(2.055*tp,2.545*tp),(2.055*tp,2.625*tp),(1.875*tp,2.625*tp),(1.875*tp,2.285*tp),(1.535*tp,2.285*tp),(1.535*tp,2.685*tp),(1.625*tp,2.685*tp),(1.625*tp,2.855*tp),(1.525*tp,2.855*tp),(1.525*tp,3.105*tp),(1.7825*tp,3.105*tp),(1.7825*tp,3.225*tp),(1.8725*tp,3.225*tp),(1.8725*tp,3.015*tp),(1.615*tp,3.015*tp),(1.615*tp,2.945*tp),(1.715*tp,2.945*tp),(1.715*tp,2.595*tp),(1.625*tp,2.595*tp),(1.625*tp,2.375*tp),(1.785*tp,2.375*tp),(1.785*tp,2.715*tp),(2.145*tp,2.715*tp),(2.145*tp,2.455*tp),(2.060*tp,2.455*tp),(2.060*tp,2.375*tp),(2.255*tp,2.375*tp),(2.255*tp,2.575*tp),(2.710*tp,2.575*tp),(2.710*tp,2.205*tp),(2.615*tp,2.205*tp),(2.615*tp,2.045*tp),(2.715*tp,2.045*tp),(2.715*tp,1.785*tp),(2.655*tp,1.785*tp),(2.655*tp,1.695*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.515*tp,0.285*tp),(3.515*tp,0.375*tp),(3.930*tp,0.375*tp),(3.930*tp,0.680*tp),(4.185*tp,0.680*tp),(4.185*tp,0.500*tp),(4.095*tp,0.500*tp),(4.095*tp,0.590*tp),(4.020*tp,0.590*tp),(4.020*tp,0.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.335*tp,5.725*tp),(3.335*tp,5.890*tp),(3.560*tp,5.890*tp),(3.560*tp,5.965*tp),(3.310*tp,5.965*tp),(3.310*tp,6.215*tp),(3.555*tp,6.215*tp),(3.555*tp,6.295*tp),(3.365*tp,6.295*tp),(3.365*tp,6.550*tp),(3.455*tp,6.550*tp),(3.455*tp,6.385*tp),(3.645*tp,6.385*tp),(3.645*tp,6.125*tp),(3.400*tp,6.125*tp),(3.400*tp,6.055*tp),(3.650*tp,6.055*tp),(3.650*tp,5.800*tp),(3.425*tp,5.800*tp),(3.425*tp,5.725*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.7825*tp,3.780*tp),(1.7825*tp,3.8975*tp),(1.2875*tp,3.8975*tp),(1.2875*tp,4.1725*tp),(1.6275*tp,4.1725*tp),(1.6275*tp,4.4025*tp),(1.3925*tp,4.4025*tp),(1.3925*tp,4.2875*tp),(0.7725*tp,4.2875*tp),(0.7725*tp,4.7075*tp),(1.0275*tp,4.7075*tp),(1.0275*tp,4.5725*tp),(1.1175*tp,4.5725*tp),(1.1175*tp,4.7025*tp),(1.2925*tp,4.7025*tp),(1.2925*tp,5.3775*tp),(1.495*tp,5.3775*tp),(1.495*tp,5.2925*tp),(1.3775*tp,5.2925*tp),(1.3775*tp,4.6175*tp),(1.2025*tp,4.6175*tp),(1.2025*tp,4.4875*tp),(0.9425*tp,4.4875*tp),(0.9425*tp,4.6225*tp),(0.8575*tp,4.6225*tp),(0.8575*tp,4.3725*tp),(1.3075*tp,4.3725*tp),(1.3075*tp,4.4875*tp),(1.7125*tp,4.4875*tp),(1.7125*tp,4.0875*tp),(1.3725*tp,4.0875*tp),(1.3725*tp,3.9825*tp),(1.8675*tp,3.9825*tp),(1.8675*tp,3.780*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.490*tp,3.5825*tp),(2.490*tp,3.6975*tp),(3.155*tp,3.6975*tp),(3.155*tp,3.5825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.710*tp,3.410*tp),(0.710*tp,3.590*tp),(1.180*tp,3.590*tp),(1.180*tp,3.410*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.650*tp,1.345*tp),(2.650*tp,1.495*tp),(2.850*tp,1.495*tp),(2.850*tp,1.345*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,5.470*tp),(0.575*tp,5.675*tp),(0.715*tp,5.675*tp),(0.715*tp,5.470*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.290*tp,1.340*tp),(2.290*tp,1.6175*tp),(2.660*tp,1.6175*tp),(2.660*tp,1.4875*tp),(2.420*tp,1.4875*tp),(2.420*tp,1.340*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.480*tp,5.370*tp),(1.480*tp,5.525*tp),(1.690*tp,5.525*tp),(1.690*tp,5.370*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.410*tp,6.465*tp),(3.410*tp,6.605*tp),(3.690*tp,6.605*tp),(3.690*tp,6.465*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.200*tp,6.430*tp),(4.200*tp,6.605*tp),(4.340*tp,6.605*tp),(4.340*tp,6.570*tp),(4.570*tp,6.570*tp),(4.570*tp,6.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,0.720*tp),(0.420*tp,1.150*tp),(0.580*tp,1.150*tp),(0.580*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,1.080*tp),(0.420*tp,1.220*tp),(0.570*tp,1.220*tp),(0.570*tp,1.410*tp),(0.710*tp,1.410*tp),(0.710*tp,1.080*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.420*tp,2.720*tp),(4.420*tp,3.1225*tp),(4.580*tp,3.1225*tp),(4.580*tp,2.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.305*tp,3.1975*tp),(4.305*tp,3.460*tp),(4.445*tp,3.460*tp),(4.445*tp,3.3375*tp),(4.565*tp,3.3375*tp),(4.565*tp,3.1975*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.495*tp,3.500*tp),(3.495*tp,3.655*tp),(3.685*tp,3.655*tp),(3.685*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.420*tp,0.750*tp),(4.420*tp,1.280*tp),(4.580*tp,1.280*tp),(4.580*tp,0.750*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.290*tp,0.515*tp),(4.290*tp,0.820*tp),(4.580*tp,0.820*tp),(4.580*tp,0.680*tp),(4.430*tp,0.680*tp),(4.430*tp,0.515*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.890*tp,1.430*tp),(0.890*tp,1.570*tp),(1.285*tp,1.570*tp),(1.285*tp,1.915*tp),(1.425*tp,1.915*tp),(1.425*tp,1.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.555*tp,2.280*tp),(0.555*tp,3.345*tp),(0.695*tp,3.345*tp),(0.695*tp,2.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.535*tp,0.360*tp),(1.535*tp,2.070*tp),(1.320*tp,2.070*tp),(1.320*tp,2.420*tp),(1.460*tp,2.420*tp),(1.460*tp,2.210*tp),(1.675*tp,2.210*tp),(1.675*tp,0.360*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.330*tp,3.690*tp),(4.330*tp,4.080*tp),(4.430*tp,4.080*tp),(4.430*tp,4.570*tp),(4.570*tp,4.570*tp),(4.570*tp,3.940*tp),(4.470*tp,3.940*tp),(4.470*tp,3.690*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.430*tp,5.330*tp),(4.430*tp,6.570*tp),(4.570*tp,6.570*tp),(4.570*tp,5.330*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.100*tp,3.570*tp),(2.100*tp,3.780*tp),(2.275*tp,3.780*tp),(2.275*tp,3.570*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.415*tp,5.545*tp),(2.415*tp,5.635*tp),(2.870*tp,5.635*tp),(2.870*tp,5.710*tp),(3.330*tp,5.710*tp),(3.330*tp,5.620*tp),(2.960*tp,5.620*tp),(2.960*tp,5.545*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.100*tp,3.220*tp),(2.100*tp,3.430*tp),(2.275*tp,3.430*tp),(2.275*tp,3.220*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.720*tp,6.420*tp),(1.720*tp,6.580*tp),(2.400*tp,6.580*tp),(2.400*tp,6.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,5.535*tp),(0.575*tp,5.675*tp),(1.380*tp,5.675*tp),(1.380*tp,5.535*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,6.510*tp),(0.575*tp,6.730*tp),(0.430*tp,6.730*tp),(0.430*tp,6.870*tp),(0.715*tp,6.870*tp),(0.715*tp,6.510*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.500*tp,0.290*tp),(1.500*tp,0.430*tp),(2.700*tp,0.430*tp),(2.700*tp,0.290*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,0.130*tp),(1.430*tp,0.395*tp),(1.290*tp,0.395*tp),(1.290*tp,0.535*tp),(1.570*tp,0.535*tp),(1.570*tp,0.130*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.170*tp,0.285*tp),(3.170*tp,0.425*tp),(3.595*tp,0.425*tp),(3.595*tp,0.285*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.705*tp,3.3075*tp),(2.705*tp,3.4325*tp),(3.490*tp,3.4325*tp),(3.490*tp,3.3075*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.175*tp,5.5725*tp),(2.175*tp,5.6775*tp),(2.570*tp,5.6775*tp),(2.570*tp,5.5725*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.025*tp,3.285*tp),(1.025*tp,3.715*tp),(1.6325*tp,3.715*tp),(1.6325*tp,3.285*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.830*tp,0.5475*tp),(2.830*tp,0.7125*tp),(3.2875*tp,0.7125*tp),(3.2875*tp,1.065*tp),(3.4525*tp,1.065*tp),(3.4525*tp,0.5475*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.000*tp,3.595*tp),(3.000*tp,3.715*tp),(3.285*tp,3.715*tp),(3.285*tp,3.7475*tp),(3.485*tp,3.7475*tp),(3.485*tp,3.6275*tp),(3.405*tp,3.6275*tp),(3.405*tp,3.595*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,6.700*tp),(0.400*tp,7.000*tp),(0.600*tp,7.000*tp),(0.600*tp,6.700*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.400*tp,6.400*tp),(4.400*tp,7.000*tp),(4.600*tp,7.000*tp),(4.600*tp,6.400*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.400*tp,0.000*tp),(1.400*tp,0.300*tp),(1.600*tp,0.300*tp),(1.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,4.535*tp),(0.300*tp,5.365*tp),(0.700*tp,5.365*tp),(0.700*tp,4.535*tp)])
        return elems        

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=0.830*tp,center=(0.500*tp,4.950*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(0.500*tp,0.850*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(4.500*tp,1.150*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.160*tp,center=(1.850*tp,6.500*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(4.500*tp,3.260*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.060*tp,center=(4.500*tp,4.505*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.055*tp,center=(3.630*tp,6.5375*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.045*tp,center=(0.6475*tp,5.5425*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(3.240*tp,0.355*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(2.355*tp,1.4125*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(1.360*tp,1.845*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.060*tp,center=(0.615*tp,2.350*tp))
       
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
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,3.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,4.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,5.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,4.96*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.18*tp,4.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.085*tp,4.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.165*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,4.735*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.965*tp,1.500*tp),transformation=ls.r270)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.300*tp,5.275*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.22*tp,4.485*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.85*tp,2.555*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.83*tp,5.305*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.335*tp,5.185*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.07*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.425*tp,2.13*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.88*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.875*tp,5.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.875*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.975*tp,4.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.07*tp,0.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.255*tp,3.385*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.48*tp,5.815*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.445*tp,1.815*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.035*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.66*tp,2.08*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.095*tp,2.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.325*tp,2.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.665*tp,6.885*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.665*tp,6.055*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.94*tp,2.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.66*tp,6.88*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.655*tp,4.97*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.12*tp,0.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.12*tp,2.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.64*tp,4.405*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.435*tp,5.695*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.475*tp,6.53*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.155*tp,5.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.685*tp,4.62*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.305*tp,3.13*tp),transformation=ls.r270)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.705*tp,3.285*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.400*tp,5.53*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(3.000*tp,3.545*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(3.285*tp,0.895*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.195*tp,3.415*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.585*tp,6.885*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.585*tp,0.285*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(4.585*tp,6.585*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_112(),midpoint=(1.355*tp,1.900*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(4.500*tp,5.455*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_249(),midpoint=(3.57*tp,6.535*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_249(),midpoint=(2.545*tp,0.355*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_203(),midpoint=(1.45*tp,2.35*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_148(),midpoint=(0.645*tp,5.485*tp))
        elems += spira.SRef(bias.ib_148(),midpoint=(2.355*tp,0.305*tp))
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_166_sg(),midpoint=(3.615*tp,1.435*tp))
        elems += spira.SRef(jj.jj_166_sg(),midpoint=(3.435*tp,5.615*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_156_sg(),midpoint=(0.615*tp,3.445*tp))
        elems += spira.SRef(jj.jj_144_sg(),midpoint=(1.585*tp,5.28*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_144_sg(),midpoint=(2.67*tp,1.595*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_141_s(),midpoint=(2.01*tp,3.325*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_141_s(),midpoint=(2.01*tp,3.675*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_126_s(),midpoint=(2.75*tp,1.255*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_126_s(),midpoint=(1.47*tp,5.62*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_103_s(),midpoint=(3.59*tp,3.74*tp))
        elems += spira.SRef(jj.jj_103_s(),midpoint=(3.59*tp,3.41*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.795*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(2.500*tp,6.495*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(4.205*tp,0.41*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_179_sg(),midpoint=(2.385*tp,3.685*tp))
        elems += spira.SRef(jj.jj_179_sg(),midpoint=(2.385*tp,3.325*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(4.265*tp,3.575*tp),transformation=ls.r270)
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(4.500*tp,3.005*tp),alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 5):
                if ((x == 0 and y == 0) or (x == 1 and y == 6) or (x == 4 and y in [1,2])):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(5.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(2.000*tp,7.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(5.000*tp,2.000*tp),transformation=ls.r180)
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