******************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
*		        Version: 1.1.31			 *
*										 *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 5 March 2016, JA Delport, SU  *
* Modified 28 Nov 2016, CJ Fourie, SU    *
*   (Deleted current sources, altered    *
*    circuit to make functional;         *
*    optimized)                          *
* Modified 23 Mar 2018, L Schindler, SU  *
*	(Added PTL drivers & Receivers and   *
*	  reduced JJ count)      			 *
* Last mod 20 April 2018, L Schindler, SU *
*    (Adapted to work with TimEx to      *
*     produce verilog file)              *
* Last mod 26 Oct 2018, L Schindler, SU  *
*   (Updated parameter values)	         *
******************************************
*                 IN_IN    CLK     OUT
*$Ports           in_in    in_clk  out_out
.SUBCKT mitll_nott 51 46 57 
*==============  Begin SPICE netlist of main design ============
B01        12         13         jmitll     area=1.3488
B01_rx2    45         47         jmitll     area=1.2476
B01_rx1    50         52         jmitll     area=1.2613
B01_tx1    55         58         jmitll     area=2.8510
B02        8          10         jmitll     area=0.7718
B03        21         8          jmitll     area=1.2227
B05        5          6          jmitll     area=1.2221
B06        15         16         jmitll     area=1.0432
B07        1          3          jmitll     area=2.2139
B09        18         19         jmitll     area=1.4100
B10        24         25         jmitll     area=1.7227
B11        28         29         jmitll     area=1.4193
IB01_rx2   0          48         pwl(0      0 5p 0.000181215)
IB01_rx1   0          53         pwl(0      0 5p 0.000146094)
IB01_tx1   0          60         pwl(0      0 5p 0.000187178)
IB02       0          9          pwl(0      0 5p 9.6978e-05)
IB03       0          31         pwl(0      0 5p 9.5221e-05)
IB04       0          38         pwl(0      0 5p 0.000101564)
IB06       0          44         pwl(0      0 5p 0.000108369)
L01        5          13         2.2847e-012    
L01_rx2    46         45         2.1457e-012
L01_rx1    51         50         1.8571e-012
L01_tx1    18         55         4.5195e-012
L02_rx2    45         2          2.5468e-012
L02_rx1    50         30         4.4718e-012
L02_tx1    55         56         3.4724e-012
L03        5          7          6.5962e-012    
L04        7          8          4.2413e-013    
L06        4          5          3.2860e-012    
L07        12         10         4.9986e-013    
L08        23         21         8.6946e-013    
L09        12         15         2.8417e-013    
L10        15         17         5.3651e-012
L12        27         23         2.6532e-012    
L13        2          1          2.1566e-012    
L16        30         28         2.6117e-012    
L17        1          4          9.9180e-013    
L18        23         24         2.5842e-013    
L19        24         26         3.1681e-012    
L20        28         27         1.1676e-012    
L21        17         18         7.4611e-013    
LP01_rx2   0          47         3.4e-013
LP01_rx1   0          52         3.4e-013
LP01_tx1   0          58         5e-014
LP05       0          6          5.67e-013   
LP06       0          16         2.7e-013   
LP07       0          3          3.28e-013   
LP09       0          19         1.2e-013   
LP10       0          25         2.39e-013   
LP11       0          29         1.09e-013   
LPR01_rx2  2          48         2e-013
LPR01_rx1  30         53         2e-013
LPR01_tx1  55         60         2e-013
LPR02      7          9          2.3e-014  
LPR03      4          31         2.08e-013  
LPR04      27         38         2.16e-013  
LPR06      17         44         1.3e-013  
LRB01      14         12         1e-012  
LRB01_rx2  0          49         1e-012
LRB01_rx1  0          54         1e-012
LRB01_tx1  0          59         1e-012
LRB02      10         11         1e-012  
LRB03      21         22         1e-012  
LRB05      0          33         1e-012  
LRB06      0          34         1e-012  
LRB07      0          32         1e-012  
LRB09      0          35         1e-012  
LRB10      0          37         1e-012  
LRB11      0          36         1e-012  
RB01       14         13         5.08598   
RB01_rx2   49         45         4.73894
RB01_rx1   54         50         7.9642
RB01_tx1   59         55         2.58771
RB02       11         8          8.88809   
RB03       22         8          5.61061   
RB05       33         5          7.43943   
RB06       34         15         6.57567   
RB07       32         1          3.09855   
RB09       35         18         4.86536   
RB10       37         24         3.98204   
RB11       36         28         4.83327   
RD         26         0          3.54      
RINS_tx1   56         57         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_nott
