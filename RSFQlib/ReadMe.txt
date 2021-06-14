Author: L. Schindler
Version: 2.1
Release date: 11 June 2021

-----------------------------------------------------------------------------------------

Copyright (c) 2018-2021 Lieze Schindler, Stellenbosch University

Permission is hereby granted, free of charge, to any person obtaining a copy
of this cell library and associated documentation files (the "Library"), to deal
in the Library without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Library, and to permit persons to whom the Library is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Library.

THE LIBRARY IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE LIBRARY OR THE USE OR OTHER DEALINGS IN THE
LIBRARY.


-----------------------------------------------------------------------------------------

For questions about the library, contact Lieze Schindler, lschindler@sun.ac.za

-----------------------------------------------------------------------------------------

This RSFQ cell library is developed under the IARPA SuperTools/ColdFlux contract via the U.S. Army Research Office grant W911NF-17-1-0120. The aim is to create a generic and open-source cell library with RSFQ logic~\cite{Likharev:RSFQ} as part of the IARPA SuperTools.

The free and open-source tools XIC, JoSIM, JoSIM-tools, KLayout and TimEx are used to develop and test the RSFQ cells. The circuit schematics are drawn using XIC. JoSIM is used as the SPICE engine for simulating the cells, while JoSIM-tools is used for operating margin analysis as well as cell parameter optimization. KLayout is used to construct the cell layouts. TimEx is used to extract the characteristics of the cell to generate the Mealy Finite State Machine diagram and Verilog files. Icarus Verilog and GTKWave can be used to simulate and view the verilog files for each cell. Additionally, InductEx is used for impedance extraction during cell layout design. A free version of InductEx is available, but has limited capacity.

Version 2.1 of the RSFQ cell library includes two versions of each cell: one with standard connections designed to be connected directly with other cells, and a version designed to be connected to Passive Transmission Lines (PTLs). The version of the cell designed to be connected to PTLs include integrated PTL transmitter and receiver cells. To indicate the integration of PTL transmitters and receivers within a cell, the letter `T' is added at the end of a cell name, for example the DFF with integrated PTL transmitters and receivers will be referred to as DFFT.

The following core cells are included in the RSFQ cell library:
  Interconnects: JTL, JTLT, SPLIT, SPLITT, MERGE, MERGET, PTLTX, PTLRX, Always0 (synchronous and asynchronous) and Always0T (synchronous and asynchronous).
  Logic cells: AND2, AND2T, OR2, OR2T, XOR, XORT, NOT, NOTT, XNOR, XNORT.
  Buffers: DFF, DFFT, NDRO, NDROT, BUFF and BUFFT.
  Interfacing cells: DCSFQ, DCSFQ-PTLTX, PTLRX-SFQDC and SFQDC.

More complex functions can be constructed through connecting several core cells. The cells are currently optimized to run at a maximum clock frequency of 50 GHz.

-----------------------------------------------------------------------------------------

!...The XIC schematic files are included as a visual reference. If any inconsistencies
arise between the XIC schematic and the .cir file, the .cir file should be assumed
as correct...!

-----------------------------------------------------------------------------------------