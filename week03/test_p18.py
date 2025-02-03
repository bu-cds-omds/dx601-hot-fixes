#!/usr/bin/env python3

import unittest
import test_utils


class P18TestCase(test_utils.TestCase):
    def test_p18(self):
        self.assertScalarByName("p18", expected_projections=[0.00998134384834979])


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
