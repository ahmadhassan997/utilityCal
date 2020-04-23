#! /usr/bin/python3
import os

if __name__ == "__main__":
    cwd = os.getcwd()
    print("generating stationary traces 0.5 sec granularity")
    os.system(cwd + "/artificial_traces.py artificial-traces/stationary-15-20-0.5 120 15 20 S0.5")
    print("generating stationary traces 1 sec granularity")
    os.system(cwd + "/artificial_traces.py artificial-traces/stationary-15-20-1.0 120 15 20 S1.0")
    print("generating stationary traces 1.5 sec granularity")
    os.system(cwd + "/artificial_traces.py artificial-traces/stationary-15-20-1.5 120 15 20 S1.5")
