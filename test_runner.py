import unittest
import Calculator_test

test_load = unittest.TestLoader()
suites = test_load.loadTestsFromModule(Calculator_test)

test_result = unittest.TestResult()

runner = unittest.TextTestRunner(verbosity=2)
test_result = runner.run(suites)
print("ERRORS  ", len(test_result.errors))
print("FAILURES  ", len(test_result.failures))
print("SKIPPED  ", len(test_result.skipped))
print("TESTS_RUN  ", test_result.testsRun)
