*****************************************
* Begin .SUBCKT model                   *
* spice-sdb ver 4.28.2007               *
*                                       *
*		        Version: 1.1.31			*
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
* Modified 26 Oct 2018, L Schindler, SU *
*   (Updated parameter values)	        *
* Last mod 31 Jan 2019, L Schindler, SU *
*   (Updated parameter values to		*
*		comply with layouts)	        *
*****************************************
*                   IN_A  in_B  OUT
*$Ports             in_A  in_B  out_out
.SUBCKT mitll_merget 26 31 36 
*==============  Begin SPICE netlist of main design ============
B01_rx1    25         27         jmitll     area=0.88429     
B01_rx2    30         32         jmitll     area=0.88429     
B01_tx1    14         37         jmitll     area=0.842106     
B1         1          2          jjmitll100 area=1.45438 
B2         5          6          jjmitll100 area=0.960422 
B3         3          4          jjmitll100 area=1.45438 
B4         7          8          jjmitll100 area=0.960422 
B5         9          10         jjmitll100 area=0.805138 
IB01_rx1   0          28         pwl(0 0 5p 0.000106334) 
IB01_rx2   0          33         pwl(0 0 5p 0.000106334) 
IB01_tx1   0          39         pwl(0 0 5p 5.04979e-005) 
IB1        0          12         pwl(0 0 5p 0.000186124) 
L01_rx1    26         25         2e-012 
L01_rx2    31         30         2e-012 
L02_rx1    25         11         1.27924e-012 
L02_rx2    30         13         1.27924e-012 
L02_tx1    14         35         4.81637e-012 
L1         11         1          1.75737e-012      
L1b        1          5          1e-012     
L2         6          12         2e-012      
L3         13         3          1.75737e-012      
L3b        3          7          1e-012     
L4         8          12         2e-012      
L6         12         9          2.22418e-012      
L7         9          14         8.49377e-012      
LP01_rx1   0          27         2e-013         
LP01_rx2   0          32         2e-013         
LP01_tx1   0          37         2e-013         
Lp1        2          0          2e-013     
Lp3        4          0          2e-013     
Lp5        10         0          2e-013     
LPR01_rx1  11         28         2e-013        
LPR01_rx2  13         33         2e-013        
LPR01_tx1  14         39         2e-013        
LRB01_rx1  0          29         4.58301e-012        
LRB01_rx2  0          34         4.58301e-012        
LRB01_tx1  0          38         4.80257e-012        
LRB1       16         0          2.86495e-012    
LRB2       18         6          4.23557e-012    
LRB3       15         0          2.86495e-012    
LRB4       19         8          4.23557e-012    
LRB5       17         0          5.01389e-012    
RB01_rx1   29         25         7.75753         
RB01_rx2   34         30         7.75753         
RB01_tx1   38         14         8.14613         
RB1        1          16         4.71672     
RB2        5          18         7.14259     
RB3        3          15         4.71672     
RB4        7          19         7.14259     
RB5        9          17         8.52016     
RINS_tx1   35         36         1.36        
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_merget
*******************************