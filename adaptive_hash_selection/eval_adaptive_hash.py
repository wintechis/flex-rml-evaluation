import subprocess
import re
import math

# Function to convert memory usage string to an integer (kilobytes)
def parse_memory_to_kb(memory_str):
    try:
        return int(memory_str.split()[0])
    except ValueError:
        return 0

def parse_time_to_seconds(time_str):
    """
    Converts a time string in the format h:mm:ss.ss or m:ss.ss to seconds.
    """
    parts = time_str.split(':')
    if len(parts) == 3:
        hours, minutes, seconds = parts
        total_seconds = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    elif len(parts) == 2:
        minutes, seconds = parts
        total_seconds = int(minutes) * 60 + float(seconds)
    else:
        # Handle unexpected format
        total_seconds = 0
        print("Unexpected Format!")

    return total_seconds

def run_command_and_parse_output(command):
    # Running your command and capturing both stdout and stderr
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Combine stdout and stderr for parsing
    combined_output = result.stdout + result.stderr

    # Initializing variables for the data to be extracted
    elapsed_walltime = None
    peak_memory = None

    # Regex patterns for matching the required information
    time_pattern = r'Elapsed \(wall clock\) time \(h:mm:ss or m:ss\): (.*)'
    memory_pattern = r'Maximum resident set size \(kbytes\): (.*)'

    for line in combined_output.splitlines():
        if time_match := re.search(time_pattern, line):
            elapsed_walltime = time_match.group(1)
        if memory_match := re.search(memory_pattern, line):
            peak_memory = memory_match.group(1) + ' kilobytes'

    return elapsed_walltime, peak_memory

# Commands to be run
commands = [
    ['/usr/bin/time', '-v', './FlexRML', '-m', './10k_genomic/mapping.ttl', '-o', 'res', '-d', '-t', "-a", "-p", "0.05"],    
    ['/usr/bin/time', '-v', './FlexRML', '-m', './100k_genomic/mapping.ttl', '-o', 'res', '-d', '-t', "-a", "-p", "0.05"], 
    ['/usr/bin/time', '-v', './FlexRML', '-m', './1M_genomic/mapping.ttl', '-o', 'res', '-d', '-t', "-a", "-p", "0.05"],
    ['/usr/bin/time', '-v', './FlexRML', '-m', './GTFS_10/mapping.nt', '-o', 'res', '-d', '-t', "-a", "-p", "0.05"],
    ['/usr/bin/time', '-v', './FlexRML', '-m', './GTFS_100/mapping.nt', '-o', 'res', '-d', '-t', "-a", "-p", "0.05"], 
    ['/usr/bin/time', '-v', './FlexRML', '-m', './GTFS_500/mapping.nt', '-o', 'res', '-d', '-t', "-a", "-p", "0.05"],
    ['/usr/bin/time', '-v', './FlexRML', '-m', './10k_genomic/mapping.ttl', '-o', 'res', '-d', '-t', "-b", "128"],    
    ['/usr/bin/time', '-v', './FlexRML', '-m', './100k_genomic/mapping.ttl', '-o', 'res', '-d', '-t', "-b", "128"], 
    ['/usr/bin/time', '-v', './FlexRML', '-m', './1M_genomic/mapping.ttl', '-o', 'res', '-d', '-t', "-b", "128"],
    ['/usr/bin/time', '-v', './FlexRML', '-m', './GTFS_10/mapping.nt', '-o', 'res', '-d', '-t', "-b", "128"],
    ['/usr/bin/time', '-v', './FlexRML', '-m', './GTFS_100/mapping.nt', '-o', 'res', '-d', '-t', "-b", "128"], 
    ['/usr/bin/time', '-v', './FlexRML', '-m', './GTFS_500/mapping.nt', '-o', 'res', '-d', '-t', "-b", "128"], 
]

with open('results.txt', 'w') as file:
    with open('aggregated_results.csv', 'w') as file2:
        file2.write("Command,Mean Time in s, Memory in kb\n")

        # Running the function for each command and printing the results
        for command in commands:
            print(f"Working on {command}")

            # Lists to store times and memories for each run
            peak_memory_arr = []
            elapsed_time_arr = []

            # Perform 3 runs
            for i in range(3):
                elapsed_walltime, peak_memory = run_command_and_parse_output(command)
                time_in_seconds = parse_time_to_seconds(elapsed_walltime)
                memory_in_kb = parse_memory_to_kb(peak_memory)

                # Appending results to arrays
                elapsed_time_arr.append(time_in_seconds)
                peak_memory_arr.append(memory_in_kb)

                # Writing results to the file
                file.write(f"Command: {' '.join(command)}\n")
                file.write(f"Elapsed Wall Time (s): {time_in_seconds}\n")
                file.write(f"Peak Memory Usage (KB): {memory_in_kb}\n")

            # Calculating the mean time and memory
            mean_time = sum(elapsed_time_arr) / len(elapsed_time_arr)
            mean_peak_memory = sum(peak_memory_arr) / len(peak_memory_arr)

            # Writing mean values to the file
            file.write(f"Mean Elapsed Time for {' '.join(command)}: {mean_time} seconds\n")
            file.write(f"Mean Peak Memory Usage for {' '.join(command)}: {mean_peak_memory} kilobytes\n\n")
            file.write("=====================================\n")
            file.write("=====================================\n")


            #Write data in csv format
            file2.write(f"{' '.join(command)},{mean_time},{mean_peak_memory}\n")
