import layer_setup as ls
import connectors as conns
import spira.all as spira
from spira.technologies.mit.process.database import RDD

# JJ 63uA shunted cell
class jj_063_s(spira.Cell):
    __name_prefix__ = 'jj_063_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,8.5625))
        elems += spira.Box(layer=ls.M6,width=1.700,height=2.925,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,7.810))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.430))
        elems += spira.Box(layer=ls.R5,width=1.150,height=7.450,center=(0.000,4.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=7.925,center=(0.000,6.1375))
        elems += spira.Box(layer=ls.M5,width=2.000,height=3.175,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,9.225))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.660, 0.660))
        elems += spira.Circle(layer=ls.J5,box_size=(0.950, 0.950))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 72uA shunted and grounded cell
class jj_072_sg(spira.Cell):
    __name_prefix__ = 'jj_072_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,8.200))
        elems += spira.Box(layer=ls.M6,width=1.750,height=3.000,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.8875))
        elems += spira.Box(layer=ls.M5,width=2.050,height=3.250,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=7.200,center=(0.000,5.825))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.550))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.490))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,7.130))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.725,center=(0.000,4.3125))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.500))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.700, 0.700))
        elems += spira.Circle(layer=ls.J5,box_size=(1.100, 1.100))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 72uA shunted cell
class jj_072_s(spira.Cell):
    __name_prefix__ = 'jj_072_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=7.200,center=(0.000,5.825))
        elems += spira.Box(layer=ls.M5,width=2.050,height=3.250,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.010, 1.010))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.6725,center=(0.000,4.3125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.550))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.720, 0.720))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.490))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,7.130))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.8875))
        elems += spira.Box(layer=ls.M6,width=1.750,height=3.000,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports          
        
# JJ 73uA shunted cell
class jj_073_s(spira.Cell):
    __name_prefix__ = 'jj_073_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=7.125,center=(0.000,5.7625))
        elems += spira.Box(layer=ls.M5,width=2.050,height=3.225,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.020, 1.020))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.650,center=(0.000,4.250))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.450))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.720, 0.720))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.470))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,7.040))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.7875))
        elems += spira.Box(layer=ls.M6,width=1.750,height=2.975,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 74uA shunted cell
class jj_074_s(spira.Cell):
    __name_prefix__ = 'jj_074_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=7.050,center=(0.000,5.750))
        elems += spira.Box(layer=ls.M5,width=2.050,height=3.250,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.020, 1.020))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.575,center=(0.000,4.2375))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.400))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.720, 0.720))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.500))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,7.000))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,7.750))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.000,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 75uA shunted and grounded cell
class jj_075_sg(spira.Cell):
    __name_prefix__ = 'jj_075_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.975))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.6625))
        elems += spira.Box(layer=ls.M6,width=1.800,height=3.000,center=(0.000,0.600))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.910))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.470))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.500,center=(0.000,4.200))
        elems += spira.Box(layer=ls.M5,width=1.750,height=7.000,center=(0.000,5.700))
        elems += spira.Box(layer=ls.M5,width=2.100,height=3.250,center=(0.000,0.575))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.325))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.525))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.720, 0.720))
        elems += spira.Circle(layer=ls.J5,box_size=(1.030, 1.030))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 77uA shunted cell
class jj_077_s(spira.Cell):
    __name_prefix__ = 'jj_077_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.800,height=3.050,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.5625))
        elems += spira.Box(layer=ls.M5,width=2.100,height=3.300,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.850,center=(0.000,5.675))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.225))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.375,center=(0.000,4.1625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.510))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.810))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.740, 0.740))
        elems += spira.Circle(layer=ls.J5,box_size=(1.040, 1.040))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 77uA shunted and grounded cell
class jj_077_sg(spira.Cell):
    __name_prefix__ = 'jj_077_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.875))
        elems += spira.Box(layer=ls.M6,width=1.800,height=3.050,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.5625))
        elems += spira.Box(layer=ls.M5,width=2.100,height=3.300,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.850,center=(0.000,5.675))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.225))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.525))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.375,center=(0.000,4.1625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.510))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.810))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.740, 0.740))
        elems += spira.Circle(layer=ls.J5,box_size=(1.040, 1.040))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 78uA shunted cell
class jj_078_s(spira.Cell):
    __name_prefix__ = 'jj_078_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.4875))
        elems += spira.Box(layer=ls.M6,width=1.800,height=3.025,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.730))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.480))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.325,center=(0.000,4.1125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.800,center=(0.000,5.625))
        elems += spira.Box(layer=ls.M5,width=2.100,height=3.275,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.150))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.740, 0.740))
        elems += spira.Circle(layer=ls.J5,box_size=(1.050, 1.050))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 80uA shunted and grounded cell
class jj_080_sg(spira.Cell):
    __name_prefix__ = 'jj_080_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.700))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.050))
        elems += spira.Box(layer=ls.M6,width=1.800,height=3.050,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.3875))
        elems += spira.Box(layer=ls.M5,width=2.100,height=3.300,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.5875,center=(0.000,6.675))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.525))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.200,center=(0.000,4.075))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.510))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.640))
        elems += spira.Circle(layer=ls.J5,box_size=(1.060, 1.060))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.760, 0.760))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 81uA shunted and grounded cell
class jj_081_sg(spira.Cell):
    __name_prefix__ = 'jj_081_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.3125))
        elems += spira.Box(layer=ls.M6,width=1.800,height=3.025,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.560))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.490))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.150,center=(0.000,4.025))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.625,center=(0.000,5.5375))
        elems += spira.Box(layer=ls.M5,width=2.100,height=3.275,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.975))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.525))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.760, 0.760))
        elems += spira.Circle(layer=ls.J5,box_size=(1.070, 1.070))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 82uA shunted and grounded cell
class jj_082_sg(spira.Cell):
    __name_prefix__ = 'jj_082s_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,8.300))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.2875))
        elems += spira.Box(layer=ls.M6,width=1.800,height=3.050,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.540))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.520))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.100,center=(0.000,4.025))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.5750,center=(0.000,5.5375))
        elems += spira.Box(layer=ls.M5,width=2.100,height=3.300,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.950))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.525))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.780, 0.780))
        elems += spira.Circle(layer=ls.J5,box_size=(1.070, 1.070))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 83uA shunted and grounded cell
class jj_083_sg(spira.Cell):
    __name_prefix__ = 'jj_083_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.550))
        elems += spira.Box(layer=ls.M6,width=1.850,height=3.075,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.2375))
        elems += spira.Box(layer=ls.M5,width=2.150,height=3.325,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.525,center=(0.000,5.5125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.520))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.490))
        elems += spira.Box(layer=ls.R5,width=1.150,height=6.025,center=(0.000,4.0125))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.550))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.780, 0.780))
        elems += spira.Circle(layer=ls.J5,box_size=(1.040, 1.040))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 85uA shunted cell
class jj_085_s(spira.Cell):
    __name_prefix__ = 'jj_085_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.1125))
        elems += spira.Box(layer=ls.M6,width=1.850,height=3.075,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.360))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.500))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.925,center=(0.000,3.9375))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.400,center=(0.000,5.450))
        elems += spira.Box(layer=ls.M5,width=2.150,height=3.325,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.775))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.820, 0.820))
        elems += spira.Circle(layer=ls.J5,box_size=(1.090, 1.090))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports         

# JJ 86uA shunted and grounded cell
class jj_086_sg(spira.Cell):
    __name_prefix__ = 'jj_086_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.400))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.0875))
        elems += spira.Box(layer=ls.M6,width=1.850,height=3.100,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.340))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.530))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.875,center=(0.000,3.9375))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.350,center=(0.000,5.450))
        elems += spira.Box(layer=ls.M5,width=2.150,height=3.350,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.750))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.550))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.800, 0.800))
        elems += spira.Circle(layer=ls.J5,box_size=(1.100, 1.100))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 87uA shunted cell
class jj_087_s(spira.Cell):
    __name_prefix__ = 'jj_087_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,7.0375))
        elems += spira.Box(layer=ls.M6,width=1.850,height=3.100,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.290))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.540))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.825,center=(0.000,3.9125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.300,center=(0.000,5.425))
        elems += spira.Box(layer=ls.M5,width=2.150,height=3.350,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.700))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.800, 0.800))
        elems += spira.Circle(layer=ls.J5,box_size=(1.100, 1.100))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 88uA shunted and grounded cell
class jj_088_sg(spira.Cell):
    __name_prefix__ = 'jj_088_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.300))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.775,center=(0.000,3.8625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.220))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.510))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,6.975))
        elems += spira.Box(layer=ls.M6,width=1.850,height=3.075,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.250,center=(0.000,5.375))
        elems += spira.Box(layer=ls.M5,width=2.150,height=3.325,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.550))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.800, 0.800))
        elems += spira.Circle(layer=ls.J5,box_size=(1.110, 1.110))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 89uA shunted and grounded cell
class jj_089_sg(spira.Cell):
    __name_prefix__ = 'jj_089_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.250))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.550))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.225,center=(0.000,5.3625))
        elems += spira.Box(layer=ls.M5,width=2.150,height=3.325,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.600))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.9375))
        elems += spira.Box(layer=ls.M6,width=1.850,height=3.075,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.750,center=(0.000,3.850))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.180))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.520))
        elems += spira.Circle(layer=ls.J5,box_size=(1.110, 1.110))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.824, 0.824))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 90uA shunted cell
class jj_090_s(spira.Cell):
    __name_prefix__ = 'jj_090_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.8875))
        elems += spira.Box(layer=ls.M6,width=1.850,height=3.075,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.140))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.520))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.700,center=(0.000,3.825))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.175,center=(0.000,5.3375))
        elems += spira.Box(layer=ls.M5,width=2.150,height=3.325,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.550))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.820, 0.820))
        elems += spira.Circle(layer=ls.J5,box_size=(1.120, 1.120))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports          

# JJ 90uA shunted and grounded cell
class jj_090_sg(spira.Cell):
    __name_prefix__ = 'jj_090_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.200))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.700,center=(0.000,3.825))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.140))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.520))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.8875))
        elems += spira.Box(layer=ls.M6,width=1.850,height=3.075,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.175,center=(0.000,5.3375))
        elems += spira.Box(layer=ls.M5,width=2.150,height=3.325,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.550))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.550))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.820, 0.820))
        elems += spira.Circle(layer=ls.J5,box_size=(1.120, 1.120))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 92uA shunted and grounded cell
class jj_092_sg(spira.Cell):
    __name_prefix__ = 'jj_092_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.125))
        elems += spira.Box(layer=ls.M6,width=1.900,height=3.100,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.8125))
        elems += spira.Box(layer=ls.M5,width=2.200,height=3.350,center=(0.000,0.575))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.100,center=(0.000,5.300))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.475))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.530))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.050))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.600,center=(0.000,3.800))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.575))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.860, 0.860))
        elems += spira.Circle(layer=ls.J5,box_size=(1.130, 1.130))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 93uA shunted and grounded cell
