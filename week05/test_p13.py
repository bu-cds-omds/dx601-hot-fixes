#!/usr/bin/env python3

import inspect
import unittest
import homework


class P13TestCase(unittest.TestCase):
    def test_p13(self):
        self.assertTrue(hasattr(homework, "p13"), "Variable p13 is missing.")

        p13 = homework.p13
        self.assertFalse(isinstance(p13, type(...)), "Variable p13 was not set...")

        def check(x, p_expected):
            with self.subTest(x=x):
                p = p13(x)
                self.assertIsNotNone(p)
                self.assertAlmostEqual(p, p_expected)

        check(-1, 0)
        check(-0.5, 0)
        check(0, 0.25)
        check(0.5, 0.5)
        check(1.0, 0.75)
        check(1.5, 1.00)
        check(2.0, 1.0)

############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
