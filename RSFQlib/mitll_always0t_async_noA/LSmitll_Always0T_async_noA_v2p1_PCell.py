import sys
# Change this to the location that contains the subcells.py folder
subcell_path = '..\\subcells'
if subcell_path not in sys.path:
    sys.path.append(subcell_path)
import subcells as sc
import os
import spira.all as spira
from spira.technologies.mit.process.database import RDD

IXPORT = spira.RDD.PLAYER.IXPORT
TEXT = spira.Layer(number=182)

## Parameterization
# Trackpitch in microns
tp = 10
sc.tp = tp

# Inductor widths
Scaling = (1+(tp-10)*0.25)
LA_width = 0.16370967741935485*tp*Scaling
LRA_width = 0.1664473684210526*tp*Scaling
LQ_width = 0.165*tp*Scaling
LRQ_width = 0.1715517241379311*tp*Scaling

class Always0T_noA(spira.PCell):
    __name_prefix__ = "LSmitll_Always0T_async_v2p1_noA"
    def create_elements(self, elems):
        jfill = spira.SRef(junction_fill())
        vias = spira.SRef(M4M5M6M7_connections())
        res = spira.SRef(resistors())
        tblocks = spira.SRef(trackblocks())
        elems += [jfill, vias, res, tblocks]
        sys.stdout.write("Adding inductors.\n")
        pptl_out = spira.Port(name='PPTL_OUT',midpoint=tblocks.ports.north_ports[29].midpoint,process=spira.RDD.PROCESS.M6)
        pres_out_north = spira.Port(name='PRES_OUT_NORTH',midpoint=res.ports[4].midpoint,process=spira.RDD.PROCESS.M6)
        pres_out_south = spira.Port(name='PRES_OUT_SOUTH',midpoint=res.ports[10].midpoint,process=spira.RDD.PROCESS.M6)
        x = res.ports[4].x
        y = vias.ports.south_ports[8].midpoint.y
        pvia_out = spira.Port(name='PVIA_OUT',midpoint=(x,y),process=spira.RDD.PROCESS.M6)
        LQ = spira.Route90(port1=pptl_out,port2=pres_out_south,layer=sc.M6,width=LQ_width)
        LRQ = spira.Route90(port1=pres_out_north,port2=pvia_out,layer=sc.M6,width=LRQ_width)
        elems += [LQ, LRQ]
        sys.stdout.write("Adding labels.\n")
        elems += spira.Label(text="q",position=(0.5*tp,0.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='GND',position=(0.4875*tp,6.8575*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='RQ',position=(0.5025*tp,1.6121*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='q',position=(0.505*tp,0.505*tp),layer=spira.Layer(number=60,datatype=1))
        sys.stdout.write("Constructing layout.\n")
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding 3um junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,3.31*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,4.2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5.835*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.32*tp,2.745*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.32*tp,2.375*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.32*tp,1.42*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.68*tp,3.855*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.68*tp,4.67*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.68*tp,5.505*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.68*tp,6.3625*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.68*tp,6.75*tp),transformation=sc.r180)
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        sys.stdout.write("Adding resistors.\n")
        elems += spira.SRef(sc.ls_res_2(),midpoint=(0.5*tp,0.9425*tp))
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            if y == 0:
                elems += spira.SRef(sc.ls_tr_PTLconnection(),midpoint=(0.0,0+y*tp))
            else:
                elems += spira.SRef(sc.ls_tr_u_M4(),midpoint=(0.0,0+y*tp))
                elems += spira.SRef(sc.ls_tr_M7(),midpoint=(0.0,0+y*tp))
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

D = Always0T_noA()
sys.stdout.write("Writing output.\n")
D.gdsii_output('./LSmitll_Always0T_async_v2p1_noA_PCell')