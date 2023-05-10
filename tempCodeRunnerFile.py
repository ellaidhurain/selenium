from concurrent.futures import ThreadPoolExecutor
import io
from modules.login import TestLogin
# from modules.profile import TestProfile
from modules.news import TestNews
# from modules.mail import TestMail
import unittest
from HtmlTestRunner import HTMLTestRunner
import concurrent.futures
import multiprocessing
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()            
    
# if __name__ == "__main__":
#     test_suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Create a buffer to hold the HTML report
#         buffer = io.StringIO()
        
#         # Create an HTMLTestRunner with output directed to the buffer
#         runner = HTMLTestRunner(stream=buffer)
        
#         # Execute the tests in parallel
#         results = executor.map(lambda test: runner.run(test), test_suite)
        
#         # Write the HTML report to a file
#         with open("report.html", "w") as outfile:
#             outfile.write(buffer.getvalue())

#     # Check the results of the test execution
#     for result in results:
#         if result.errors or result.failures:
#             exit(1)

# # parallel test
# if __name__ == "__main__":
#     test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMail)
    
#     # generate report
#     # outfile = open("report.html", "w")
#     # runner = HTMLTestRunner(output='reports')
#     # runner.run(test_suite)
#     # outfile.close()  
    
    
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         results = executor.map(lambda test: unittest.TextTestRunner().run(test), test_suite)

#     for result in results:
#         if result.errors or result.failures:
#             exit(1)

import multiprocessing
import unittest

# define the test functions to run in parallel
test_functions = [(TestLogin,), (TestNews,)]

# create a function to run a test function and return its result
def run_test_function(test_function):
    try:
        suite = unittest.TestLoader().loadTestsFromModule(test_function[0])
        result = unittest.TextTestRunner().run(suite)
        return result.wasSuccessful(), f"{test_function[0].__name__} passed"
    except AssertionError as e:
        return False, f"{test_function[0].__name__} failed: {str(e)}"

if __name__ == '__main__':
    # create a process pool to run the test functions in parallel
    with multiprocessing.Pool(processes=len(test_functions)) as pool:
        # map each test function to a process and store the resulting async result object
        async_results = [pool.apply_async(run_test_function, (test_function,)) for test_function in test_functions]

        # wait for all the async results to complete and print the results
        for async_result in async_results:
            success, message = async_result.get()
            if success:
                print(f"{message} - Passed")
            else:
                print(f"{message} - Failed")

