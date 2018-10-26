*****************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
*		        Version: 1.1			 *
*										 *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 1 March 2016, JA Delport, SU  *
* Modified 11 Oct 2016, CJ Fourie, SU    *
*   (Added B10, optimized)               *
* Modified 23 Mar 2018, L Schindler, SU  *
*	(Added PTL drivers & Receivers and   *
*	  reduced JJ count)      			 *
* Modified 30 Apr 2018, L Schindler, SU  *
*	(Optimized cell)					 *
* Last mod 26 Oct 2018, L Schindler, SU  *
*   (Updated parameter values)	         *
******************************************
*                 IN_A   IN_B   CLK   OUT
*$Ports             in_A  in_B  in_clk  out_out
.SUBCKT mitll_or2t 62 54 5 16 
*==============  Begin SPICE netlist of main design ============
B01        30         31         jmitll     area=1.9518
B01_rx1    4          9          jmitll     area=0.8056
B01_rx2    53         55         jmitll     area=1.1720
B01_rx3    61         63         jmitll     area=1.1720
B01_tx1    13         17         jmitll     area=1.9004
B02        30         34         jmitll     area=1.3074
B02_rx1    7          67         jmitll     area=0.7521
B03        32         33         jmitll     area=1.9518
B03_rx1    7          8          jmitll     area=0.6339
B04        32         35         jmitll     area=1.3074
B05        36         37         jmitll     area=1.7221
B08        22         23         jmitll     area=1.3953
B09        14         26         jmitll     area=1.6170
B10        48         36         jmitll     area=2.2048
IB01       0          47         pwl(0      0 5p 0.0003277005)
IB01_rx1   0          10         pwl(0      0 5p 9.8325e-05)
IB01_rx2   0          56         pwl(0      0 5p 0.0001412752)
IB01_rx3   0          64         pwl(0      0 5p 0.0001412752)
IB01_tx1   0          19         pwl(0      0 5p 0.0001765029)
IB02       0          29         pwl(0      0 5p 8.1358e-05)
IB04       0          50         pwl(0      0 5p 8.0964e-05)
L01        38         30         2.6809e-12
L01_rx1    5          4          1.4136e-12
L01_rx2    54         53         2.0307e-12
L01_rx3    62         61         2.0307e-12
L01_tx1    14         13         4.2904e-12
L02        34         39         1.3486e-12
L02_rx1    4          6          3.3652e-12
L02_rx2    53         40         2.0822e-12
L02_rx3    61         38         2.0822e-12
L02_tx1    13         15         2.7779e-12
L03        40         32         1.1992e-012    
L03_rx1    6          7          4.0267e-12
L04        35         39         1.3486e-12   
L05        39         41         3.7250e-13
L06        41         48         1.8890e-12
L07        36         28         2.1922e-13 
L08        28         8          5.4916e-12
L09        8          22         1.5727e-12
L13        22         25         2.0776e-12  
L14        25         14         8.8496e-13
LP01       31         0          2e-013   
LP01_rx1   0          9          3.4e-013
LP01_rx2   0          55         3.4e-013
LP01_rx3   0          63         3.4e-013
LP01_tx1   0          17         5e-014
LP02_rx1   0          67         3.4e-013
LP03       33         0          2e-013   
LP05       37         0          2e-013   
LP08       0          23         1.17e-013   
LP09       0          26         1.51e-013   
LP_IB01    41         47         2e-013
LP_IB02    28         29         2e-013
LP_IB04    25         50         2e-013
LPR01_rx1  6          10         2e-013
LPR01_rx2  40         56         2e-013
LPR01_rx3  38         64         2e-013
LPR01_tx1  13         19         2e-013
LRB01      43         0          1e-012  
LRB01_rx1  0          11         5e-013
LRB01_rx2  0          57         5e-013
LRB01_rx3  0          65         5e-013
LRB01_tx1  0          18         1e-012
LRB02      45         34         1e-012  
LRB02_rx1  0          68         5e-013
LRB03      42         0          1e-012  
LRB03_rx1  8          12         1e-012
LRB04      46         35         1e-012  
LRB05      44         0          1e-012  
LRB08      24         0          1e-012  
LRB09      27         0          1e-012  
LRB10      49         36         1e-012  
RB01       30         43         4.7755   
RB01_rx1   11         4          13.7683
RB01_rx2   57         53         9.01423
RB01_rx3   65         61         9.01423
RB01_tx1   18         13         4.82513
RB02       30         45         6.68158   
RB02_rx1   68         7          9.67072
RB03       32         42         4.7755   
RB03_rx1   12         7          10.9809
RB04       32         46         6.68158   
RB05       36         44         6.37527   
RB08       24         22         6.79868   
RB09       27         14         3.8504   
RB10       48         49         3.68953   
RINS_tx1   15         16         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_or2t
*******************************