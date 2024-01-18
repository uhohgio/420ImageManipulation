import subprocess

# Specify the full path to the MATLAB executable
matlab_executable = 'C:\Program Files\MATLAB\R2023b\\bin\matlab.exe'
# Run the matlabcode1 script in MATLAB
matlab_process = subprocess.run([matlab_executable, "-batch", "run('matlabcode1.m'); pause(1);"], capture_output=True)

# Read values from 'input.txt'
with open('input.txt', 'r') as file:
    line = file.readline()
    input_array = [int(value) for value in line.split()] 
    input_array = [str(element) for element in input_array] # turns the input into a string to be read/distributed

# input_array = ["1","2","200","201","5"]

#* C Section *
# Compile the C program 
subprocess.run(["gcc", "CProg.c", "-o", "CProg"])
# Run the compiled C program with the input array as arguments
process = subprocess.run(["./CProg"] + input_array, capture_output=True, text=True)
# Store the output of the C program in a Python variable
output_variable = process.stdout.strip()
# Save the result to c_output.txt
with open('c_output.txt', 'w') as f:
    f.write(output_variable)
# print("C Output: ")
# print(output_variable)



#* Haskell Section *
# Compile the Haskell program 
subprocess.run(['ghc','hcode.hs'])
# Run the compiled Haskell program with the input array as arguments
process = subprocess.run(['./hcode'] + [str(x) for x in input_array],text = True, capture_output = True)
# Store the output of the Haskell program in a Python variable
result = process.stdout.strip()
# Save the result to a hs_output.txt
with open('hs_output.txt', 'w') as f:
    f.write(result)
# print("Haskell Output: ")
# print(result)

#* Prolog Section *
# Compile the Prolog program 
prolog_input = "[" + ",".join(map(str, input_array)) + "]."
# Run the compiled Prolog program with the input array as arguments
result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'pcode.pl'], input=prolog_input, capture_output=True, text=True)
# Store the output of the Prolog program in a Python variable
output_result = result.stdout.strip()
# Save the result to pl_output.txt
with open('pl_output.txt', 'w') as f:
    f.write(output_result)
# print("Prolog Output: ")
# print(output_result)

# matlabcode2, outputs the transposed image
matlab_output = subprocess.run([matlab_executable, "-batch", "run('matlabcode2.m'); pause(30);"], capture_output=True)