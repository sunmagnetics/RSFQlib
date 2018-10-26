*****************************************
* Begin .SUBCKT model                   *
* spice-sdb ver 4.28.2007               *
*                                       *
*		        Version: 1.1			*
*										*
* RSFQ generic cell for MITLL sfq5ee    *
* Project under IARPA-BAA-16-03         *
* Authored 3 Nov 2015, CJ Fourie, SU    *
* Last mod 23 Mar 2018, L Schindler, SU *
*	(Added PTL drivers & Receivers and  *
*	  reduced JJ count)      			*
* Modified 23 Mar 2018, L Schindler, SU *
*	(Added PTL drivers & Receivers and  *
*	  reduced JJ count)      			*
* Modified 30 Apr 2018, L Schindler, SU *
*	(Optimized cell)					*
* Last mod 26 Oct 2018, L Schindler, SU *
*   (Updated parameter values)	        *
*****************************************
*                   IN_A  in_B  OUT
*$Ports             in_A  in_B  out_out
.SUBCKT mitll_merget 24 29 34 
*==============  Begin SPICE netlist of main design ============
B01_rx1    23         25         jmitll     area=0.4061
B01_rx2    28         30         jmitll     area=0.4061
B01_tx1    12         35         jmitll     area=1.6170
B1         1          2          jmitll     area=1.3297
B2         1          5          jmitll     area=0.9442
B3         3          4          jmitll     area=1.3297
B4         3          6          jmitll     area=0.9442
B5         7          8          jmitll     area=0.4700
IB01_rx1   0          26         pwl(0      0 5p 5.7813e-05)
IB01_rx2   0          31         pwl(0      0 5p 5.7813e-05)
IB01_tx1   0          37         pwl(0      0 5p 9.8658e-05)
IB1        0          10         pwl(0      0 5p 2.1302e-04)
L01_rx1    24         23         1.0229e-13
L01_rx2    29         28         1.0229e-13
L02_rx1    23         9          3.6521e-13
L02_rx2    28         11         3.6521e-13
L02_tx1    12         33         7.9683e-13
L1         9          1          1.9845e-12  
L2         5          10         4.2510e-13 
L3         11         3          1.9845e-12
L4         6          10         4.2510e-13    
L6         10         7          3.2498e-12  
L7         7          12         3.1137e-12
LP01_rx1   0          25         3.4e-013
LP01_rx2   0          30         3.4e-013
LP01_tx1   0          35         5e-014
Lp1        2          0          2e-013    
Lp3        4          0          2e-013    
Lp5        8          0          2e-013    
LPR01_rx1  9          26         2e-013
LPR01_rx2  11         31         2e-013
LPR01_tx1  12         37         2e-013
LRB01_rx1  0          27         5e-013
LRB01_rx2  0          32         5e-013
LRB01_tx1  0          36         1e-012
LRB1       14         0          1e-012   
LRB2       16         5          1e-012   
LRB3       13         0          1e-012   
LRB4       17         6          1e-012   
LRB5       15         0          1e-012   
RB01_rx1   27         23         16.8923
RB01_rx2   32         28         16.8923
RB01_tx1   36         12         4.24229
RB1        1          14         5.15887    
RB2        1          16         7.26569     
RB3        3          13         5.15887    
RB4        3          17         7.26569      
RB5        7          15         14.5969      
RINS_tx1   33         34         1.36       
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_merget
*******************************