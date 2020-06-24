import os
import unittest
from solution.day5 import Day5
from solution.day2 import Day2

class TestDay5(unittest.TestCase):
    def test_validateInputType(self):
        inputs = ["/asd", "/tmp", 1, True]
        for input in inputs:
            self.assertRaises(FileNotFoundError, Day5().readProgramFromFile, input)

    def test_run(self):
        inputs = [
            {"program": [1,0,0,0,99], "result": [2,0,0,0,99]},
            {"program": [2,3,0,3,99], "result": [2,3,0,6,99]},
            {"program": [2,4,4,5,99,0], "result": [2,4,4,5,99,9801]},
            {"program": [1,1,1,4,99,5,6,0,99], "result": [30,1,1,4,2,5,6,0,99]},
            {"program": [3,0,4,0,99], "result": [1,0,4,0,99]},
        ]
        for input in inputs:
            test = Day5(input["program"])
            test.run()
            self.assertEqual(test.program, input["result"])

    def test_runOutput(self):
        inputs = [
            # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
            {"input": 1, "program": [3,9,8,9,10,9,4,9,99,-1,8], "output": [0]},
            {"input": 8, "program": [3,9,8,9,10,9,4,9,99,-1,8], "output": [1]},

            # # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
            {"input": 1, "program": [3,9,7,9,10,9,4,9,99,-1,8], "output": [1]},
            {"input": 8, "program": [3,9,7,9,10,9,4,9,99,-1,8], "output": [0]},

            # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
            {"input": 1, "program": [3,3,1108,-1,8,3,4,3,99], "output": [0]},
            {"input": 8, "program": [3,3,1108,-1,8,3,4,3,99], "output": [1]},

            # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
            {"input": 1, "program": [3,3,1107,-1,8,3,4,3,99], "output": [1]},
            {"input": 8, "program": [3,3,1107,-1,8,3,4,3,99], "output": [0]},

            # Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
            {"input": 0, "program": [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], "output": [0]},
            {"input": 1, "program": [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], "output": [1]},
            {"input": 0, "program": [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], "output": [0]},
            {"input": 1, "program": [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], "output": [1]},

            # The above example program uses an input instruction to ask for a single number.
            # The program will then output 999 if the input value is below 8, output 1000 if
            # the input value is equal to 8, or output 1001 if the input value is greater than 8.
            {
                "input": 1,
                "program": [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],
                "output": [999]
            },
            {
                "input": 8,
                "program": [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],
                "output": [1000]
            },
            {
                "input": 10,
                "program": [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],
                "output": [1001]
            },
        ]
        for input in inputs:
            test = Day5(input["program"])
            output = test.run(input["input"])
            self.assertEqual(output, input["output"])
