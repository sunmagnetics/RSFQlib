# RSFQlib
Author: Lieze Schindler
RSFQ cell library V1.1.31


This cell library was developed under the IARPA SuperTools/ColdFlux contract via the U.S. Army Research Office grant W911NF-17-1-0120. The aim was to create a generic RSFQ cell library which can be used by circuit designers. 
The libraries were developed using open-source tools - WRspice and XIC. 
The RSFQ library is designed with integrated Passive Transmission Line (PTL) drivers and receivers to minimize complexity and, possibly, surface area required when constructing circuits. Separate PTL driver and receiver interconnects are therefore no longer necessary when connecting the cells to PTLs. To indicate the integration of PTL drivers and receivers, the letter ‘T’ is added at the end of the cell name, for example the DFF will be referred to as DFFT.
The RSFQ cell library consists of basic logic gates which, when connected, can be used to construct more complex functions. The following core cells form the generic RSFQ cell library: JTLT, SPLITT, MERGET, DFFT, AND2T, OR2T, NOTT, XORT and NDROT. The cells are currently optimized to run at a maximum of 50 GHz.