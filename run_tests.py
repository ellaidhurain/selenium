from concurrent.futures import ThreadPoolExecutor
import io
import unittest
from HtmlTestRunner import HTMLTestRunner
import concurrent.futures
import multiprocessing
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

#modules
# from modules.login import TestLogin
# from modules.profile import TestProfile
# from modules.news import TestNews
# from modules.regional_school import TestRegionalSchool
# from modules.roles import TestRole
# from modules.department import TestDepartment
from modules.class_group import TestClassGroup
# from modules.calendar import TestCalendar
# from modules.staffs import TestStaffs
# from modules.students import TestStudents
# from modules.classroom import TestClassRoom
# from modules.lessonplan import TestLessonPlan
# from modules.time_table import TestTimeTable
# from modules.attendance import TestAttendance
# from modules.exams import TestExams
# from modules.reports import TestReports
# from modules.communication import TestCommunication
# from modules.mail import TestMail
            
 
# parallel test   
# Load all test modules into a test suite
# test_suite = unittest.TestSuite()
# test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
# # test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestNews))


# if __name__ == "__main__":
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
    


  
# test module one by one           
test_functions = [
    # TestLogin, 
    # TestNews,
    # TestProfile,
    # TestRegionalSchool,
    # TestRole,
    # TestDepartment,
    TestClassGroup
    # TestCalendar,
    # TestStaffs,
    # TestStudents,
    # TestClassRoom,
    # TestLessonPlan,
    # TestTimeTable,
    # TestAttendance,
    # TestExams,
    # TestReports,
    # TestCommunication
    
    ]

# create a function to run a test function and return its result
def run_test_function(test_function):
    try:
        test_function()
        return True, f"{test_function.__name__} passed"
    except AssertionError as e:
        return False, f"{test_function.__name__} failed: {str(e)}"

if __name__ == '__main__':
    # create a thread pool to run the test functions in parallel
    with concurrent.futures.ProcessPoolExecutor(max_workers=len(test_functions)) as executor:
        # submit each test function to the executor and store the resulting future object
        futures = [executor.submit(run_test_function, test_function) for test_function in test_functions]

        # wait for all the futures to complete and print the results
        for future in concurrent.futures.as_completed(futures):
            success, message = future.result()
            if success:
                print(f"{message} - Passed")
            else:
                print(f"{message} - Failed")

    # run all the tests in the modules sequentially
    unittest.main()
    
