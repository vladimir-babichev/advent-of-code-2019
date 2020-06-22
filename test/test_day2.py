import os
import unittest
from solution.day2 import Day2

class TestDay2(unittest.TestCase):
    def test_validateInputType(self):
        inputs = ["/asd", "/tmp", 1, True]
        for input in inputs:
            self.assertRaises(FileNotFoundError, Day2().readProgramFromFile, input)

    def test_run(self):
        inputs = [
            {"program": [1,0,0,0,99], "result": [2,0,0,0,99]},
            {"program": [2,3,0,3,99], "result": [2,3,0,6,99]},
            {"program": [2,4,4,5,99,0], "result": [2,4,4,5,99,9801]},
            {"program": [1,1,1,4,99,5,6,0,99], "result": [30,1,1,4,2,5,6,0,99]}
        ]
        for input in inputs:
            test = Day2(input["program"])
            test.run()
            self.assertEqual(test.program, input["result"])
