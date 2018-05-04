// ---------------------------------------------------------------------------
// Verilog testbench file, created with TimEx v2.02.01
// Timing description and structural design for IARPA-BAA-14-03 via
// U.S. Air Force Research Laboratory contract FA8750-15-C-0203 and
// IARPA-BAA-16-03 via U.S. Army Research Office grant W911NF-17-1-0120.
// For questions about TimEx, contact CJ Fourie, coenrad@sun.ac.za
// (c) 2016-2018 Stellenbosch University
// ---------------------------------------------------------------------------
`timescale 1ps/100fs
module tb_mitll_splitt;
   reg in = 0;
   initial
      begin
         $dumpfile("tb_mitll_splittopt.vcd");
         $dumpvars;
         // Now in state 0
         #20 in = !in;
         // Now in state 0
      end

   initial
      begin
         $display("\t\ttime,\tin,\tout1,\tout2");
         $monitor("%d,\t%b,\t%b,\t%b",$time,in,out1,out2);
      end

   mitll_splittopt DUT (in, out1, out2);

   initial
      #30 $finish;
endmodule
