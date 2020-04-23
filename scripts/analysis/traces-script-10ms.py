#! /usr/bin/python3
import os

if __name__ == "__main__":
    cwd = os.getcwd()
    print("generating stationary traces")
    os.system(cwd + "/artificial_traces.py artificial-traces/stationary-15-20 120 15 20 S")
    print("generating normal handoffs traces")
    os.system(cwd + "/artificial_traces.py artificial-traces/normal-15-20 120 15 20 N")
    print("generating frequent handoffs traces")
    os.system(cwd + "/artificial_traces.py artificial-traces/frequent-15-20 120 15 20 F")
