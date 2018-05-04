// ---------------------------------------------------------------------------
// Automatically extracted verilog file, created with TimEx v2.02.01
// Timing description and structural design for IARPA-BAA-14-03 via
// U.S. Air Force Research Laboratory contract FA8750-15-C-0203 and
// IARPA-BAA-16-03 via U.S. Army Research Office grant W911NF-17-1-0120.
// For questions about TimEx, contact CJ Fourie, coenrad@sun.ac.za
// (c) 2016-2018 Stellenbosch University
// ---------------------------------------------------------------------------
`timescale 1ps/100fs
module test_nott (in, clk, out);

input
  in, clk;

output
  out;

reg
  out;

real
  delay_state0_clk_out = 14.0,
  ct_state0_clk_in = 7.4,
  ct_state0_clk_clk = 15.9,
  ct_state1_in_clk = 10.9;

reg
   errorsignal_in,
   errorsignal_clk;

integer
   outfile,
   cell_state; // internal state of the cell

initial
   begin
      errorsignal_in = 0;
      errorsignal_clk = 0;
      cell_state = 0; // Startup state
      out = 0; // All outputs start at 0
   end

always @(posedge in or negedge in) // execute at positive and negative edges of input
   begin
      if ($time>4) // arbitrary steady-state time)
         begin
            if (errorsignal_in == 1'b1)  // A critical timing is active for this input
               begin
                  outfile = $fopen("errors.txt", "a");
                  $fdisplay(outfile, "Violation of critical timing in module %m; %0d ps.\n", $stime);
                  $fclose(outfile);
                  out <= 1'bX;  // Set all outputs to unknown
               end
            if (errorsignal_in == 0)
               begin
                  case (cell_state)
                     0: begin
                           cell_state = 1;  // Blocking statement -- immediately
                        end
                     1: begin
                           errorsignal_clk = 1;  // Critical timing on this input; assign immediately
                           errorsignal_clk <= #(ct_state1_in_clk) 0;  // Clear error signal after critical timing expires
                        end
                  endcase
               end
         end
   end

always @(posedge clk or negedge clk) // execute at positive and negative edges of input
   begin
      if ($time>4) // arbitrary steady-state time)
         begin
            if (errorsignal_clk == 1'b1)  // A critical timing is active for this input
               begin
                  outfile = $fopen("errors.txt", "a");
                  $fdisplay(outfile, "Violation of critical timing in module %m; %0d ps.\n", $stime);
                  $fclose(outfile);
                  out <= 1'bX;  // Set all outputs to unknown
               end
            if (errorsignal_clk == 0)
               begin
                  case (cell_state)
                     0: begin
                           out <= #(delay_state0_clk_out) !out;
                           errorsignal_in = 1;  // Critical timing on this input; assign immediately
                           errorsignal_in <= #(ct_state0_clk_in) 0;  // Clear error signal after critical timing expires
                           errorsignal_clk = 1;  // Critical timing on this input; assign immediately
                           errorsignal_clk <= #(ct_state0_clk_clk) 0;  // Clear error signal after critical timing expires
                        end
                     1: begin
                           cell_state = 0;  // Blocking statement -- immediately
                        end
                  endcase
               end
         end
   end

endmodule
