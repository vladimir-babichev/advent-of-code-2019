#!/usr/bin/env python3

import os
from typing import List

class Day3:
    def __init__(self, input):
        self.intersections = []
        self.instructions = []
        self.readInstructions(input)
        self.getMaxStep()
        self.matrix = [["."] * 50 * self.maxStep for i in range(50 * self.maxStep)]
        self.cX = self.cY = self.maxStep // 2

    def readInstructions(self, input):
        if type(input) == str:
            self.readInstructionsFromFile(input)
        elif type(input) == list:
            for line in input:
                self.instructions.append(line.split(","))
        else:
            raise TypeError("Input should be either a file name or a list of strings with comma separated instructions")

    def readInstructionsFromFile(self, fileName: str):
        if not os.path.isfile(fileName):
            raise FileNotFoundError(f"Can't read file {fileName}")
        with open(fileName) as fp:
            for line in fp:
                self.instructions.append(line.split(","))

    def getMaxStep(self):
        self.maxStep = 0
        for instructions in self.instructions:
            for instruction in instructions:
                self.maxStep = max(self.maxStep, int(instruction[1:]))
        if self.maxStep % 2 != 0:
            self.maxStep += 1

    def applyInstructions(self):
        for i, instructions in enumerate(self.instructions):
            # print(f"Going through: {instructions}")
            x = self.cX
            y = self.cY

            for instruction in instructions:
                # print(f"Applying {instruction}")
                if instruction[0] == "R":
                    kx, ky = 1, 0
                if instruction[0] == "U":
                    kx, ky = 0, 1
                if instruction[0] == "L":
                    kx, ky = -1, 0
                if instruction[0] == "D":
                    kx, ky = 0, -1

                for step in range(int(instruction[1:])):
                    # print(f"[{x},{y}] -> [{x+kx*1},{y+ky*1}]")
                    x = x + kx * 1
                    y = y + ky * 1
                    if (self.matrix[x][y] != ".") and (self.matrix[x][y] != str(i+1)):
                        self.intersections.append([x, y])
                        self.matrix[x][y] = "X"
                    else:
                        self.matrix[x][y] = str(i+1)

    def printMatrix(self):
        for i in range(len(self.matrix)-1,-1,-1):
            print("".join(map(str, self.matrix[i])))

    def getShortestDistance(self) -> int:
        distance = abs(self.intersections[0][0]-self.cX)+abs(self.intersections[0][1]-self.cY)
        for cross in self.intersections:
            distance = min(distance, abs(cross[0]-self.cX)+abs(cross[1]-self.cY))
        return distance

def main():
    inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")

    task1 = Day3(f"{inputDir}/day3.txt")
    task1.applyInstructions()
    print(f"Task 1: {task1.getShortestDistance()}")
    # task1.matrix[task1.cX][task1.cY] = "O"
    # task1.printMatrix()

    return

if __name__ == "__main__":
    main()
