#!/usr/bin/env python3

import os
from typing import List

class Day4:
    def readInput(self, input):
        if type(input) == str:
            self.readInputFromFile(input)
        elif type(input) == list:
            try:
                self.start, self.finish = map(tuple, input)
            except:
                raise TypeError("Input should be a file name of a list of integers")
        else:
            raise TypeError("Input should be either a file name or a list of integers")

    def readInputFromFile(self, fileName: str):
        if not os.path.isfile(fileName):
            raise FileNotFoundError(f"Can't read file {fileName}")
        with open(fileName) as fp:
            self.start, self.finish = map(int, fp.read().splitlines())

    def validateNumber(self, number: int):
        hasAdj = False

        prevDigit = number % 10
        number //= 10
        while number > 0:
            currDigit = number % 10
            if currDigit > prevDigit:
                return False
            if currDigit == prevDigit:
                hasAdj = True
            prevDigit = currDigit
            number //= 10
        return hasAdj

    def validateNumberPart2(self, number: int):
        adjList = []
        currAdj = []

        prevDigit = number % 10
        number //= 10
        while number > 0:
            currDigit = number % 10
            if currDigit > prevDigit:
                return False
            if currDigit == prevDigit:
                currAdj.append(currDigit)
            elif len(currAdj) > 0:
                adjList.append(currAdj)
                currAdj = []
            prevDigit = currDigit
            number //= 10

        if len(currAdj) > 0:
            adjList.append(currAdj)
        for adj in adjList:
            if len(adj) == 1:
                return True

        return False

    def countCombinations(self):
        counter = 0
        for num in range(self.start, self.finish):
            if self.validateNumber(num):
                counter += 1
        return counter

    def countCombinationsPart2(self):
        counter = 0
        for num in range(self.start, self.finish):
            if self.validateNumberPart2(num):
                counter += 1
        return counter

def main():
    inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")
    task = Day4()
    task.readInput(f"{inputDir}/day4.txt")
    print(f"Task 1: {task.countCombinations()}")
    print(f"Task 2: {task.countCombinationsPart2()}")

if __name__ == "__main__":
    main()
