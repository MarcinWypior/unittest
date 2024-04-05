import unittest

class MyTest(unittest.TestCase):
    def tearDown(self):

        if hasattr(self._outcome, 'errors'):
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)


        if result.errors:
            print('errors:')
            print(result.errors)

        if result.failures:
            print("failures:")
            print(result.failures)

    def test_error(self):
        self.assertEqual(1 / 0, 1)

    def test_fail(self):
        self.assertEqual(2, 1)

    def test_success(self):
        self.assertEqual(1, 1)