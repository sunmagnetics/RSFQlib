// ---------------------------------------------------------------------------
// Automatically extracted verilog file, created with TimEx v2.05
// Timing description and structural design for IARPA-BAA-14-03 via
// U.S. Air Force Research Laboratory contract FA8750-15-C-0203 and
// IARPA-BAA-16-03 via U.S. Army Research Office grant W911NF-17-1-0120.
// For questions about TimEx, contact CJ Fourie, coenrad@sun.ac.za
// (c) 2016-2018 Stellenbosch University
// ---------------------------------------------------------------------------
`timescale 1ps/100fs
module THmitll_SPLITT_v3p0_extracted (a, q0, q1);

input
  a;

output
  q0, q1;

reg
  q0, q1;

real
  delay_state0_a_q0 = 7.3,
  delay_state0_a_q1 = 7.3,
  ct_state0_a_a = 11.1;

reg
   errorsignal_a;

integer
   outfile,
   cell_state; // internal state of the cell

initial
   begin
      errorsignal_a = 0;
      cell_state = 0; // Startup state
      q0 = 0; // All outputs start at 0
      q1 = 0; // All outputs start at 0
   end

always @(posedge a or negedge a) // execute at positive and negative edges of input
   begin
      if ($time>4) // arbitrary steady-state time)
         begin
            if (errorsignal_a == 1'b1)  // A critical timing is active for this input
               begin
                  outfile = $fopen("errors.txt", "a");
                  $fdisplay(outfile, "Violation of critical timing in module %m; %0d ps.\n", $stime);
                  $fclose(outfile);
                  q0 <= 1'bX;  // Set all outputs to unknown
                  q1 <= 1'bX;  // Set all outputs to unknown
               end
            if (errorsignal_a == 0)
               begin
                  case (cell_state)
                     0: begin
                           q0 <= #(delay_state0_a_q0) !q0;
                           q1 <= #(delay_state0_a_q1) !q1;
                           errorsignal_a = 1;  // Critical timing on this input; assign immediately
                           errorsignal_a <= #(ct_state0_a_a) 0;  // Clear error signal after critical timing expires
                        end
                  endcase
               end
         end
   end

endmodule
