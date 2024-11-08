#!/usr/bin/env python3

import inspect
import homework

import test_utils

import numpy as np

class P5TestCase(test_utils.TestCase):
    def test_p5(self):
        self.assertTrue(hasattr(homework, "p5"), "Variable p5 is missing.")

        p5 = homework.p5
        self.assertFalse(isinstance(p5, type(Ellipsis)), "Variable p5 was not set.")

        p5 = np.asarray(p5)
        self.assertEqual(p5.shape, (2, 4))
        self.assertValues(p5, expected_projections=[21.213726633378926, 21.75628049685876, 5.628613082218872, 30.885682694089844, 16.993325103298098, 25.554395697302418, 15.627428509613846, 32.29281074520435])


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
