#!/usr/bin/env python3

import unittest
from solution.day3 import Day3

class TestDay3(unittest.TestCase):
    def test_readInstructionsError(self):
        inputs = [
            {"exception": TypeError, "params": 1},
            {"exception": TypeError, "params": True},
            {"exception": TypeError, "params": {}},
            {"exception": FileNotFoundError, "params": "str"},
            {"exception": FileNotFoundError, "params": "/asd"},
            {"exception": FileNotFoundError, "params": "/tmp"}
        ]
        for input in inputs:
            self.assertRaises(input["exception"], Day3([]).readInstructions, input["params"])

    def test_readInstructions(self):
        inputs = [
            {
                "params": ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"],
                "result": [["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"], ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]]
            },
            {
                "params": ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"],
                "result": [["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"], ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]]
            }
        ]
        for input in inputs:
            test = Day3(input["params"])
            # test.readInstructions()
            self.assertEqual(test.instructions, input["result"])

    def test_getClosestDistance(self):
        inputs = [
            {
                "params": ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"],
                "result": 159
            },
            {
                "params": ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"],
                "result": 135
            }
        ]
        for input in inputs:
            test = Day3(input["params"])
            test.applyInstructions()
            self.assertEqual(test.getClosestDistance(), input["result"])

    def test_getShortestDistance(self):
        inputs = [
            {
                "params": ["R8,U5,L5,D3", "U7,R6,D4,L4"],
                "result": 30
            },
            {
                "params": ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"],
                "result": 610
            },
            {
                "params": ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"],
                "result": 410
            }
        ]
        for input in inputs:
            test = Day3(input["params"])
            test.applyInstructions()
            test.traceWire()
            self.assertEqual(test.getShortestDistance(), input["result"])
