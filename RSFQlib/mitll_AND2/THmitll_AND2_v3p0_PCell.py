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
    __name_prefix__ = "THmitll_AND2_v3p0"
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
        elems += spira.Label(text='P3 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='clk',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q',position=(5.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P4 M6 M4',position=(5.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(3.58*tp,5.215*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(2.085*tp,3.975*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M5 M6',position=(3.500*tp,3.675*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J12 M5 M6',position=(3.500*tp,3.33*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J11 M6 M5',position=(2.09*tp,3.015*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M6 M5',position=(2.435*tp,3.005*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(3.475*tp,0.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M6 M5',position=(3.585*tp,1.785*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M5 M6',position=(3.52*tp,1.425*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J13 M6 M5',position=(0.500*tp,3.56*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J14 M6 M5',position=(1.500*tp,3.57*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J15 M6 M5',position=(4.435*tp,3.56*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M5 M6',position=(3.52*tp,5.575*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(2.36*tp,5.200*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(3.06*tp,0.36*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(2.36*tp,1.815*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB5 M6 M4',position=(0.465*tp,4.365*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB6 M6 M4',position=(1.595*tp,3.84*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB7 M6 M4',position=(4.36*tp,3.905*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(3.500*tp,7.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(3.500*tp,7.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(3.48*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(3.055*tp,6.645*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(3.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='b',position=(3.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(2.435*tp,3.995*tp),layer=spira.Layer(number=182,datatype=0))

        
        # LVS Labels
        elems += spira.Label(text='RIB1',position=(2.600*tp,6.645*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(2.365*tp,5.73*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.61*tp,0.365*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(2.355*tp,1.345*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(0.900*tp,4.375*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB6',position=(1.595*tp,4.52*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB7',position=(4.375*tp,4.38*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(3.76*tp,6.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(3.845*tp,5.585*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(3.585*tp,4.92*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(2.425*tp,4.285*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(2.09*tp,4.325*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(3.500*tp,3.99*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(3.755*tp,0.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(3.855*tp,1.425*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(3.58*tp,2.085*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(2.43*tp,2.665*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB11',position=(2.09*tp,2.665*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB12',position=(3.500*tp,2.985*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB13',position=(0.51*tp,3.265*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB14',position=(1.500*tp,3.28*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB15',position=(4.44*tp,3.27*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='clk',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(3.500*tp,7.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='b',position=(3.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(5.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='GND',position=(4.89*tp,6.32*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='VDD',position=(4.89*tp,6.505*tp),layer=spira.Layer(number=1,datatype=0))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(3.400*tp,0.075*tp),(3.485*tp,0.160*tp),(3.485*tp,0.075*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.485*tp,6.840*tp),(3.400*tp,6.925*tp),(3.485*tp,6.925*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.510*tp),(0.100*tp,3.600*tp),(0.190*tp,3.510*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.400*tp,6.925*tp),(3.400*tp,7.000*tp),(3.600*tp,7.000*tp),(3.600*tp,6.925*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.400*tp,0.000*tp),(3.400*tp,0.075*tp),(3.600*tp,0.075*tp),(3.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.900*tp,3.400*tp),(4.900*tp,3.600*tp),(5.000*tp,3.600*tp),(5.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.3975*tp,3.425*tp),(3.3975*tp,3.575*tp),(3.6025*tp,3.575*tp),(3.6025*tp,3.425*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.585*tp,3.3075*tp),(3.585*tp,3.6875*tp),(4.375*tp,3.6875*tp),(4.375*tp,3.3075*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.500*tp,3.400*tp),(4.500*tp,3.600*tp),(4.900*tp,3.600*tp),(4.900*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.465*tp,1.525*tp),(3.465*tp,1.675*tp),(3.695*tp,1.675*tp),(3.695*tp,1.525*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.465*tp,5.325*tp),(3.465*tp,5.475*tp),(3.695*tp,5.475*tp),(3.695*tp,5.325*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.485*tp,0.075*tp),(3.485*tp,0.160*tp),(3.6325*tp,0.160*tp),(3.6325*tp,0.380*tp),(3.7175*tp,0.380*tp),(3.7175*tp,0.075*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.6225*tp,0.625*tp),(3.6225*tp,0.730*tp),(3.300*tp,0.730*tp),(3.300*tp,1.020*tp),(3.390*tp,1.020*tp),(3.390*tp,0.820*tp),(3.7125*tp,0.820*tp),(3.7125*tp,0.625*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.6325*tp,6.620*tp),(3.6325*tp,6.840*tp),(3.485*tp,6.840*tp),(3.485*tp,6.925*tp),(3.7175*tp,6.925*tp),(3.7175*tp,6.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.300*tp,5.985*tp),(3.300*tp,6.275*tp),(3.6225*tp,6.275*tp),(3.6225*tp,6.380*tp),(3.7125*tp,6.380*tp),(3.7125*tp,6.185*tp),(3.390*tp,6.185*tp),(3.390*tp,5.985*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.5025*tp,1.495*tp),(2.5025*tp,1.890*tp),(2.6325*tp,1.890*tp),(2.6325*tp,1.965*tp),(2.2825*tp,1.965*tp),(2.2825*tp,2.225*tp),(2.6325*tp,2.225*tp),(2.6325*tp,2.9775*tp),(2.530*tp,2.9775*tp),(2.530*tp,3.0625*tp),(2.7175*tp,3.0625*tp),(2.7175*tp,2.140*tp),(2.3675*tp,2.140*tp),(2.3675*tp,2.050*tp),(2.7175*tp,2.050*tp),(2.7175*tp,1.805*tp),(2.5875*tp,1.805*tp),(2.5875*tp,1.580*tp),(2.7025*tp,1.580*tp),(2.7025*tp,1.715*tp),(2.9575*tp,1.715*tp),(2.9575*tp,1.580*tp),(3.0425*tp,1.580*tp),(3.0425*tp,1.715*tp),(3.2825*tp,1.715*tp),(3.2825*tp,2.025*tp),(3.500*tp,2.025*tp),(3.500*tp,1.940*tp),(3.3675*tp,1.940*tp),(3.3675*tp,1.630*tp),(3.1275*tp,1.630*tp),(3.1275*tp,1.495*tp),(2.8725*tp,1.495*tp),(2.8725*tp,1.630*tp),(2.7875*tp,1.630*tp),(2.7875*tp,1.495*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.290*tp,6.095*tp),(2.290*tp,6.285*tp),(1.700*tp,6.285*tp),(1.700*tp,6.425*tp),(2.430*tp,6.425*tp),(2.430*tp,6.095*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.090*tp,6.355*tp),(2.090*tp,6.715*tp),(2.230*tp,6.715*tp),(2.230*tp,6.355*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.985*tp,6.470*tp),(2.985*tp,6.715*tp),(3.125*tp,6.715*tp),(3.125*tp,6.610*tp),(3.360*tp,6.610*tp),(3.360*tp,6.470*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.290*tp,1.285*tp),(2.290*tp,1.885*tp),(2.430*tp,1.885*tp),(2.430*tp,1.425*tp),(3.270*tp,1.425*tp),(3.270*tp,1.455*tp),(3.450*tp,1.455*tp),(3.450*tp,1.315*tp),(3.410*tp,1.315*tp),(3.410*tp,1.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.700*tp,0.575*tp),(1.700*tp,0.715*tp),(2.290*tp,0.715*tp),(2.290*tp,0.915*tp),(2.430*tp,0.915*tp),(2.430*tp,0.575*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.090*tp,0.285*tp),(2.090*tp,0.645*tp),(2.230*tp,0.645*tp),(2.230*tp,0.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.985*tp,0.290*tp),(2.985*tp,0.535*tp),(3.360*tp,0.535*tp),(3.360*tp,0.395*tp),(3.125*tp,0.395*tp),(3.125*tp,0.290*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.175*tp,2.805*tp),(2.175*tp,3.115*tp),(2.335*tp,3.115*tp),(2.335*tp,2.805*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.180*tp,3.890*tp),(2.180*tp,4.200*tp),(2.325*tp,4.200*tp),(2.325*tp,3.890*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.600*tp,3.3975*tp),(1.600*tp,3.6025*tp),(2.080*tp,3.6025*tp),(2.080*tp,3.3975*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.530*tp,3.9375*tp),(2.530*tp,4.0225*tp),(2.6325*tp,4.0225*tp),(2.6325*tp,4.7725*tp),(2.2825*tp,4.7725*tp),(2.2825*tp,5.0325*tp),(2.6325*tp,5.0325*tp),(2.6325*tp,5.1075*tp),(2.5025*tp,5.1075*tp),(2.5025*tp,5.5025*tp),(2.7875*tp,5.5025*tp),(2.7875*tp,5.3675*tp),(2.8725*tp,5.3675*tp),(2.8725*tp,5.5025*tp),(3.1275*tp,5.5025*tp),(3.1275*tp,5.3675*tp),(3.3675*tp,5.3675*tp),(3.3675*tp,5.060*tp),(3.500*tp,5.060*tp),(3.500*tp,4.975*tp),(3.2825*tp,4.975*tp),(3.2825*tp,5.2825*tp),(3.0425*tp,5.2825*tp),(3.0425*tp,5.4175*tp),(2.9575*tp,5.4175*tp),(2.9575*tp,5.2825*tp),(2.7025*tp,5.2825*tp),(2.7025*tp,5.4175*tp),(2.5875*tp,5.4175*tp),(2.5875*tp,5.1925*tp),(2.7175*tp,5.1925*tp),(2.7175*tp,4.9475*tp),(2.3675*tp,4.9475*tp),(2.3675*tp,4.8575*tp),(2.7175*tp,4.8575*tp),(2.7175*tp,3.9375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.955*tp,3.455*tp),(0.955*tp,3.535*tp),(0.615*tp,3.535*tp),(0.615*tp,3.625*tp),(1.045*tp,3.625*tp),(1.045*tp,3.545*tp),(1.400*tp,3.545*tp),(1.400*tp,3.455*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.375*tp),(0.100*tp,3.510*tp),(0.190*tp,3.510*tp),(0.190*tp,3.465*tp),(0.385*tp,3.465*tp),(0.385*tp,3.375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.310*tp,3.105*tp),(2.310*tp,3.430*tp),(2.540*tp,3.430*tp),(2.540*tp,3.105*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.310*tp,3.570*tp),(2.310*tp,3.895*tp),(2.540*tp,3.895*tp),(2.540*tp,3.570*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.435*tp,3.670*tp),(1.435*tp,3.910*tp),(1.660*tp,3.910*tp),(1.660*tp,3.770*tp),(1.575*tp,3.770*tp),(1.575*tp,3.670*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.290*tp,4.295*tp),(1.290*tp,5.100*tp),(1.430*tp,5.100*tp),(1.430*tp,4.295*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.360*tp,5.025*tp),(1.360*tp,5.165*tp),(1.660*tp,5.165*tp),(1.660*tp,5.025*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.290*tp,5.095*tp),(1.290*tp,5.385*tp),(1.540*tp,5.385*tp),(1.540*tp,6.295*tp),(1.680*tp,6.295*tp),(1.680*tp,5.245*tp),(1.430*tp,5.245*tp),(1.430*tp,5.095*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.395*tp,3.670*tp),(0.395*tp,4.435*tp),(0.535*tp,4.435*tp),(0.535*tp,3.670*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.290*tp,4.725*tp),(4.290*tp,6.295*tp),(4.430*tp,6.295*tp),(4.430*tp,4.725*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.380*tp,3.680*tp),(4.380*tp,3.835*tp),(4.290*tp,3.835*tp),(4.290*tp,3.975*tp),(4.520*tp,3.975*tp),(4.520*tp,3.680*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.290*tp,5.115*tp),(2.290*tp,5.715*tp),(3.410*tp,5.715*tp),(3.410*tp,5.685*tp),(3.450*tp,5.685*tp),(3.450*tp,5.545*tp),(3.270*tp,5.545*tp),(3.270*tp,5.575*tp),(2.430*tp,5.575*tp),(2.430*tp,5.115*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.330*tp,0.915*tp),(3.330*tp,1.015*tp),(3.6125*tp,1.015*tp),(3.6125*tp,1.310*tp),(3.7125*tp,1.310*tp),(3.7125*tp,0.915*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.985*tp,3.115*tp),(1.985*tp,3.890*tp),(2.185*tp,3.890*tp),(2.185*tp,3.115*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.350*tp,3.2825*tp),(2.350*tp,3.4475*tp),(3.395*tp,3.4475*tp),(3.395*tp,3.2825*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.350*tp,3.5525*tp),(2.350*tp,3.7175*tp),(3.395*tp,3.7175*tp),(3.395*tp,3.5525*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.6125*tp,5.690*tp),(3.6125*tp,5.985*tp),(3.330*tp,5.985*tp),(3.330*tp,6.085*tp),(3.7125*tp,6.085*tp),(3.7125*tp,5.690*tp)])

        return elems             
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(2.125*tp,4.040*tp),(2.125*tp,4.125*tp),(2.040*tp,4.125*tp),(2.040*tp,4.280*tp),(2.280*tp,4.280*tp),(2.280*tp,4.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.125*tp,3.040*tp),(2.125*tp,3.125*tp),(2.040*tp,3.125*tp),(2.040*tp,3.280*tp),(2.280*tp,3.280*tp),(2.280*tp,3.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.040*tp,3.720*tp),(2.040*tp,3.875*tp),(2.125*tp,3.875*tp),(2.125*tp,3.960*tp),(2.280*tp,3.960*tp),(2.280*tp,3.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.040*tp,2.720*tp),(2.040*tp,2.875*tp),(2.125*tp,2.875*tp),(2.125*tp,2.960*tp),(2.280*tp,2.960*tp),(2.280*tp,2.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(5.000*tp,6.650*tp),(5.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.350*tp,0.500*tp),(1.350*tp,6.500*tp),(1.650*tp,6.500*tp),(1.650*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(4.125*tp,6.000*tp),(4.125*tp,6.040*tp),(4.875*tp,6.040*tp),(4.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(3.125*tp,6.000*tp),(3.125*tp,6.040*tp),(3.875*tp,6.040*tp),(3.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,6.000*tp),(0.125*tp,6.040*tp),(0.875*tp,6.040*tp),(0.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,5.125*tp),(1.000*tp,5.875*tp),(1.040*tp,5.875*tp),(1.040*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,5.125*tp),(1.000*tp,5.875*tp),(1.040*tp,5.875*tp),(1.040*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,4.125*tp),(1.000*tp,4.875*tp),(1.040*tp,4.875*tp),(1.040*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,3.125*tp),(1.000*tp,3.875*tp),(1.040*tp,3.875*tp),(1.040*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,1.125*tp),(1.000*tp,1.875*tp),(1.040*tp,1.875*tp),(1.040*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,0.125*tp),(1.000*tp,0.875*tp),(1.040*tp,0.875*tp),(1.040*tp,0.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,0.125*tp),(1.960*tp,0.875*tp),(2.000*tp,0.875*tp),(2.000*tp,0.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,1.125*tp),(1.960*tp,1.875*tp),(2.000*tp,1.875*tp),(2.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,2.125*tp),(1.960*tp,2.875*tp),(2.000*tp,2.875*tp),(2.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,3.125*tp),(1.960*tp,3.875*tp),(2.000*tp,3.875*tp),(2.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,4.125*tp),(1.960*tp,4.875*tp),(2.000*tp,4.875*tp),(2.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,5.125*tp),(1.960*tp,5.875*tp),(2.000*tp,5.875*tp),(2.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,2.125*tp),(1.000*tp,2.875*tp),(1.040*tp,2.875*tp),(1.040*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,4.775*tp),(0.300*tp,6.895*tp),(0.700*tp,6.895*tp),(0.700*tp,4.775*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.635*tp,5.300*tp),(0.635*tp,5.700*tp),(1.130*tp,5.700*tp),(1.130*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,0.105*tp),(0.300*tp,2.225*tp),(0.700*tp,2.225*tp),(0.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.655*tp,1.300*tp),(0.655*tp,1.700*tp),(1.990*tp,1.700*tp),(1.990*tp,1.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,1.655*tp),(1.300*tp,2.125*tp),(1.700*tp,2.125*tp),(1.700*tp,1.655*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.310*tp,0.660*tp),(4.310*tp,2.350*tp),(4.710*tp,2.350*tp),(4.710*tp,0.660*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.450*tp,6.995*tp),(3.450*tp,7.005*tp),(3.550*tp,7.005*tp),(3.550*tp,6.995*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.450*tp,-0.005*tp),(3.450*tp,0.005*tp),(3.550*tp,0.005*tp),(3.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(4.995*tp,3.450*tp),(4.995*tp,3.550*tp),(5.005*tp,3.550*tp),(5.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.030*tp,6.620*tp),(3.030*tp,6.670*tp),(3.085*tp,6.670*tp),(3.085*tp,6.620*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.335*tp,5.175*tp),(2.335*tp,5.225*tp),(2.390*tp,5.225*tp),(2.390*tp,5.175*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.030*tp,0.330*tp),(3.030*tp,0.385*tp),(3.090*tp,0.385*tp),(3.090*tp,0.330*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.325*tp,1.785*tp),(2.325*tp,1.840*tp),(2.385*tp,1.840*tp),(2.385*tp,1.785*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.435*tp,4.335*tp),(0.435*tp,4.390*tp),(0.495*tp,4.390*tp),(0.495*tp,4.335*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.565*tp,3.815*tp),(1.565*tp,3.870*tp),(1.620*tp,3.870*tp),(1.620*tp,3.815*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(4.335*tp,3.875*tp),(4.335*tp,3.930*tp),(4.390*tp,3.930*tp),(4.390*tp,3.875*tp)])

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.930*tp,5.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.305*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,0.735*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.165*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.595*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,2.025*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.510*tp,0.860*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.510*tp,1.290*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.510*tp,1.720*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.510*tp,2.150*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.790*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.360*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.930*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.695*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.265*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.835*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.405*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,4.975*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.950*tp,2.515*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.925*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,1.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,6.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,3.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,4.000*tp),transformation=ls.r270)

        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__ = "M0M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.35*tp,3.275*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2*tp,3.415*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.35*tp,3.555*tp))
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(3.455*tp,1.085*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(3.455*tp,6.085*tp),transformation=ls.r180)

        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.415*tp,4.510*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.855*tp,4.555*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.545*tp,0.560*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.690*tp,5.810*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.695*tp,4.510*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.260*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.160*tp,2.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.445*tp,2.500*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.880*tp,4.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.575*tp,2.490*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.260*tp,4.290*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.915*tp,5.340*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.190*tp,5.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.045*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.440*tp,5.590*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.685*tp,4.955*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.875*tp,5.380*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.685*tp,4.070*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.150*tp,4.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.270*tp,2.350*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.955*tp,2.350*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.245*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.960*tp,4.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.700*tp,5.820*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.695*tp,0.850*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.040*tp,0.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.880*tp,2.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.780*tp,0.535*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.645*tp,0.260*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.890*tp,2.610*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.870*tp,6.425*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.595*tp,2.455*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.615*tp,2.760*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_175(),midpoint=(3.110*tp,6.645*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_175(),midpoint=(1.415*tp,4.365*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_175(),midpoint=(4.365*tp,4.855*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(2.105*tp,0.355*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_162(),midpoint=(2.360*tp,5.145*tp))
        elems += spira.SRef(bias.ib_162(),midpoint=(2.360*tp,1.870*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_124(),midpoint=(1.590*tp,5.145*tp),transformation=ls.r180)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.500*tp,3.555*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(4.435*tp,3.560*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.480*tp,6.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.480*tp,0.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_194_sg(),midpoint=(3.580*tp,1.785*tp))
        elems += spira.SRef(jj.jj_194_sg(),midpoint=(3.580*tp,5.215*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_171_sg(),midpoint=(1.500*tp,3.565*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_160_s(),midpoint=(3.520*tp,5.575*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_160_s(),midpoint=(3.520*tp,1.425*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_157_sg(),midpoint=(2.430*tp,3.995*tp))
        elems += spira.SRef(jj.jj_157_sg(),midpoint=(2.430*tp,3.005*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_125_s(),midpoint=(3.500*tp,3.670*tp))
        elems += spira.SRef(jj.jj_125_s(),midpoint=(2.085*tp,3.975*tp))
        elems += spira.SRef(jj.jj_125_s(),midpoint=(3.500*tp,3.330*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_125_s(),midpoint=(2.085*tp,3.025*tp),transformation=ls.r180)
        return elems
        

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 5):
                if ((x == 1 and y in [0,6]) or (x == 4 and y == 6)):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
                elif ((x in [0,2,3] and y == 6) or (x == 1 and y in range(1, 6))):
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