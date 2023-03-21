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
module THmitll_XORT_v3p0_extracted #(parameter begin_time = `begin_time) (a, b, clk, q);

// Define inputs
input
  a, b, clk;

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
  internal_state_0, internal_state_1, internal_state_2;

assign internal_state_0 = state === 0;
assign internal_state_1 = state === 1;
assign internal_state_2 = state === 2;

specify
  specparam delay_state1_clk_q = 8.8;
  specparam delay_state2_clk_q = 8.8;

  specparam ct_state0_clk_a = 3.2;
  specparam ct_state0_clk_b = 3.1;
  specparam ct_state1_a_b = 9.5;
  specparam ct_state1_a_clk = 6.6;
  specparam ct_state1_b_b = 5.2;
  specparam ct_state1_clk_b = 7.8;
  specparam ct_state2_a_a = 5.2;
  specparam ct_state2_b_a = 9.5;
  specparam ct_state2_b_clk = 6.7;
  specparam ct_state2_clk_a = 7.6;

  if (internal_state_1) (clk => q) = delay_state1_clk_q;
  if (internal_state_2) (clk => q) = delay_state2_clk_q;

  $hold( posedge clk &&& internal_state_0, a, ct_state0_clk_a);
  $hold( negedge clk &&& internal_state_0, a, ct_state0_clk_a);
  $hold( posedge clk &&& internal_state_0, b, ct_state0_clk_b);
  $hold( negedge clk &&& internal_state_0, b, ct_state0_clk_b);
  $hold( posedge a &&& internal_state_1, b, ct_state1_a_b);
  $hold( negedge a &&& internal_state_1, b, ct_state1_a_b);
  $hold( posedge a &&& internal_state_1, clk, ct_state1_a_clk);
  $hold( negedge a &&& internal_state_1, clk, ct_state1_a_clk);
  $hold( posedge b &&& internal_state_1, b, ct_state1_b_b);
  $hold( negedge b &&& internal_state_1, b, ct_state1_b_b);
  $hold( posedge clk &&& internal_state_1, b, ct_state1_clk_b);
  $hold( negedge clk &&& internal_state_1, b, ct_state1_clk_b);
  $hold( posedge a &&& internal_state_2, a, ct_state2_a_a);
  $hold( negedge a &&& internal_state_2, a, ct_state2_a_a);
  $hold( posedge b &&& internal_state_2, a, ct_state2_b_a);
  $hold( negedge b &&& internal_state_2, a, ct_state2_b_a);
  $hold( posedge b &&& internal_state_2, clk, ct_state2_b_clk);
  $hold( negedge b &&& internal_state_2, clk, ct_state2_b_clk);
  $hold( posedge clk &&& internal_state_2, a, ct_state2_clk_a);
  $hold( negedge clk &&& internal_state_2, a, ct_state2_clk_a);
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
   2: begin
      state = 0;
   end
endcase
always @(posedge b or negedge b)
case (state)
   0: begin
      state = 2;
   end
   1: begin
      state = 0;
   end
   2: begin
   end
endcase
always @(posedge clk or negedge clk)
case (state)
   0: begin
   end
   1: begin
      internal_q = !internal_q;
      state = 0;
   end
   2: begin
      internal_q = !internal_q;
      state = 0;
   end
endcase

endmodule
`endcelldefine
