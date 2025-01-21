import math
module_file_name = "comparater.v"
dut_file = open(module_file_name,"r")
lines = dut_file.readlines()
tb_module_name = module_file_name.replace(".v","")
tb_module_file_name = tb_module_name +"_tb.v"
tb_file = open(tb_module_file_name,"w")
output_file_name = "output_" + f'{tb_module_file_name.upper().replace(".V","")}.txt'
print(output_file_name)
module_name = lines[0].split()[1].replace('(',"")
found = 0
line_iterator = 1
input_elements = []
output_elements = []
tb_file.write(lines[0].replace('(\n',"") + f'_tb;\n')
while found == 0:
    curr_line_elements = lines[line_iterator].split()
    if curr_line_elements[0] == ");":
        found = 1
    else:
        if curr_line_elements[0] == 'input':
            #print(curr_line_elements[2])
            if curr_line_elements[2][0] == '[':
                curr_character = ""
                number = ""
                character_iterator = 1
                while curr_character != ':':
                    curr_character = curr_line_elements[2][character_iterator]
                    number += curr_line_elements[2][character_iterator]
                    character_iterator += 1
                input_elements.append((curr_line_elements[3].replace(',',""),int(number.replace(':',"")) + 1))
            else:
                input_elements.append((curr_line_elements[2].replace(',',""),1))
        else:
            #print(curr_line_elements[2])
            if curr_line_elements[2][0] == '[':
                curr_character = ""
                number = ""
                character_iterator = 1
                while curr_character != ':':
                    curr_character = curr_line_elements[2][character_iterator]
                    number += curr_line_elements[2][character_iterator]
                    character_iterator += 1
                output_elements.append((curr_line_elements[3].replace(',',""),int(number.replace(':',""))+1))
            else:
                output_elements.append((curr_line_elements[2].replace(',',""),1))
        line_iterator += 1
# we get our input and output element arrays by here
print(input_elements)
print(output_elements)
for i in input_elements:
    if i[1] == 1:
        tb_file.write(f'reg {i[0].upper()};\n')
    else:
        tb_file.write(f'reg [{i[1]-1}:0] {i[0].upper()};\n')
for i in output_elements:
    if i[1] == 1:
        tb_file.write(f'wire {i[0].upper()};\n')
    else:
        tb_file.write(f'wire [{i[1]-1}:0] {i[0].upper()};\n')
tb_file.write('integer i;\n')
tb_file.write('integer file_handle;\n')
tb_file.write('\n')
tb_file.write(f'{module_name} dut(\n')
total_input_size = 0
for i in input_elements:
    tb_file.write(f'\t.{i[0]}({i[0].upper()}),\n')
    total_input_size += i[1]
for i in output_elements:
    if i == output_elements[-1]:
        tb_file.write(f'\t.{i[0]}({i[0].upper()})\n')
    else:
        tb_file.write(f'\t.{i[0]}({i[0].upper()}),\n')
tb_file.write(');\n')
tb_file.write('initial begin\n')
tb_file.write(f'\tfile_handle = $fopen("{output_file_name}","w");\n')
tb_file.write(f'\t$dumpfile("{tb_module_name}.vcd");\n')
tb_file.write(f'\t$dumpvars(0,{module_name+"_tb"});\n')
input_string_concatenated = "{"
output_string_concatenated = "{"
for i in input_elements:
    input_string_concatenated += i[0] + ','
for i in output_elements:
    output_string_concatenated += i[0] + ','
input_string_concatenated = input_string_concatenated[:-1] + '}'
output_string_concatenated = output_string_concatenated[:-1] + '}'
print(output_string_concatenated)
print(output_string_concatenated.upper())
total_input_hex_characters = math.ceil(total_input_size/4)
print(input_string_concatenated)
tb_file.write(f'\t$fdisplay(file_handle,"{str(input_elements).replace("[","").replace("]","").replace("'","")} || {str(output_elements).replace("[","").replace("]","").replace("'","")}");\n')
tb_file.write(f'\tfor (i=0; i < {2**total_input_size}; i++) begin\n')
tb_file.write(f'\t\t{input_string_concatenated.upper()} = i; #3 \n')
tb_file.write(f'\t\t$fdisplay(file_handle,"%b || %b",i,{output_string_concatenated.upper()});\n')
tb_file.write('\tend\n')
tb_file.write('\t$stop;\n')
tb_file.write('\t$finish;\n')
tb_file.write('end\n')
tb_file.write('endmodule\n')
tb_file.close()
