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
    __name_prefix__ = "THmitll_XOR_v3p0"
    def create_elements(self, elems):
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        vias = spira.SRef(M5M6_connections())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M5Strips, IXports, jjfill, vias, M4M5M6M7conns, ib, jjs, ind, tblocks]

        # Text Labels
        elems += spira.Label(text='PB3 M6 M4',position=(2.77*tp,4.35*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(1.525*tp,3.215*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.545*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M6 M5',position=(2.44*tp,0.51*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.52*tp,4.44*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(0.900*tp,4.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(2.44*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(2.44*tp,5.57*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(2.500*tp,5.19*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(2.62*tp,2.445*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J11 M6 M5',position=(3.500*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M5 M6',position=(2.595*tp,2.085*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(1.935*tp,0.49*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.46*tp,3.095*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(2.015*tp,6.52*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB5 M6 M4',position=(3.645*tp,3.95*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P4 M6 M4',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(2.500*tp,7.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))

        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(3.96*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(3.95*tp,6.325*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='b',position=(2.500*tp,7.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='clk',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='RIB3',position=(3.02*tp,4.355*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(1.52*tp,2.915*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.84*tp,3.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(2.735*tp,0.51*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.52*tp,4.73*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.185*tp,4.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(2.73*tp,6.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(2.73*tp,5.57*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(2.500*tp,4.895*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(2.625*tp,2.735*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(2.595*tp,1.76*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB11',position=(3.21*tp,3.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(3.64*tp,4.400*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(1.475*tp,0.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.455*tp,2.65*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.585*tp,6.52*tp),layer=spira.Layer(number=52,datatype=11))
        return elems        
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.400*tp),(3.800*tp,3.500*tp),(3.900*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.500*tp),(0.100*tp,3.600*tp),(0.200*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.500*tp,6.800*tp),(2.400*tp,6.900*tp),(2.500*tp,6.900*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.525*tp,3.480*tp),(1.525*tp,3.620*tp),(2.555*tp,3.620*tp),(2.555*tp,4.425*tp),(2.890*tp,4.425*tp),(2.890*tp,4.285*tp),(2.695*tp,4.285*tp),(2.695*tp,3.480*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.405*tp,3.335*tp),(1.405*tp,3.620*tp),(1.645*tp,3.620*tp),(1.645*tp,3.335*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.600*tp,3.500*tp),(3.600*tp,3.600*tp),(3.900*tp,3.600*tp),(3.900*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.930*tp,2.340*tp),(1.930*tp,2.460*tp),(2.510*tp,2.460*tp),(2.510*tp,2.340*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.505*tp,0.620*tp),(2.505*tp,1.070*tp),(2.685*tp,1.070*tp),(2.685*tp,0.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.415*tp,0.100*tp),(2.415*tp,0.400*tp),(2.585*tp,0.400*tp),(2.585*tp,0.100*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.400*tp),(0.100*tp,3.500*tp),(0.450*tp,3.500*tp),(0.450*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.380*tp,3.025*tp),(0.380*tp,3.165*tp),(0.505*tp,3.165*tp),(0.505*tp,3.385*tp),(0.645*tp,3.385*tp),(0.645*tp,3.025*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.615*tp,3.620*tp),(0.615*tp,3.760*tp),(0.425*tp,3.760*tp),(0.425*tp,4.040*tp),(0.615*tp,4.040*tp),(0.615*tp,4.140*tp),(0.455*tp,4.140*tp),(0.455*tp,4.330*tp),(0.545*tp,4.330*tp),(0.545*tp,4.230*tp),(0.705*tp,4.230*tp),(0.705*tp,3.950*tp),(0.515*tp,3.950*tp),(0.515*tp,3.850*tp),(0.705*tp,3.850*tp),(0.705*tp,3.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.570*tp,6.620*tp),(2.570*tp,6.800*tp),(2.500*tp,6.800*tp),(2.500*tp,6.900*tp),(2.670*tp,6.900*tp),(2.670*tp,6.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.345*tp,5.675*tp),(2.345*tp,5.885*tp),(2.455*tp,5.885*tp),(2.455*tp,5.960*tp),(2.290*tp,5.960*tp),(2.290*tp,6.230*tp),(2.545*tp,6.230*tp),(2.545*tp,6.385*tp),(2.635*tp,6.385*tp),(2.635*tp,6.140*tp),(2.380*tp,6.140*tp),(2.380*tp,6.050*tp),(2.545*tp,6.050*tp),(2.545*tp,5.795*tp),(2.435*tp,5.795*tp),(2.435*tp,5.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.715*tp,2.5675*tp),(2.715*tp,2.6625*tp),(3.3325*tp,2.6625*tp),(3.3325*tp,3.385*tp),(3.4275*tp,3.385*tp),(3.4275*tp,2.5675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.400*tp,0.000*tp),(2.400*tp,0.100*tp),(2.600*tp,0.100*tp),(2.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.870*tp,0.420*tp),(1.870*tp,0.560*tp),(2.320*tp,0.560*tp),(2.320*tp,0.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.700*tp,0.400*tp),(0.700*tp,0.600*tp),(1.105*tp,0.600*tp),(1.105*tp,0.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.5025*tp,2.190*tp),(2.5025*tp,2.345*tp),(2.7025*tp,2.345*tp),(2.7025*tp,2.190*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.900*tp,3.400*tp),(3.900*tp,3.600*tp),(4.000*tp,3.600*tp),(4.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.430*tp,3.620*tp),(3.430*tp,4.020*tp),(3.705*tp,4.020*tp),(3.705*tp,3.880*tp),(3.570*tp,3.880*tp),(3.570*tp,3.620*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.410*tp,5.200*tp),(3.410*tp,6.280*tp),(3.590*tp,6.280*tp),(3.590*tp,5.200*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.570*tp,4.775*tp),(3.570*tp,5.130*tp),(3.500*tp,5.130*tp),(3.500*tp,5.270*tp),(3.710*tp,5.270*tp),(3.710*tp,4.775*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.290*tp,4.285*tp),(3.290*tp,5.270*tp),(3.500*tp,5.270*tp),(3.500*tp,5.130*tp),(3.430*tp,5.130*tp),(3.430*tp,4.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.100*tp,3.600*tp),(0.100*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.630*tp,4.375*tp),(0.630*tp,4.625*tp),(0.780*tp,4.625*tp),(0.780*tp,4.375*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.380*tp,0.720*tp),(0.380*tp,2.270*tp),(0.520*tp,2.270*tp),(0.520*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.400*tp,6.900*tp),(2.400*tp,7.000*tp),(2.600*tp,7.000*tp),(2.600*tp,6.900*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.375*tp,5.310*tp),(2.375*tp,5.455*tp),(2.625*tp,5.455*tp),(2.625*tp,5.310*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.950*tp,6.450*tp),(1.950*tp,6.590*tp),(2.320*tp,6.590*tp),(2.320*tp,6.450*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.720*tp,6.450*tp),(0.720*tp,6.590*tp),(1.185*tp,6.590*tp),(1.185*tp,6.450*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.320*tp,3.580*tp),(2.420*tp,3.680*tp),(2.420*tp,3.580*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.325*tp,3.545*tp),(1.325*tp,4.420*tp),(1.415*tp,4.420*tp),(1.415*tp,3.635*tp),(1.525*tp,3.635*tp),(1.525*tp,3.545*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.4175*tp,3.465*tp),(2.4175*tp,5.330*tp),(2.5825*tp,5.330*tp),(2.5825*tp,3.465*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.525*tp,3.465*tp),(1.525*tp,3.580*tp),(2.420*tp,3.580*tp),(2.420*tp,3.465*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.975*tp,2.415*tp),(1.975*tp,2.5825*tp),(1.505*tp,2.5825*tp),(1.505*tp,2.6825*tp),(2.075*tp,2.6825*tp),(2.075*tp,2.415*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.505*tp,0.915*tp),(2.505*tp,1.390*tp),(2.685*tp,1.390*tp),(2.685*tp,0.915*tp)])
        return elems

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M0,shape=[(0.350*tp,0.500*tp),(0.350*tp,7.000*tp),(0.650*tp,7.000*tp),(0.650*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(4.000*tp,6.650*tp),(4.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(3.125*tp,6.000*tp),(3.125*tp,6.040*tp),(3.875*tp,6.040*tp),(3.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,5.125*tp),(0.960*tp,5.875*tp),(1.000*tp,5.875*tp),(1.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,4.125*tp),(0.960*tp,4.875*tp),(1.000*tp,4.875*tp),(1.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,3.125*tp),(0.960*tp,3.875*tp),(1.000*tp,3.875*tp),(1.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,2.125*tp),(0.960*tp,2.875*tp),(1.000*tp,2.875*tp),(1.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,1.125*tp),(0.960*tp,1.875*tp),(1.000*tp,1.875*tp),(1.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,0.125*tp),(0.960*tp,0.875*tp),(1.000*tp,0.875*tp),(1.000*tp,0.125*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.300*tp,0.105*tp),(3.300*tp,2.225*tp),(3.700*tp,2.225*tp),(3.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,0.870*tp),(1.300*tp,2.130*tp),(1.700*tp,2.130*tp),(1.700*tp,0.870*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.845*tp,1.300*tp),(0.845*tp,1.700*tp),(2.105*tp,1.700*tp),(2.105*tp,1.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.105*tp,5.300*tp),(0.105*tp,5.700*tp),(1.795*tp,5.700*tp),(1.795*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,5.650*tp),(1.300*tp,6.125*tp),(1.700*tp,6.125*tp),(1.700*tp,5.650*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(2.450*tp,6.995*tp),(2.450*tp,7.005*tp),(2.550*tp,7.005*tp),(2.550*tp,6.995*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.995*tp,3.450*tp),(3.995*tp,3.550*tp),(4.005*tp,3.550*tp),(4.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.450*tp,-0.005*tp),(2.450*tp,0.005*tp),(2.550*tp,0.005*tp),(2.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.545*tp),(0.005*tp,3.545*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.990*tp,6.495*tp),(1.990*tp,6.550*tp),(2.045*tp,6.550*tp),(2.045*tp,6.495*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.665*tp,3.925*tp),(3.675*tp,3.925*tp),(3.675*tp,3.925*tp),(3.665*tp,3.925*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.615*tp,3.925*tp),(3.615*tp,3.975*tp),(3.670*tp,3.975*tp),(3.670*tp,3.925*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.745*tp,4.330*tp),(2.745*tp,4.385*tp),(2.800*tp,4.385*tp),(2.800*tp,4.330*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.910*tp,0.465*tp),(1.910*tp,0.515*tp),(1.965*tp,0.515*tp),(1.965*tp,0.465*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.435*tp,3.070*tp),(0.435*tp,3.120*tp),(0.490*tp,3.120*tp),(0.490*tp,3.070*tp)])

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,0.305*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,0.735*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,1.165*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,1.595*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,2.025*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.905*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.475*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.045*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.93*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.07*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.925*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.595*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.165*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.735*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.305*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r180)

        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__ = "M0M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.085*tp,2.305*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.685*tp,1.085*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.44*tp,3.635*tp),transformation=ls.r270)

        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.365*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.335*tp,5.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.88*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.15*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.155*tp,4.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.845*tp,4.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.700*tp,3.87*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.805*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.73*tp,1.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.88*tp,2.385*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.085*tp,5.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.695*tp,2.84*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.66*tp,0.755*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.64*tp,6.02*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.66*tp,6.88*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.67*tp,6.385*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.625*tp,5.185*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.625*tp,4.91*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.665*tp,2.405*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.665*tp,0.265*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.635*tp,2.485*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.205*tp,2.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.15*tp,1.565*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.145*tp,4.700*tp),transformation=ls.r180)

        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_273(),midpoint=(2.72*tp,4.355*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_175(),midpoint=(3.64*tp,3.895*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(0.455*tp,2.145*tp))
        elems += spira.SRef(bias.ib_175(),midpoint=(1.065*tp,6.52*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_175(),midpoint=(0.985*tp,0.485*tp),transformation=ls.r270)

        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_202_s(),midpoint=(2.500*tp,5.195*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_202_s(),midpoint=(0.89*tp,4.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_200_sg(),midpoint=(0.515*tp,4.44*tp))
        elems += spira.SRef(jj.jj_200_sg(),midpoint=(2.41*tp,5.57*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_196_s(),midpoint=(1.525*tp,3.23*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_165_sg(),midpoint=(2.61*tp,2.445*tp))
        elems += spira.SRef(jj.jj_146_s(),midpoint=(2.595*tp,2.09*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.49*tp,3.500*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.545*tp,3.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.44*tp,0.51*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.44*tp,6.500*tp),transformation=ls.r270)

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
                elif ((x == 0 and y in range(1,6)) or (x in [1,2] and y == 6)):
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