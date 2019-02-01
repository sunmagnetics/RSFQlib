******************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
*		        Version: 1.1.31			 *
*										 *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 2 Nov 2015, CJ Fourie, SU     *
* Modified 23 Aug 2016, CJ Fourie, SU    *
* Modified 23 Mar 2018, L Schindler, SU  *
*	(Added PTL drivers & Receivers and   *
*	  reduced JJ count)      			 *
* Modified 30 April 2018, L Schindler, SU *
*	(Optimized cell)					 *
* Last mod 26 Oct 2018, L Schindler, SU  *
*   (Updated parameter values)	         *
******************************************
*					in		out
*$Ports             in_in  out_out
.SUBCKT mitll_jtlt 2 13 
*==============  Begin SPICE netlist of main design ============
B01rx1     1          6          jmitll     area=0.6979
B01tx1     10         14         jmitll     area=1.7851
B02rx1     4          5          jmitll     area=0.4432
B1         17         21         jmitll     area=0.4881
B2         11         22         jmitll     area=0.4881
IB01rx1    0          7          pwl(0      0 5p 8.6451e-05)
IB01tx1    0          16         pwl(0      0 5p 5.5312e-05)
IB1        0          23         pwl(0      0 5p 0.00012008)
L01rx1     2          1          3.3252e-13    
L01tx1     11         10         2.32563e-12    
L02rx1     1          3          2.40322e-12    
L03rx1     3          4          1.67725e-12  
L03tx1     10         12         2.36302e-12     
L1         4          17         2.51091e-12       
L2         17         18         8.66521e-13       
L3         18         11         8.66521e-13       
LB1        19         0          1p        
LB2        20         0          1p        
LP01       18         23         0.2p      
LP01rx1    0          6          0.34p     
LP01tx1    0          14         0.05p     
LP02rx1    0          5          0.06p     
Lp1        21         0          0.2p      
Lp2        22         0          0.2p      
LPR01rx1   3          7          0.2p      
LPR01tx1   10         16         0.2p      
LRB01rx1   0          8          0.5p      
LRB01tx1   0          15         1p        
LRB02rx1   0          9          1p        
RB01rx1    8          1          9.8294       
RB01tx1    15         10         3.84286     
RB02rx1    9          4          15.4797       
RB1        17         19         14.0557        
RB2        11         20         14.0557        
RINStx1    12         13         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_jtlt
*******************************
