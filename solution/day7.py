#!/usr/bin/env python3

import os
from typing import List
import time
from solution.day5 import Day5
# from day5 import Day5

class Day7:
    def calculateThrusterSignal(self, program, phaseSequence, input=0) -> int:
        output = [input]
        amplifiers = []
        for phaseSetting in phaseSequence:
            amplifiers.append(Day5(input=program, phaseSetting=phaseSetting))

        while True:
            if amplifiers[-1].finished:
                break
            for amplifierId in range(5):
                output = amplifiers[amplifierId].run(output)

        return output

    def findMaxThrusterSignal(self, program, phaseSettings = [0,1,2,3,4], rangeStart = 0, rangeFinish = 4):
        result = {"signal": None, "sequence": []}
        for a in range(rangeStart, rangeFinish+1):
            for b in range(rangeStart, rangeFinish+1):
                if b == a:
                    continue
                for c in range(rangeStart, rangeFinish+1):
                    if c == b or c == a:
                        continue
                    for d in range(rangeStart, rangeFinish+1):
                        if d == c or d == b or d == a:
                            continue
                        for e in range(rangeStart, rangeFinish+1):
                            if e == d or e == c or e == b or e == a:
                                continue
                            signal = self.calculateThrusterSignal(program, [a,b,c,d,e])
                            if (result["signal"] is None) or (result["signal"] < signal):
                                result["signal"] = signal
                                result["sequence"] = [a,b,c,d,e]
        return result


def main():
    inputDir = os.path.abspath(f"{os.path.dirname(__file__)}/../input")
    task = Day7().findMaxThrusterSignal(f"{inputDir}/day7.txt")
    print(f"Task 1: {task['signal'][0]}")

    task = Day7().findMaxThrusterSignal(f"{inputDir}/day7.txt", rangeStart=5, rangeFinish=9)
    print(f"Task 2: {task['signal'][0]}")


if __name__ == "__main__":
    main()
