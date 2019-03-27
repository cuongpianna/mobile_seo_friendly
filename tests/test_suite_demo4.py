import sys
import time
import unittest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from tests.home_test import HomeTest
from config import TIME_TO_RUN


while True:
    tc1 = unittest.TestLoader().loadTestsFromTestCase(HomeTest)

    smokeTest = unittest.TestSuite([tc1])
    unittest.TextTestRunner(verbosity=2).run(smokeTest)
    time.sleep(TIME_TO_RUN)
