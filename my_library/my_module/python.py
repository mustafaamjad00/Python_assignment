import os
import csv
import datetime
import shutil
import pyscreenshot as ImageGrab
import traceback
from screeninfo import get_monitors


################################################################################################
# Define the required resolution
RequiredResolution = (1920, 1156)
Testname = "Test_folder"
GoldenFileSource="/home/emumba/Desktop"
GoldenFileName ="Test_Name.Golden"
LogFile = "output_log.txt"  # Name of the log file
log_file = open(LogFile, "w")
#################################################################################################
def log_to_file(message):
    print(message)
    log_file.write(message + "\n")
#################################################################################################

#################################################################################################           
# This function initializes the script by creating the working directory.
# This function initializes the script by creating the working directory.
def initial_setup():
    try:
        # Create the 'Test_folder' directory if it doesn't exist
        if not os.path.exists(Testname):
            os.makedirs(Testname)
            log_to_file(f"Directory '{Testname}' created.")
        else:
            log_to_file(f"Directory '{Testname}' already exists. Removing and creating a new one.")
            shutil.rmtree(Testname)
            os.makedirs(Testname)
        
        os.chdir(Testname)
    except OSError as e:
        log_to_file("Error creating or accessing directory:", e)

try:
    initial_setup()  # Call initial_setup to create/access the directories
except Exception as e:
    log_to_file("An error occurred during initial setup:", e)


###########################################################################################

def log_step(test_case, status, csv_file):
    field_names = ["Test Case", "Status", "Timestamp"]

    with open(csv_file, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerow(
            {
                "Test Case": test_case,
                "Status": status,
                "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

def csv_log_setup():
    csv_file = "test_result.csv"
    
    if not os.path.exists(csv_file):
        with open(csv_file, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Test Case", "Status", "Timestamp"])
            writer.writeheader()
    
    return csv_file

############################################################################################
def take_screenshot(test_case, status):
    # Create the screenshot directory if it doesn't exist
    screenshot_directory = os.path.join("screenshots")
    os.makedirs(screenshot_directory, exist_ok=True)

    screenshot_name = f"{test_case}_{status}.png"
    screenshot_path = os.path.join(screenshot_directory, screenshot_name)

    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)
 ############################################################################################

def error_handler(e,csv_file):
    # Take a screenshot and log the error message
    error_msg = traceback.format_exc()
    take_screenshot("Error", "Failed")
    log_step("Error", "Failed",csv_file)
    with open("error_log.txt", "w") as error_file:
        error_file.write(error_msg)
    log_to_file("An error occurred. Details saved in 'error_log.txt'.")
###############################################################################################
def resolution_check(csv_file):
    def get_screen_resolution():
        monitor = get_monitors()[0]
        return monitor.width, monitor.height
    # Retrieve the current resolution and set the required resolution
    current_resolution = get_screen_resolution()  # Replace with actual resolution retrieval
    log_to_file(f"Current resolution: {current_resolution}")
    if current_resolution != RequiredResolution:
        error_msg = f"Resolution mismatch. Required: {RequiredResolution}, Current: {current_resolution}"
        log_step("Resolution Check", "Fail",csv_file)
        take_screenshot("Resolution Check", "Fail")
        log_to_file(error_msg)
  ############################################################################################
def cuda_check(csv_file):
    try:
        import torch
        if not torch.cuda.is_available():
            log_step("CUDA Check", "Fail",csv_file)
            take_screenshot("CUDA Check", "Fail")
            log_to_file("CUDA is not available on this system.")
          
           
    except ImportError:
        log_step("CUDA Check", "Fail",csv_file)
        take_screenshot("CUDA Check", "Fail")
        log_to_file("PyTorch is not installed. Install it to use CUDA.")
        
  #############################################################################################
def navigate_to_previous_directory():
    current_directory=os.getcwd()
    log_to_file("current_directory :"+ current_directory)
    previous_directory=os.path.dirname(current_directory)
    log_to_file("previous_directory : "+ previous_directory)

    if previous_directory:
        os.chdir(previous_directory)
        log_to_file(f"navigate to previous directory:{previous_directory}")
    else:
        log_to_file("No previous directory")    
###############################################################################################
def copy_golden_file():
    destination_path = os.path.join(Testname, GoldenFileName)
    log_to_file(destination_path)
    try:
        if os.path.exists(os.path.join(GoldenFileSource, GoldenFileName)):
            shutil.copy(os.path.join(GoldenFileSource, GoldenFileName), destination_path)
            log_to_file(f"Golden file {GoldenFileName} copied successfully to {destination_path}")
        else:
            log_to_file(f"Golden file not found in the source folder")

    except Exception as e:
        log_to_file(f"An error occurred while copying the golden file: {e}")


################################################################################################
def compare_and_update_golden_log(LogFile, Testname):
    try:
        with open(LogFile, "r") as log_file:
            log_contents = log_file.read()

        with open(os.path.join(Testname, "Test_Name.Golden"), "r") as golden_file:
            golden_contents = golden_file.read()

        if log_contents == golden_contents:
            print("Log file matches golden file.")
        else:
            print("Log file does not match golden file. Copying output data to Golden file")
            with open(os.path.join(Testname, "Test_Name.Golden"), "w") as golden_file:
                golden_file.write(log_contents)
    except Exception as e:
        print("An error occurred:", e)


####################################################################################################  
 
if __name__ == "__main__":
    csv_file = csv_log_setup()
    
    try:
        cuda_check(csv_file)
        resolution_check(csv_file)
    
        
      
        # Simulate an error for demonstration
        raise Exception("This is a simulated error.")

    except Exception as e:
        error_handler(e,csv_file)
  
    navigate_to_previous_directory()
    copy_golden_file()
    log_file.close()  
    compare_and_update_golden_log(LogFile, Testname)
  
   
################################################################################################
