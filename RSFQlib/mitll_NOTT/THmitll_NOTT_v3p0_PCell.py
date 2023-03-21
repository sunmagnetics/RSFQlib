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
    __name_prefix__ = "THmitll_NOTT_v3p0"
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
        elems += spira.Label(text='P2 M6 M4',position=(3.15*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(2.500*tp,6.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(3.485*tp,5.44*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(2.365*tp,5.635*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.500*tp,6.15*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(1.500*tp,4.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.500*tp,5.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.52*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J10 M6 M5',position=(2.43*tp,0.73*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(2.745*tp,0.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J9 M6 M5',position=(3.39*tp,2.75*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.855*tp,1.365*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(1.625*tp,2.61*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M5 M6',position=(3.09*tp,2.615*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M5 M6',position=(3.425*tp,3.725*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(3.56*tp,3.38*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(1.955*tp,0.585*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(1.500*tp,6.965*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(0.505*tp,0.04*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='GND',position=(1.34*tp,6.96*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RB6',position=(2.215*tp,6.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(3.485*tp,5.73*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.025*tp,5.64*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.795*tp,5.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(1.505*tp,4.79*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.81*tp,3.495*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB10',position=(2.435*tp,0.435*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(1.495*tp,0.575*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(2.85*tp,0.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(3.395*tp,2.32*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(2.615*tp,2.62*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.155*tp,1.355*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.63*tp,2.24*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(3.42*tp,4.02*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(3.145*tp,3.375*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='clk',position=(3.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(3.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems

class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(3.280*tp,0.280*tp),(3.060*tp,0.500*tp),(3.280*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.280*tp,6.280*tp),(3.060*tp,6.500*tp),(3.280*tp,6.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,6.060*tp),(0.280*tp,6.280*tp),(0.720*tp,6.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,5.030*tp),(1.430*tp,6.570*tp),(1.570*tp,6.570*tp),(1.570*tp,5.030*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,5.565*tp),(1.430*tp,5.705*tp),(1.765*tp,5.705*tp),(1.765*tp,5.565*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,0.510*tp),(0.430*tp,0.650*tp),(1.130*tp,0.650*tp),(1.130*tp,0.510*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.8775*tp,0.420*tp),(2.8775*tp,0.580*tp),(3.280*tp,0.580*tp),(3.280*tp,0.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.6675*tp,0.435*tp),(2.6675*tp,0.565*tp),(2.545*tp,0.565*tp),(2.545*tp,0.705*tp),(2.8075*tp,0.705*tp),(2.8075*tp,0.435*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.885*tp,0.510*tp),(1.885*tp,0.710*tp),(2.310*tp,0.710*tp),(2.310*tp,0.570*tp),(2.025*tp,0.570*tp),(2.025*tp,0.510*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.290*tp,5.565*tp),(2.290*tp,5.705*tp),(2.550*tp,5.705*tp),(2.550*tp,5.565*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.320*tp,2.825*tp),(3.320*tp,3.105*tp),(3.570*tp,3.105*tp),(3.570*tp,2.965*tp),(3.460*tp,2.965*tp),(3.460*tp,2.825*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.410*tp,3.610*tp),(0.410*tp,3.930*tp),(0.590*tp,3.930*tp),(0.590*tp,4.020*tp),(0.345*tp,4.020*tp),(0.345*tp,4.340*tp),(0.450*tp,4.340*tp),(0.450*tp,4.495*tp),(0.550*tp,4.495*tp),(0.550*tp,4.240*tp),(0.445*tp,4.240*tp),(0.445*tp,4.120*tp),(0.690*tp,4.120*tp),(0.690*tp,3.830*tp),(0.510*tp,3.830*tp),(0.510*tp,3.610*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.600*tp,6.420*tp),(2.600*tp,6.580*tp),(3.280*tp,6.580*tp),(3.280*tp,6.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,5.600*tp),(0.420*tp,6.280*tp),(0.580*tp,6.280*tp),(0.580*tp,5.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,4.425*tp),(0.500*tp,4.565*tp),(1.575*tp,4.565*tp),(1.575*tp,4.425*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.000*tp,5.290*tp),(3.000*tp,5.565*tp),(2.910*tp,5.565*tp),(2.910*tp,5.315*tp),(2.625*tp,5.315*tp),(2.625*tp,5.565*tp),(2.550*tp,5.565*tp),(2.550*tp,5.665*tp),(2.725*tp,5.665*tp),(2.725*tp,5.415*tp),(2.810*tp,5.415*tp),(2.810*tp,5.665*tp),(3.100*tp,5.665*tp),(3.100*tp,5.390*tp),(3.190*tp,5.390*tp),(3.190*tp,5.505*tp),(3.370*tp,5.505*tp),(3.370*tp,5.405*tp),(3.290*tp,5.405*tp),(3.290*tp,5.290*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.450*tp,4.495*tp),(0.450*tp,5.410*tp),(0.550*tp,5.410*tp),(0.550*tp,4.495*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.310*tp,0.845*tp),(2.310*tp,1.050*tp),(2.380*tp,1.050*tp),(2.380*tp,1.175*tp),(2.290*tp,1.175*tp),(2.290*tp,1.455*tp),(3.280*tp,1.455*tp),(3.280*tp,1.700*tp),(3.605*tp,1.700*tp),(3.605*tp,2.670*tp),(3.465*tp,2.670*tp),(3.465*tp,2.770*tp),(3.705*tp,2.770*tp),(3.705*tp,1.600*tp),(3.380*tp,1.600*tp),(3.380*tp,1.355*tp),(2.390*tp,1.355*tp),(2.390*tp,1.275*tp),(2.480*tp,1.275*tp),(2.480*tp,0.950*tp),(2.410*tp,0.950*tp),(2.410*tp,0.845*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.165*tp,2.5325*tp),(3.165*tp,2.7175*tp),(3.315*tp,2.7175*tp),(3.315*tp,2.5325*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.500*tp,5.635*tp),(2.500*tp,5.790*tp),(2.365*tp,5.790*tp),(2.365*tp,6.085*tp),(2.550*tp,6.085*tp),(2.550*tp,6.180*tp),(2.300*tp,6.180*tp),(2.300*tp,6.400*tp),(2.400*tp,6.400*tp),(2.400*tp,6.280*tp),(2.650*tp,6.280*tp),(2.650*tp,5.985*tp),(2.465*tp,5.985*tp),(2.465*tp,5.890*tp),(2.600*tp,5.890*tp),(2.600*tp,5.635*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,0.430*tp),(0.430*tp,1.430*tp),(0.570*tp,1.430*tp),(0.570*tp,0.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.280*tp,1.295*tp),(1.280*tp,1.685*tp),(1.420*tp,1.685*tp),(1.420*tp,1.435*tp),(1.925*tp,1.435*tp),(1.925*tp,1.295*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.340*tp,3.465*tp),(3.340*tp,3.610*tp),(3.540*tp,3.610*tp),(3.540*tp,3.465*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.535*tp,3.765*tp),(3.535*tp,3.855*tp),(3.625*tp,3.855*tp),(3.625*tp,4.925*tp),(3.390*tp,4.925*tp),(3.390*tp,5.325*tp),(3.480*tp,5.325*tp),(3.480*tp,5.015*tp),(3.715*tp,5.015*tp),(3.715*tp,3.765*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.755*tp,2.285*tp),(0.755*tp,2.525*tp),(0.530*tp,2.525*tp),(0.530*tp,3.385*tp),(0.630*tp,3.385*tp),(0.630*tp,2.625*tp),(0.855*tp,2.625*tp),(0.855*tp,2.385*tp),(1.145*tp,2.385*tp),(1.145*tp,2.690*tp),(1.545*tp,2.690*tp),(1.545*tp,2.590*tp),(1.245*tp,2.590*tp),(1.245*tp,2.285*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.400*tp,6.400*tp),(1.400*tp,7.000*tp),(1.600*tp,7.000*tp),(1.600*tp,6.400*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,0.000*tp),(0.400*tp,0.600*tp),(0.600*tp,0.600*tp),(0.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.650*tp,2.3475*tp),(1.650*tp,2.7175*tp),(3.1825*tp,2.7175*tp),(3.1825*tp,2.3475*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,1.530*tp),(1.300*tp,2.515*tp),(1.525*tp,2.515*tp),(1.525*tp,2.395*tp),(1.420*tp,2.395*tp),(1.420*tp,1.530*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.400*tp,2.950*tp),(3.400*tp,3.280*tp),(3.600*tp,3.280*tp),(3.600*tp,2.950*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.550*tp,2.700*tp),(1.550*tp,2.920*tp),(1.615*tp,2.920*tp),(1.615*tp,3.440*tp),(1.930*tp,3.440*tp),(1.930*tp,3.385*tp),(2.050*tp,3.385*tp),(2.050*tp,3.715*tp),(2.350*tp,3.715*tp),(2.350*tp,3.625*tp),(2.450*tp,3.625*tp),(2.450*tp,3.715*tp),(2.750*tp,3.715*tp),(2.750*tp,3.670*tp),(3.050*tp,3.670*tp),(3.050*tp,3.715*tp),(3.300*tp,3.715*tp),(3.300*tp,3.615*tp),(3.150*tp,3.615*tp),(3.150*tp,3.570*tp),(2.650*tp,3.570*tp),(2.650*tp,3.615*tp),(2.550*tp,3.615*tp),(2.550*tp,3.525*tp),(2.250*tp,3.525*tp),(2.250*tp,3.615*tp),(2.150*tp,3.615*tp),(2.150*tp,3.285*tp),(1.830*tp,3.285*tp),(1.830*tp,3.340*tp),(1.715*tp,3.340*tp),(1.715*tp,2.820*tp),(1.650*tp,2.820*tp),(1.650*tp,2.700*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,1.570*tp),(0.300*tp,2.400*tp),(0.700*tp,2.400*tp),(0.700*tp,1.570*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.300*tp,4.360*tp),(2.300*tp,5.190*tp),(2.700*tp,5.190*tp),(2.700*tp,4.360*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.675*tp,4.360*tp),(2.675*tp,4.700*tp),(3.135*tp,4.700*tp),(3.135*tp,4.360*tp)])
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=0.830*tp,center=(0.500*tp,1.985*tp))
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=0.830*tp,center=(2.500*tp,4.775*tp))
        elems += spira.Box(layer=ls.M5,width=0.460*tp,height=0.340*tp,center=(2.905*tp,4.530*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.160*tp,center=(3.150*tp,6.500*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.000*tp,center=(0.500*tp,6.150*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.050*tp,center=(2.3675*tp,5.635*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.055*tp,center=(1.500*tp,4.4975*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.050*tp,center=(1.9575*tp,0.580*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.050*tp,center=(2.7475*tp,0.500*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.055*tp,center=(1.8525*tp,1.3625*tp))
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,1.04*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,1.77*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,0.94*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,2.200*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.77*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,4.56*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,4.99*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.935*tp,4.500*tp),transformation=ls.r180)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.61*tp,3.56*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.565*tp,1.37*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.325*tp,0.135*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.385*tp,2.84*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.44*tp,2.845*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.88*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,3.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,4.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.445*tp,2.94*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.26*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.98*tp,6.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.695*tp,0.97*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.45*tp,4.51*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.45*tp,3.085*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.42*tp,3.37*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.44*tp,3.915*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,4.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.18*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.135*tp,1.695*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.63*tp,6.88*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.985*tp,5.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.43*tp,5.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.645*tp,2.23*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.435*tp,2.665*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.14*tp,1.68*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.07*tp,0.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.09*tp,0.44*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.15*tp,1.675*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.56*tp,4.155*tp),transformation=ls.r270)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.415*tp,0.585*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(3.415*tp,3.12*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.415*tp,6.585*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.265*tp,1.700*tp),transformation=ls.r270)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_267(),midpoint=(1.500*tp,5.155*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_241(),midpoint=(1.645*tp,5.635*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_175(),midpoint=(1.005*tp,0.58*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_114(),midpoint=(0.445*tp,1.36*tp),transformation=ls.r270)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.43*tp,0.725*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_238_sg(),midpoint=(0.52*tp,3.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_218_sg(),midpoint=(3.485*tp,5.435*tp))
        elems += spira.SRef(jj.jj_198_s(),midpoint=(3.425*tp,3.725*tp))
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(2.500*tp,6.500*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.500*tp,5.500*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_087_s(),midpoint=(3.555*tp,3.38*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_082_sg(),midpoint=(3.39*tp,2.745*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_077_s(),midpoint=(1.625*tp,2.61*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_073_s(),midpoint=(3.08*tp,2.615*tp),transformation=ls.r90)
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(2.69*tp,0.500*tp),transformation=ls.r270,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 4):
                if ((x == 0 and y == 6) or (x == 3 and y in [0,6])):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,7.000*tp),transformation=ls.r180)
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(4.000*tp,7.000*tp),transformation=ls.r180)
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