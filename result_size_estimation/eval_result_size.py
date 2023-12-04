import subprocess
import re
import csv

def run_command_and_parse_output(filename):
    estimation_time_pattern = r"Estimation took: (\d+) milliseconds"
    unique_elements_pattern = r"Estimated number of unique elements: (\d+)"

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Probability', 'Mean Estimation Time (ms)', 'Mean Number of Unique Elements'])

        for probability in [i / 10 for i in range(1, 10)]:  # Iterate from 0.1 to 0.90 in steps of 0.1
            command = f"/usr/bin/time -v ./FlexRML -m combined_mapping.ttl -o res.nq -d -t -a -p {probability}"

            total_estimation_time = 0
            total_unique_elements = 0
            
            repeats = 3

            for _ in range(repeats):  # Repeat measurement 3 times
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                output = stdout.decode()

                estimation_time = re.search(estimation_time_pattern, output)
                unique_elements = re.search(unique_elements_pattern, output)

                if estimation_time:
                    total_estimation_time += int(estimation_time.group(1))
                if unique_elements:
                    total_unique_elements += int(unique_elements.group(1))

            mean_estimation_time = total_estimation_time / repeats
            mean_unique_elements = total_unique_elements / repeats

            # Write results to CSV
            writer.writerow([probability, mean_estimation_time, mean_unique_elements])

# Run the function and write results to a CSV file
output_filename = 'results.csv'
run_command_and_parse_output(output_filename)
print(f"Results written to {output_filename}")
