*****************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
* RSFQ generic cell for MITLL sfq5ee     *
* Project under IARPA-BAA-16-03          *
* Authored 5 Nov 2015, CJ Fourie, SU     *
* Modified 1 March 2016, JA Delport, SU  *
* Modified 23 Aug 2016, CJ Fourie, SU    *
* Modified 9 Oct 2016, CJ Fourie, SU     *
*   (added DMP junction B2, optmized)    *
* Modified 23 Mar 2018, L Schindler, SU  *
*	(Added PTL drivers & Receivers and   *
*	  reduced JJ count)      			 *
* Last mod 30 April 2018, L Schindler, SU *
*	(Optimized cell)					 *
******************************************
*					in		clk		out
*$Ports             in_in  in_clk  out_out
.SUBCKT mitll_dfft 9 7 10 
*
*==============  Begin SPICE netlist of main design ============
B01rx1     20         22         jmitll     area=0.793833
B01rx2     12         16         jmitll     area=0.906104
B01tx      26         27         jmitll     area=3.02709
B02rx2     14         15         jmitll     area=0.963766
B1         30         31         jmitll     area=1.42778
B2         39         52         jmitll     area=1.49875
B3         45         51         jmitll     area=0.960227
B4         32         33         jmitll     area=1.6952
B5         43         32         jmitll     area=1.17345
B6         36         37         jmitll     area=1.36404
B7         34         35         jmitll     area=1.49997
IB01rx1    0          23         pwl(0      0 5p 0.000115456)
IB01rx2    0          17         pwl(0      0 5p 0.000101889)
IB01tx     0          29         pwl(0      0 5p 0.000181403)
IB1        0          53         pwl(0      0 5p 0.000120402)
IB2        0          54         pwl(0      0 5p 6.34786e-005)
IB3        0          55         pwl(0      0 5p 0.000153633)
IB4        0          56         pwl(0      0 5p 0.00016173)
L01rx1     9          20         1.40665e-012 
L01rx2     7          12         1.23102e-012 
L01tx1     26         25         1.80401e-012 
L02rx1     20         21         3.29467e-012 
L02rx2     12         13         2.44036e-012 
L03rx2     13         14         3.64944e-012 
L1         21         30         1.12845e-012     
L2a        30         48         5.40283e-013    
L2b        48         39         1.60289e-012    
L3a        45         49         9.45374e-013    
L3b        49         32         4.44009e-012    
L4         52         45         1.11414e-012     
L5a        32         50         3.63494e-012    
L5b        50         34         5.93935e-013    
L6         34         26         1.32327e-012     
L7         36         43         1.9079e-012     
L8         14         36         1.79764e-012     
LIB01rx2   13         17         2e-013
LIB01tx    26         29         2e-013
LIB2       49         54         2e-013   
LIB3       50         55         2e-013   
LPB01rx1   0          22         3.4e-013
LPB01rx2   0          16         3.4e-013
LPB01tx    0          27         5e-014
LPB02rx2   0          15         6e-014
LPB1       31         0          2e-013   
LPB3       51         0          2e-013   
LPB4       33         0          2e-013   
LPB6       37         0          2e-013   
LPB7       35         0          2e-013   
LPIB01rx1  21         23         2e-013
LPIB1      48         53         2e-013  
LPIB4      56         36         2e-013  
LRB01rx1   0          24         5e-013
LRB01rx2   0          18         5e-013
LRB01tx    0          28         1e-012
LRB02rx2   0          19         1e-012
LRB1       41         0          1e-012   
LRB2       38         52         1e-012   
LRB3       44         0          1e-012   
LRB4       46         0          1e-012   
LRB5       42         32         1e-012   
LRB6       40         0          1e-012   
LRB7       47         0          1e-012   
RB01rx1    24         20         8.6415
RB01rx2    18         12         7.57077
RB01tx     28         26         2.26617 
RB02rx2    19         14         7.11781
RB1        30         41         4.80461    
RB2        39         38         4.5771    
RB3        45         44         7.14404    
RB4        32         46         4.04666    
RB5        43         42         5.84592    
RB6        40         36         5.02909    
RB7        34         47         4.57337    
RINStx     25         10         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_dfft
*******************************
