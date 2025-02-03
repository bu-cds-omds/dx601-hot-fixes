#!/usr/bin/env python3

import unittest
import test_utils


class P5TestCase(test_utils.TestCase):
    def test_p5(self):
        f5 = self.homework.f5
        if f5({"green_rating": 1.0, "softness": 0.0, "yellow_rating": 0.0}):
            f5_fixed = True
        else:
            f5_fixed = False

        if f5_fixed:
            self.assertArrayByName(
                "p5",
                expected_length=8,
                expected_projections=[
                    13.613816371683132,
                    11.22689816180878,
                    10.527418281350403,
                    12.903789839711873,
                    5.641556189802811,
                    18.395585378678604,
                    3.1324450707025124,
                    7.553342480476515,
                ],
            )
        else:
            self.assertArrayByName(
                "p5",
                expected_length=8,
                expected_projections=[
                    11.712984000075336,
                    9.927821075450309,
                    9.353454120012412,
                    11.25642668362092,
                    4.990315181764306,
                    16.175942151340404,
                    2.7871915443640916,
                    6.954922796600389,
                ],
            )


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
