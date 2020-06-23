#!/usr/bin/env python3

import os
from typing import List

class Day3:
    def __init__(self, input):
        self.intersections = []
        self.instructions = []
        self.readInstructions(input)
        self.getBoundaries()
        self.matrix = [["."] * (abs(self.boundaries["R"]) + abs(self.boundaries["L"]) + 2) for i in range(abs(self.boundaries["U"]) + abs(self.boundaries["D"]) + 3)]
        self.cX = abs(self.boundaries["L"])
        self.cY = abs(self.boundaries["D"])+1
        self.matrix[self.cY][self.cX] = "O"
        self.wireDistances = {}

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

    def getBoundaries(self):
        self.boundaries = {"L": 1, "R": 1, "U": 1, "D": 1}
        for instructions in self.instructions:
            xPos = yPos = 0
            for instruction in instructions:
                if instruction[0] == "R":
                    xPos += int(instruction[1:])
                    self.boundaries["R"] = max(xPos, self.boundaries["R"])
                elif instruction[0] == "L":
                    xPos -= int(instruction[1:])
                    self.boundaries["L"] = min(xPos, self.boundaries["L"])
                elif instruction[0] == "U":
                    yPos += int(instruction[1:])
                    self.boundaries["U"] = max(yPos, self.boundaries["U"])
                elif instruction[0] == "D":
                    yPos -= int(instruction[1:])
                    self.boundaries["D"] = min(yPos, self.boundaries["D"])


    def applyInstructions(self):
        for i, instructions in enumerate(self.instructions):
            x = self.cX
            y = self.cY

            for instruction in instructions:
                if instruction[0] == "R":
                    kx, ky = 1, 0
                if instruction[0] == "U":
                    kx, ky = 0, 1
                if instruction[0] == "L":
                    kx, ky = -1, 0
                if instruction[0] == "D":
                    kx, ky = 0, -1

                for step in range(int(instruction[1:])):
                    x += kx
                    y += ky
                    if (self.matrix[y][x] != ".") and (self.matrix[y][x] != str(i+1)):
                        self.intersections.append([x, y])
                        self.matrix[y][x] = "X"
                    else:
                        self.matrix[y][x] = str(i+1)

    def printMatrix(self):
        for i in range(len(self.matrix)-1,-1,-1):
            print("".join(map(str, self.matrix[i])))

    def getClosestDistance(self) -> int:
        distance = abs(self.intersections[0][0]-self.cX)+abs(self.intersections[0][1]-self.cY)
        for cross in self.intersections:
            distance = min(distance, abs(cross[0]-self.cX)+abs(cross[1]-self.cY))
        return distance

    def traceWire(self):
        for i in range(1, len(self.instructions)+1):
            currX = prevX = self.cX
            currY = prevY = self.cY
            distance = 0

            while True:
                foundStep = False
                dirX = currX - prevX
                dirY = currY - prevY

                for dX, dY in [[dirX, dirY], [0,1], [1,0], [0,-1], [-1,0]]:
                    if (currX + dX != prevX) or (currY + dY != prevY):
                        if self.matrix[currY + dY][currX + dX] in [str(i), "X"]:
                            prevX, prevY = currX, currY
                            currX += dX
                            currY += dY
                            distance += 1
                            foundStep = True
                            if self.matrix[currY][currX] == "X":
                                if f"{currX}:{currY}" in self.wireDistances:
                                    self.wireDistances[f"{currX}:{currY}"] += distance
                                else:
                                    self.wireDistances[f"{currX}:{currY}"] = distance
                            break
                if not foundStep:
                    break


    def getShortestDistance(self):
        return self.wireDistances[min(self.wireDistances.keys(), key=(lambda k: self.wireDistances[k]))]


def main():
    inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")
    task = Day3(f"{inputDir}/day3.txt")

    task.applyInstructions()
    print(f"Task 1: {task.getClosestDistance()}")

    task.traceWire()
    print(f"Task 2: {task.getShortestDistance()}")

if __name__ == "__main__":
    main()
