import os
import sys



file_path = 'out.txt'
file_path_method = 'meth.txt'


def uses():
    print("Uses")

def grep(script_name,file_path,file_path_method):
    os.system(f'grep raw {script_name}  > {file_path}')
    os.system(f'grep method {script_name}  > {file_path_method}')

def replace_string_in_file(file_path, old_string, new_string):
    # Read the file contents
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Replace the old string with the new string
    modified_contents = file_contents.replace(old_string, new_string)

    # Write the modified contents back to the file
    with open(file_path, 'w') as file:
        file.write(modified_contents)


def method_replace_string_in_file(file_path, old_string, new_string):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    modified_contents = file_contents.replace(old_string, new_string)
    with open(file_path, 'w') as file:
        file.write(modified_contents)

def replace_data(file_path,file_path_method):
    replace_string_in_file(file_path,  '"mode": "raw",', '')
    replace_string_in_file(file_path,  '"raw": {', '')
    replace_string_in_file(file_path_method,  '"method"', '')
    replace_string_in_file(file_path_method,  '"', '')
    replace_string_in_file(file_path_method,  ':', '')
    replace_string_in_file(file_path_method,  ',', '')

def ThreeArgv(cmd):
    if(cmd.startswith("--method")):
        file = open(file_path, 'r')
        file_method = open(file_path_method, 'r')

        count = 0

        firstVerifyDomain = '"raw": "{{'
        SecondVerifyDomain = '"raw": "http'

        for line in file:
            if(firstVerifyDomain in line or SecondVerifyDomain in line):
                for line_meth in file_method:
                    count = count+1
                    line = line.replace('"raw":',"")
                    line = line.replace('"',"")
                    print(f"{line_meth.strip()} : {line.strip()}")
                    break
            else: 
                pass 

        file.close()
        print('Total API: ',count)
    else:
        file = open(file_path, 'r')
        file_method = open(file_path_method, 'r')

        count = 0

        firstVerifyDomain = '"raw": "{{'
        SecondVerifyDomain = '"raw": "http'

        for line in file:
            if(firstVerifyDomain in line or SecondVerifyDomain in line):
                for line_meth in file_method:
                    count = count+1
                    line = line.replace('"raw":',"")
                    line = line.replace('"',"")
                    print(f"{line.strip()}")
                    break
            else: 
                pass 

        file.close()
        print('Total API: ',count)     
               
if(len(sys.argv) == 2):
    script_name = sys.argv[1]
    grep(script_name,file_path,file_path_method)
    replace_data(file_path,file_path_method)
    ThreeArgv('all')

elif(len(sys.argv) == 3):
    script_name = sys.argv[1]
    cmd = sys.argv[2]
    grep(script_name,file_path,file_path_method)
    replace_data(file_path,file_path_method)
    print(cmd)
    ThreeArgv(cmd)
else:
    uses()
    exit()



