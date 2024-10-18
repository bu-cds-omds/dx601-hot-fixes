#!/usr/bin/env python3

import inspect
import unittest
import homework

import numpy as np
class P17TestCase(unittest.TestCase):
    def test_p17a(self):
        self.assertTrue(hasattr(homework, "p17a"), "Variable p17a is missing.")

        p17a = homework.p17a
        self.assertFalse(isinstance(p17a, type(Ellipsis)), "Variable p17a was not set.")

        p17a = np.asarray(p17a)
        self.assertIn(p17a.shape, [(10, 2), (10, 3)])

        self.assertTrue(np.array_equal(p17a[:,0], [x*x for x in range(10)]))
        self.assertTrue(np.array_equal(p17a[:,1], [x for x in range(10)]))

        if p17a.shape[1] == 3:
            self.assertTrue(np.array_equal(p17a[:,2], np.ones(10)))


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
