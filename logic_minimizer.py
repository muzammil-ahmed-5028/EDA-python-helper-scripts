import logicmin

def removeCommaAndBrackets(string1):
    return string1.replace("(","").replace(")","").replace(",","")

def cleanList(input_string):
    input_list = []
    output_list = []
    i=0
    curr_part = ""
    found = 0
    for parts in input_string:
        curr_part = removeCommaAndBrackets(parts)
        if curr_part == "||" or found == 1:
            output_list.append(curr_part)
            found = 1
        else:
            input_list.append(removeCommaAndBrackets(parts))
    output_list = output_list[1:]
    return input_list,output_list

def createXnamesAndYnames(input_list,output_list):
    xnames = []
    ynames = []
    i=0
    curr_element_index = 1
    while curr_element_index <= len(input_list):
        for j in range(int(input_list[curr_element_index])-1,-1,-1):
            xnames.append(f'{input_list[curr_element_index-1]}[{j}]')
        curr_element_index += 2

    curr_element_index = 1
    while curr_element_index <= len(output_list):
        for j in range(int(output_list[curr_element_index])-1,-1,-1):
            ynames.append(f'{output_list[curr_element_index-1]}[{j}]')
        curr_element_index += 2    
    return xnames,ynames

def determineInputBits(input_string):
    found = 0
    string_iterator = -1
    while found == 0:
        if(input_string[string_iterator] == "1"):
            string_iterator -=1
        else:
            found = 1
    return -1*(string_iterator) -1

def getTT(lines):
    inputStringLength = determineInputBits(lines[-1].split()[0])
    inputStringIndex = 32-inputStringLength
    tt = logicmin.TT(inputStringLength,len(lines[0].split()[2]))
    for x in lines:
        curr_parts = x.split()
        tt.add(curr_parts[0][inputStringIndex:],curr_parts[2])
    return tt
tt_file = open("output_COMPARATER_TB.txt","r")
lines = tt_file.readlines()
x,y = cleanList(lines[0].split())
xnames,ynames = createXnamesAndYnames(x,y)
print(determineInputBits(lines[-1].split()[0]))
tt = getTT(lines[1:])
sols = tt.solve()
print(sols.printN(xnames=xnames,ynames=ynames,syntax = "VHDL"))