class jj_093_sg(spira.Cell):
    __name_prefix__ = 'jj_093_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.100))
        elems += spira.Box(layer=ls.M6,width=1.900,height=3.150,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.7875))
        elems += spira.Box(layer=ls.M5,width=2.200,height=3.400,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=6.025,center=(0.000,5.3125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.450))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.550))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,6.040))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.550,center=(0.000,3.800))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.575))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.840, 0.840))
        elems += spira.Circle(layer=ls.J5,box_size=(1.140, 1.140))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 94uA shunted and grounded cell
class jj_094_sg(spira.Cell):
    __name_prefix__ = 'jj_094_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.050))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,6.725))
        elems += spira.Box(layer=ls.M6,width=1.900,height=3.125,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.970))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.530))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.500,center=(0.000,3.750))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.975,center=(0.000,5.2625))
        elems += spira.Box(layer=ls.M5,width=2.200,height=3.375,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.575))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.840, 0.840))
        elems += spira.Circle(layer=ls.J5,box_size=(1.140, 1.140))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 95uA shunted cell
class jj_095_s(spira.Cell):
    __name_prefix__ = 'jj_095_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.475,center=(0.000,3.7375))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.940))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.530))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.6875))
        elems += spira.Box(layer=ls.M6,width=1.900,height=3.125,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.350))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.950,center=(0.000,5.250))
        elems += spira.Box(layer=ls.M5,width=2.200,height=3.375,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.150, 1.150))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.840, 0.840))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 99uA shunted and grounded cell
class jj_099_sg(spira.Cell):
    __name_prefix__ = 'jj_099_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.875))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.5625))
        elems += spira.Box(layer=ls.M6,width=1.900,height=3.150,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.810))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.570))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.325,center=(0.000,3.6875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.800,center=(0.000,5.200))
        elems += spira.Box(layer=ls.M5,width=2.200,height=3.400,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.225))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.575))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.860, 0.860))
        elems += spira.Circle(layer=ls.J5,box_size=(1.170, 1.170))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 100uA shunted and grounded cell
class jj_100_sg(spira.Cell):
    __name_prefix__ = 'jj_100_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.825))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.5125))
        elems += spira.Box(layer=ls.M6,width=1.950,height=3.150,center=(0.000,0.600))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.750))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.550))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.275,center=(0.000,3.6625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.775,center=(0.000,5.1625))
        elems += spira.Box(layer=ls.M5,width=2.250,height=3.400,center=(0.000,0.575))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.175))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.600))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.880, 0.880))
        elems += spira.Circle(layer=ls.J5,box_size=(1.180, 1.180))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 101uA shunted and grounded cell
class jj_101_sg(spira.Cell):
    __name_prefix__ = 'jj_101_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,7.500))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.4875))
        elems += spira.Box(layer=ls.M6,width=1.950,height=3.175,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.740))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.580))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.225,center=(0.000,3.6625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.725,center=(0.000,5.1625))
        elems += spira.Box(layer=ls.M5,width=2.250,height=3.425,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.150))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.600))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.880, 0.880))
        elems += spira.Circle(layer=ls.J5,box_size=(1.180, 1.180))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        
        
# JJ 103uA shunted cell
class jj_103_s(spira.Cell):
    __name_prefix__ = 'jj_103_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.100))
        elems += spira.Box(layer=ls.M6,width=1.950,height=3.200,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.4375))
        elems += spira.Box(layer=ls.M5,width=2.250,height=3.450,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.150,center=(0.000,5.650))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.175,center=(0.000,3.6375))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.580))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.680))
        elems += spira.Circle(layer=ls.J5,box_size=(1.190, 1.190))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.900, 0.900))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 104uA shunted and grounded cell
class jj_104_sg(spira.Cell):
    __name_prefix__ = 'jj_104_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.725))
        elems += spira.Box(layer=ls.M6,width=1.950,height=3.200,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,6.400))
        elems += spira.Box(layer=ls.M5,width=2.250,height=3.450,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.600,center=(0.000,5.125))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.125,center=(0.000,3.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.580))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.650))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.900, 0.900))
        elems += spira.Circle(layer=ls.J5,box_size=(1.200, 1.200))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports       

# JJ 105uA shunted cell
class jj_105_s(spira.Cell):
    __name_prefix__ = 'jj_105_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,7.000))
        elems += spira.Box(layer=ls.M6,width=1.950,height=3.175,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.3375))
        elems += spira.Box(layer=ls.M5,width=2.250,height=3.425,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.575,center=(0.000,5.0875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.100,center=(0.000,3.5750))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.560))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.590))
        elems += spira.Circle(layer=ls.J5,box_size=(1.200, 1.200))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.900, 0.900))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 107uA shunted cell
class jj_107_s(spira.Cell):
    __name_prefix__ = 'jj_107_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.950))
        elems += spira.Box(layer=ls.M6,width=1.950,height=3.175,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.2875))
        elems += spira.Box(layer=ls.M5,width=2.250,height=3.425,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.525,center=(0.000,5.0625))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.050,center=(0.000,3.550))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.570))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.530))
        elems += spira.Circle(layer=ls.J5,box_size=(1.210, 1.210))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.920, 0.920))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 108uA shunted cell
class jj_108_s(spira.Cell):
    __name_prefix__ = 'jj_108_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.950))
        elems += spira.Box(layer=ls.M6,width=1.950,height=3.200,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.2875))
        elems += spira.Box(layer=ls.M5,width=2.250,height=3.450,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.500,center=(0.000,5.075))
        elems += spira.Box(layer=ls.R5,width=1.150,height=5.025,center=(0.000,3.5625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.590))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.530))
        elems += spira.Circle(layer=ls.J5,box_size=(1.220, 1.220))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.920, 0.920))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 109uA shunted and grounded cell
class jj_109_sg(spira.Cell):
    __name_prefix__ = 'jj_109_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.550))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.450,center=(0.000,5.025))
        elems += spira.Box(layer=ls.M5,width=2.250,height=3.425,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.220, 1.220))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.975,center=(0.000,3.5125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.000))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.920, 0.920))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.570))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.470))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,6.225))
        elems += spira.Box(layer=ls.M6,width=1.950,height=3.175,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 110uA shunted and grounded cell
class jj_110_sg(spira.Cell):
    __name_prefix__ = 'jj_110_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.525))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.425,center=(0.000,5.0375))
        elems += spira.Box(layer=ls.M5,width=2.300,height=3.475,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.230, 1.230))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.925,center=(0.000,3.5375))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.875))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.940, 0.940))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.600))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.460))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.2125))
        elems += spira.Box(layer=ls.M6,width=2.000,height=3.225,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 113uA shunted cell
class jj_113_s(spira.Cell):
    __name_prefix__ = 'jj_113_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.850,center=(0.000,3.500))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.390))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.610))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.1375))
        elems += spira.Box(layer=ls.M6,width=2.000,height=3.250,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.325,center=(0.000,5.0125))
        elems += spira.Box(layer=ls.M5,width=2.300,height=3.500,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.800))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.940, 0.940))
        elems += spira.Circle(layer=ls.J5,box_size=(1.240, 1.240))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 116uA shunted and grounded cell
class jj_116_sg(spira.Cell):
    __name_prefix__ = 'jj_116_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.350))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.700))
        elems += spira.Box(layer=ls.M6,width=2.000,height=3.225,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.0375))
        elems += spira.Box(layer=ls.M5,width=2.300,height=3.475,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.250,center=(0.000,4.950))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.775,center=(0.000,3.4375))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.590))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.290))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.625))
        elems += spira.Circle(layer=ls.J5,box_size=(1.260, 1.260))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.960, 0.960))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 117uA shunted cell
class jj_117_s(spira.Cell):
    __name_prefix__ = 'jj_117_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.225,center=(0.000,4.9375))
        elems += spira.Box(layer=ls.M5,width=2.300,height=3.475,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.270, 1.270))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.750,center=(0.000,3.425))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.675))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.960, 0.960))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.590))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.260))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.0125))
        elems += spira.Box(layer=ls.M6,width=2.000,height=3.225,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 117uA shunted and grounded cell
class jj_117_sg(spira.Cell):
    __name_prefix__ = 'jj_117_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.325))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.225,center=(0.000,4.9375))
        elems += spira.Box(layer=ls.M5,width=2.300,height=3.475,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.270, 1.270))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.750,center=(0.000,3.425))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.675))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.625))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.960, 0.960))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.590))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.260))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,6.0125))
        elems += spira.Box(layer=ls.M6,width=2.000,height=3.225,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 118uA shunted cell
class jj_118_s(spira.Cell):
    __name_prefix__ = 'jj_118_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.200,center=(0.000,4.925))
        elems += spira.Box(layer=ls.M5,width=2.300,height=3.475,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.270, 1.270))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.725,center=(0.000,3.4125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.650))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.980, 0.980))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.600))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.240))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.9875))
        elems += spira.Box(layer=ls.M6,width=2.000,height=3.225,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 119uA shunted cell
class jj_119_s(spira.Cell):
    __name_prefix__ = 'jj_119_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.175,center=(0.000,4.9375))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.525,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.280, 1.280))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.675,center=(0.000,3.4375))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.650))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.980, 0.980))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.620))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.240))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.9875))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.275,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 121uA shunted and grounded cell
class jj_121_sg(spira.Cell):
    __name_prefix__ = 'jj_121_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.250))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.275,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.9125))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.525,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.100,center=(0.000,4.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.600))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.170))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.625,center=(0.000,3.3875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.650))
        elems += spira.Circle(layer=ls.C5J,box_size=(0.980, 0.980))
        elems += spira.Circle(layer=ls.J5,box_size=(1.290, 1.290))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 122uA shunted cell
class jj_122_s(spira.Cell):
    __name_prefix__ = 'jj_122_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.300,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.925))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.550,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.075,center=(0.000,4.9125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.575))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.650))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.600,center=(0.000,3.400))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.630))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.170))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.000, 1.000))
        elems += spira.Circle(layer=ls.J5,box_size=(1.290, 1.290))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 122uA shunted and grounded cell
class jj_122_sg(spira.Cell):
    __name_prefix__ = 'jj_122_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.250))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.300,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.925))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.550,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.075,center=(0.000,4.9125))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.650))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.600,center=(0.000,3.400))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.630))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.170))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.000, 1.000))
        elems += spira.Circle(layer=ls.J5,box_size=(1.290, 1.290))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 125uA shunted cell
class jj_125_s(spira.Cell):
    __name_prefix__ = 'jj_125_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.025,center=(0.000,4.8875))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.550,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.300, 1.300))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.550,center=(0.000,3.3375))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.525))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.000, 1.000))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.640))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.110))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.8625))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.300,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 125uA shunted and grounded cell
class jj_125_sg(spira.Cell):
    __name_prefix__ = 'jj_125_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.175))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.300,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.8625))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.550,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.025,center=(0.000,4.8875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.525))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.650))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.550,center=(0.000,3.375))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.640))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.110))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.000, 1.000))
        elems += spira.Circle(layer=ls.J5,box_size=(1.310, 1.310))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 126uA shunted cell
class jj_126_s(spira.Cell):
    __name_prefix__ = 'jj_126_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.000,center=(0.000,4.875))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.550,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.310, 1.310))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.525,center=(0.000,3.3625))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.500))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.020, 1.020))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.640))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.090))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.8375))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.300,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 126uA shunted and grounded cell
class jj_126_sg(spira.Cell):
    __name_prefix__ = 'jj_126_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.150))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.525,center=(0.000,3.3625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.090))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.640))
        elems += spira.Box(layer=ls.M5,width=1.750,height=5.000,center=(0.000,4.875))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.550,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.310, 1.310))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.500))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.650))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.020, 1.020))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.8375))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.300,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 127uA shunted and grounded cell
