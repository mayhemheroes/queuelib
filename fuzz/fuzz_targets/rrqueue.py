#!/usr/bin/env python3

import atheris
import sys
import os

with atheris.instrument_imports():
    from queuelib import FifoDiskQueue, RoundRobinQueue

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)

    qfactory = lambda priority: FifoDiskQueue(f"rrqueuefile-{priority}")
    q = RoundRobinQueue(qfactory)

    for i in range(fdp.ConsumeIntInRange(1, 20)):
        if fdp.ConsumeBool():
            q.push(fdp.ConsumeBytes(32), str(fdp.ConsumeIntInRange(1, 3)))
        else:
            q.pop()
    q.close()

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()