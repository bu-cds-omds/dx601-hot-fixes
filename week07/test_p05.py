#!/usr/bin/env python3

import inspect
import math
import unittest
import homework


class P5TestCase(unittest.TestCase):
    def test_p5(self):
        self.assertTrue(hasattr(homework, "p5"), "Variable p5 is missing.")

        p5 = homework.p5
        self.assertFalse(isinstance(p5, type(Ellipsis)), "Variable p5 was not set.")

        # check variance calculation
        self.assertAlmostEqual(0.75**2, 0.5**2 + 0.5**2 + 2 * p5 * math.sqrt(0.5**2 * 0.5**2), msg="variance does not match with this correlation")


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
