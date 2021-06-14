// ---------------------------------------------------------------------------
// Author: L. Schindler
// Version: 2.1
// Last modification date: 8 June 2021
// Last modification by: L. Schindler
// ---------------------------------------------------------------------------

// ---------------------------------------------------------------------------
// Automatically extracted verilog file, created with TimEx v2.05
// Timing description and structural design for IARPA-BAA-14-03 via
// U.S. Air Force Research Laboratory contract FA8750-15-C-0203 and
// IARPA-BAA-16-03 via U.S. Army Research Office grant W911NF-17-1-0120.
// For questions about TimEx, contact CJ Fourie, coenrad@sun.ac.za
// (c) 2016-2020 Stellenbosch University
// ---------------------------------------------------------------------------
`ifndef begin_time
`define begin_time 8
`endif
`timescale 1ps/100fs

`celldefine
module LSmitll_NOT_v2p1_optimized #(parameter begin_time = `begin_time) (a, clk, q);

// Define inputs
input
  a, clk;

// Define outputs
output
  q;

// Define internal output variables
reg
  internal_q;
assign q = internal_q;

// Define state
integer state;

wire
  internal_state_0, internal_state_1;

assign internal_state_0 = state === 0;
assign internal_state_1 = state === 1;

specify
  specparam delay_state0_clk_q = 10.8;

  specparam ct_state0_a_clk = 2.6;
  specparam ct_state0_clk_a = 8.4;
  specparam ct_state0_clk_clk = 12.8;
  specparam ct_state1_a_clk = 4.2;

  if (internal_state_0) (clk => q) = delay_state0_clk_q;

  $hold( posedge a &&& internal_state_0, clk, ct_state0_a_clk);
  $hold( negedge a &&& internal_state_0, clk, ct_state0_a_clk);
  $hold( posedge clk &&& internal_state_0, a, ct_state0_clk_a);
  $hold( negedge clk &&& internal_state_0, a, ct_state0_clk_a);
  $hold( posedge clk &&& internal_state_0, clk, ct_state0_clk_clk);
  $hold( negedge clk &&& internal_state_0, clk, ct_state0_clk_clk);
  $hold( posedge a &&& internal_state_1, clk, ct_state1_a_clk);
  $hold( negedge a &&& internal_state_1, clk, ct_state1_a_clk);
endspecify

// Set initial state
initial begin
   state = 1'bX;
   internal_q = 0; // All outputs start at 0
   #begin_time state = 0;
   end

always @(posedge a or negedge a)
case (state)
   0: begin
      state = 1;
   end
   1: begin
   end
endcase
always @(posedge clk or negedge clk)
case (state)
   0: begin
      internal_q = !internal_q;
   end
   1: begin
      state = 0;
   end
endcase

endmodule
`endcelldefine
