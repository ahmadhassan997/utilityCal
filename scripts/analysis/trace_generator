#! /usr/bin/python3
'''
Idea taken from Alfalfa project and extended
'''
from random import randint
import sys

if __name__=="__main__":
    if (len(sys.argv) != 6):
        print ("Usage: ./trace_generator OUTPUT_FILE INTERVALS MIN_T MAX_T LOSSRATE")
        exit()
    else:
        print ("Generating Artificial Traces")
    FILE = sys.argv[1]
    INTERVALS = int(sys.argv[2])
    MIN_T = int(sys.argv[3])
    MAX_T = int(sys.argv[4])
    LOSS = int(sys.argv[5])
    if (LOSS < 0 or LOSS > 100):
        print ("LOSS RATE MUST BE IN THE RANGE 0-100")
        exit()
    with open(FILE, "w") as output_file:
        timestamp = 0
        for interval in range(INTERVALS):
            t_put = randint(MIN_T, MAX_T)
            mbpms = t_put * 1000
            pktsp10ms = int(float(mbpms) / (1500 * 8) * 10)
            for i in range(0, 500):
                if randint(0, 100) > LOSS:
                    for j in range(pktsp10ms):
                        output_file.write(str(timestamp) + "\n")
                timestamp += 10
        output_file.close()

