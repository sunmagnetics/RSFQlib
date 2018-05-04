// ---------------------------------------------------------------------------
// Verilog testbench file, created with TimEx v2.02.01
// Timing description and structural design for IARPA-BAA-14-03 via
// U.S. Air Force Research Laboratory contract FA8750-15-C-0203 and
// IARPA-BAA-16-03 via U.S. Army Research Office grant W911NF-17-1-0120.
// For questions about TimEx, contact CJ Fourie, coenrad@sun.ac.za
// (c) 2016-2018 Stellenbosch University
// ---------------------------------------------------------------------------
`timescale 1ps/100fs
module tb_test_nott;
   reg in = 0;
   reg clk = 0;
   initial
      begin
         $dumpfile("tb_test_nott.vcd");
         $dumpvars;
         // Now in state 0
         #20 in = !in;
         // Now in state 1
         #10 in = !in;
         // Now in state 1
         #10 clk = !clk;
         // Now in state 0
         #10 clk = !clk;
         // Now in state 0
      end

   initial
      begin
         $display("\t\ttime,\tin,\tclk,\tout");
         $monitor("%d,\t%b,\t%b,\t%b",$time,in,clk,out);
      end

   test_nott DUT (in, clk, out);

   initial
      #60 $finish;
endmodule
