import layer_setup as ls
import spira.all as spira
from spira.technologies.mit.process.database import RDD

# 1.5um junction fill cell
class FakeJJ_1p5x1p5um(spira.Device):
    __name_prefix__ = 'FakeJJ_1p5x1p5um'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M4,width=0.25*ls.tp,height=0.25*ls.tp)
        elems += spira.Box(layer=ls.M5,width=0.25*ls.tp,height=0.25*ls.tp)
        elems += spira.Box(layer=ls.J5,width=0.15*ls.tp,height=0.15*ls.tp)
        elems += spira.Box(layer=ls.C5J,width=0.13*ls.tp,height=0.13*ls.tp)
        elems += spira.Box(layer=ls.M6,width=0.2*ls.tp,height=0.2*ls.tp)

        return elems

# 3um junction fill cell
class FakeJJ_3umx3um(spira.Cell):
    __name_prefix__ = 'FakeJJ_3umx3um'
    def create_elements(self, elems):
        elems += spira.Box(layer=ls.M4,width=0.4*ls.tp,height=0.4*ls.tp)
        elems += spira.Box(layer=ls.M5,width=0.4*ls.tp,height=0.4*ls.tp)
        elems += spira.Box(layer=ls.J5,width=0.3*ls.tp,height=0.3*ls.tp)
        elems += spira.Box(layer=ls.C5J,width=0.28*ls.tp,height=0.28*ls.tp)
        elems += spira.Box(layer=ls.M6,width=0.35*ls.tp,height=0.35*ls.tp)

        return elems
