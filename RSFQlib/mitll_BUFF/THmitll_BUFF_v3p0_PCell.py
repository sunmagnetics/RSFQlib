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
    __name_prefix__ = "THmitll_BUFF_v3p0"
    def create_elements(self, elems):
        M0M5Strips = spira.SRef(M0M5_strips())
        IXports = spira.SRef(IX_ports())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        ib = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        ind = spira.SRef(inductors())
        tblocks = spira.SRef(trackblocks())
        elems += [M0M5Strips, IXports, jjfill, M4M5M6M7conns, ib, jjs, ind, tblocks]
        
        # Text Labels
        elems += spira.Label(text='P1 M6 M4',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='P2 M6 M4',position=(3.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='q',position=(3.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J1 M6 M5',position=(0.700*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J2 M6 M5',position=(0.62*tp,2.56*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J3 M6 M5',position=(2.38*tp,2.565*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='J4 M6 M5',position=(2.300*tp,3.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB1 M6 M4',position=(0.295*tp,4.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB4 M6 M4',position=(2.705*tp,4.500*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB3 M6 M4',position=(2.575*tp,1.505*tp),layer=spira.Layer(number=182,datatype=0))
        elems += spira.Label(text='PB2 M6 M4',position=(0.43*tp,1.51*tp),layer=spira.Layer(number=182,datatype=0))
        
        # LVS Labels
        elems += spira.Label(text='VDD',position=(2.91*tp,6.495*tp),layer=spira.Layer(number=1,datatype=0))
        elems += spira.Label(text='GND',position=(2.925*tp,6.315*tp),layer=spira.Layer(number=40,datatype=0))
        elems += spira.Label(text='RB1',position=(0.985*tp,3.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB2',position=(0.615*tp,2.265*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB3',position=(2.385*tp,2.265*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RB4',position=(2.015*tp,3.495*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB1',position=(0.79*tp,4.51*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB4',position=(2.255*tp,4.500*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB2',position=(0.785*tp,1.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='RIB3',position=(2.23*tp,1.505*tp),layer=spira.Layer(number=52,datatype=11))
        elems += spira.Label(text='a',position=(0.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        elems += spira.Label(text='q',position=(3.000*tp,3.500*tp),layer=spira.Layer(number=60,datatype=5))
        return elems

class inductors(spira.Cell):
    __name_prefix__ = "inductors"
    def create_elements(self, elems):  
        elems += spira.Polygon(layer=ls.M6,shape=[(0.150*tp,3.500*tp),(0.150*tp,3.600*tp),(0.250*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.750*tp,3.500*tp),(2.850*tp,3.600*tp),(2.850*tp,3.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.4925*tp,2.675*tp),(0.4925*tp,2.705*tp),(0.345*tp,2.705*tp),(0.345*tp,2.975*tp),(0.605*tp,2.975*tp),(0.605*tp,3.065*tp),(0.285*tp,3.065*tp),(0.285*tp,3.325*tp),(0.5725*tp,3.325*tp),(0.5725*tp,3.385*tp),(0.6625*tp,3.385*tp),(0.6625*tp,3.235*tp),(0.375*tp,3.235*tp),(0.375*tp,3.155*tp),(0.695*tp,3.155*tp),(0.695*tp,2.885*tp),(0.435*tp,2.885*tp),(0.435*tp,2.795*tp),(0.5825*tp,2.795*tp),(0.5825*tp,2.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.4175*tp,2.675*tp),(2.4175*tp,2.795*tp),(2.565*tp,2.795*tp),(2.565*tp,2.885*tp),(2.305*tp,2.885*tp),(2.305*tp,3.155*tp),(2.625*tp,3.155*tp),(2.625*tp,3.235*tp),(2.3375*tp,3.235*tp),(2.3375*tp,3.385*tp),(2.4275*tp,3.385*tp),(2.4275*tp,3.325*tp),(2.715*tp,3.325*tp),(2.715*tp,3.065*tp),(2.395*tp,3.065*tp),(2.395*tp,2.975*tp),(2.655*tp,2.975*tp),(2.655*tp,2.705*tp),(2.5075*tp,2.705*tp),(2.5075*tp,2.675*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.740*tp,2.360*tp),(0.740*tp,2.460*tp),(2.260*tp,2.460*tp),(2.260*tp,2.360*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.035*tp,1.435*tp),(1.035*tp,1.575*tp),(1.300*tp,1.575*tp),(1.300*tp,1.435*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.700*tp,1.435*tp),(1.700*tp,1.575*tp),(1.970*tp,1.575*tp),(1.970*tp,1.435*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.400*tp,4.500*tp),(1.400*tp,6.500*tp),(1.600*tp,6.500*tp),(1.600*tp,4.500*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(1.130*tp,4.430*tp),(1.130*tp,4.570*tp),(1.870*tp,4.570*tp),(1.870*tp,4.430*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.000*tp,3.400*tp),(0.000*tp,3.600*tp),(0.150*tp,3.600*tp),(0.150*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.150*tp,3.400*tp),(0.150*tp,3.500*tp),(0.320*tp,3.500*tp),(0.320*tp,3.6275*tp),(0.580*tp,3.6275*tp),(0.580*tp,3.5275*tp),(0.420*tp,3.5275*tp),(0.420*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.580*tp,3.400*tp),(2.580*tp,3.5275*tp),(2.420*tp,3.5275*tp),(2.420*tp,3.6275*tp),(2.680*tp,3.6275*tp),(2.680*tp,3.500*tp),(2.850*tp,3.500*tp),(2.850*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.850*tp,3.400*tp),(2.850*tp,3.600*tp),(3.000*tp,3.600*tp),(3.000*tp,3.400*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.590*tp,3.615*tp),(0.590*tp,4.440*tp),(0.225*tp,4.440*tp),(0.225*tp,4.560*tp),(0.710*tp,4.560*tp),(0.710*tp,3.615*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.290*tp,3.615*tp),(2.290*tp,4.560*tp),(2.775*tp,4.560*tp),(2.775*tp,4.440*tp),(2.410*tp,4.440*tp),(2.410*tp,3.615*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(0.370*tp,1.435*tp),(0.370*tp,1.640*tp),(0.305*tp,1.640*tp),(0.305*tp,2.4275*tp),(0.505*tp,2.4275*tp),(0.505*tp,2.3075*tp),(0.425*tp,2.3075*tp),(0.425*tp,1.760*tp),(0.490*tp,1.760*tp),(0.490*tp,1.435*tp)])
        elems += spira.Polygon(layer=ls.M6,shape=[(2.515*tp,1.435*tp),(2.515*tp,1.760*tp),(2.580*tp,1.760*tp),(2.580*tp,2.3075*tp),(2.500*tp,2.3075*tp),(2.500*tp,2.4275*tp),(2.700*tp,2.4275*tp),(2.700*tp,1.640*tp),(2.635*tp,1.640*tp),(2.635*tp,1.435*tp)])

        return elems

class M0M5_strips(spira.Cell):
    __name_prefix__ = "M6M5_strips"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=ls.M0,shape=[(0.000*tp,6.350*tp),(0.000*tp,6.650*tp),(3.000*tp,6.650*tp),(3.000*tp,6.350*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.350*tp,1.500*tp),(1.350*tp,6.500*tp),(1.650*tp,6.500*tp),(1.650*tp,1.500*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(0.125*tp,6.000*tp),(0.125*tp,6.040*tp),(0.875*tp,6.040*tp),(0.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(2.125*tp,6.000*tp),(2.125*tp,6.040*tp),(2.875*tp,6.040*tp),(2.875*tp,6.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,2.125*tp),(1.960*tp,2.875*tp),(2.000*tp,2.875*tp),(2.000*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.125*tp,1.000*tp),(1.125*tp,1.040*tp),(1.875*tp,1.040*tp),(1.875*tp,1.000*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,1.125*tp),(1.960*tp,1.875*tp),(2.000*tp,1.875*tp),(2.000*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,3.125*tp),(1.960*tp,3.875*tp),(2.000*tp,3.875*tp),(2.000*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,4.125*tp),(1.960*tp,4.875*tp),(2.000*tp,4.875*tp),(2.000*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.960*tp,5.125*tp),(1.960*tp,5.875*tp),(2.000*tp,5.875*tp),(2.000*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,5.125*tp),(1.000*tp,5.875*tp),(1.040*tp,5.875*tp),(1.040*tp,5.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,4.125*tp),(1.000*tp,4.875*tp),(1.040*tp,4.875*tp),(1.040*tp,4.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,3.125*tp),(1.000*tp,3.875*tp),(1.040*tp,3.875*tp),(1.040*tp,3.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,2.125*tp),(1.000*tp,2.875*tp),(1.040*tp,2.875*tp),(1.040*tp,2.125*tp)])
        elems += spira.Polygon(layer=ls.M0,shape=[(1.000*tp,1.125*tp),(1.000*tp,1.875*tp),(1.040*tp,1.875*tp),(1.040*tp,1.125*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.225*tp,0.300*tp),(0.225*tp,0.700*tp),(2.775*tp,0.700*tp),(2.775*tp,0.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.300*tp,5.680*tp),(0.300*tp,6.560*tp),(0.700*tp,6.560*tp),(0.700*tp,5.680*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.300*tp,5.675*tp),(2.300*tp,6.560*tp),(2.700*tp,6.560*tp),(2.700*tp,5.675*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(2.055*tp,5.300*tp),(2.055*tp,5.700*tp),(2.885*tp,5.700*tp),(2.885*tp,5.300*tp)])
        elems += spira.Polygon(layer=ls.M5,shape=[(0.115*tp,5.300*tp),(0.115*tp,5.700*tp),(0.945*tp,5.700*tp),(0.945*tp,5.300*tp)])
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Polygon(layer=IXPORT,shape=[(-0.005*tp,3.450*tp),(-0.005*tp,3.550*tp),(0.005*tp,3.550*tp),(0.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.995*tp,3.450*tp),(2.995*tp,3.550*tp),(3.005*tp,3.550*tp),(3.005*tp,3.450*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.270*tp,4.470*tp),(0.270*tp,4.525*tp),(0.330*tp,4.525*tp),(0.330*tp,4.470*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(0.405*tp,1.480*tp),(0.405*tp,1.530*tp),(0.455*tp,1.530*tp),(0.455*tp,1.480*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.550*tp,1.480*tp),(2.550*tp,1.530*tp),(2.600*tp,1.530*tp),(2.600*tp,1.480*tp)])
        elems += spira.Polygon(layer=IXPORT,shape=[(2.675*tp,4.475*tp),(2.675*tp,4.525*tp),(2.735*tp,4.525*tp),(2.735*tp,4.475*tp)])
       
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.685*tp,5.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.255*tp,5.500*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,5.93*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.500*tp,6.36*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,5.93*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.500*tp,6.36*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.745*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.315*tp,5.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.575*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(2.145*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.715*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(1.285*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.855*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_3umx3um(),midpoint=(0.425*tp,0.500*tp),transformation=ls.r180)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,6.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,5.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,4.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,3.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,2.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(2.000*tp,1.000*tp),transformation=ls.r90)
        elems += spira.SRef(fill.FakeJJ_1p5x1p5um(),midpoint=(1.000*tp,1.000*tp),transformation=ls.r90)
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.335*tp,2.715*tp))
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.445*tp,3.845*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.885*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.245*tp,5.335*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.08*tp,6.345*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.04*tp,6.34*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.69*tp,3.835*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.57*tp,0.805*tp),transformation=ls.r90)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.66*tp,5.175*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.665*tp,0.97*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.67*tp,1.265*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.66*tp,1.26*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.665*tp,6.855*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.66*tp,6.84*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.66*tp,0.965*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.66*tp,3.185*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.665*tp,3.92*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(1.67*tp,4.26*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(2.66*tp,4.875*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.66*tp,4.87*tp),transformation=ls.r180)
        elems += spira.SRef(conns.conn_M4M5M6M7(),midpoint=(0.665*tp,5.17*tp),transformation=ls.r180)
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(bias.ib_175(),midpoint=(0.245*tp,4.500*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_175(),midpoint=(1.75*tp,4.500*tp),transformation=ls.r270)
        elems += spira.SRef(bias.ib_237p5(),midpoint=(1.16*tp,1.505*tp),transformation=ls.r90)
        elems += spira.SRef(bias.ib_237p5(),midpoint=(2.63*tp,1.505*tp),transformation=ls.r90)
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.300*tp,3.500*tp),transformation=ls.r90)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.62*tp,2.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(2.38*tp,2.56*tp),transformation=ls.r180)
        elems += spira.SRef(jj.jj_250_sg(),midpoint=(0.700*tp,3.500*tp),transformation=ls.r270)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 3):
                if ((x in [0,2] and y == 6) or (x == 1 and y in [2,3,4,5])):
                    elems += spira.SRef(tb.tr_u_M4_alt(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(tb.tr_M7(),midpoint=(0+x*tp,0+y*tp))
                elif (x == 1 and y in [1, 6]):
                    elems += spira.SRef(tb.tr_bias_pillar_M0M6(),midpoint=(0+x*tp,0+y*tp))
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