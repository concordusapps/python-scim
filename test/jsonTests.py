import usertest
import configtest
import unittest


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(configtest.ConfigTestCase))
    test_suite.addTest(unittest.makeSuite(usertest.UserTestCase))
    return test_suite


mySuite = suite()
runner = unittest.TextTestRunner()
runner.run(mySuite)
