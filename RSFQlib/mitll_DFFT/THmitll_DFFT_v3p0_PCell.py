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
    __name_prefix__ = "THmitll_DFFT_v3p0"
    def create_elements(self, elems):
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
        elems += [IXports, M0M4M7tracks, jjfill, M4M5M6M7conns,
                  vias, ib, jjs, rs, ind, tblocks]

        # Text Labels
        elems += spira.Label(text="J1 M6 M5",position=(0.525*tp,1.505*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(0.440*tp,3.395*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(2.475*tp,1.500*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(2.560*tp,3.410*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(0.740*tp,4.580*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(2.275*tp,5.440*tp),layer=TEXT)
        elems += spira.Label(text="J9 M6 M5",position=(1.510*tp,6.255*tp),layer=TEXT)
        elems += spira.Label(text="J3 M5 M6",position=(0.370*tp,4.600*tp),layer=TEXT)
        elems += spira.Label(text="J7 M5 M6",position=(2.620*tp,5.525*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(1.360*tp,2.460*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(1.635*tp,2.470*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(0.650*tp,5.070*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(1.200*tp,6.355*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(1.795*tp,6.500*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(0.500*tp,0.850*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(2.500*tp,0.850*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(0.500*tp,6.960*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='GND',position=(0.350*tp,6.950*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RB1',position=(0.805*tp,1.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.735*tp,3.390*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(0.380*tp,4.275*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.025*tp,4.580*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(2.210*tp,1.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(2.280*tp,3.415*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(2.630*tp,5.190*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(2.265*tp,5.720*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(1.495*tp,6.555*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(1.900*tp,6.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(1.350*tp,2.150*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(0.645*tp,5.460*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(1.630*tp,2.085*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(0.795*tp,6.350*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='q',position=(2.500*tp,6.505*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='clk',position=(2.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(2.280*tp,6.280*tp),(2.060*tp,6.500*tp),(2.280*tp,6.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.280*tp,0.720*tp),(0.500*tp,0.940*tp),(0.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.280*tp,0.720*tp),(2.500*tp,0.940*tp),(2.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.9325*tp,6.420*tp),(1.9325*tp,6.580*tp),(2.280*tp,6.580*tp),(2.280*tp,6.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.420*tp,0.720*tp),(0.420*tp,1.235*tp),(0.495*tp,1.235*tp),(0.495*tp,1.400*tp),(0.655*tp,1.400*tp),(0.655*tp,1.075*tp),(0.580*tp,1.075*tp),(0.580*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.420*tp,0.720*tp),(2.420*tp,1.055*tp),(2.345*tp,1.055*tp),(2.345*tp,1.400*tp),(2.505*tp,1.400*tp),(2.505*tp,1.215*tp),(2.580*tp,1.215*tp),(2.580*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.430*tp,0.430*tp),(1.430*tp,1.350*tp),(1.570*tp,1.350*tp),(1.570*tp,0.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.500*tp,1.280*tp),(1.500*tp,1.420*tp),(1.570*tp,1.420*tp),(1.570*tp,1.720*tp),(1.710*tp,1.720*tp),(1.710*tp,1.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.290*tp,1.280*tp),(1.290*tp,1.915*tp),(1.430*tp,1.915*tp),(1.430*tp,1.420*tp),(1.500*tp,1.420*tp),(1.500*tp,1.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.475*tp,4.460*tp),(0.475*tp,4.700*tp),(0.625*tp,4.700*tp),(0.625*tp,4.460*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.325*tp,3.490*tp),(0.325*tp,3.780*tp),(0.695*tp,3.780*tp),(0.695*tp,3.690*tp),(0.415*tp,3.690*tp),(0.415*tp,3.490*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,4.685*tp),(0.575*tp,5.145*tp),(0.715*tp,5.145*tp),(0.715*tp,4.685*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.500*tp,2.390*tp),(0.500*tp,2.530*tp),(1.430*tp,2.530*tp),(1.430*tp,2.390*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.455*tp,2.460*tp),(0.455*tp,2.705*tp),(0.590*tp,2.705*tp),(0.590*tp,2.800*tp),(0.310*tp,2.800*tp),(0.310*tp,3.105*tp),(0.570*tp,3.105*tp),(0.570*tp,3.285*tp),(0.660*tp,3.285*tp),(0.660*tp,3.015*tp),(0.400*tp,3.015*tp),(0.400*tp,2.890*tp),(0.680*tp,2.890*tp),(0.680*tp,2.615*tp),(0.545*tp,2.615*tp),(0.545*tp,2.460*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.930*tp,2.290*tp),(1.930*tp,2.395*tp),(1.570*tp,2.395*tp),(1.570*tp,2.535*tp),(2.070*tp,2.535*tp),(2.070*tp,2.430*tp),(2.500*tp,2.430*tp),(2.500*tp,2.290*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.405*tp,1.600*tp),(2.405*tp,2.045*tp),(2.455*tp,2.045*tp),(2.455*tp,2.360*tp),(2.545*tp,2.360*tp),(2.545*tp,1.955*tp),(2.495*tp,1.955*tp),(2.495*tp,1.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.855*tp,4.290*tp),(0.855*tp,4.470*tp),(0.945*tp,4.470*tp),(0.945*tp,4.380*tp),(1.605*tp,4.380*tp),(1.605*tp,4.430*tp),(1.780*tp,4.430*tp),(1.780*tp,4.605*tp),(1.605*tp,4.605*tp),(1.605*tp,4.815*tp),(1.315*tp,4.815*tp),(1.315*tp,5.080*tp),(1.615*tp,5.080*tp),(1.615*tp,5.175*tp),(1.385*tp,5.175*tp),(1.385*tp,5.440*tp),(2.160*tp,5.440*tp),(2.160*tp,5.350*tp),(1.475*tp,5.350*tp),(1.475*tp,5.265*tp),(1.705*tp,5.265*tp),(1.705*tp,4.990*tp),(1.405*tp,4.990*tp),(1.405*tp,4.905*tp),(1.695*tp,4.905*tp),(1.695*tp,4.695*tp),(1.870*tp,4.695*tp),(1.870*tp,4.340*tp),(1.695*tp,4.340*tp),(1.695*tp,4.290*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.345*tp,5.530*tp),(1.345*tp,5.815*tp),(1.615*tp,5.815*tp),(1.615*tp,5.930*tp),(1.515*tp,5.930*tp),(1.515*tp,6.140*tp),(1.605*tp,6.140*tp),(1.605*tp,6.020*tp),(1.705*tp,6.020*tp),(1.705*tp,5.725*tp),(1.435*tp,5.725*tp),(1.435*tp,5.620*tp),(2.160*tp,5.620*tp),(2.160*tp,5.530*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.610*tp,6.300*tp),(1.610*tp,6.430*tp),(1.7275*tp,6.430*tp),(1.7275*tp,6.570*tp),(1.8575*tp,6.570*tp),(1.8575*tp,6.300*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.375*tp,5.3225*tp),(2.375*tp,5.6225*tp),(2.530*tp,5.6225*tp),(2.530*tp,5.3225*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.125*tp,6.285*tp),(1.125*tp,6.425*tp),(1.385*tp,6.425*tp),(1.385*tp,6.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.230*tp,6.285*tp),(0.230*tp,6.425*tp),(0.430*tp,6.425*tp),(0.430*tp,6.770*tp),(0.570*tp,6.770*tp),(0.570*tp,6.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.575*tp,5.765*tp),(0.575*tp,6.285*tp),(0.500*tp,6.285*tp),(0.500*tp,6.425*tp),(0.715*tp,6.425*tp),(0.715*tp,5.765*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.355*tp,3.480*tp),(2.355*tp,4.440*tp),(2.475*tp,4.440*tp),(2.475*tp,3.480*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.455*tp,1.595*tp),(0.455*tp,1.895*tp),(0.595*tp,1.895*tp),(0.595*tp,2.155*tp),(0.455*tp,2.155*tp),(0.455*tp,2.460*tp),(0.545*tp,2.460*tp),(0.545*tp,2.245*tp),(0.685*tp,2.245*tp),(0.685*tp,1.805*tp),(0.545*tp,1.805*tp),(0.545*tp,1.595*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.500*tp,2.340*tp),(2.500*tp,2.430*tp),(2.575*tp,2.430*tp),(2.575*tp,2.505*tp),(2.290*tp,2.505*tp),(2.290*tp,2.755*tp),(2.625*tp,2.755*tp),(2.625*tp,2.825*tp),(2.285*tp,2.825*tp),(2.285*tp,3.075*tp),(2.570*tp,3.075*tp),(2.570*tp,3.145*tp),(2.355*tp,3.145*tp),(2.355*tp,3.330*tp),(2.445*tp,3.330*tp),(2.445*tp,3.235*tp),(2.660*tp,3.235*tp),(2.660*tp,2.985*tp),(2.375*tp,2.985*tp),(2.375*tp,2.915*tp),(2.715*tp,2.915*tp),(2.715*tp,2.665*tp),(2.380*tp,2.665*tp),(2.380*tp,2.595*tp),(2.665*tp,2.595*tp),(2.665*tp,2.340*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.400*tp,0.000*tp),(1.400*tp,0.600*tp),(1.600*tp,0.600*tp),(1.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.625*tp,3.625*tp),(0.625*tp,4.245*tp),(0.455*tp,4.245*tp),(0.455*tp,4.335*tp),(0.715*tp,4.335*tp),(0.715*tp,3.625*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,6.600*tp),(0.400*tp,7.000*tp),(0.600*tp,7.000*tp),(0.600*tp,6.600*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.355*tp,4.285*tp),(2.355*tp,4.570*tp),(2.290*tp,4.570*tp),(2.290*tp,5.160*tp),(2.540*tp,5.160*tp),(2.540*tp,5.040*tp),(2.410*tp,5.040*tp),(2.410*tp,4.690*tp),(2.475*tp,4.690*tp),(2.475*tp,4.285*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.455*tp,4.335*tp),(0.455*tp,4.355*tp),(0.500*tp,4.355*tp),(0.500*tp,4.335*tp)])
        return elems          

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.010*tp,center=(2.500*tp,0.850*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0.160*tp,height=0.010*tp,center=(0.500*tp,0.850*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.050*tp,center=(1.360*tp,2.460*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.050*tp,center=(1.6375*tp,2.465*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.050*tp,center=(1.2025*tp,6.350*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.055*tp,center=(0.6475*tp,5.0725*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.055*tp,center=(1.790*tp,6.4975*tp))
       
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(2.125*tp,6.040*tp),(2.125*tp,6.125*tp),(2.040*tp,6.125*tp),(2.040*tp,6.280*tp),(2.280*tp,6.280*tp),(2.280*tp,6.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape=spira.Shape(points=[(2.040*tp,5.720*tp),(2.040*tp,5.875*tp),(2.125*tp,5.875*tp),(2.125*tp,5.960*tp),(2.280*tp,5.960*tp),(2.280*tp,5.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.495*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,2.855*tp),transformation=ls.r90)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.270*tp,2.340*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.445*tp,5.805*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.960*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.445*tp,4.895*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.260*tp,5.340*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.165*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.260*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.680*tp,5.810*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.880*tp,4.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.700*tp,3.770*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.880*tp,2.2825*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.150*tp,4.340*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.875*tp,0.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.265*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.975*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.260*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.880*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.135*tp,6.695*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.660*tp,3.365*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.610*tp,3.665*tp),transformation=ls.r180)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.710*tp,3.795*tp),transformation=ls.r180,alias='via1')
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.330*tp,4.285*tp),alias='via2')
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.585*tp,0.415*tp),transformation=ls.r90,alias='via3')
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.585*tp,6.615*tp),transformation=ls.r90,alias='via4')
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_175(),midpoint=(1.255*tp,6.350*tp),transformation=ls.r90,alias='bias4')
        elems += spira.SRef(bias.ib_194(),midpoint=(1.640*tp,2.520*tp),transformation=ls.r180,alias='bias2')
        elems += spira.SRef(bias.ib_206(),midpoint=(0.645*tp,5.895*tp),transformation=ls.r180,alias='bias1')
        elems += spira.SRef(bias.ib_262(),midpoint=(1.360*tp,2.515*tp),transformation=ls.r180,alias='bias3')
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_127_sg(),midpoint=(2.555*tp,3.415*tp),transformation=ls.r90,alias='J1')
        elems += spira.SRef(jj.jj_128_s(),midpoint=(2.625*tp,5.520*tp),transformation=ls.r180,alias='J2')
        elems += spira.SRef(jj.jj_136_s(),midpoint=(0.380*tp,4.595*tp),transformation=ls.r180,alias='J3')
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(2.475*tp,1.500*tp),transformation=ls.r90,alias='J4')
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(0.525*tp,1.500*tp),transformation=ls.r270,alias='J5')
        elems += spira.SRef(jj.jj_182_sg(),midpoint=(0.440*tp,3.390*tp),transformation=ls.r270,alias='J6')
        elems += spira.SRef(jj.jj_189_sg(),midpoint=(2.265*tp,5.440*tp),alias='J7')
        elems += spira.SRef(jj.jj_207_sg(),midpoint=(0.740*tp,4.580*tp),transformation=ls.r270,alias='J8')
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(1.500*tp,6.260*tp),alias='J9')

        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(2.050*tp,6.500*tp),transformation=ls.r90,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                if (x == 2 and y in [0,6]) or (x == 0 and y == 0):
                    elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
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