#!/usr/bin/env python3

import os
from typing import List

class ListNode:
    def __init__(self, val=0, next=[]):
        self.val = val
        self.next = next

class Day6:
    def __init__(self, input=[]):
        self.orbitList = []
        self.orbitMap = {}
        if type(input) == str:
            self.readInputFromFile(input)
        elif type(input) == list:
            self.orbitList = input
        else:
            raise TypeError("Input should be eaither file name or a list of integers")

    def readInputFromFile(self, inputFile: str):
        self.validateInput(inputFile)
        with open(inputFile, "r") as fp:
            self.orbitList = fp.read().splitlines()

    def validateInput(self, inputFile: str):
        if not os.path.isfile(inputFile):
            raise FileNotFoundError(f"Input file '{inputFile}' doesn't exist")

    def mapOrbit(self):
        for orbit in self.orbitList:
            leftObj, rightObj = orbit.split(')')
            # print(f"Left {leftObj} - Right {rightObj}")
            if leftObj not in self.orbitMap:
                self.orbitMap[leftObj] = {"orbitCount": None, "objects": []}
            if rightObj not in self.orbitMap:
                self.orbitMap[rightObj] = {"orbitCount": None, "objects": []}
            if leftObj == 'COM':
                self.orbitMap[leftObj]["orbitCount"] = 0
            self.orbitMap[leftObj]["objects"].append(rightObj)

    def countOrbits(self, child: str):
        if self.orbitMap[child]["orbitCount"] is not None:
            return self.orbitMap[child]["orbitCount"]
        for parent, properties in self.orbitMap.items():
            if child in properties["objects"]:
                if properties["orbitCount"] is None:
                    properties["orbitCount"] = self.countOrbits(parent)
                    return properties["orbitCount"] + 1
                else:
                    return properties["orbitCount"] + 1
        return None

    def countAllOrbits(self):
        count = 0
        for obj, props in self.orbitMap.items():
            if props["orbitCount"] is None:
                props["orbitCount"] = self.countOrbits(obj)
            count += props["orbitCount"]
        return count

    def findParent(self, obj: str) -> str:
        for parent, properties in self.orbitMap.items():
            if obj in properties["objects"]:
                return parent
        return None

    def findCommonOrbit(self, left: str, right: str) -> str:
        if left == right:
            return left
        if self.orbitMap[left]["orbitCount"] > self.orbitMap[right]["orbitCount"]:
            left = self.findParent(left)
        elif self.orbitMap[left]["orbitCount"] < self.orbitMap[right]["orbitCount"]:
            right = self.findParent(right)
        else:
            left = self.findParent(left)
            right = self.findParent(right)
        return self.findCommonOrbit(left, right)

    def countHopsBetweenOrbits(self, left: str, right: str) -> int:
        common = self.findCommonOrbit(left, right)
        return self.orbitMap[left]['orbitCount'] + self.orbitMap[right]['orbitCount'] - 2 * self.orbitMap[common]['orbitCount'] - 2


def main():
    inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")
    task = Day6(f"{inputDir}/day6.txt")
    task.mapOrbit()
    print(f"Task 1: {task.countAllOrbits()}")
    print(f"Task 2: {task.countHopsBetweenOrbits('YOU', 'SAN')}")

if __name__ == '__main__':
    main()

