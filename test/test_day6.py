import os
import unittest
from solution.day6 import Day6

class TestDay6(unittest.TestCase):
    def test_validateInputType(self):
        inputs = ["/asd", "/tmp", 1, True]
        for input in inputs:
            self.assertRaises(FileNotFoundError, Day6().readInputFromFile, input)

    def test_countOrbits(self):
        inputs = [
            {
                "mapData": ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"],
                "object": "L",
                "orbitCount": 7
            },
            {
                "mapData": ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"],
                "object": "D",
                "orbitCount": 3
            },
            {
                "mapData": ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"],
                "object": "COM",
                "orbitCount": 0
            },
        ]
        for input in inputs:
            test = Day6(input["mapData"])
            test.mapOrbit()
            self.assertEqual(test.countOrbits(input["object"]), input["orbitCount"])

    def test_countAllOrbits(self):
        inputs = [
            {
                "mapData": ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"],
                "orbitCount": 42
            },
        ]
        for input in inputs:
            test = Day6(input["mapData"])
            test.mapOrbit()
            self.assertEqual(test.countAllOrbits(), input["orbitCount"])

    def test_countHopsBetweenOrbits(self):
        inputs = [
            {
                "mapData": ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"],
                "hops": 4
            },
        ]
        for input in inputs:
            test = Day6(input["mapData"])
            test.mapOrbit()
            test.countAllOrbits()
            self.assertEqual(test.countHopsBetweenOrbits('YOU', 'SAN'), input["hops"])
