import os
from my_module.python import (
    resolution_check,
    cuda_check,
    navigate_to_previous_directory,
    copy_golden_file,
    error_handler,
    csv_log_setup,
    log_step,
    compare_and_update_golden_log,
  
)

Testname = "Test_folder"

if __name__ == "__main__":
    csv_file = csv_log_setup()
    
    
    try:
       
        log_step("Sample Test Case", "Pass", csv_file)
        cuda_check(csv_file)
        resolution_check(csv_file)
    
        
      
        # Simulate an error for demonstration
        raise Exception("This is a simulated error.")

    except Exception as e:
        error_handler(e,csv_file)
  
    navigate_to_previous_directory()
    copy_golden_file()
    LogFile = "output_log.txt" 
    compare_and_update_golden_log(LogFile, Testname)
     
  