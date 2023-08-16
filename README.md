# Automated Testing

## Description:
The Automated Testing is a python script designed to streamline testing and resolution verification processes. It automates various tasks including resolution check,CUDA availability, error handling and comparison of log file with Golden file.

## Key features:
Automated resolution checks: The tool compares the current resolution with the required resolution and logs any mismatches.
CUDA availability check: The tool verifies if CUDA is available on the system and logs the result.
Error handling: The script captures and logs errors, along with corresponding screenshots.
Comparison with golden logs: The tool compares generted logs with the Golden logs,and save the mismatch logs into Golden logs file.

## Usage Scenario:
Imagine a software testing environment where multiple system configurations need to be tested for resolution and CUDA availability. Instead of manually checking each system, this tool automates the process, ensuring faster and more consistent testing.

## Requirements:
1. 'Python 3'
2. 'pyscreenshot' library
3. 'screeninfo' library
4. 'torch' library

## How to use:
1. clone the repository.
2. Install required libraries using 'pip install -r requirements.txt'.
3. Run the main script using 'python main.py'.
4. Follow on-screen instruction to initiate the automated testing process.

## Contribution:
Contribution to this project are welcome! Feel free to report issues,suggest improvements, or submit pull request through GitHub.    

