#!/usr/bin/env python3

import os

class Day8:
    def __init__(self, inputImage: str, width=25, height=6):
        if not inputImage.isdigit():
            inputImage = self.readFromFile(inputImage)
        self.imageWidth = width
        self.imageHeight = height
        self.imageLayers = list(self.chunkString(inputImage, self.imageWidth * self.imageHeight))

    def readFromFile(self, inputFile: str):
        self.validateInput(inputFile)
        with open(inputFile, "r") as fp:
            return fp.read().splitlines()[0]

    def validateInput(self, inputFile: str):
        if not os.path.isfile(inputFile):
            raise FileNotFoundError(f"Input file '{inputFile}' doesn't exist")

    def chunkString(self, string, length):
        return (string[0+i:length+i] for i in range(0, len(string), length))

    def validateImage(self):
        controlLayer = 0
        contorlZeroCount = self.imageLayers[controlLayer].count("0")
        for i, layer in enumerate(self.imageLayers):
            zeroCount = layer.count("0")
            if zeroCount < contorlZeroCount:
                controlLayer = i
                contorlZeroCount = zeroCount
        hashSum = self.imageLayers[controlLayer].count("1") * self.imageLayers[controlLayer].count("2")
        return(hashSum)

    def decodeImage(self):
        self.image = ""
        for i in range(self.imageWidth * self.imageHeight):
            for j in range(len(self.imageLayers)):
                if self.imageLayers[j][i] != "2":
                    self.image += self.imageLayers[j][i]
                    break

    def printImage(self):
        for line in self.chunkString(self.image, self.imageWidth):
            print(line.replace("0", " "))

def main():
    inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")
    task = Day8(f"{inputDir}/day8.txt")
    print(f"Task 1: {task.validateImage()}")

    task.decodeImage()
    print("Task 2:")
    task.printImage()

if __name__ == "__main__":
    main()
