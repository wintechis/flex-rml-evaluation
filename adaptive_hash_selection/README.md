# FlexRML Adaptive Hash Selection Evaluation

## Overview
This Python script evaluates the resource usage of FlexRML once using adaptive hash selection and once using a fixed 128-bit hash size. The script runs the SDM Genomics Testbed in dataset sizes of 10k, 100k, and 1M with duplicate rates of 75% and each entry repeated 20 times, and the GTFS Madrid bench with scale factors of 10, 100, and 500, and analyzes the output. The results, including average execution times and peak memory usage, are logged to a text file and summarized in a CSV file for further analysis.

## Requirements
- Python 3.X
- FlexRML and corresponding datasets and mapping files in the same directory as the script

## Setup
1. Clone the repository with this script to your local machine.
2. Generate the [GTFS Madrid data](https://github.com/oeg-upm/gtfs-bench) with scale factors of 10, 100, and 500 in csv.
3. Download the [SDM Genomic Testbed](https://figshare.com/articles/dataset/SDM-Genomic-Datasets/14838342/1) and [mappings](https://github.com/SDM-TIB/SDM-RDFizer-Experiments/tree/master/cikm2020/experiments/mappings).
4. Adjust the path in the mappings to fit the names of the SDM Genomic data you want to benchmark.
5. Place FlexRML in the root directory.

## Usage
Execute the script by navigating to its directory in your terminal and running:
```bash
python3 eval_adaptive_hash.py
```

The script performs the following:

- Executes predefined FlexRML commands using varying mapping files and once with adaptive hash selection and once with fixed 128 bit hash size.
- Each command is run three times to gather consistent data.
- Parses the elapsed wall time and peak memory usage from the command line output.
- Calculates the mean time in seconds and peak memory usage in kilobytes for each command.
- Logs detailed run information in a text file called `results.txt`.
- Summarizes mean values for each command in a CSV file called `aggregated_results.csv`.

## Output
The script generates two output files:

1. results.txt - Contains detailed logs for each run, including the command executed, individual run times, memory usage, and mean values.
2. aggregated_results.csv - Summarizes the results with columns for Command, Mean Time (in seconds), and Memory Usage (in kilobytes), allows easier analysis and comparison of FlexRML's resource usage across different scenarios.

## Results
The results of our evaluation can be found in the `results` directory.