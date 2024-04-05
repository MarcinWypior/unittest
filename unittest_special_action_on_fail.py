import unittest

class MyTest(unittest.TestCase):
    def tearDown(self):
        if hasattr(self._outcome, 'errors'):
            # Python 3.4 - 3.10  (These two methods have no side effects)
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
        else:
            # Python 3.11+
            result = self._outcome.result
        ok = all(test != self for test, text in result.errors + result.failures)

        # Demo output:  (print short info immediately - not important)
        if ok:
            print('\nOK: %s' % (self.id(),))
        for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
            for test, text in errors:
                if test is self:
                    #  the full traceback is in the variable `text`
                    msg = [x for x in text.split('\n')[1:]
                           if not x.startswith(' ')][0]
                    print("\n\n%s: %s\n     %s" % (typ, self.id(), msg))

    def test_error(self):
        self.assertEqual(1 / 0, 1)

    def test_fail(self):
        self.assertEqual(2, 1)

    def test_success(self):
        self.assertEqual(1, 1)