class jj_127_sg(spira.Cell):
    __name_prefix__ = 'jj_127_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.800),transformation=ls.r270)
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.500,center=(0.000,3.325))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.040))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.620))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.975,center=(0.000,4.8375))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.525,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.320, 1.320))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.450))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.650))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.020, 1.020))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.7875))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.275,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        
        
# JJ 128uA shunted and grounded cell
class jj_128_sg(spira.Cell):
    __name_prefix__ = 'jj_128_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.075))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.475,center=(0.000,3.3125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.010))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.620))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.950,center=(0.000,4.825))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.525,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.320, 1.320))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.425))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.650))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.020, 1.020))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.7625))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.275,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports  

# JJ 128uA shunted cell
class jj_128_s(spira.Cell):
    __name_prefix__ = 'jj_128_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.7625))
        elems += spira.Box(layer=ls.M6,width=2.050,height=3.275,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.950,center=(0.000,4.825))
        elems += spira.Box(layer=ls.M5,width=2.350,height=3.525,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.425))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.020))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.620))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.475,center=(0.000,3.3125))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.020, 1.020))
        elems += spira.Circle(layer=ls.J5,box_size=(1.320, 1.320))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 129uA shunted cell
class jj_129_s(spira.Cell):
    __name_prefix__ = 'jj_129_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.775))
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.325,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.925,center=(0.000,4.8375))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.575,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.425))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,5.030))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.650))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.425,center=(0.000,3.3375))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.020, 1.020))
        elems += spira.Circle(layer=ls.J5,box_size=(1.330, 1.330))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 131uA shunted cell
class jj_131_s(spira.Cell):
    __name_prefix__ = 'jj_131_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.7375))
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.350,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.990))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.650))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.400,center=(0.000,3.325))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.875,center=(0.000,4.8375))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.600,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.400))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.040, 1.040))
        elems += spira.Circle(layer=ls.J5,box_size=(1.340, 1.340))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 132uA shunted and grounded cell
class jj_132_sg(spira.Cell):
    __name_prefix__ = 'jj_132_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.000))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.375,center=(0.000,3.2875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.940))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.630))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.6875))
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.325,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.850,center=(0.000,4.800))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.575,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.350))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.675))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.040, 1.040))
        elems += spira.Circle(layer=ls.J5,box_size=(1.340, 1.340))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 134uA shunted cell
class jj_134_s(spira.Cell):
    __name_prefix__ = 'jj_134_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.325))
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.325,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.6625))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.575,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.825,center=(0.000,4.7875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.350,center=(0.000,3.275))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.630))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.910))
        elems += spira.Circle(layer=ls.J5,box_size=(1.350, 1.350))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.040, 1.040))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 135uA shunted cell
class jj_135_s(spira.Cell):
    __name_prefix__ = 'jj_135_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.325,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.6375))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.575,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.800,center=(0.000,4.775))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.300))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.325,center=(0.000,3.2625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.640))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.890))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.060, 1.060))
        elems += spira.Circle(layer=ls.J5,box_size=(1.350, 1.350))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 136uA shunted cell
class jj_136_s(spira.Cell):
    __name_prefix__ = 'jj_136_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.6375))
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.350,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.775,center=(0.000,4.7875))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.600,center=(0.000,0.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.300,center=(0.000,3.275))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.660))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.300))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.060, 1.060))
        elems += spira.Circle(layer=ls.J5,box_size=(1.360, 1.360))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 136uA shunted and grounded cell
class jj_136_sg(spira.Cell):
    __name_prefix__ = 'jj_136_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.650))
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.350,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.6375))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.600,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.775,center=(0.000,4.7875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.300))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.660))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.890))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.300,center=(0.000,3.275))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.675))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.060, 1.060))
        elems += spira.Circle(layer=ls.J5,box_size=(1.360, 1.360))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 137uA shunted and grounded cell
class jj_137_sg(spira.Cell):
    __name_prefix__ = 'jj_137_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.950))
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.350,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.6375))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.600,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.775,center=(0.000,4.7875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.300))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.670))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.880))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.300,center=(0.000,3.275))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.675))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.060, 1.060))
        elems += spira.Circle(layer=ls.J5,box_size=(1.360, 1.360))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 138uA shunted cell
class jj_138_s(spira.Cell):
    __name_prefix__ = 'jj_138_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.750,center=(0.000,4.750))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.575,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.370, 1.370))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.275,center=(0.000,3.2375))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.250))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.060, 1.060))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.640))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.840))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.5875))
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.325,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 139uA shunted cell
class jj_139_s(spira.Cell):
    __name_prefix__ = 'jj_139_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.725,center=(0.000,4.7625))
        elems += spira.Box(layer=ls.M5,width=2.400,height=3.575,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.370, 1.370))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.250,center=(0.000,3.250))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.250))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.080, 1.080))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.670))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.840))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.5875))
        elems += spira.Box(layer=ls.M6,width=2.100,height=3.350,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 140uA shunted and grounded cell
class jj_140_sg(spira.Cell):
    __name_prefix__ = 'jj_140_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.900))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.225,center=(0.000,3.2375))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.800))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.650))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.5625))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.350,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.725,center=(0.000,4.7375))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.600,center=(0.000,0.575))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.700))
        elems += spira.Circle(layer=ls.J5,box_size=(1.380, 1.380))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.080, 1.080))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 141uA shunted and grounded cell
class jj_141_sg(spira.Cell):
    __name_prefix__ = 'jj_141_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.850))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.350,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.5375))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.600,center=(0.000,0.575))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.700,center=(0.000,4.725))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.200))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.700))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.200,center=(0.000,3.225))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.650))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.790))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.080, 1.080))
        elems += spira.Circle(layer=ls.J5,box_size=(1.380, 1.380))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 141uA shunted and grounded cell
class jj_141_s(spira.Cell):
    __name_prefix__ = 'jj_141_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.350,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.5375))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.600,center=(0.000,0.575))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.700,center=(0.000,4.725))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.200))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.200,center=(0.000,3.225))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.650))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.790))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.080, 1.080))
        elems += spira.Circle(layer=ls.J5,box_size=(1.380, 1.380))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports    

# JJ 142uA shunted and grounded cell
class jj_142_s(spira.Cell):
    __name_prefix__ = 'jj_142_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.400,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.5375))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.650,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.650,center=(0.000,4.750))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.200))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.175,center=(0.000,3.2375))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.680))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.800))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.080, 1.080))
        elems += spira.Circle(layer=ls.J5,box_size=(1.390, 1.390))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports           

# JJ 142uA shunted and grounded cell
class jj_142_sg(spira.Cell):
    __name_prefix__ = 'jj_142_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.875))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.400,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.5375))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.650,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.650,center=(0.000,4.750))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.700))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.175,center=(0.000,3.2375))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.680))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.800))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.080, 1.080))
        elems += spira.Circle(layer=ls.J5,box_size=(1.390, 1.390))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 144uA shunted cell
class jj_144_s(spira.Cell):
    __name_prefix__ = 'jj_144_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.150,center=(0.000,3.225))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.760))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.680))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.5125))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.400,center=(0.000,0.625))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.175))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.625,center=(0.000,4.7375))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.650,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.400, 1.400))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.100, 1.100))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 144uA shunted and grounded cell
class jj_144_sg(spira.Cell):
    __name_prefix__ = 'jj_144_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.825))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.400,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.5125))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.650,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.625,center=(0.000,4.7375))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.700))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.150,center=(0.000,3.225))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.680))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.760))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.175))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.100, 1.100))
        elems += spira.Circle(layer=ls.J5,box_size=(1.400, 1.400))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 145uA shunted cell
class jj_145_s(spira.Cell):
    __name_prefix__ = 'jj_145_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.600,center=(0.000,4.700))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.625,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.475))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.375,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.125,center=(0.000,3.1875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.720))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.660))
        elems += spira.Circle(layer=ls.J5,box_size=(1.400, 1.400))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.100, 1.100))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 145uA shunted and grounded cell
class jj_145_sg(spira.Cell):
    __name_prefix__ = 'jj_145_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.775))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.375,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.475))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.625,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.600,center=(0.000,4.700))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.700))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.125,center=(0.000,3.1875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.660))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.710))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.125))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.100, 1.100))
        elems += spira.Circle(layer=ls.J5,box_size=(1.400, 1.400))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports   
        
# JJ 146uA shunted cell
class jj_146_s(spira.Cell):
    __name_prefix__ = 'jj_146_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.600,center=(0.000,4.700))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.625,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.4625))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.375,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.125,center=(0.000,3.1875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.710))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.660))
        elems += spira.Circle(layer=ls.J5,box_size=(1.410, 1.410))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.100, 1.100))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports           

# JJ 147uA shunted cell
class jj_147_s(spira.Cell):
    __name_prefix__ = 'jj_147_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.575,center=(0.000,4.6875))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.625,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.100))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.4375))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.375,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.100,center=(0.000,3.175))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.690))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.670))
        elems += spira.Circle(layer=ls.J5,box_size=(1.410, 1.410))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.140, 1.140))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports      

# JJ 148uA shunted cell
class jj_148_s(spira.Cell):
    __name_prefix__ = 'jj_148_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.575,center=(0.000,4.6875))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.625,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.100))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.4375))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.375,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.100,center=(0.000,3.175))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.680))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.670))
        elems += spira.Circle(layer=ls.J5,box_size=(1.410, 1.410))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.120, 1.120))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports    

