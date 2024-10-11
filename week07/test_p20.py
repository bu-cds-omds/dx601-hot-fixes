#!/usr/bin/env python3

import inspect
import unittest
import homework


class P20TestCase(unittest.TestCase):
    def test_p20(self):
        self.assertTrue(hasattr(homework, "p20"), "Variable p20 is missing.")

        p20 = homework.p20
        self.assertFalse(isinstance(p20, type(Ellipsis)), "Variable p20 was not set.")

        self.assertAlmostEqual(p20, 0.6367728838002948)


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
