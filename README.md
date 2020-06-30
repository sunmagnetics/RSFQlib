# RSFQlib
Author: Lieze Schindler
RSFQ cell library V1.5.1


This RSFQ cell library is developed under the IARPA SuperTools/ColdFlux contract via the U.S. Army Research Office grant W911NF-17-1-0120. The aim is to create a generic and open-source cell library with RSFQ logic as part of the IARPA SuperTools Program.

The free and open-source tools Xic, JoSIM, JoSIM-tools, KLayout and TimEx are used to develop and test the RSFQ cells. The circuit schematics are drawn using Xic. JoSIM is used as the SPICE engine for simulating the cells, while JoSIM-tools is used for operating margin analysis as well as cell parameter optimization. TimEx is used to extracted the characteristics of the cell to generate the Mealy Finite State Machine diagram and Verilog files.

The RSFQ cell library is currently designed to only be connected using Passive Transmission Lines (PTLs). The cells are designed with integrated PTL transmitters and receivers to minimize complexity and surface area required on a chip. Separate PTL transmitters and receivers are therefore no longer necessary when connecting the cells to PTLs. To indicate the integration of PTL transmitters and receivers within a cell, the letter 'T' is added at the end of a cell name, for example the DFF with integrated PTL transmitters and receivers will be referred to as DFFT.

The following core cells are included in the RSFQ cell library:
  - Interconnects: JTLT, SPLITT, MERGET, PTLTX and PTLRX.
  - Logic cells: AND2T, OR2T, XORT and NOTT.
  - Buffers: DFFT, NDROT, BUFF and BUFFT.
  - Interfacing cells: DCSFQ, DCSFQ-PTLTX, PTLRX-SFQDC and SFQDC.
  
More complex functions can be constructed through connecting several core cells. Versions of each cell without integrated PTL transmitters and receivers are also in development. The cells are currently optimized to run at a maximum clock frequency of 50 GHz.
