#!/usr/bin/env python3

import unittest
from solution.day4 import Day4

class TestDay3(unittest.TestCase):
    def test_readInputError(self):
        inputs = [
            {"exception": TypeError, "params": 1},
            {"exception": TypeError, "params": True},
            {"exception": TypeError, "params": {}},
            {"exception": FileNotFoundError, "params": "str"},
            {"exception": FileNotFoundError, "params": "/asd"},
            {"exception": FileNotFoundError, "params": "/tmp"}
        ]
        for input in inputs:
            self.assertRaises(input["exception"], Day4().readInput, input["params"])

    # def test_validateNumber(self):
    #     inputs = [
    #         { "num": 111111, "res": True },
    #         { "num": 111123, "res": True },
    #         { "num": 223459, "res": True },
    #         { "num": 223450, "res": False },
    #         { "num": 123789, "res": False }
    #     ]
    #     for input in inputs:
    #         self.assertEqual(Day4().validateNumber(input["num"]), input["res"])

    def test_validateNumberPart2(self):
        inputs = [
            { "num": 111111, "res": False },
            { "num": 111123, "res": False },
            { "num": 223459, "res": True },
            { "num": 223450, "res": False },
            { "num": 123789, "res": False },

            { "num": 112233, "res": True },
            { "num": 123444, "res": False },
            { "num": 111122, "res": True }
        ]
        for input in inputs:
            self.assertEqual(Day4().validateNumberPart2(input["num"]), input["res"])
