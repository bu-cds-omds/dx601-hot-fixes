#!/usr/bin/env python3

import unittest
import test_utils


class P6TestCase(test_utils.TestCase):
    def test_p6(self):
        f6 = self.homework.f6
        if f6({"green_rating": 1.0, "softness": 0.0, "wrinkles": 0.0, "yellow_rating": 0.0}):
            f6_fixed = True
        else:
            f6_fixed = False

        if f6_fixed:
            self.assertScalarByName(
                "p6",
                expected_projections=[0.5099123064065627],
                known_mistakes=[(30.36, "p6 is sum of L2 losses instead of average.")],
            )
        else:
            self.assertScalarByName(
                "p6",
                expected_projections=[0.4496163518611226],
                known_mistakes=[(26.77, "p6 is sum of L2 losses instead of average.")],
            )


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
