#!/usr/bin/env python3

import inspect
import unittest
import homework


class P18TestCase(unittest.TestCase):
    def test_p18a(self):
        self.assertTrue(hasattr(homework, "p18a"), "Variable p18 is missing.")

        p18a = homework.p18a
        self.assertFalse(isinstance(p18a, type(Ellipsis)), "Variable p18 was not set.")

        self.assertAlmostEqual(p18a, -0.6372529878771659)


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
