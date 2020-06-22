#!/usr/bin/env python3

import os
import unittest
from solution.day1 import Day1

class TestDay1(unittest.TestCase):
    def test_calculateFuelForMass(self):
        inputs = [
            { "mass": 12, "fuel": 2},
            { "mass": 14, "fuel": 2},
            { "mass": 1969, "fuel": 654},
            { "mass": 100756, "fuel": 33583},
        ]
        for input in inputs:
            self.assertEqual(Day1().calculateFuelForMass(input["mass"]), input["fuel"])

    def test_calculateFuelForMassAndFuel(self):
        inputs = [
            { "mass": 14, "fuel": 2},
            { "mass": 1969, "fuel": 966},
            { "mass": 100756, "fuel": 50346},
        ]
        for input in inputs:
            fuel = Day1().calculateFuelForMassAndFuel(input["mass"])
            self.assertEqual(fuel, input["fuel"])

    def test_validateInput(self):
        inputs = [ "/asd", "/tmp" ]
        for input in inputs:
            self.assertRaises(FileNotFoundError, Day1().validateInput, input)

    def test_calculateRequiredFuel(self):
        inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")
        inputs = [{
            "file": f"{inputDir}/day1.txt",
            "task1": 3216744,
            "task2": 4822249
        }]
        for input in inputs:
            task1, task2 = Day1().calculateRequiredFuel(input["file"])
            self.assertEqual(task1, input["task1"])
            self.assertEqual(task2, input["task2"])
