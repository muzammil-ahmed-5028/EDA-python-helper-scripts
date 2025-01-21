# Helper Scripts

A collection of Python scripts to aid in Verilog development.

### 1. `verilog_file_generator.py`
This script allows you to add an instantiation of a Verilog module (or a list of Verilog modules) to a file.

### 2. `tb_creator.py`
This script generates a testbench for a Verilog module, assuming the initiation code is written in a specific way. It works properly only for combinational modules and uses a truth table file to generate the necessary code for the testbench.

### 3. `logic_minimizer.py`
This script reduces the form of a binary function from a truth table. It integrates with the `tb_creator.py` file to automatically minimize the truth table and optimize the logic.

### 4. `inst_rom_generator.py`
This script takes a file containing assembly instructions as input and generates a behavioral combinational instruction ROM based on those instructions.