# JJ 149uA shunted cell
class jj_149_s(spira.Cell):
    __name_prefix__ = 'jj_149_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.400,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.4375))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.650,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.550,center=(0.000,4.700))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.100))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.690))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.690))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.075,center=(0.000,3.1875))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.120, 1.120))
        elems += spira.Circle(layer=ls.J5,box_size=(1.420, 1.420))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 150uA shunted cell
class jj_150_s(spira.Cell):
    __name_prefix__ = 'jj_150_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.050))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.050,center=(0.000,3.150))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.650))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.670))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.400))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.375,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.525,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.625,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.120, 1.120))
        elems += spira.Circle(layer=ls.J5,box_size=(1.420, 1.420))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 150uA shunted and grounded cell
class jj_150_sg(spira.Cell):
    __name_prefix__ = 'jj_150_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.5725))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.050,center=(0.000,3.150))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.650))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.670))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.400))
        elems += spira.Box(layer=ls.M6,width=2.150,height=3.375,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.525,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M5,width=2.450,height=3.625,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.700))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.120, 1.120))
        elems += spira.Circle(layer=ls.J5,box_size=(1.420, 1.420))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 151uA shunted and grounded cell
class jj_151_sg(spira.Cell):
    __name_prefix__ = 'jj_151_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.725))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.4125))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.425,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.660))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.700))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.025,center=(0.000,3.1875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.525,center=(0.000,4.6875))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.675,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.075))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.725))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.120, 1.120))
        elems += spira.Circle(layer=ls.J5,box_size=(1.430, 1.430))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 152uA shunted cell
class jj_152_s(spira.Cell):
    __name_prefix__ = 'jj_152_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.500,center=(0.000,4.650))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.650,center=(0.000,0.575))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.3625))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.400,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.025))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.000,center=(0.000,3.150))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.620))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.680))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.140, 1.140))
        elems += spira.Circle(layer=ls.J5,box_size=(1.430, 1.430))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 152uA shunted and grounded cell
class jj_152_sg(spira.Cell):
    __name_prefix__ = 'jj_152_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.375))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.3625))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.400,center=(0.000,0.600))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.610))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.680))
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.00,center=(0.000,3.150))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.500,center=(0.000,4.650))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.650,center=(0.000,0.575))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.025))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.725))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.140, 1.140))
        elems += spira.Circle(layer=ls.J5,box_size=(1.430, 1.430))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 153uA shunted cell
class jj_153_s(spira.Cell):
    __name_prefix__ = 'jj_153_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=1.150,height=4.000,center=(0.000,3.150))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.610))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.680))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.3625))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.425,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.475,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.675,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.025))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.140, 1.140))
        elems += spira.Circle(layer=ls.J5,box_size=(1.440, 1.440))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 154uA shunted cell
class jj_154_s(spira.Cell):
    __name_prefix__ = 'jj_154_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.000))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.450,center=(0.000,4.650))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.675,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.440, 1.440))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.975,center=(0.000,3.1375))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.140, 1.140))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.680))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.600))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.3375))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.425,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 154uA shunted and grounded cell
class jj_154_sg(spira.Cell):
    __name_prefix__ = 'jj_154_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.700))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.725))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.450,center=(0.000,4.650))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.675,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.440, 1.440))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.975,center=(0.000,3.1375))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.140, 1.140))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.680))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.600))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.3375))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.425,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 156uA shunted cell
class jj_156_s(spira.Cell):
    __name_prefix__ = 'jj_156_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.975))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.425,center=(0.000,4.6375))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.675,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.450, 1.450))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.950,center=(0.000,3.125))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.160, 1.160))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.690))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.570))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.3125))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.425,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports     

# JJ 156uA shunted and grounded cell
class jj_156_sg(spira.Cell):
    __name_prefix__ = 'jj_156_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.625))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.725))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.425,center=(0.000,4.6375))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.675,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.450, 1.450))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.950,center=(0.000,3.125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.975))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.160, 1.160))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.690))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.560))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.3125))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.450,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 157uA shunted and grounded cell
class jj_157_sg(spira.Cell):
    __name_prefix__ = 'jj_157_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.650))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.725))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.425,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.700,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.460, 1.460))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.950,center=(0.000,3.150))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,6.000))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.160, 1.160))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.710))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.580))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.3375))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.450,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 159uA shunted and grounded cell
class jj_159_sg(spira.Cell):
    __name_prefix__ = 'jj_159_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.625))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.450,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.3125))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.700,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.400,center=(0.000,4.650))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.925,center=(0.000,3.1375))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.720))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.560))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.725))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.975))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.160, 1.160))
        elems += spira.Circle(layer=ls.J5,box_size=(1.460, 1.460))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports 

# JJ 160uA shunted cell
class jj_160_s(spira.Cell):
    __name_prefix__ = 'jj_160_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.375,center=(0.000,4.6125))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.675,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.470, 1.470))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.900,center=(0.000,3.100))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.925))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.160, 1.160))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.690))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.520))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2625))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.425,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 160uA shunted and grounded cell
class jj_160_sg(spira.Cell):
    __name_prefix__ = 'jj_160_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.275),transformation=ls.r270)
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.425,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2625))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.675,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.375,center=(0.000,4.6125))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.900,center=(0.000,3.100))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.690))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.510))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.725))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.925))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.160, 1.160))
        elems += spira.Circle(layer=ls.J5,box_size=(1.470, 1.470))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
# JJ 161uA shunted cell
class jj_161_s(spira.Cell):
    __name_prefix__ = 'jj_161_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.375,center=(0.000,4.6375))
        elems += spira.Box(layer=ls.M5,width=2.500,height=3.700,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.470, 1.470))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.900,center=(0.000,3.125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.950))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.180, 1.180))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.720))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.530))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2875))
        elems += spira.Box(layer=ls.M6,width=2.200,height=3.450,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 162uA shunted cell
class jj_162_s(spira.Cell):
    __name_prefix__ = 'jj_162_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.350,center=(0.000,4.600))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.700,center=(0.000,0.575))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.900))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2375))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.450,center=(0.000,0.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.850,center=(0.000,3.100))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.490))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.700))
        elems += spira.Circle(layer=ls.J5,box_size=(1.480, 1.480))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.180, 1.180))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 162uA shunted cell and grounded
class jj_162_sg(spira.Cell):
    __name_prefix__ = 'jj_162_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.550))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.350,center=(0.000,4.600))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.700,center=(0.000,0.575))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.900))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.750))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2375))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.450,center=(0.000,0.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.850,center=(0.000,3.100))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.490))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.700))
        elems += spira.Circle(layer=ls.J5,box_size=(1.480, 1.480))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.180, 1.180))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 163uA shunted cell
class jj_163_s(spira.Cell):
    __name_prefix__ = 'jj_163_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.850,center=(0.000,3.100))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.480))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.700))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2375))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.450,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.900))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.350,center=(0.000,4.600))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.700,center=(0.000,0.575))
        elems += spira.Circle(layer=ls.J5,box_size=(1.480, 1.480))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.180, 1.180))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 163uA shunted and grounded cell
class jj_163_sg(spira.Cell):
    __name_prefix__ = 'jj_163_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.550))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.850,center=(0.000,3.100))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.480))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.700))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2375))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.450,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.900))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.350,center=(0.000,4.600))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.700,center=(0.000,0.575))
        elems += spira.Circle(layer=ls.J5,box_size=(1.480, 1.480))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.180, 1.180))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 164uA shunted cell
class jj_164_s(spira.Cell):
    __name_prefix__ = 'jj_164_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2375))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.500,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.500))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.730))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.825,center=(0.000,3.1125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.300,center=(0.000,4.625))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.750,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.900))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.180, 1.180))
        elems += spira.Circle(layer=ls.J5,box_size=(1.490, 1.490))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 164uA shunted and grounded cell
class jj_164_sg(spira.Cell):
    __name_prefix__ = 'jj_164_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.575))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2375))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.500,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.300,center=(0.000,4.625))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.750,center=(0.000,0.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.825,center=(0.000,3.1125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.500))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.730))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.750))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.180, 1.180))
        elems += spira.Circle(layer=ls.J5,box_size=(1.490, 1.490))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 165uA shunted cell
class jj_165_s(spira.Cell):
    __name_prefix__ = 'jj_165_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2125))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.475,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.460))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.710))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.825,center=(0.000,3.0875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.300,center=(0.000,4.600))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.725,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.875))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.200, 1.200))
        elems += spira.Circle(layer=ls.J5,box_size=(1.490, 1.490))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 165uA shunted and grounded cell
class jj_165_sg(spira.Cell):
    __name_prefix__ = 'jj_165_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.525))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.875))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.475,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2125))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.725,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.300,center=(0.000,4.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.825,center=(0.000,3.0875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.710))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.460))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.750))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.220, 1.220))
        elems += spira.Circle(layer=ls.J5,box_size=(1.490, 1.490))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports  

# JJ 166uA shunted and grounded cell
class jj_166_sg(spira.Cell):
    __name_prefix__ = 'jj_166_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.525))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,8.050))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.475,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.200))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.725,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.275,center=(0.000,4.5875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.800,center=(0.000,3.075))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.710))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.450))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.750))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.200, 1.200))
        elems += spira.Circle(layer=ls.J5,box_size=(1.490, 1.490))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 167uA shunted cell
class jj_167_s(spira.Cell):
    __name_prefix__ = 'jj_167_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.275,center=(0.000,4.6125))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.750,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.875))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2125))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.500,center=(0.000,0.625))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.800,center=(0.000,3.100))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.460))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.730))
        elems += spira.Circle(layer=ls.J5,box_size=(1.500, 1.500))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.200, 1.200))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports    

# JJ 167uA shunted and grounded cell
class jj_167_sg(spira.Cell):
    __name_prefix__ = 'jj_167_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.225))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.875))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.500,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.2125))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.750,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.275,center=(0.000,4.6125))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.800,center=(0.000,3.100))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.730))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.460))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.750))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.200, 1.200))
        elems += spira.Circle(layer=ls.J5,box_size=(1.500, 1.500))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports   

# JJ 169uA shunted cell
class jj_169_s(spira.Cell):
    __name_prefix__ = 'jj_169_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.250,center=(0.000,4.600))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.750,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.850))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.1875))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.500,center=(0.000,0.625))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.775,center=(0.000,3.0875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.440))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.740))
        elems += spira.Circle(layer=ls.J5,box_size=(1.510, 1.510))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.200, 1.200))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports         

# JJ 169uA shunted and grounded cell
class jj_169_sg(spira.Cell):
    __name_prefix__ = 'jj_169_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.500))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.750))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.250,center=(0.000,4.600))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.750,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.510, 1.510))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.775,center=(0.000,3.0875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.350,0.350))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.200, 1.200))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.740))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.440))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.1875))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.500,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 171uA shunted cell
