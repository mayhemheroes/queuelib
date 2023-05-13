#!/usr/bin/env python3

import atheris
import sys
import os

with atheris.instrument_imports():
    from queuelib import LifoDiskQueue

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    q = LifoDiskQueue("lifoqueuefile")
    for i in range(fdp.ConsumeIntInRange(1, 20)):
        if fdp.ConsumeBool():
            q.push(fdp.ConsumeBytes(32))
        else:
            q.pop()
    q.close()

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()