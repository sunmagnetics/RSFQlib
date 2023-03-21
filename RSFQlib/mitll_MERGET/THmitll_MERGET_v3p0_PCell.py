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
    __name_prefix__ = "THmitll_MERGET_v3p0"
    def create_elements(self, elems):
        M0M4M7strips = spira.SRef(M0M4M7_strips())
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
        elems += [M0M4M7strips, M6M5Strips, IXports, jjfill, M4M5M6M7conns,
                  vias, ib, jjs, rs, ind, tblocks]

        # Text Labels
        elems += spira.Label(text="J9 M6 M5",position=(3.385*tp,3.440*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(1.610*tp,1.460*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(0.445*tp,2.495*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(1.230*tp,3.450*tp),layer=TEXT)
        elems += spira.Label(text="J4 M6 M5",position=(1.615*tp,3.445*tp),layer=TEXT)
        elems += spira.Label(text="J5 M6 M5",position=(4.505*tp,5.560*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(2.560*tp,5.620*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(2.565*tp,4.770*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(2.565*tp,4.380*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(3.640*tp,6.635*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(2.835*tp,6.410*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(2.460*tp,2.640*tp),layer=TEXT)
        elems += spira.Label(text="PB6 M6 M4",position=(3.650*tp,2.995*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(2.640*tp,1.745*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(0.400*tp,2.145*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(4.500*tp,6.150*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.500*tp,0.850*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(3.760*tp,3.500*tp),layer=TEXT)
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(1.500*tp,6.955*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(0.500*tp,0.050*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='VDD',position=(3.500*tp,0.045*tp),layer=spira.Layer(number=50,datatype=0))
        elems += spira.Label(text='RIB1',position=(2.640*tp,1.135*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(0.395*tp,1.705*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.930*tp,6.650*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(2.345*tp,6.415*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB5',position=(2.905*tp,2.635*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB6',position=(3.665*tp,2.550*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(1.605*tp,1.740*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.840*tp,2.495*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(1.235*tp,3.745*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.620*tp,3.760*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(4.495*tp,5.275*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(2.170*tp,5.615*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(2.170*tp,4.770*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(2.225*tp,4.385*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB9',position=(3.375*tp,3.730*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RD',position=(3.860*tp,3.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='GND',position=(1.345*tp,6.915*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='b',position=(4.500*tp,6.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(1.500*tp,0.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(4.500*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(4.500*tp,6.060*tp),(4.280*tp,6.280*tp),(4.720*tp,6.280*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.280*tp,0.720*tp),(1.500*tp,0.940*tp),(1.720*tp,0.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.280*tp,3.280*tp),(4.060*tp,3.500*tp),(4.280*tp,3.720*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.005*tp,1.285*tp),(1.005*tp,1.625*tp),(0.925*tp,1.625*tp),(0.925*tp,1.290*tp),(0.635*tp,1.290*tp),(0.635*tp,1.390*tp),(0.415*tp,1.390*tp),(0.415*tp,1.780*tp),(0.625*tp,1.780*tp),(0.625*tp,1.885*tp),(0.560*tp,1.885*tp),(0.560*tp,2.400*tp),(0.650*tp,2.400*tp),(0.650*tp,1.975*tp),(0.715*tp,1.975*tp),(0.715*tp,1.690*tp),(0.505*tp,1.690*tp),(0.505*tp,1.480*tp),(0.725*tp,1.480*tp),(0.725*tp,1.380*tp),(0.835*tp,1.380*tp),(0.835*tp,1.715*tp),(1.095*tp,1.715*tp),(1.095*tp,1.375*tp),(1.175*tp,1.375*tp),(1.175*tp,1.715*tp),(1.430*tp,1.715*tp),(1.430*tp,1.445*tp),(1.515*tp,1.445*tp),(1.515*tp,1.355*tp),(1.340*tp,1.355*tp),(1.340*tp,1.625*tp),(1.265*tp,1.625*tp),(1.265*tp,1.285*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.305*tp,4.935*tp),(3.305*tp,5.625*tp),(3.120*tp,5.625*tp),(3.120*tp,5.300*tp),(2.780*tp,5.300*tp),(2.780*tp,5.620*tp),(2.640*tp,5.620*tp),(2.640*tp,5.710*tp),(2.870*tp,5.710*tp),(2.870*tp,5.390*tp),(3.030*tp,5.390*tp),(3.030*tp,5.715*tp),(3.395*tp,5.715*tp),(3.395*tp,5.025*tp),(3.610*tp,5.025*tp),(3.610*tp,5.380*tp),(3.855*tp,5.380*tp),(3.855*tp,5.420*tp),(4.395*tp,5.420*tp),(4.395*tp,5.330*tp),(3.945*tp,5.330*tp),(3.945*tp,5.290*tp),(3.700*tp,5.290*tp),(3.700*tp,4.935*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.430*tp,3.360*tp),(2.430*tp,3.640*tp),(3.265*tp,3.640*tp),(3.265*tp,3.360*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.4125*tp,2.575*tp),(0.4125*tp,3.5175*tp),(1.110*tp,3.5175*tp),(1.110*tp,3.3425*tp),(0.5875*tp,3.3425*tp),(0.5875*tp,2.575*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.895*tp,3.420*tp),(3.895*tp,3.580*tp),(4.300*tp,3.580*tp),(4.300*tp,3.420*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.490*tp,3.430*tp),(3.490*tp,3.570*tp),(3.825*tp,3.570*tp),(3.825*tp,3.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.335*tp,4.485*tp),(2.335*tp,4.645*tp),(2.665*tp,4.645*tp),(2.665*tp,4.485*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.345*tp,3.340*tp),(1.345*tp,3.670*tp),(1.525*tp,3.670*tp),(1.525*tp,3.340*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(4.420*tp,5.655*tp),(4.420*tp,6.295*tp),(4.580*tp,6.295*tp),(4.580*tp,5.655*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.575*tp,5.525*tp),(3.575*tp,6.710*tp),(3.715*tp,6.710*tp),(3.715*tp,5.665*tp),(4.400*tp,5.665*tp),(4.400*tp,5.525*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.425*tp,6.430*tp),(1.425*tp,6.570*tp),(1.700*tp,6.570*tp),(1.700*tp,6.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.845*tp,6.335*tp),(1.845*tp,6.430*tp),(1.700*tp,6.430*tp),(1.700*tp,6.570*tp),(1.985*tp,6.570*tp),(1.985*tp,6.335*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.845*tp,6.500*tp),(1.845*tp,6.705*tp),(2.345*tp,6.705*tp),(2.345*tp,6.565*tp),(1.985*tp,6.565*tp),(1.985*tp,6.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.445*tp,5.705*tp),(2.445*tp,6.475*tp),(2.910*tp,6.475*tp),(2.910*tp,6.335*tp),(2.585*tp,6.335*tp),(2.585*tp,5.705*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.585*tp,4.880*tp),(2.585*tp,5.155*tp),(2.345*tp,5.155*tp),(2.345*tp,5.525*tp),(2.435*tp,5.525*tp),(2.435*tp,5.245*tp),(2.675*tp,5.245*tp),(2.675*tp,4.880*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.575*tp,2.920*tp),(3.575*tp,3.030*tp),(3.290*tp,3.030*tp),(3.290*tp,3.330*tp),(3.430*tp,3.330*tp),(3.430*tp,3.170*tp),(3.715*tp,3.170*tp),(3.715*tp,2.920*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.385*tp,2.570*tp),(2.385*tp,3.045*tp),(2.430*tp,3.045*tp),(2.430*tp,3.500*tp),(2.570*tp,3.500*tp),(2.570*tp,2.905*tp),(2.525*tp,2.905*tp),(2.525*tp,2.570*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.300*tp,2.030*tp),(3.300*tp,2.710*tp),(3.440*tp,2.710*tp),(3.440*tp,2.170*tp),(3.715*tp,2.170*tp),(3.715*tp,2.030*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.430*tp,0.470*tp),(3.430*tp,0.730*tp),(3.300*tp,0.730*tp),(3.300*tp,2.100*tp),(3.440*tp,2.100*tp),(3.440*tp,0.870*tp),(3.570*tp,0.870*tp),(3.570*tp,0.470*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.320*tp,2.075*tp),(0.320*tp,2.215*tp),(0.345*tp,2.215*tp),(0.345*tp,2.405*tp),(0.485*tp,2.405*tp),(0.485*tp,2.075*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,0.500*tp),(0.430*tp,0.815*tp),(0.325*tp,0.815*tp),(0.325*tp,1.305*tp),(0.465*tp,1.305*tp),(0.465*tp,0.955*tp),(0.570*tp,0.955*tp),(0.570*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.555*tp,0.300*tp),(2.555*tp,0.440*tp),(2.930*tp,0.440*tp),(2.930*tp,0.570*tp),(3.500*tp,0.570*tp),(3.500*tp,0.430*tp),(3.070*tp,0.430*tp),(3.070*tp,0.300*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.710*tp,1.380*tp),(1.710*tp,1.520*tp),(2.565*tp,1.520*tp),(2.565*tp,1.815*tp),(2.705*tp,1.815*tp),(2.705*tp,1.380*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.420*tp,0.700*tp),(1.420*tp,1.210*tp),(1.530*tp,1.210*tp),(1.530*tp,1.360*tp),(1.690*tp,1.360*tp),(1.690*tp,1.050*tp),(1.580*tp,1.050*tp),(1.580*tp,0.700*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.400*tp,6.400*tp),(1.400*tp,7.000*tp),(1.600*tp,7.000*tp),(1.600*tp,6.400*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.400*tp,0.000*tp),(0.400*tp,0.600*tp),(0.600*tp,0.600*tp),(0.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.400*tp,0.000*tp),(3.400*tp,0.600*tp),(3.600*tp,0.600*tp),(3.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.730*tp,3.385*tp),(1.730*tp,3.635*tp),(2.600*tp,3.635*tp),(2.600*tp,3.385*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.385*tp,3.390*tp),(2.385*tp,4.270*tp),(2.615*tp,4.270*tp),(2.615*tp,3.390*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,3.915*tp),(0.300*tp,6.895*tp),(0.700*tp,6.895*tp),(0.700*tp,3.915*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.610*tp,4.300*tp),(0.610*tp,4.700*tp),(1.130*tp,4.700*tp),(1.130*tp,4.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.640*tp,5.300*tp),(0.640*tp,5.700*tp),(1.130*tp,5.700*tp),(1.130*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(4.300*tp,0.105*tp),(4.300*tp,3.085*tp),(4.700*tp,3.085*tp),(4.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.870*tp,1.300*tp),(3.870*tp,1.700*tp),(4.345*tp,1.700*tp),(4.345*tp,1.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.660*tp,6.300*tp),(0.660*tp,6.700*tp),(1.130*tp,6.700*tp),(1.130*tp,6.300*tp)])
        return elems 

class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(1.720*tp,4.720*tp),(1.720*tp,4.960*tp),(1.875*tp,4.960*tp),(1.875*tp,4.875*tp),(1.960*tp,4.875*tp),(1.960*tp,4.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape = spira.Shape(points=[(2.040*tp,4.720*tp),(2.040*tp,4.875*tp),(2.125*tp,4.875*tp),(2.125*tp,4.960*tp),(2.280*tp,4.960*tp),(2.280*tp,4.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape = spira.Shape(points=[(1.040*tp,3.720*tp),(1.040*tp,3.875*tp),(1.125*tp,3.875*tp),(1.125*tp,3.960*tp),(1.280*tp,3.960*tp),(1.280*tp,3.720*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        shape = spira.Shape(points=[(1.125*tp,4.040*tp),(1.125*tp,4.125*tp),(1.040*tp,4.125*tp),(1.040*tp,4.280*tp),(1.280*tp,4.280*tp),(1.280*tp,4.040*tp)])
        elems += spira.Polygon(shape=shape,layer=ls.M0)
        elems += spira.Polygon(shape=shape,layer=ls.M4)
        elems += spira.Polygon(shape=shape,layer=ls.M7)
        return elems

class M6M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=2.980*tp,center=(0.500*tp,5.405*tp))
        elems += spira.Box(layer=ls.M5,width=0.520*tp,height=0.400*tp,center=(0.870*tp,4.500*tp))
        elems += spira.Box(layer=ls.M5,width=0.490*tp,height=0.400*tp,center=(0.885*tp,5.500*tp))
        elems += spira.Box(layer=ls.M5,width=0.400*tp,height=2.980*tp,center=(4.500*tp,1.595*tp))
        elems += spira.Box(layer=ls.M5,width=0.475*tp,height=0.400*tp,center=(4.1075*tp,1.500*tp))
        elems += spira.Box(layer=ls.M5,width=0.470*tp,height=0.400*tp,center=(0.895*tp,6.500*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.160*tp,center=(4.500*tp,6.150*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.000*tp,height=0.160*tp,center=(1.500*tp,0.850*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(0.395*tp,2.150*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.060*tp,center=(2.640*tp,1.7425*tp))
        elems += spira.Box(layer=IXPORT,width=0.045*tp,height=0.050*tp,center=(3.655*tp,2.9925*tp))
        elems += spira.Box(layer=IXPORT,width=0.055*tp,height=0.055*tp,center=(2.4575*tp,2.6375*tp))
        elems += spira.Box(layer=IXPORT,width=0.060*tp,height=0.050*tp,center=(2.845*tp,6.405*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(3.645*tp,6.635*tp))
        elems += spira.Box(layer=IXPORT,width=0.050*tp,height=0.050*tp,center=(3.760*tp,3.500*tp))
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(4.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.515*tp,4.630*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,0.305*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,0.735*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,1.165*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,1.595*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,2.025*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,2.455*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,2.885*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.070*tp,1.500*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.080*tp,2.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.695*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.265*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.835*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.405*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,4.975*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,4.545*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,4.115*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.930*tp,5.500*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,4.945*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(4.500*tp,4.035*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.930*tp,6.500*tp),transformation=ls.r270)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.930*tp,4.500*tp),transformation=ls.r270)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.885*tp,4.300*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.380*tp,4.165*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.265*tp,4.385*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.695*tp,1.030*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.695*tp,1.570*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.160*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.865*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.880*tp,5.320*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.995*tp,4.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.555*tp,4.395*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.460*tp,5.840*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.585*tp,2.305*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.990*tp,0.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.400*tp,4.300*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.705*tp,4.300*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.265*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.860*tp,0.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.140*tp,0.330*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.465*tp,0.655*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.685*tp,2.025*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.440*tp,1.620*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.440*tp,6.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.660*tp,5.415*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.660*tp,5.810*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.660*tp,6.275*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.155*tp,2.565*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.175*tp,1.570*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.660*tp,3.180*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.700*tp,2.910*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.715*tp,3.795*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.170*tp,2.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.145*tp,4.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.440*tp,0.445*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.140*tp,6.540*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.120*tp,3.615*tp),transformation=ls.r270)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(4.735*tp,4.690*tp),transformation=ls.r270)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.585*tp,3.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(0.585*tp,0.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.585*tp,6.585*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(3.585*tp,0.585*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_112(),midpoint=(2.635*tp,0.310*tp))
        elems += spira.SRef(bias.ib_112(),midpoint=(3.700*tp,6.635*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_170(),midpoint=(0.395*tp,1.170*tp))
        elems += spira.SRef(bias.ib_170(),midpoint=(2.895*tp,6.405*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_171(),midpoint=(2.400*tp,2.640*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_175(),midpoint=(3.650*tp,2.040*tp))
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_110_sg(),midpoint=(2.560*tp,5.615*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_110_sg(),midpoint=(0.445*tp,2.490*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_156_s(),midpoint=(1.620*tp,3.445*tp))
        elems += spira.SRef(jj.jj_156_s(),midpoint=(2.560*tp,4.385*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(1.610*tp,1.460*tp))
        elems += spira.SRef(jj.jj_160_sg(),midpoint=(4.500*tp,5.555*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.380*tp,3.440*tp))
        elems += spira.SRef(jj.jj_261_sg(),midpoint=(1.230*tp,3.445*tp))
        elems += spira.SRef(jj.jj_261_sg(),midpoint=(2.560*tp,4.765*tp),transformation=ls.r90)
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(res.res_1p36(),midpoint=(3.705*tp,3.500*tp),transformation=ls.r270,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 5):
                if (x == 1 and y == 0) or (x == 4 and y in [3,6]):
                    pass
                else:
                    elems += spira.SRef(tb.tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(1.000*tp,0.000*tp),alias='A')
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(4.000*tp,3.000*tp),alias='Q')
        elems += spira.SRef(tb.tr_PTLconnection(),midpoint=(4.000*tp,6.000*tp),alias='B')
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