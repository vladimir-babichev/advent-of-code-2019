#!/usr/bin/env python3

import os

class Day1:
    def validateInput(self, inputFile: str):
        if not os.path.isfile(inputFile):
            raise FileNotFoundError(f"Input file '{inputFile}' doesn't exist")

    def calculateFuelForMass(self, mass: int) -> int:
        return mass // 3 - 2

    def calculateFuelForMassAndFuel(self, fuel: int) -> int:
        requiredFuel = self.calculateFuelForMass(fuel)
        if requiredFuel > 0:
            return requiredFuel + self.calculateFuelForMassAndFuel(requiredFuel)
        return 0

    def calculateRequiredFuel(self, inputFile: str) -> (int, int):
        self.validateInput(inputFile)
        ret1 = 0
        ret2 = 0
        with open(inputFile) as fp:
            for line in fp:
                ret1 += self.calculateFuelForMass(int(line))
                ret2 += self.calculateFuelForMassAndFuel(int(line))
        return ret1, ret2


def main():
    inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")
    solution = Day1()

    task1, task2 = solution.calculateRequiredFuel(f"{inputDir}/day1.txt")
    print(f"Task 1: {task1}")
    print(f"Task 2: {task2}")

if __name__ == "__main__":
    main()