class jj_171_s(spira.Cell):
    __name_prefix__ = 'jj_171_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.225,center=(0.000,4.5875))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.750,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.825))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.1625))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.500,center=(0.000,0.625))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.750,center=(0.000,3.075))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.420))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.740))
        elems += spira.Circle(layer=ls.J5,box_size=(1.520, 1.520))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.220, 1.220))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 171uA shunted and grounded cell
class jj_171_sg(spira.Cell):
    __name_prefix__ = 'jj_171_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.175))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.500,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.1625))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.750,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.225,center=(0.000,4.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.825))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.750))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.750,center=(0.000,3.075))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.740))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.410))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.220, 1.220))
        elems += spira.Circle(layer=ls.J5,box_size=(1.560, 1.560))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 172uA shunted and grounded cell
class jj_172_sg(spira.Cell):
    __name_prefix__ = 'jj_172_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.450))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.475,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.1375))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.725,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.225,center=(0.000,4.5625))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.800))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.750))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.750,center=(0.000,3.050))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.720))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.380))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.220, 1.220))
        elems += spira.Circle(layer=ls.J5,box_size=(1.520, 1.520))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 173uA shunted cell
class jj_173_s(spira.Cell):
    __name_prefix__ = 'jj_173_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.200,center=(0.000,4.550))
        elems += spira.Box(layer=ls.M5,width=2.550,height=3.725,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.775))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.125))
        elems += spira.Box(layer=ls.M6,width=2.250,height=3.475,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.725,center=(0.000,3.0375))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.370))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.720))
        elems += spira.Circle(layer=ls.J5,box_size=(1.520, 1.520))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.220, 1.220))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 175uA shunted and grounded cell
class jj_175_sg(spira.Cell):
    __name_prefix__ = 'jj_175_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.425))
        elems += spira.Box(layer=ls.M6,width=2.300,height=3.500,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.1125))
        elems += spira.Box(layer=ls.M5,width=2.600,height=3.750,center=(0.000,0.575))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.200,center=(0.000,4.550))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.775))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.775))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.700,center=(0.000,3.050))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.730))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.350))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.240, 1.240))
        elems += spira.Circle(layer=ls.J5,box_size=(1.530, 1.530))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 176uA shunted and grounded cell
class jj_176_sg(spira.Cell):
    __name_prefix__ = 'jj_176_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.450))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.675,center=(0.000,3.0625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.370))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.750))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.1125))
        elems += spira.Box(layer=ls.M6,width=2.300,height=3.550,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.150,center=(0.000,4.575))
        elems += spira.Box(layer=ls.M5,width=2.600,height=3.800,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.775))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.240, 1.240))
        elems += spira.Circle(layer=ls.J5,box_size=(1.540, 1.540))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 177uA shunted cell
class jj_177_s(spira.Cell):
    __name_prefix__ = 'jj_177_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.1125))
        elems += spira.Box(layer=ls.M6,width=2.300,height=3.550,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.360))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.760))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.675,center=(0.000,3.0625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.150,center=(0.000,4.575))
        elems += spira.Box(layer=ls.M5,width=2.600,height=3.800,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.775))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.240, 1.240))
        elems += spira.Circle(layer=ls.J5,box_size=(1.540, 1.540))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 179uA shunted and grounded cell
class jj_179_sg(spira.Cell):
    __name_prefix__ = 'jj_179_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.100))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.650,center=(0.000,3.050))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.340))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.760))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.0875))
        elems += spira.Box(layer=ls.M6,width=2.300,height=3.550,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.125,center=(0.000,4.5625))
        elems += spira.Box(layer=ls.M5,width=2.600,height=3.800,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.775))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.750))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.260, 1.260))
        elems += spira.Circle(layer=ls.J5,box_size=(1.550, 1.550))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 180uA shunted cell
class jj_180_s(spira.Cell):
    __name_prefix__ = 'jj_180_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.0875))
        elems += spira.Box(layer=ls.M6,width=2.300,height=3.550,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.330))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.760))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.650,center=(0.000,3.050))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.125,center=(0.000,4.5625))
        elems += spira.Box(layer=ls.M5,width=2.600,height=3.800,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.750))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.260, 1.260))
        elems += spira.Circle(layer=ls.J5,box_size=(1.550, 1.550))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        
        
# JJ 182uA shunted cell
class jj_182_s(spira.Cell):
    __name_prefix__ = 'jj_182_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.0625))
        elems += spira.Box(layer=ls.M6,width=2.300,height=3.550,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.310))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.770))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.625,center=(0.000,3.0375))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.100,center=(0.000,4.550))
        elems += spira.Box(layer=ls.M5,width=2.600,height=3.800,center=(0.000,0.500))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.725))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.260, 1.240))
        elems += spira.Circle(layer=ls.J5,box_size=(1.560, 1.560))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports    

# JJ 182uA shunted and grounded cell
class jj_182_sg(spira.Cell):
    __name_prefix__ = 'jj_182_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,6.075),transformation=ls.r270)
        elems += spira.Box(layer=ls.M6,width=2.300,height=3.550,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,5.0625))
        elems += spira.Box(layer=ls.M5,width=2.600,height=3.800,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.100,center=(0.000,4.550))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.775))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.770))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.310))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.625,center=(0.000,3.0375))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.725))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.260, 1.260))
        elems += spira.Circle(layer=ls.J5,box_size=(1.560, 1.560))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 186uA shunted cell
class jj_186_s(spira.Cell):
    __name_prefix__ = 'jj_186_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.050,center=(0.000,4.525))
        elems += spira.Box(layer=ls.M5,width=2.650,height=3.825,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.025))
        elems += spira.Box(layer=ls.M6,width=2.350,height=3.575,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.675))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.550,center=(0.000,3.025))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.280))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.770))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.280, 1.280))
        elems += spira.Circle(layer=ls.J5,box_size=(1.580, 1.580))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 189uA shunted and grounded cell
class jj_189_sg(spira.Cell):
    __name_prefix__ = 'jj_189_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.325))
        elems += spira.Box(layer=ls.M6,width=2.340,height=3.600,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,5.000))
        elems += spira.Box(layer=ls.M5,width=2.650,height=3.850,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.000,center=(0.000,4.525))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.800))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.780))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.250))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.525,center=(0.000,3.0125))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.300, 1.300))
        elems += spira.Circle(layer=ls.J5,box_size=(1.590, 1.590))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 190uA shunted and grounded cell
class jj_190_sg(spira.Cell):
    __name_prefix__ = 'jj_190_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.300))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9625))
        elems += spira.Box(layer=ls.M6,width=2.350,height=3.575,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.220))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.760))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.500,center=(0.000,2.9875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.000,center=(0.000,4.500))
        elems += spira.Box(layer=ls.M5,width=2.650,height=3.825,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.800))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.300, 1.300))
        elems += spira.Circle(layer=ls.J5,box_size=(1.600, 1.600))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 191uA shunted and grounded cell
class jj_191_sg(spira.Cell):
    __name_prefix__ = 'jj_191_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.300))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.800))
        elems += spira.Box(layer=ls.M5,width=1.750,height=4.000,center=(0.000,4.525))
        elems += spira.Box(layer=ls.M5,width=2.650,height=3.850,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.600, 1.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.525,center=(0.000,3.0125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.650))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.300, 1.300))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.780))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.240))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9875))
        elems += spira.Box(layer=ls.M6,width=2.350,height=3.600,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 192uA shunted cell
class jj_192_s(spira.Cell):
    __name_prefix__ = 'jj_192_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.975,center=(0.000,4.5125))
        elems += spira.Box(layer=ls.M5,width=2.650,height=3.850,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.600, 1.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.500,center=(0.000,3.000))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.625))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.300, 1.300))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.790))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.230))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.975))
        elems += spira.Box(layer=ls.M6,width=2.350,height=3.600,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 194uA shunted and grounded cell
class jj_194_sg(spira.Cell):
    __name_prefix__ = 'jj_194_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.950))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9375))
        elems += spira.Box(layer=ls.M6,width=2.350,height=3.575,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.190))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.770))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.500,center=(0.000,2.975))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.975,center=(0.000,4.4875))
        elems += spira.Box(layer=ls.M5,width=2.650,height=3.825,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.800))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.600))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.320, 1.320))
        elems += spira.Circle(layer=ls.J5,box_size=(1.610, 1.610))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 195uA shunted and grounded cell
class jj_195_sg(spira.Cell):
    __name_prefix__ = 'jj_195_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.275))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9375))
        elems += spira.Box(layer=ls.M6,width=2.350,height=3.575,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.180))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.770))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.500,center=(0.000,2.975))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.975,center=(0.000,4.4875))
        elems += spira.Box(layer=ls.M5,width=2.650,height=3.825,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.800))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.320, 1.320))
        elems += spira.Circle(layer=ls.J5,box_size=(1.620, 1.620))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 196uA shunted cell
class jj_196_s(spira.Cell):
    __name_prefix__ = 'jj_196_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9375))
        elems += spira.Box(layer=ls.M6,width=2.340,height=3.600,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.200))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.790))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.475,center=(0.000,2.9875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.950,center=(0.000,4.450))
        elems += spira.Box(layer=ls.M5,width=2.650,height=3.850,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.600))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.320, 1.320))
        elems += spira.Circle(layer=ls.J5,box_size=(1.620, 1.620))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 198uA shunted cell
class jj_198_s(spira.Cell):
    __name_prefix__ = 'jj_198_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9375))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.180))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.800))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.450,center=(0.000,3.000))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.950,center=(0.000,4.500))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.875,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.600))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.320, 1.320))
        elems += spira.Circle(layer=ls.J5,box_size=(1.630, 1.630))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 198uA shunted and grounded cell
class jj_198_sg(spira.Cell):
    __name_prefix__ = 'jj_198_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.250))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9375))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.875,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.950,center=(0.000,4.500))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.600))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.825))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.800))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.180))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.450,center=(0.000,3.000))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.320, 1.320))
        elems += spira.Circle(layer=ls.J5,box_size=(1.630, 1.630))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 199uA shunted cell
class jj_199_s(spira.Cell):
    __name_prefix__ = 'jj_199_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.925,center=(0.000,4.4625))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.850,center=(0.000,0.575))
        elems += spira.Circle(layer=ls.J5,box_size=(1.630, 1.630))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.425,center=(0.000,2.9625))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.550))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.340, 1.340))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.780))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.150))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.900))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.600,center=(0.000,0.600))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 200uA shunted cell
