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
    __name_prefix__ = "THmitll_NOT_v3p0"
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
        elems += spira.Label(text='J3 M5 M6',position=(2.07*tp,3.445*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J7 M6 M5',position=(2.395*tp,3.42*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(1.63*tp,3.445*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M5 M6',position=(2.095*tp,2.495*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J6 M6 M5',position=(2.47*tp,2.575*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P3 M6 M4',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J8 M6 M5',position=(3.600*tp,3.56*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(3.500*tp,3.900*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.500*tp,4.100*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.365*tp,3.565*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(2.06*tp,0.43*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J5 M6 M5',position=(2.44*tp,0.39*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(1.365*tp,4.100*tp),layer=spira.Layer(number=182,datatype=0))

        
        # LVS Labels
        elems += spira.Label(text='q',position=(4.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='clk',position=(2.500*tp,0.000*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='VDD',position=(3.955*tp,6.500*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(3.955*tp,6.32*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RB3',position=(2.07*tp,3.85*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB7',position=(2.385*tp,3.795*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(1.625*tp,3.865*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB6',position=(2.81*tp,2.575*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(1.795*tp,2.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB8',position=(3.605*tp,3.265*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(3.500*tp,4.355*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB1',position=(0.385*tp,3.265*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.500*tp,4.575*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB5',position=(2.735*tp,0.39*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(1.605*tp,0.435*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(1.375*tp,4.635*tp),layer=spira.Layer(number=52,datatype=11))
        return elems
        
class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(2.380*tp,2.010*tp),(2.480*tp,2.110*tp),(2.480*tp,2.010*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.100*tp,3.600*tp),(0.150*tp,3.650*tp),(0.150*tp,3.600*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.400*tp,0.100*tp),(2.350*tp,0.150*tp),(2.400*tp,0.150*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.600*tp,0.100*tp),(2.600*tp,0.150*tp),(2.650*tp,0.150*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.150*tp,3.350*tp),(0.100*tp,3.400*tp),(0.150*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.140*tp,3.320*tp),(2.140*tp,3.630*tp),(2.305*tp,3.630*tp),(2.305*tp,3.320*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.285*tp,3.315*tp),(3.285*tp,3.585*tp),(3.175*tp,3.585*tp),(3.175*tp,3.335*tp),(2.885*tp,3.335*tp),(2.885*tp,3.455*tp),(2.460*tp,3.455*tp),(2.460*tp,3.545*tp),(2.975*tp,3.545*tp),(2.975*tp,3.425*tp),(3.085*tp,3.425*tp),(3.085*tp,3.675*tp),(3.375*tp,3.675*tp),(3.375*tp,3.405*tp),(3.500*tp,3.405*tp),(3.500*tp,3.315*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.480*tp,2.010*tp),(2.480*tp,2.500*tp),(2.620*tp,2.500*tp),(2.620*tp,2.010*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.505*tp,3.3625*tp),(0.505*tp,3.4775*tp),(1.550*tp,3.4775*tp),(1.550*tp,3.3625*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.285*tp,3.560*tp),(1.285*tp,4.175*tp),(1.425*tp,4.175*tp),(1.425*tp,3.560*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.210*tp,2.365*tp),(2.210*tp,2.675*tp),(2.370*tp,2.675*tp),(2.370*tp,2.365*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.285*tp,2.910*tp),(2.285*tp,3.365*tp),(2.685*tp,3.365*tp),(2.685*tp,2.910*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.380*tp,0.505*tp),(2.380*tp,2.010*tp),(2.620*tp,2.010*tp),(2.620*tp,0.505*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.850*tp,3.400*tp),(3.850*tp,3.600*tp),(4.000*tp,3.600*tp),(4.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.150*tp,3.600*tp),(0.150*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.320*tp,3.670*tp),(0.320*tp,4.170*tp),(0.570*tp,4.170*tp),(0.570*tp,4.030*tp),(0.460*tp,4.030*tp),(0.460*tp,3.670*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.570*tp,3.550*tp),(3.570*tp,3.830*tp),(3.430*tp,3.830*tp),(3.430*tp,3.970*tp),(3.710*tp,3.970*tp),(3.710*tp,3.550*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.430*tp,4.920*tp),(0.430*tp,5.355*tp),(0.570*tp,5.355*tp),(0.570*tp,4.920*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.400*tp,5.355*tp),(0.400*tp,6.500*tp),(0.600*tp,6.500*tp),(0.600*tp,5.355*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.700*tp,3.400*tp),(3.700*tp,3.600*tp),(3.850*tp,3.600*tp),(3.850*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.150*tp,3.350*tp),(0.150*tp,3.650*tp),(0.280*tp,3.650*tp),(0.280*tp,3.350*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.400*tp,0.000*tp),(2.400*tp,0.150*tp),(2.600*tp,0.150*tp),(2.600*tp,0.000*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.350*tp,0.150*tp),(2.350*tp,0.310*tp),(2.650*tp,0.310*tp),(2.650*tp,0.150*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.990*tp,0.360*tp),(1.990*tp,0.500*tp),(2.325*tp,0.500*tp),(2.325*tp,0.360*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.710*tp,0.360*tp),(0.710*tp,0.500*tp),(1.230*tp,0.500*tp),(1.230*tp,0.360*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.295*tp,5.220*tp),(1.295*tp,5.285*tp),(0.400*tp,5.285*tp),(0.400*tp,5.425*tp),(1.435*tp,5.425*tp),(1.435*tp,5.220*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(3.400*tp,4.725*tp),(3.400*tp,6.500*tp),(3.600*tp,6.500*tp),(3.600*tp,4.725*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.715*tp,3.335*tp),(1.715*tp,3.665*tp),(1.990*tp,3.665*tp),(1.990*tp,3.335*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.350*tp,2.670*tp),(2.350*tp,3.030*tp),(2.700*tp,3.030*tp),(2.700*tp,2.670*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.255*tp,3.525*tp),(1.255*tp,3.665*tp),(1.535*tp,3.665*tp),(1.535*tp,3.525*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.205*tp,2.410*tp),(1.205*tp,2.7175*tp),(1.2825*tp,2.7175*tp),(1.2825*tp,2.875*tp),(1.605*tp,2.875*tp),(1.605*tp,2.975*tp),(1.300*tp,2.975*tp),(1.300*tp,3.255*tp),(1.525*tp,3.255*tp),(1.525*tp,3.350*tp),(1.615*tp,3.350*tp),(1.615*tp,3.165*tp),(1.390*tp,3.165*tp),(1.390*tp,3.065*tp),(1.695*tp,3.065*tp),(1.695*tp,2.785*tp),(1.3725*tp,2.785*tp),(1.3725*tp,2.6275*tp),(1.295*tp,2.6275*tp),(1.295*tp,2.500*tp),(1.500*tp,2.500*tp),(1.500*tp,2.410*tp)])

        return elems
        
class M0M4M7_strips(spira.Cell):
    __name_prefix__ = "M0M4M7_strips"
    def create_elements(self, elems):
        shape = spira.Shape(points=[(2.040*tp,3.720*tp),(2.040*tp,3.875*tp),(2.125*tp,3.875*tp),(2.125*tp,3.960*tp),(2.280*tp,3.960*tp),(2.280*tp,3.720*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        shape = spira.Shape(points=[(2.125*tp,4.040*tp),(2.125*tp,4.125*tp),(2.040*tp,4.125*tp),(2.040*tp,4.280*tp),(2.280*tp,4.280*tp),(2.280*tp,4.040*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=shape)
        elems += spira.Polygon(layer=ls.M4,shape=shape)
        elems += spira.Polygon(layer=ls.M7,shape=shape)
        return elems        

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,5.630*tp),(1.300*tp,6.890*tp),(1.700*tp,6.890*tp),(1.700*tp,5.630*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(3.300*tp,0.105*tp),(3.300*tp,2.225*tp),(3.700*tp,2.225*tp),(3.700*tp,0.105*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,0.845*tp),(0.300*tp,2.535*tp),(0.700*tp,2.535*tp),(0.700*tp,0.845*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(1.300*tp,0.870*tp),(1.300*tp,1.335*tp),(1.700*tp,1.335*tp),(1.700*tp,0.870*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.635*tp,1.300*tp),(0.635*tp,1.700*tp),(1.980*tp,1.700*tp),(1.980*tp,1.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.300*tp,4.770*tp),(2.300*tp,6.890*tp),(2.700*tp,6.890*tp),(2.700*tp,4.770*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(4.000*tp,6.650*tp),(4.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.350*tp,0.500*tp),(0.350*tp,6.500*tp),(0.650*tp,6.500*tp),(0.650*tp,0.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(3.125*tp,6.000*tp),(3.125*tp,6.040*tp),(3.875*tp,6.040*tp),(3.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,6.000*tp),(1.125*tp,6.040*tp),(1.875*tp,6.040*tp),(1.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,5.125*tp),(0.960*tp,5.875*tp),(1.000*tp,5.875*tp),(1.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,4.125*tp),(0.960*tp,4.875*tp),(1.000*tp,4.875*tp),(1.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,3.125*tp),(0.960*tp,3.875*tp),(1.000*tp,3.875*tp),(1.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,2.125*tp),(0.960*tp,2.875*tp),(1.000*tp,2.875*tp),(1.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,1.125*tp),(0.960*tp,1.875*tp),(1.000*tp,1.875*tp),(1.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.960*tp,0.125*tp),(0.960*tp,0.875*tp),(1.000*tp,0.875*tp),(1.000*tp,0.125*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(3.995*tp,3.450*tp),(3.995*tp,3.550*tp),(4.005*tp,3.550*tp),(4.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.450*tp,-0.005*tp),(2.450*tp,0.005*tp),(2.550*tp,0.005*tp),(2.550*tp,-0.005*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(3.475*tp,3.870*tp),(3.475*tp,3.925*tp),(3.530*tp,3.925*tp),(3.530*tp,3.870*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.470*tp,4.070*tp),(0.470*tp,4.125*tp),(0.525*tp,4.125*tp),(0.525*tp,4.070*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.030*tp,0.405*tp),(2.030*tp,0.455*tp),(2.085*tp,0.455*tp),(2.085*tp,0.405*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(1.335*tp,4.075*tp),(1.335*tp,4.130*tp),(1.390*tp,4.130*tp),(1.390*tp,4.075*tp)])

        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(3.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,0.305*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,0.735*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,1.165*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,1.595*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(3.500*tp,2.025*tp))
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,1.07*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.000*tp,6.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.000*tp,5.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.045*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.475*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,1.905*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,2.335*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,5.83*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.26*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.500*tp,6.69*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.925*tp,1.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.69*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.26*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,5.83*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,5.400*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,4.97*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.78*tp,1.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.35*tp,1.500*tp),transformation=ls.r180)

        return elems
        
class M5M6_connections(spira.Cell):
    __name_prefix__ = "M0M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(1.425*tp,3.715*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M5M6(),midpoint=(2.415*tp,3.03*tp),transformation=ls.r270)

        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.375*tp,2.09*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.96*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.96*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.88*tp,5.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.26*tp,5.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.695*tp,4.63*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.685*tp,5.17*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.855*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.185*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.175*tp,1.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.26*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.07*tp,6.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.07*tp,6.325*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.88*tp,4.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.255*tp,4.33*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.885*tp,1.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.24*tp,1.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.88*tp,2.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.975*tp,2.355*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.66*tp,4.59*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.66*tp,0.27*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.665*tp,0.755*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.645*tp,1.96*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.66*tp,2.805*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.615*tp,2.82*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(3.61*tp,2.500*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.12*tp,5.700*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.165*tp,4.55*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_131(),midpoint=(1.365*tp,5.34*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(3.500*tp,4.85*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(0.500*tp,5.05*tp),transformation=ls.r180)
        elems += spira.SRef(bias.ib_175(),midpoint=(1.105*tp,0.43*tp),transformation=ls.r270)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_078_s(),midpoint=(1.63*tp,3.445*tp))
        elems += spira.SRef(jj.jj_085_s(),midpoint=(2.06*tp,3.415*tp))
        elems += spira.SRef(jj.jj_101_sg(),midpoint=(2.385*tp,3.42*tp))
        elems += spira.SRef(jj.jj_142_s(),midpoint=(2.47*tp,2.57*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(3.600*tp,3.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.39*tp,3.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.44*tp,0.405*tp),transformation=ls.r270)
        elems += spira.SRef(jj.jj_269_s(),midpoint=(2.09*tp,2.495*tp),transformation=ls.r90)
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
                elif ((x in [1,2] and y == 6) or (x == 0 and y in range(1, 6))):
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