# FlexRML Conformance Tester

## Overview
This Python script is designed to check the conformance of FlexRML to RML test cases. The script runs FlexRML against a set of predefined test cases, compares the output with the expected results, and reports any discrepancies.

## Requirements
- Python 3.x
- FlexRML in the same folder as the test script

## Setup

1. Clone the repository containing this script to your local machine.
2. Ensure that FlexRML is in the same folder as the test script.
3. Place the test case directories in the same directory as the script.

# Usage 
To run the script, navigate to the script's directory in your terminal and execute:
```bash
python3 eval_test_cases.py
```

The script will:
- Iterate through each test case directory.
- Run FlexRML with the specified mapping and output files.
- Compare the generated output with the expected output.
- Report the results of each test case, indicating success or failure.

## Test Case Structure
Each test case should be in its own directory, containing:
- A mapping file named mapping.ttl.
- An expected output file named output.nq.

The test cases are based on the [RML test cases](https://github.com/kg-construct/rml-test-cases). However, each output.nq file is customized to be handled by the validation script.

## Output
The script will output the result of each test case to the terminal. It will clearly state whether each test has passed or failed, and in case of failure, it will detail the discrepancies between the generated and expected output.

## License

This project is a derivative work of software originally copyrighted by Ghent University – imec and is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

### Original Work

The original work is licensed under the Creative Commons Attribution 4.0 International License. You can view a copy of this license at [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/).

### Modifications

The modifications made in this project are also licensed under the Creative Commons Attribution 4.0 International License. As per the terms of this license, you are free to use, share, and adapt these modifications, provided you give appropriate credit to the original creator (Ghent University – imec) and indicate if changes were made. These terms do not in any way suggest that the licensor endorses you or your use of the work.

For more details on the requirements of this license, please refer to the link provided above.