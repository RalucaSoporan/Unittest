import unittest
import HtmlTestRunner

from login_page import Login_page
from dashboard import Dashboard
from search_button import Search_button
from menu_aplication import Menu_aplication

class TestSuite(unittest.TestCase):

    def test_suite(self):
        '''We establish and add in a suite the tests we want to run'''

        tests_to_run= unittest.TestSuite()

        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login_page),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dashboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(Search_button),
            unittest.defaultTestLoader.loadTestsFromTestCase(Menu_aplication)
        ])
        '''I am creating a runner'''
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True, # we want to generate a single report with all the tests
            report_title="Test Execution Report",
            report_name="Raport final project"
        )

        runner.run(tests_to_run)
