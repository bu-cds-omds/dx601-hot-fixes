#!/usr/bin/env python3

import inspect
import homework

import test_utils


class P13TestCase(test_utils.TestCase):
    def test_p13(self):
        self.assertTrue(hasattr(homework, "p13"), "Variable p13 is missing.")

        p13 = homework.p13
        self.assertFalse(isinstance(p13, type(Ellipsis)), "Variable p13 was not set.")

        self.assertValues(p13, expected_projections=[1.5613383558638163])


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
