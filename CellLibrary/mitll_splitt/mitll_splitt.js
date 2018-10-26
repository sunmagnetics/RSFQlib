******************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
*		        Version: 1.1			 *
*										 *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 3 Nov 2015, CJ Fourie, SU     *
* Modified 8 Nov 2016, CJ Fourie, SU     *
*   (Added TimEx port descriptors)       *
* Modified 23 Mar 2018, L Schindler, SU  *
*	(Added PTL drivers & Receivers and   *
*	  reduced JJ count)      			 *
* Modified 30 Apr 2018, L Schindler, SU  *
*	(Optimized cell)					 *
* Last mod 26 Oct 2018, L Schindler, SU  *
*   (Updated parameter values)	         *
******************************************
*                      in out1 out2
*$Ports                in_in  out_out1  out_out2
.SUBCKT MITLL_SPLITT 5 13 36 
*==============  Begin SPICE netlist of main design ============
B01_rx2    4          6          jjmitll100 area=1.0070
B01_tx1    9          14         jjmitll100 area=1.6993
B01_tx2    33         37         jjmitll100 area=1.6993
B1         19         20         jjmitll100 area=1.6960
B2         21         22         jjmitll100 area=1.2095
B3         23         24         jjmitll100 area=1.2095
IB01_rx2   0          7          pwl(0      0 5p 0.000134948)
IB01_tx1   0          16         pwl(0      0 5p 7.6267e-005)
IB01_tx2   0          39         pwl(0      0 5p 7.6267e-005)
IB1        0          31         pwl(0      0 5p 0.000359683)
L01_rx2    5          4          2.6757e-013
L02_tx1    9          12         2.2253e-012
L02_tx2    33         35         2.2253e-012
L1         4          19         1.5259e-012     
L2         19         25         2.9154e-012     
L3         25         26         4.8137e-013     
L4         26         21         1.2716e-012     
L5         21         9          1.2572e-012     
L6         26         23         1.2716e-012     
L7         23         33         1.2572e-012     
LP01_rx2   0          6          3.4e-013
LP01_tx1   0          14         5e-014
LP01_tx2   0          37         5e-014
Lp1        20         0          2e-013    
Lp2        22         0          2e-013    
Lp3        24         0          2e-013    
LP_IB1     25         31         2e-013 
LPR01_rx2  4          7          2e-013
LPR01_tx1  9          16         2e-013
LPR01_tx2  33         39         2e-013
LRB01_rx2  0          8          5e-013
LRB01_tx1  0          15         1e-012
LRB01_tx2  0          38         1e-012
LRB1       28         0          1e-012   
LRB2       30         0          1e-012   
LRB3       29         0          1e-012   
RB01_rx2   8          4          6.81198
RB01_tx1   15         9          4.03684
RB01_tx2   38         33         4.03684
RB1        19         28         4.04483    
RB2        21         30         5.67164    
RB3        23         29         5.67164    
RINS_tx1   12         13         1.36      
RINS_tx2   35         36         1.36            
.model jjmitll100 jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends MITLL_SPLITT