class jj_200_s(spira.Cell):
    __name_prefix__ = 'jj_200_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.425,center=(0.000,2.9875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.170))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.800))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9125))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.925,center=(0.000,4.4875))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.875,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.825))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.340, 1.340))
        elems += spira.Circle(layer=ls.J5,box_size=(1.630, 1.630))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 200uA shunted and grounded cell
class jj_200_sg(spira.Cell):
    __name_prefix__ = 'jj_200_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.250))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.425,center=(0.000,2.9875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.170))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.800))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9125))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.925,center=(0.000,4.4875))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.875,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.825))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.340, 1.340))
        elems += spira.Circle(layer=ls.J5,box_size=(1.630, 1.630))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 201uA shunted cell
class jj_201_s(spira.Cell):
    __name_prefix__ = 'jj_201_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.900,center=(0.000,4.500))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.900,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.640, 1.640))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.425,center=(0.000,2.9875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.575))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.340, 1.340))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.800))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.160))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9125))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 201uA shunted and grounded cell
class jj_201_sg(spira.Cell):
    __name_prefix__ = 'jj_201_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.925))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.425,center=(0.000,2.9875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.160))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.800))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.9125))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.650,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.900,center=(0.000,4.500))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.900,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.575))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.825))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.340, 1.340))
        elems += spira.Circle(layer=ls.J5,box_size=(1.640, 1.640))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports           

# JJ 202uA shunted cell
class jj_202_s(spira.Cell):
    __name_prefix__ = 'jj_202_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.400,center=(0.000,2.950))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.130))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.780))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.875))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.875,center=(0.000,4.4625))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.875,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.525))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.340, 1.340))
        elems += spira.Circle(layer=ls.J5,box_size=(1.640, 1.640))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports 
        
# JJ 202uA shunted and grounded cell
class jj_202_sg(spira.Cell):
    __name_prefix__ = 'jj_202_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.175))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.400,center=(0.000,2.950))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.110))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.780))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.875))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.875,center=(0.000,4.4625))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.875,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.525))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.825))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.340, 1.340))
        elems += spira.Circle(layer=ls.J5,box_size=(1.640, 1.640))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports    

# JJ 204uA shunted and grounded cell
class jj_204_sg(spira.Cell):
    __name_prefix__ = 'jj_204_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.175))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.400,center=(0.000,2.950))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.110))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.790))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.8625))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.875,center=(0.000,4.4625))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.875,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.525))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.825))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.360, 1.360))
        elems += spira.Circle(layer=ls.J5,box_size=(1.650, 1.650))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 206uA shunted and grounded cell
class jj_206_sg(spira.Cell):
    __name_prefix__ = 'jj_206_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.200))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.825))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.850,center=(0.000,4.450))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.875,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.660, 1.660))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.375,center=(0.000,2.9375))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.360, 1.360))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.790))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.100))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.850))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 207uA shunted and grounded cell
class jj_207_sg(spira.Cell):
    __name_prefix__ = 'jj_207_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.850),transformation=ls.r270)
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.825))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.850,center=(0.000,4.450))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.875,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.660, 1.660))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.375,center=(0.000,2.9375))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.360, 1.360))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.790))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.090))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.8375))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.625,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.500))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 209uA shunted and grounded cell
class jj_209_sg(spira.Cell):
    __name_prefix__ = 'jj_209_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.200))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.850,center=(0.000,4.475))
        elems += spira.Box(layer=ls.M5,width=2.700,height=3.900,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.8625))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.650,center=(0.000,0.625))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.825))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.375,center=(0.000,2.9625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.100))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.820))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.380, 1.380))
        elems += spira.Circle(layer=ls.J5,box_size=(1.670, 1.670))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 212uA shunted cell
class jj_212_s(spira.Cell):
    __name_prefix__ = 'jj_212_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.675,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.8375))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.925,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.825,center=(0.000,4.4625))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.500))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.090))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.325,center=(0.000,2.9625))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.380, 1.380))
        elems += spira.Circle(layer=ls.J5,box_size=(1.680, 1.680))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 212uA shunted and grounded cell
class jj_212_sg(spira.Cell):
    __name_prefix__ = 'jj_212_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.150))
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.675,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.8375))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.925,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.825,center=(0.000,4.4625))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.500))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.850))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.090))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.325,center=(0.000,2.9625))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.380, 1.380))
        elems += spira.Circle(layer=ls.J5,box_size=(1.680, 1.680))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 215uA shunted and grounded cell
class jj_215_sg(spira.Cell):
    __name_prefix__ = 'jj_215_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.8125))
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.700,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.060))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.300,center=(0.000,2.950))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.775,center=(0.000,4.4625))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.950,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.850))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.475))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.400, 1.400))
        elems += spira.Circle(layer=ls.J5,box_size=(1.690, 1.690))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports       

# JJ 216uA shunted and grounded cell
class jj_216_sg(spira.Cell):
    __name_prefix__ = 'jj_216_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.800))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7875))
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.675,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.040))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.810))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.300,center=(0.000,2.925))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.775,center=(0.000,4.4375))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.925,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.850))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.450))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.400, 1.400))
        elems += spira.Circle(layer=ls.J5,box_size=(1.700, 1.700))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports           

# JJ 218uA shunted and grounded cell
class jj_218_sg(spira.Cell):
    __name_prefix__ = 'jj_218_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.800))
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.700,center=(0.000,0.625))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.050))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.840))
        elems += spira.Box(layer=ls.R5,width=1.250,height=3.175,center=(0.000,2.9375))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.750,center=(0.000,4.450))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.950,center=(0.000,0.600))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.850))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.400, 1.400))
        elems += spira.Circle(layer=ls.J5,box_size=(1.700, 1.700))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 220uA shunted cell
class jj_220_s(spira.Cell):
    __name_prefix__ = 'jj_220_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.97625))
        elems += spira.Box(layer=ls.M6,width=2.400,height=3.675,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.010))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.820))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.275,center=(0.000,2.9125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.750,center=(0.000,4.425))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.925,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.425))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.420, 1.420))
        elems += spira.Circle(layer=ls.J5,box_size=(1.710, 1.710))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 220uA shunted and grounded cell
class jj_220_sg(spira.Cell):
    __name_prefix__ = 'jj_220_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.100))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.850))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.750,center=(0.000,4.425))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.925,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.710, 1.710))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.275,center=(0.000,2.9125))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.420, 1.420))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.820))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.010))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7625))
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.675,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 221uA shunted and grounded cell
class jj_221_sg(spira.Cell):
    __name_prefix__ = 'jj_221_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.075))
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.675,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7625))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.925,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.750,center=(0.000,4.425))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.425))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.850))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.275,center=(0.000,2.9125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.820))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.010))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.420, 1.420))
        elems += spira.Circle(layer=ls.J5,box_size=(1.720, 1.720))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 222uA shunted and grounded cell
class jj_222_sg(spira.Cell):
    __name_prefix__ = 'jj_222_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.100))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.725,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.925,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.750))
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.675,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.850))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.250,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.000))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.820))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.420, 1.420))
        elems += spira.Circle(layer=ls.J5,box_size=(1.720, 1.720))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 222uA shunted cell
class jj_222_s(spira.Cell):
    __name_prefix__ = 'jj_222_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.750))
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.675,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.725,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.925,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.250,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.000))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.820))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.400))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.420, 1.420))
        elems += spira.Circle(layer=ls.J5,box_size=(1.720, 1.720))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 223uA shunted cell
class jj_223_s(spira.Cell):
    __name_prefix__ = 'jj_223_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7375))
        elems += spira.Box(layer=ls.M6,width=2.450,height=3.675,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.725,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.750,height=3.925,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.250,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,4.000))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.820))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.400))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.420, 1.420))
        elems += spira.Circle(layer=ls.J5,box_size=(1.720, 1.720))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 225uA shunted cell
class jj_225_s(spira.Cell):
    __name_prefix__ = 'jj_225_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.225,center=(0.000,2.9125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.980))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7375))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.700,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.725,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.950,center=(0.000,0.575))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.400))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.440, 1.440))
        elems += spira.Circle(layer=ls.J5,box_size=(1.730, 1.730))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 225uA shunted and grounded cell
class jj_225_sg(spira.Cell):
    __name_prefix__ = 'jj_225_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.050))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.225,center=(0.000,2.9125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.980))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7375))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.700,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.725,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.950,center=(0.000,0.575))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.400))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.2875))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.440, 1.440))
        elems += spira.Circle(layer=ls.J5,box_size=(1.730, 1.730))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 227uA shunted cell
class jj_227_s(spira.Cell):
    __name_prefix__ = 'jj_227_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.675,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.975,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.725))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.725,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.375))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.200,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.970))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Circle(layer=ls.J5,box_size=(1.740, 1.740))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.440, 1.440))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 227uA shunted and grounded cell
class jj_227_sg(spira.Cell):
    __name_prefix__ = 'jj_227_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.050))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.200,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.970))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.725))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.725,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.675,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.975,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.2875))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.440, 1.440))
        elems += spira.Circle(layer=ls.J5,box_size=(1.740, 1.740))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 228uA shunted cell
class jj_228_s(spira.Cell):
    __name_prefix__ = 'jj_228_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.675,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.975,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7125))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.725,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.375))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.200,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.970))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Circle(layer=ls.J5,box_size=(1.740, 1.740))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.440, 1.440))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 228uA shunted and grounded cell
class jj_228_sg(spira.Cell):
    __name_prefix__ = 'jj_228_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.050))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.675,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.975,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7125))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.725,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.200,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.970))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Circle(layer=ls.J5,box_size=(1.740, 1.740))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.440, 1.440))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 230uA shunted and grounded cell
class jj_230_sg(spira.Cell):
    __name_prefix__ = 'jj_230_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.725))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.675,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.975,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7125))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.725,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.200,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.960))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.830))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.375))        
        elems += spira.Circle(layer=ls.J5,box_size=(1.750, 1.750))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.460, 1.460))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 231uA shunted cell
class jj_231_s(spira.Cell):
    __name_prefix__ = 'jj_231_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.200,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.840))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.950))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.725,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.375))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.975,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.675,center=(0.000,4.4125))
        elems += spira.Circle(layer=ls.J5,box_size=(1.750, 1.750))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.460, 1.460))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 232uA shunted and grounded cell
class jj_232_sg(spira.Cell):
    __name_prefix__ = 'jj_232_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.050))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.750,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.725))
        elems += spira.Box(layer=ls.M5,width=2.800,height=4.000,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.650,center=(0.000,4.425))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.860))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.970))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.175,center=(0.000,2.9125))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.460, 1.460))
        elems += spira.Circle(layer=ls.J5,box_size=(1.760, 1.760))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 234uA shunted cell
