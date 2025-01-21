# Helper Scripts
Some python scripts to help in verilog developtment.
verilog_file_generator.py: This file can be used to add an instantiation of a verilog module or list of verilog modules in a file.
tb_creator.py: Assuming the initiation code of a verilog file is written in a certain way this module make a testbench for the module with a code for a file which contains the truth table of the module.
- works only for combinational modules properly.
logic_minimizer.py: used to get the reduced form of a binary function from a truth table. This works with the tb_creator.py file to automatically minimize a file
inst_rom_generatot.py: given as input a file with assembly instructions it will make a behavioral combinational instruction rom.
