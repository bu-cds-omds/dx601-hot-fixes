#!/usr/bin/env python3

import inspect
import homework

import test_utils

import numpy as np
class P7TestCase(test_utils.TestCase):
    def test_p7(self):
        self.assertTrue(hasattr(homework, "p7"), "Variable p7 is missing.")

        p7 = homework.p7
        self.assertFalse(isinstance(p7, type(Ellipsis)), "Variable p7 was not set.")

        p7 = np.asarray(p7)
        self.assertEqual(p7.shape, (3, 3))
        self.assertValues(p7, expected_projections=[17.635765967738152, 12.418418025922836, 9.440606082983045, 14.296517321751141, 5.5770930986366825, 8.516901505578467, 19.131274967794738, 10.274930973433761, 13.057124279806008])


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
