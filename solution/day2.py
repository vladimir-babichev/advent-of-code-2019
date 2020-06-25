#!/usr/bin/env python3

import os

class Day2():
    def __init__(self, input=[]):
        if type(input) == str:
            self.readProgramFromFile(input)
        elif type(input) == list:
            self.program = input
        else:
            raise TypeError("Input should be eaither file name or a list of integers")

    def readProgramFromFile(self, inputFile: str):
        self.validateInput(inputFile)
        with open(inputFile, "r") as fp:
            self.program = list(map(int, fp.read().split(',')))

    def validateInput(self, inputFile: str):
        if not os.path.isfile(inputFile):
            raise FileNotFoundError(f"Input file '{inputFile}' doesn't exist")

    def run(self):
        for i in range(0, len(self.program), 4):
            if self.program[i] == 99:
                break
            if self.program[i] == 1:
                self.program[self.program[i+3]] = self.program[self.program[i+1]] + self.program[self.program[i+2]]
            elif self.program[i] == 2:
                self.program[self.program[i+3]] = self.program[self.program[i+1]] * self.program[self.program[i+2]]


def main():
    inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")

    task1 = Day2(f"{inputDir}/day2.txt")
    task1.program[1] = 12
    task1.program[2] = 2
    task1.run()
    result1 = task1.program[0]
    print(f"Task 1: {result1}")

    stop = False
    for noun in range(100):
        if stop:
            break
        for verb in range(100):
            task2 = Day2(f"{inputDir}/day2.txt")
            task2.program[1] = noun
            task2.program[2] = verb
            task2.run()
            if task2.program[0] == 19690720:
                result2 = 100 * noun + verb
                print(f"Task 2: {result2}")
                stop = True

if __name__ == "__main__":
    main()
