*****************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
*		        Version: 1.1			 *
*										 *
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
* Modified 30 Apr 2018, L Schindler, SU  *
*	(Optimized cell)					 *
* Last mod 26 Oct 2018, L Schindler, SU  *
*   (Updated parameter values)	         *
******************************************
*					in		clk		out
*$Ports             in_in  in_clk  out_out
.SUBCKT mitll_dfft 9 7 10 
*
*==============  Begin SPICE netlist of main design ============
B01rx1     20         22         jmitll     area=0.7938
B01rx2     12         16         jmitll     area=0.9061
B01tx      26         27         jmitll     area=3.0271
B02rx2     14         15         jmitll     area=0.9638
B1         30         31         jmitll     area=1.4278
B2         39         52         jmitll     area=1.4988
B3         45         51         jmitll     area=0.9602
B4         32         33         jmitll     area=1.6952
B5         43         32         jmitll     area=1.1735
B6         36         37         jmitll     area=1.3640
B7         34         35         jmitll     area=1.5000
IB01rx1    0          23         pwl(0      0 5p 0.000115456)
IB01rx2    0          17         pwl(0      0 5p 0.000101889)
IB01tx     0          29         pwl(0      0 5p 0.000181403)
IB1        0          53         pwl(0      0 5p 0.0001204025)
IB2        0          54         pwl(0      0 5p 6.34786e-005)
IB3        0          55         pwl(0      0 5p 0.00015363)
IB4        0          56         pwl(0      0 5p 0.00016173)
L01rx1     9          20         1.4067e-012 
L01rx2     7          12         1.2310e-012 
L01tx1     26         25         1.8040e-012 
L02rx1     20         21         3.2947e-012 
L02rx2     12         13         2.4404e-012 
L03rx2     13         14         3.6494e-012 
L1         21         30         1.1285e-012     
L2a        30         48         5.4028e-013    
L2b        48         39         1.6029e-012    
L3a        45         49         9.4537e-013    
L3b        49         32         4.4401e-012    
L4         52         45         1.1141e-012     
L5a        32         50         3.6349e-012    
L5b        50         34         5.9394e-013    
L6         34         26         1.3233e-012     
L7         36         43         1.9079e-012     
L8         14         36         1.7976e-012     
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
RB01rx2    18         12         7.5708
RB01tx     28         26         2.2662 
RB02rx2    19         14         7.1178
RB1        30         41         4.8046    
RB2        39         38         4.5771    
RB3        45         44         7.1440    
RB4        32         46         4.0467    
RB5        43         42         5.8459    
RB6        40         36         5.0291    
RB7        34         47         4.5734    
RINStx     25         10         1.36      
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_dfft
*******************************
