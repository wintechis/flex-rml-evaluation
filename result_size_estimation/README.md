# FlexRML Result Size Estimation Evaluation

## Overview
This Python script evaluates the accuracy of the result size estimation by FlexRML. It executes FlexRML with varying estimation probabilities, captures the output, and calculates mean estimation times and mean number of unique elements. The results are saved to a CSV file for analysis.

The mapping rule used is based on the SDM RDFizer evaluations, combining the 4POM and 5OJM mappings into a single RML mapping. This allows for evaluating a more complex scenario. For more details, visit [SDM RDFizer Experiments](https://github.com/SDM-TIB/SDM-RDFizer-Experiments/tree/master/cikm2020/experiments/mappings).

## Requirements
- Python 3.x
- FlexRML and mapping file in the same folder as the test script

## Setup

1. Clone the repository containing this script to your local machine.
2. Ensure that FlexRML and the mapping file are in the same folder as the test script.

# Usage 
To run the script, navigate to the script's directory in your terminal and execute:
```bash
python3 eval_result_size.py
```

The script will perform the following actions:

- Iteratively run the FlexRML command with probabilities ranging from 0.1 to 0.9 in increments of 0.1.
- For each probability, the script will execute the command three times to gather data.
- It extracts the estimation time and number of unique elements from the cli output using regular expressions.
- Calculates the mean estimation time and mean number of unique elements for each probability.
- Writes these values into a CSV file named `results.csv`

## Output
The output of the script is a CSV file named `results.csv`. The file contains columns for Probability, Mean Estimation Time (in milliseconds), and Mean Number of Unique Elements. This file can be used for further analysis and visualization of FlexRML's performance.