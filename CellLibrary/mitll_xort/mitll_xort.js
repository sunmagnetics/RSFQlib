*****************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
*		        Version: 1.1.31			 *
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
.SUBCKT mitll_xort 16 59 7 26 
*==============  Begin SPICE netlist of main design ============
B01        43         44         jmitll     area=2.7984
B01_rx1    6          11         jmitll     area=0.7236
B01_rx2    58         63         jmitll     area=1.2124
B01_rx3    15         20         jmitll     area=1.2124
B02_rx1    9          10         jmitll     area=0.7720
B02_rx2    61         62         jmitll     area=1.1586
B02_rx3    18         19         jmitll     area=1.1586
B02_tx1    25         27         jmitll     area=1.3695
B03        43         72         jmitll     area=1.9159
B03_rx1    34         74         jmitll     area=0.8280
B03_rx2    52         78         jmitll     area=0.8978
B03_rx3    53         76         jmitll     area=0.8978
B04        41         42         jmitll     area=2.7984
B06        41         70         jmitll     area=1.9159
B07        37         36         jmitll     area=1.4857
B08        38         39         jmitll     area=0.9336
B09        33         40         jmitll     area=1.2859
B10        33         45         jmitll     area=1.6863
IB01       0          51         pwl(0      0 5p 8.9218e-005)
IB01_rx1   0          12         pwl(0      0 5p 0.000131858)
IB01_rx2   0          64         pwl(0      0 5p 0.000229789)
IB01_rx3   0          21         pwl(0      0 5p 0.000229789)
IB02       0          54         pwl(0      0 5p 8.9218e-005)
IB02_tx1   0          29         pwl(0      0 5p 6.64568e-005)
IB04       0          73         pwl(0      0 5p 0.000134046)
IB05       0          50         pwl(0      0 5p 0.000177629)
L01_rx1    7          6          1.8928e-012
L01_rx2    59         58         1.8604e-012
L01_rx3    16         15         1.8604e-012
L02_rx1    6          8          2.2381e-012
L02_rx2    58         60         2.1529e-012
L02_rx3    15         17         2.1529e-012
L03        72         71         2.2793e-012    
L03_rx1    8          9          2.0205e-012
L03_rx2    60         61         1.9729e-012
L03_rx3    17         18         1.9729e-012
L03_tx1    25         24         2.2261e-012
L04_rx1    9          34         2.0178e-012
L04_rx2    61         52         2.3966e-012
L04_rx3    18         53         2.3966e-012
L06        70         71         2.2793e-012    
L08        71         36         1.7515e-012    
L09        37         38         1.2620e-012    
L10        38         40         2.2246e-012    
L11        34         33         1.8033e-012    
L12        38         25         3.8658e-012    
L14        52         43         1.6354e-012    
L15        53         41         1.6354e-012    
LP01       0          44         2e-013   
LP01_rx1   0          11         2e-013
LP01_rx2   0          63         2e-013
LP01_rx3   0          20         2e-013
LP02_rx1   0          10         2e-013
LP02_rx2   0          62         2e-013
LP02_rx3   0          19         2e-013
LP02_tx1   0          27         2e-013
LP03       0          42         2e-013   
LP03_rx1   0          74         2e-013
LP03_rx2   0          78         2e-013
LP03_rx3   0          76         2e-013
LP05       0          39         2e-013   
LP06       0          45         2e-013   
LPR01      43         51         2e-013  
LPR01_rx1  8          12         2e-013
LPR01_rx2  60         64         2e-013
LPR01_rx3  17         21         2e-013
LPR02      41         54         2e-013  
LPR02_tx1  25         29         2e-013
LPR04      73         71         2e-013  
LPR05      33         50         2e-013  
LRB01      0          47         1e-012  
LRB01_rx1  0          13         1e-012
LRB01_rx2  0          65         1e-012
LRB01_rx3  0          22         1e-012
LRB02_rx1  0          14         1e-012
LRB02_rx2  0          66         1e-012
LRB02_rx3  0          23         1e-012
LRB02_tx1  0          28         1e-012
LRB03      68         72         1e-012  
LRB03_rx1  0          75         1e-012
LRB03_rx2  0          79         1e-012
LRB03_rx3  0          77         1e-012
LRB04      0          48         1e-012  
LRB06      69         70         1e-012  
LRB07      35         37         1e-012  
LRB08      0          49         1e-012  
LRB09      55         33         1e-012  
LRB10      0          46         1e-012  
RB01       47         43         2.45141   
RB01_rx1   13         6          9.47982
RB01_rx2   65         58         5.65794
RB01_rx3   22         15         5.65794
RB02_rx1   14         9          8.88542
RB02_rx2   66         61         5.92104
RB02_rx3   23         18         5.92104
RB02_tx1   28         25         5.0092
RB03       68         43         3.58061   
RB03_rx1   75         34         8.28498
RB03_rx2   79         52         7.64122
RB03_rx3   77         53         7.64122
RB04       48         41         2.45141   
RB06       69         41         3.58061   
RB07       36         35         4.61741   
RB08       49         38         7.34778   
RB09       40         55         5.33469   
RB10       46         33         4.06803   
RINS_tx1   24         26         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_xort
*******************************