class jj_234_s(spira.Cell):
    __name_prefix__ = 'jj_234_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.350))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.725,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6875))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.975,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.650,center=(0.000,4.400))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.175,center=(0.000,2.8875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.840))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.940))
        elems += spira.Circle(layer=ls.J5,box_size=(1.760, 1.760))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.460, 1.460))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 235uA shunted cell
class jj_235_s(spira.Cell):
    __name_prefix__ = 'jj_235_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.650,center=(0.000,4.425))
        elems += spira.Box(layer=ls.M5,width=2.800,height=4.000,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.770, 1.770))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.175,center=(0.000,2.9125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.375))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.460, 1.460))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.870))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.960))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7125))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.750,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 235uA shunted and grounded cell
class jj_235_sg(spira.Cell):
    __name_prefix__ = 'jj_235_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.025))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.650,center=(0.000,4.425))
        elems += spira.Box(layer=ls.M5,width=2.800,height=4.000,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.770, 1.770))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.175,center=(0.000,2.9125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.375))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.460, 1.460))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.870))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.960))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.7125))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.750,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 236uA shunted and grounded cell
class jj_236_sg(spira.Cell):
    __name_prefix__ = 'jj_236_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.000))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6875))
        elems += spira.Box(layer=ls.M6,width=2.500,height=3.725,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.930))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.850))
        elems += spira.Box(layer=ls.R5,width=1.250,height=3.175,center=(0.000,2.8875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.650,center=(0.000,4.400))
        elems += spira.Box(layer=ls.M5,width=2.800,height=3.975,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.350))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.875))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.480, 1.480))
        elems += spira.Circle(layer=ls.J5,box_size=(1.770, 1.770))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 238uA shunted and grounded cell
class jj_238_sg(spira.Cell):
    __name_prefix__ = 'jj_238_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.675))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M6,width=2.550,height=3.750,center=(0.000,0.600))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.910))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.850))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.125,center=(0.000,2.8875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.625,center=(0.000,4.3875))
        elems += spira.Box(layer=ls.M5,width=2.800,height=4.000,center=(0.000,0.575))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.325))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.900))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.480, 1.480))
        elems += spira.Circle(layer=ls.J5,box_size=(1.780, 1.780))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 240uA shunted cell
class jj_240_s(spira.Cell):
    __name_prefix__ = 'jj_240_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=1.650,height=2.775,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M6,width=2.550,height=3.775,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.600,center=(0.000,4.400))
        elems += spira.Box(layer=ls.M5,width=2.850,height=4.025,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.125,center=(0.000,2.8875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.910))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.850))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.325))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.480, 1.480))
        elems += spira.Circle(layer=ls.J5,box_size=(1.790, 1.790))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 240uA shunted and grounded cell
class jj_240_sg(spira.Cell):
    __name_prefix__ = 'jj_240_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,4.975))
        elems += spira.Box(layer=ls.M6,width=1.650,height=2.775,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M6,width=2.550,height=3.775,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.600,center=(0.000,4.400))
        elems += spira.Box(layer=ls.M5,width=2.850,height=4.025,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.125,center=(0.000,2.8875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.910))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.850))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.325))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.900))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.480, 1.480))
        elems += spira.Circle(layer=ls.J5,box_size=(1.790, 1.790))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 242uA shunted and grounded cell
class jj_242_sg(spira.Cell):
    __name_prefix__ = 'jj_242_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.000))
        elems += spira.Box(layer=ls.M6,width=1.650,height=2.750,center=(0.000,4.675))
        elems += spira.Box(layer=ls.M6,width=2.550,height=3.800,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.575,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.850,height=4.050,center=(0.000,0.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.100,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.930))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.880))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.900))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.500, 1.500))
        elems += spira.Circle(layer=ls.J5,box_size=(1.790, 1.790))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 243uA shunted and grounded cell
class jj_243_sg(spira.Cell):
    __name_prefix__ = 'jj_243_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,4.950))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6375))
        elems += spira.Box(layer=ls.M6,width=2.550,height=3.775,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.575,center=(0.000,4.3875))
        elems += spira.Box(layer=ls.M5,width=2.850,height=4.025,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.100,center=(0.000,2.875))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.890))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.860))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.900))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.300))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.500, 1.500))
        elems += spira.Circle(layer=ls.J5,box_size=(1.800, 1.800))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        
        
# JJ 245uA shunted and grounded cell
class jj_245_sg(spira.Cell):
    __name_prefix__ = 'jj_245_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.675))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M6,width=2.550,height=3.800,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.575,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.M5,width=2.850,height=4.050,center=(0.000,0.600))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.100,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.910))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.890))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.900))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.325))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.500, 1.500))
        elems += spira.Circle(layer=ls.J5,box_size=(1.800, 1.800))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 250uA shunted and grounded cell
class jj_250_sg(spira.Cell):
    __name_prefix__ = 'jj_250_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,4.950))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.900))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.400))
        elems += spira.Box(layer=ls.M5,width=2.850,height=4.050,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.820, 1.820))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.075,center=(0.000,2.8875))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.520, 1.520))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,1.900))
        elems += spira.Box(layer=ls.C5R,width=0.520,height=0.520,center=(0.000,3.890))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.63750))
        elems += spira.Box(layer=ls.M6,width=2.550,height=3.800,center=(0.000,0.625))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 253uA shunted and grounded cell
class jj_253_sg(spira.Cell):
    __name_prefix__ = 'jj_253_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,4.950))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.925))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.575,center=(0.000,4.3875))
        elems += spira.Box(layer=ls.M5,width=2.900,height=4.050,center=(0.000,0.575))
        elems += spira.Circle(layer=ls.J5,box_size=(1.830, 1.830))
        elems += spira.Box(layer=ls.R5,width=1.100,height=3.075,center=(0.000,2.8875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.300))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.540, 1.540))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,1.880))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,3.890))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.63750))
        elems += spira.Box(layer=ls.M6,width=2.600,height=3.800,center=(0.000,0.600))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 254uA shunted and grounded cell
class jj_254_sg(spira.Cell):
    __name_prefix__ = 'jj_254_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.650))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.925))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.400))
        elems += spira.Box(layer=ls.M5,width=2.900,height=4.075,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.840, 1.840))
        elems += spira.Box(layer=ls.R5,width=1.100,height=3.075,center=(0.000,2.8875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.300))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.540, 1.540))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,1.880))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,3.880))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.63750))
        elems += spira.Box(layer=ls.M6,width=2.600,height=3.825,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 257uA shunted and grounded cell
class jj_257_sg(spira.Cell):
    __name_prefix__ = 'jj_257_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.000))
        elems += spira.Box(layer=ls.M6,width=2.600,height=3.850,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6375))
        elems += spira.Box(layer=ls.M5,width=2.900,height=4.100,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.525,center=(0.000,4.4125))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.925))
        elems += spira.Box(layer=ls.R5,width=1.100,height=3.050,center=(0.000,2.900))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,1.910))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,3.900))
        elems += spira.Circle(layer=ls.J5,box_size=(1.850, 1.850))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.540, 1.540))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 258uA shunted and grounded cell
class jj_258_sg(spira.Cell):
    __name_prefix__ = 'jj_258_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,4.950))
        elems += spira.Box(layer=ls.M6,width=2.600,height=3.825,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6125))
        elems += spira.Box(layer=ls.M5,width=2.900,height=4.075,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.525,center=(0.000,4.3875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.925))
        elems += spira.Box(layer=ls.R5,width=1.100,height=3.050,center=(0.000,2.875))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,1.880))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,3.870))
        elems += spira.Circle(layer=ls.J5,box_size=(1.850, 1.850))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.540, 1.540))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 260uA shunted and grounded cell
class jj_260_sg(spira.Cell):
    __name_prefix__ = 'jj_260_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.000))
        elems += spira.Box(layer=ls.M6,width=2.600,height=3.850,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M5,width=2.900,height=4.100,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.425))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.925))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.075,center=(0.000,2.9125))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,1.910))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,3.920))
        elems += spira.Circle(layer=ls.J5,box_size=(1.860, 1.860))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.560, 1.560))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 261uA shunted and grounded cell
class jj_261_sg(spira.Cell):
    __name_prefix__ = 'jj_261_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,4.975))
        elems += spira.Box(layer=ls.M6,width=2.600,height=3.850,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M5,width=2.900,height=4.100,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.425))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.925))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.075,center=(0.000,2.9125))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,1.910))
        elems += spira.Box(layer=ls.C5R,width=0.580,height=0.520,center=(0.000,3.910))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.325))
        elems += spira.Circle(layer=ls.J5,box_size=(1.860, 1.860))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.560, 1.560))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 266uA shunted and grounded cell
class jj_266_sg(spira.Cell):
    __name_prefix__ = 'jj_266_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.000))
        elems += spira.Box(layer=ls.M6,width=2.650,height=3.875,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.675))
        elems += spira.Box(layer=ls.M5,width=2.950,height=4.125,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.425))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.950))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.050,center=(0.000,2.925))
        elems += spira.Box(layer=ls.C5R,width=0.600,height=0.520,center=(0.000,1.920))
        elems += spira.Box(layer=ls.C5R,width=0.600,height=0.520,center=(0.000,3.930))
        elems += spira.Circle(layer=ls.J5,box_size=(1.880, 1.880))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.790, 1.790))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 269uA shunted and grounded cell
class jj_269_s(spira.Cell):
    __name_prefix__ = 'jj_269_s'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M6,width=2.650,height=3.900,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M5,width=2.950,height=4.150,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.525,center=(0.000,4.4375))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.325))
        elems += spira.Box(layer=ls.R5,width=1.150,height=3.050,center=(0.000,2.925))
        elems += spira.Box(layer=ls.C5R,width=0.600,height=0.520,center=(0.000,1.930))
        elems += spira.Box(layer=ls.C5R,width=0.600,height=0.520,center=(0.000,3.920))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.480, 1.480))
        elems += spira.Circle(layer=ls.J5,box_size=(1.890, 1.890))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports           

# JJ 271uA shunted and grounded cell
class jj_271_sg(spira.Cell):
    __name_prefix__ = 'jj_271_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.000))
        elems += spira.Box(layer=ls.M6,width=2.650,height=3.900,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6875))
        elems += spira.Box(layer=ls.M5,width=2.950,height=4.150,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.450))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.950))
        elems += spira.Box(layer=ls.R5,width=1.250,height=3.075,center=(0.000,2.9375))
        elems += spira.Box(layer=ls.C5R,width=0.620,height=0.520,center=(0.000,1.930))
        elems += spira.Box(layer=ls.C5R,width=0.620,height=0.520,center=(0.000,3.940))
        elems += spira.Circle(layer=ls.J5,box_size=(1.890, 1.890))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.600, 1.600))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.350))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 274uA shunted and grounded cell
