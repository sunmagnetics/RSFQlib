*****************************************
* Begin .SUBCKT model                   *
* spice-sdb ver 4.28.2007               *
*                                       *
*		        Version: 1.1.31			*
*										* 
* RSFQ generic cell for MITLL sfq5ee    *
* Authored 3 Nov 2015, CJ Fourie, SU    *
* Modified 26 Oct 2018, L Schindler, SU *
*   (Updated parameter values)	        *
* Last mod 31 Jan 2019, L Schindler, SU *
*   (Updated parameter values to		*
*		comply with layouts)	        *
*****************************************
.SUBCKT mitll_dcsfq 8 11 
*==============  Begin SPICE netlist of main design ============
B1   1  2  jjmitll100 area=2.25 
B2   3  4  jjmitll100 area=2.25 
B3   5  6  jjmitll100 area=2.5 
IB1  0  2  pwl(0 0 5p 275uA)
IB2  0  5  pwl(0 0 5p 175uA)
L1   8  7  1p  
L2   7  0  3.9p  
L3   7  1  0.6p  
L4   2  3  1.1p  
L5   3  5  4.5p  
L6   5  11 2p  
Lp2  4  0  0.2p  
Lp3  6  0  0.2p  
LRB1 9  2  1p  
LRB2 10 4  1p  
LRB3 12 6  1p  
RB1  1  9  3.0488  
RB2  3  10 3.0488
RB3  5  12 2.7440
.model jjmitll100 jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_dcsfq
*******************************
