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
LCLK_width = 0.16159090909090912*tp*Scaling
LRCLK_width = 0.1715517241379311*tp*Scaling
LA_width = 0.16370967741935485*tp*Scaling
LRA_width = 0.1664473684210526*tp*Scaling
LQ_width = 0.165*tp*Scaling
LRQ_width = 0.1715517241379311*tp*Scaling

class Always0T(spira.PCell):
    __name_prefix__ = "LSmitll_Always0T_sync_v2p1"
    def create_elements(self, elems):
        jfill = spira.SRef(junction_fill())
        vias = spira.SRef(M4M5M6M7_connections())
        res = spira.SRef(resistors())
        tblocks = spira.SRef(trackblocks())
        elems += [jfill, vias, res, tblocks]
        sys.stdout.write("Adding inductors.\n")
        pptl_clk = spira.Port(name='PPTL_CLK',midpoint=tblocks.ports.south_ports[221].midpoint,process=spira.RDD.PROCESS.M6)
        pptl_in = spira.Port(name='PPTL_IN',midpoint=tblocks.ports.south_ports[125].midpoint,process=spira.RDD.PROCESS.M6)
        pptl_out = spira.Port(name='PPTL_OUT',midpoint=tblocks.ports.north_ports[29].midpoint,process=spira.RDD.PROCESS.M6)
        pres_clk_north = spira.Port(name='PRES_CLK_NORTH',midpoint=res.ports[34].midpoint,process=spira.RDD.PROCESS.M6)
        pres_clk_south = spira.Port(name='PRES_CLK_SOUTH',midpoint=res.ports[28].midpoint,process=spira.RDD.PROCESS.M6)
        pres_in_north = spira.Port(name='PRES_IN_NORTH',midpoint=res.ports[22].midpoint,process=spira.RDD.PROCESS.M6)
        pres_in_south = spira.Port(name='PRES_IN_SOUTH',midpoint=res.ports[16].midpoint,process=spira.RDD.PROCESS.M6)
        pres_out_north = spira.Port(name='PRES_OUT_NORTH',midpoint=res.ports[4].midpoint,process=spira.RDD.PROCESS.M6)
        pres_out_south = spira.Port(name='PRES_OUT_SOUTH',midpoint=res.ports[10].midpoint,process=spira.RDD.PROCESS.M6)
        x = res.ports[4].x
        y = vias.ports.north_ports[14].midpoint.y
        pvia_clk = spira.Port(name='PVIA_CLK',midpoint=(x,y),process=spira.RDD.PROCESS.M6)
        y = vias.ports.north_ports[2].midpoint.y
        pvia_in = spira.Port(name='PVIA_IN',midpoint=(x,y),process=spira.RDD.PROCESS.M6)
        y = vias.ports.south_ports[4].midpoint.y
        pvia_out = spira.Port(name='PVIA_OUT',midpoint=(x,y),process=spira.RDD.PROCESS.M6)
        LCLK = spira.Route90(port1=pptl_clk,port2=pres_clk_north,layer=sc.M6,width=LCLK_width)
        LRCLK = spira.Route90(port1=pres_clk_south,port2=pvia_clk,layer=sc.M6,width=LRCLK_width)
        LA = spira.Route90(port1=pptl_in,port2=pres_in_north,layer=sc.M6,width=LA_width)
        LRA = spira.Route90(port1=pres_in_south,port2=pvia_in,layer=sc.M6,width=LRA_width)
        LQ = spira.Route90(port1=pptl_out,port2=pres_out_south,layer=sc.M6,width=LQ_width)
        LRQ = spira.Route90(port1=pres_out_north,port2=pvia_out,layer=sc.M6,width=LRQ_width)
        elems += [LCLK, LRCLK, LA, LRA, LQ, LRQ]
        sys.stdout.write("Adding labels.\n")
        elems += spira.Label(text="clk",position=(0.5*tp,6.5*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(0.5*tp,3.5*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(0.5*tp,0.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='RCLK',position=(0.5*tp,5.5894*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RQ',position=(0.4975*tp,1.3982*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RA',position=(0.5*tp,2.6287*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='GND',position=(0.4975*tp,6.89*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='a',position=(0.505*tp,3.5025*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q',position=(0.505*tp,0.495*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='clk',position=(0.51*tp,6.5075*tp),layer=spira.Layer(number=60,datatype=1))
        sys.stdout.write("Constructing layout.\n")
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding 3um junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,4.2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(0.5*tp,5*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.32*tp,2.375*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.32*tp,1.42*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.68*tp,4.67*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.68*tp,5.5175*tp),transformation=sc.r180)

        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        sys.stdout.write("Adding resistors.\n")
        elems += spira.SRef(sc.ls_res_2(),midpoint=(0.5*tp,0.9425*tp))
        elems += spira.SRef(sc.ls_res_2(),midpoint=(0.5*tp,3.0375*tp),transformation=sc.r180)
        elems += spira.SRef(sc.ls_res_2(),midpoint=(0.5*tp,5.995*tp),transformation=sc.r180)
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            if y == 0 or y == 3 or y == 6:
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

D = Always0T()
sys.stdout.write("Writing output.\n")
D.gdsii_output('./LSmitll_Always0T_sync_v2p1_PCell')