class jj_274_sg(spira.Cell):
    __name_prefix__ = 'jj_274_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,4.975))
        elems += spira.Box(layer=ls.M6,width=1.650,height=2.775,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M6,width=2.650,height=3.875,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.425))
        elems += spira.Box(layer=ls.M5,width=2.950,height=4.125,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.R5,width=1.250,height=3.075,center=(0.000,2.9125))
        elems += spira.Box(layer=ls.C5R,width=0.620,height=0.520,center=(0.000,3.900))
        elems += spira.Box(layer=ls.C5R,width=0.620,height=0.520,center=(0.000,1.910))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.325))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.950))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.600, 1.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.900, 1.900))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 276uA shunted and grounded cell
class jj_276_sg(spira.Cell):
    __name_prefix__ = 'jj_276_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.675))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6625))
        elems += spira.Box(layer=ls.M6,width=2.650,height=3.900,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.525,center=(0.000,4.4375))
        elems += spira.Box(layer=ls.M5,width=2.950,height=4.150,center=(0.000,0.600))
        elems += spira.Box(layer=ls.R5,width=1.250,height=3.050,center=(0.000,2.925))
        elems += spira.Box(layer=ls.C5R,width=0.620,height=0.520,center=(0.000,3.910))
        elems += spira.Box(layer=ls.C5R,width=0.620,height=0.520,center=(0.000,1.940))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.325))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.950))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.620, 1.620))
        elems += spira.Circle(layer=ls.J5,box_size=(1.910, 1.910))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 280uA shunted and grounded cell
class jj_280_sg(spira.Cell):
    __name_prefix__ = 'jj_280_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.000))
        elems += spira.Box(layer=ls.M6,width=2.650,height=3.900,center=(0.000,0.625))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6875))
        elems += spira.Box(layer=ls.M5,width=2.950,height=4.150,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.450))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.350))
        elems += spira.Box(layer=ls.C5R,width=0.680,height=0.520,center=(0.000,1.950))
        elems += spira.Box(layer=ls.C5R,width=0.680,height=0.520,center=(0.000,3.940))
        elems += spira.Box(layer=ls.R5,width=1.200,height=3.075,center=(0.000,2.9375))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.950))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.620, 1.620))
        elems += spira.Circle(layer=ls.J5,box_size=(1.920, 1.920))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 284uA shunted and grounded cell
class jj_284_sg(spira.Cell):
    __name_prefix__ = 'jj_284_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.000))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.775,center=(0.000,4.6875))
        elems += spira.Box(layer=ls.M6,width=2.700,height=3.925,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.C5R,width=0.680,height=0.520,center=(0.000,3.930))
        elems += spira.Box(layer=ls.C5R,width=0.680,height=0.520,center=(0.000,1.930))
        elems += spira.Box(layer=ls.R5,width=1.250,height=3.075,center=(0.000,2.9375))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.450))
        elems += spira.Box(layer=ls.M5,width=3.000,height=4.175,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.350))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.975))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.640, 1.640))
        elems += spira.Circle(layer=ls.J5,box_size=(1.940, 1.940))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 285uA shunted and grounded cell
class jj_285_sg(spira.Cell):
    __name_prefix__ = 'jj_285_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.000))
        elems += spira.Box(layer=ls.M6,width=2.700,height=3.925,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.450,height=2.750,center=(0.000,4.675))
        elems += spira.Box(layer=ls.M5,width=3.000,height=4.175,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.525,center=(0.000,4.4375))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,2.975))
        elems += spira.Box(layer=ls.R5,width=1.250,height=3.050,center=(0.000,2.925))
        elems += spira.Box(layer=ls.C5R,width=0.680,height=0.520,center=(0.000,1.930))
        elems += spira.Box(layer=ls.C5R,width=0.680,height=0.520,center=(0.000,3.920))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.640, 1.640))
        elems += spira.Circle(layer=ls.J5,box_size=(1.940, 1.940))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 300uA shunted and grounded cell
class jj_300_sg(spira.Cell):
    __name_prefix__ = 'jj_300_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.050))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,3.000))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.500))
        elems += spira.Box(layer=ls.M5,width=3.050,height=4.250,center=(0.000,0.600))
        elems += spira.Circle(layer=ls.J5,box_size=(1.990, 1.990))
        elems += spira.Box(layer=ls.R5,width=1.300,height=3.075,center=(0.000,2.9875))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.700, 1.700))
        elems += spira.Box(layer=ls.C5R,width=0.780,height=0.520,center=(0.000,1.980))
        elems += spira.Box(layer=ls.C5R,width=0.780,height=0.520,center=(0.000,3.990))
        elems += spira.Box(layer=ls.M6,width=1.500,height=2.775,center=(0.000,4.7375))
        elems += spira.Box(layer=ls.M6,width=2.750,height=4.000,center=(0.000,0.625))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.400))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports
        
# JJ 301uA shunted and grounded cell
class jj_301_sg(spira.Cell):
    __name_prefix__ = 'jj_301_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.725))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,3.000))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.475))
        elems += spira.Box(layer=ls.M5,width=3.050,height=4.225,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(1.990, 1.990))
        elems += spira.Box(layer=ls.R5,width=1.300,height=3.075,center=(0.000,2.9625))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.700, 1.700))
        elems += spira.Box(layer=ls.C5R,width=0.780,height=0.520,center=(0.000,1.960))
        elems += spira.Box(layer=ls.C5R,width=0.780,height=0.520,center=(0.000,3.960))
        elems += spira.Box(layer=ls.M6,width=1.500,height=2.775,center=(0.000,4.7125))
        elems += spira.Box(layer=ls.M6,width=2.750,height=3.975,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.375))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports        

# JJ 303uA shunted and grounded cell
class jj_303_sg(spira.Cell):
    __name_prefix__ = 'jj_303_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.050))
        elems += spira.Box(layer=ls.M6,width=2.750,height=3.975,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.500,height=2.750,center=(0.000,4.700))
        elems += spira.Box(layer=ls.M5,width=3.050,height=4.225,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.525,center=(0.000,4.4625))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,3.000))
        elems += spira.Box(layer=ls.R5,width=1.300,height=3.050,center=(0.000,2.950))
        elems += spira.Box(layer=ls.C5R,width=0.780,height=0.520,center=(0.000,1.960))
        elems += spira.Box(layer=ls.C5R,width=0.780,height=0.520,center=(0.000,3.950))
        elems += spira.Circle(layer=ls.J5,box_size=(2.000, 2.000))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.700, 1.700))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 315uA shunted and grounded cell
class jj_315_sg(spira.Cell):
    __name_prefix__ = 'jj_315_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.050))
        elems += spira.Box(layer=ls.M6,width=2.800,height=4.025,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.550,height=2.775,center=(0.000,4.7125))
        elems += spira.Box(layer=ls.M5,width=3.100,height=4.275,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.525,center=(0.000,4.4875))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,3.025))
        elems += spira.Box(layer=ls.R5,width=1.350,height=3.050,center=(0.000,2.975))
        elems += spira.Box(layer=ls.C5R,width=0.800,height=0.520,center=(0.000,1.980))
        elems += spira.Box(layer=ls.C5R,width=0.800,height=0.520,center=(0.000,3.970))
        elems += spira.Circle(layer=ls.J5,box_size=(2.040, 2.040))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.740, 1.740))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 324uA shunted and grounded cell
class jj_324_sg(spira.Cell):
    __name_prefix__ = 'jj_324_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.100))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,3.025))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.500))
        elems += spira.Box(layer=ls.M5,width=3.100,height=4.275,center=(0.000,0.5875))
        elems += spira.Circle(layer=ls.J5,box_size=(2.070, 2.070))
        elems += spira.Box(layer=ls.R5,width=1.400,height=3.075,center=(0.000,2.9875))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.760, 1.760))
        elems += spira.Box(layer=ls.C5R,width=0.840,height=0.520,center=(0.000,1.990))
        elems += spira.Box(layer=ls.C5R,width=0.840,height=0.520,center=(0.000,4.000))
        elems += spira.Box(layer=ls.M6,width=1.600,height=2.775,center=(0.000,4.7375))
        elems += spira.Box(layer=ls.M6,width=2.800,height=4.025,center=(0.000,0.6125))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 325uA shunted and grounded cell
class jj_325_sg(spira.Cell):
    __name_prefix__ = 'jj_325_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.050))
        elems += spira.Box(layer=ls.M6,width=2.800,height=4.025,center=(0.000,0.6125))
        elems += spira.Box(layer=ls.M6,width=1.600,height=2.775,center=(0.000,4.7375))
        elems += spira.Box(layer=ls.M5,width=3.100,height=4.275,center=(0.000,0.5875))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.550,center=(0.000,4.500))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,3.025))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.400))
        elems += spira.Box(layer=ls.R5,width=1.400,height=3.075,center=(0.000,2.9875))
        elems += spira.Box(layer=ls.C5R,width=0.840,height=0.520,center=(0.000,1.990))
        elems += spira.Box(layer=ls.C5R,width=0.840,height=0.520,center=(0.000,3.990))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.760, 1.760))
        elems += spira.Circle(layer=ls.J5,box_size=(2.070, 2.070))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

# JJ 329uA shunted and grounded cell
class jj_329_sg(spira.Cell):
    __name_prefix__ = 'jj_329_sg'
    def create_elements(self, elems):
        elems += spira.SRef(conns.conn_M5M6M7(), (-0.350,5.075))
        elems += spira.Box(layer=ls.M6,width=1.650,height=2.775,center=(0.000,4.7625))
        elems += spira.Box(layer=ls.M6,width=2.850,height=4.050,center=(0.000,0.600))
        elems += spira.Box(layer=ls.M5,width=1.750,height=3.575,center=(0.000,4.5125))
        elems += spira.Box(layer=ls.M5,width=3.150,height=4.300,center=(0.000,0.575))
        elems += spira.Box(layer=ls.R5,width=1.450,height=3.075,center=(0.000,3.0125))
        elems += spira.Box(layer=ls.C5R,width=0.880,height=0.520,center=(0.000,4.010))
        elems += spira.Box(layer=ls.C5R,width=0.880,height=0.520,center=(0.000,2.000))
        elems += spira.Box(layer=ls.I5,width=0.700,height=0.700,center=(0.000,5.425))
        elems += spira.Box(layer=ls.I4,width=1.000,height=1.000,center=(0.000,3.050))
        elems += spira.Circle(layer=ls.C5J,box_size=(1.780, 1.780))
        elems += spira.Circle(layer=ls.J5,box_size=(2.080, 2.080))

        return elems
    def create_ports(self,ports):
        ports += spira.Port(name="PJ",midpoint=(0.000,0.000),process=spira.RDD.PROCESS.M6)

        return ports

