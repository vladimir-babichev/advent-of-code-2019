#!/usr/bin/env python3

import os
from typing import List
from day2 import Day2

class Day5(Day2):
    def parseInstruction(self, opcode: int) -> List[int]:
        parameters = [opcode % 100]
        opcode //= 100
        for i in range(3):
            parameters.append(opcode % 10)
            opcode //= 10
        return parameters

    def getAddress(self, mode: int, pointer: int) -> int:
        if mode == 0:
            return self.program[pointer]
        elif mode == 1:
            return pointer
        return None

    def run(self, input=1) -> List[int]:
        output = []
        inputRead = False
        i = 0
        while i < len(self.program):
            offset = 4
            instruction = self.parseInstruction(self.program[i])
            # print(f"Instruction: {self.program[i]}, Parsed instructions: {instruction}")

            if instruction[0] == 99:
                break
            if instruction[0] == 1:
                self.program[self.getAddress(instruction[3],i+3)] = self.program[self.getAddress(instruction[1],i+1)] + self.program[self.getAddress(instruction[2],i+2)]
                i += 4
            elif instruction[0] == 2:
                self.program[self.getAddress(instruction[3],i+3)] = self.program[self.getAddress(instruction[1],i+1)] * self.program[self.getAddress(instruction[2],i+2)]
                i += 4
            elif instruction[0] == 3:
                if not inputRead:
                    self.program[self.getAddress(instruction[1],i+1)] = input
                else:
                    print("Something wrong. Requested input multiple times")
                    break
                i += 2
            elif instruction[0] == 4:
                output.append(self.program[self.getAddress(instruction[1],i+1)])
                i += 2
            elif instruction[0] == 5:
                if self.program[self.getAddress(instruction[1],i+1)] != 0:
                    i = self.program[self.getAddress(instruction[2],i+2)]
                else:
                    i += 3
            elif instruction[0] == 6:
                if self.program[self.getAddress(instruction[1],i+1)] == 0:
                    i = self.program[self.getAddress(instruction[2],i+2)]
                else:
                    i += 3
            elif instruction[0] == 7:
                if self.program[self.getAddress(instruction[1],i+1)] < self.program[self.getAddress(instruction[2],i+2)]:
                    self.program[self.getAddress(instruction[3],i+3)] = 1
                else:
                    self.program[self.getAddress(instruction[3],i+3)] = 0
                i += 4
            elif instruction[0] == 8:
                if self.program[self.getAddress(instruction[1],i+1)] == self.program[self.getAddress(instruction[2],i+2)]:
                    self.program[self.getAddress(instruction[3],i+3)] = 1
                else:
                    self.program[self.getAddress(instruction[3],i+3)] = 0
                i += 4
        return output

def main():
    inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")

    task = Day5(f"{inputDir}/day5.txt")
    result = task.run(1)
    print(f"Task 1: {result[-1]}")

    task = Day5(f"{inputDir}/day5.txt")
    result = task.run(5)
    print(f"Task 2: {result[0]}")

if __name__ == "__main__":
    main()
