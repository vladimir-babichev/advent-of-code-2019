import unittest
from solution.day8 import Day8

class TestDay8(unittest.TestCase):
    def test_validateImage(self):
        inputs = [
            {
                "image": "112235679012",
                "width": 3,
                "height": 2,
                "result": 4
            }
        ]
        for input in inputs:
            result = Day8(input["image"], input["width"], input["height"]).validateImage()
            self.assertEqual(result, input["result"])

    def test_decodeImage(self):
        inputs = [
            {
                "image": "0222112222120000",
                "width": 2,
                "height": 2,
                "result": "0110"
            }
        ]
        for input in inputs:
            test = Day8(input["image"], input["width"], input["height"])
            test.decodeImage()
            self.assertEqual(test.image, input["result"])
