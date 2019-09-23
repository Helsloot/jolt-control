#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 1 Oct 2019

Copyright © 2017-2018 Anders Muskens, Philip Winkler, Delmic

Licence
'''


import logging
import os
import time
import unittest
from unittest.case import skip
from src.driver import JOLT


TEST_NOHW = 1#(os.environ.get("TEST_NOHW", 0) != 0)  # Default to Hw testing


# @skip("skip")
class TestSEM(unittest.TestCase):
    """
    Tests which can share one SEM device
    """

    @classmethod
    def setUpClass(cls):
        cls.jolt = JOLT(simulated=TEST_NOHW)

    @classmethod
    def tearDownClass(cls):
        cls.jolt.terminate()

    def test_voltage(self):
        self.jolt.set_voltage(20)
        vol = self.jolt.get_voltage()
        self.assertEqual(20, vol)


if __name__ == "__main__":
    unittest.main()
