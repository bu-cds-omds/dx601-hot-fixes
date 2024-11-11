#!/usr/bin/env python3

import inspect
import homework

import test_utils

import numpy as np
class P3TestCase(test_utils.TestCase):
    def test_p3(self):
        self.assertTrue(hasattr(homework, "p3"), "Variable p3 is missing.")

        p3 = homework.p3
        self.assertFalse(isinstance(p3, type(Ellipsis)), "Variable p3 was not set.")

        p3 = np.asarray(p3)
        self.assertEqual(p3.shape, ())
        self.assertValues(p3, expected_projections=[0.40309273233720366])


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
