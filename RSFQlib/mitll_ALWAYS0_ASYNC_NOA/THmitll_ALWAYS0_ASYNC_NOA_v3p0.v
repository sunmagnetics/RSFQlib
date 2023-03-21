// ---------------------------------------------------------------------------
// Author: L. Schindler
// Version: 3.0
// Last modification date: 23 August 2022
// Last modification by: T. Hall
// ---------------------------------------------------------------------------
// Timing description and structural design for IARPA-BAA-14-03 via
// U.S. Air Force Research Laboratory contract FA8750-15-C-0203 and
// IARPA-BAA-16-03 via U.S. Army Research Office grant W911NF-17-1-0120.
// For questions about TimEx, contact CJ Fourie, coenrad@sun.ac.za
// (c) 2016-2020 Stellenbosch University
// ---------------------------------------------------------------------------
`timescale 1ps/100fs
module THmitll_ALWAYS0_ASYNC_NOA (q);


output
  q;

reg
  q;
  
initial
   begin
      q = 0; // Output always 0
   end

always
	begin
	#10 q = 0; // Output always 0
	end
endmodule
