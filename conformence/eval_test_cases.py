import os
import subprocess
import time
from collections import Counter
import sys

# Get the current working directory
current_directory = os.getcwd()

# Get a list of all files and folders in the current directory
all_format_dirs = os.listdir(current_directory)

for dir in all_format_dirs:
    if os.path.isdir(dir) == False:
        continue
    
    print("======================")
    print("Testing " + dir + " ...")
    print("======================")


    new_path = os.path.join(current_directory,dir)
    test_dirs = os.listdir(new_path)


    # Print the folder paths
    for entry in test_dirs:
        # Construct the full path of the entry
        full_path = os.path.join(new_path, entry)
        
        # Check if the entry is a directory
        if os.path.isdir(full_path) == False:
            continue

        print("Working on:", entry)

        # Create a subprocess and redirect stdout and stderr
        process = subprocess.Popen(["./FlexRML", "-m", f"./{dir}/{entry}/mapping.ttl", "-o", "result.nq", "-d"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Read the output line by line as it is being produced
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            print(line.strip())

        # Check for any remaining output after the process has finished
        remaining_output = process.communicate()
        if remaining_output[0].strip() != "":
            print(remaining_output[0].strip())  # Remaining stdout
        if remaining_output[1].strip() != "":
            print(remaining_output[1].strip())  # Remaining stderr

        # wait 
        time.sleep(0.05)

        # compare result
        file_path1 = 'result.nq'
        file_path2 = f"./{dir}/{entry}/output.nq"

        # Read the contents of the first file into a Counter object, stripping whitespaces and ignoring empty lines
        with open(file_path1, 'r') as file1:
            file1_contents = Counter(line.strip() for line in file1 if line.strip())        

        # Read the contents of the second file into a Counter object, stripping whitespaces and ignoring empty lines
        with open(file_path2, 'r') as file2:
            file2_contents = Counter(line.strip() for line in file2 if line.strip())

        # Compare the two Counter objects of file contents
        if file1_contents == file2_contents:
            print(f"Test {entry} passed.")

            # Remove content from file
            with open("result.nq", 'w'):
                pass  
        else:
            print(f"Error: Missmatch in test {entry}.")
            
            # Find lines present in the first file but not in the second file
            for line in (file1_contents - file2_contents).elements():
                print(f"Line in {file_path1} but not in {file_path2}: {line}")
            
            # Find lines present in the second file but not in the first file
            for line in (file2_contents - file1_contents).elements():
                print(f"Line in {file_path2} but not in {file_path1}: {line}")
            
            sys.exit()

        print("")


print("Passed all tests!")