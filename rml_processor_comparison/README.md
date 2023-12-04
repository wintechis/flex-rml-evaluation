# RML Processor Comparison

## Overview
This Python script evaluates the resource usage of FlexRML, Morph-KGC, and SDM-RDFizer using the SDM Genomics Testbed in dataset sizes of 10k, 100k, and 1M with duplicate rates of 75% and each entry repeated 20 times, and the GTFS Madrid bench with scale factors of 10, 100, and 500. The results, including average execution times and peak memory usage, are logged to a text file and summarized in a CSV file for further analysis.

## Requirements
- All three RML processors must be set up and accessible.

## Setup
1. Clone the repository with the scripts to your local machine.
2. Generate the [GTFS Madrid data](https://github.com/oeg-upm/gtfs-bench) with scale factors of 10, 100, and 500 in CSV format.
3. Download the [SDM Genomic Testbed](https://figshare.com/articles/dataset/SDM-Genomic-Datasets/14838342/1) and [mappings](https://github.com/SDM-TIB/SDM-RDFizer-Experiments/tree/master/cikm2020/experiments/mappings).
5. Adjust the commands and paths specified in each script to fit your setup.

## Usage
Execute the desired script by navigating to its directory. In your terminal, replace `SCRIPT_NAME.py` with the script you want to run and execute:
```bash
python3 SCRIPT_NAME.py
```

The scripts perform the following:

- Evaluate the resource usage on a RML processor mapping a specific benchmark or dataset.
- Each command is run three times to gather consistent data.
- Parses the elapsed wall time and peak memory usage from the command line output.
- Calculates the mean time in seconds and peak memory usage in kilobytes for each command.
- Logs detailed run information in a text file called `result_{RML Processor}_{dataset}.txt`.
- Summarizes mean values for each command in a CSV file called `result_{RML Processor}_{dataset}.csv`.


## Results
The results of our evaluation for the cloud and edge platforms can be found in the `results` directory.