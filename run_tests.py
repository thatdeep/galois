import unittest

# Import your test classes
from tests import TestPrimeFieldElement, TestPrimeField

# Create a test suite
suite = unittest.TestSuite()

# Add test classes to the suite
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPrimeFieldElement))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPrimeField))

# Run the tests
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)