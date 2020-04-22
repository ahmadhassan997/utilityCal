#! /usr/bin/python3

from random import randint
import sys

if __name__=="__main__":
    if (len(sys.argv) != 6):
        print ("Usage: ./artificial_traces OUTPUT_FILE TIME(secs) MIN_T MAX_T TYPE(S/L/H)")
        exit()
    else:
        print ("Generating Artificial Traces")
    FILE = sys.argv[1]
    INTERVAL = int(sys.argv[2])
    MIN_T = int(sys.argv[3])
    MAX_T = int(sys.argv[4])
    TYPE = sys.argv[5]
    with open(FILE + "-delay", "w") as ofile_d, open(FILE + "-throughput", "w") as ofile_t:
        timestamp = 0
        t_put = 0
        if TYPE == "S": # Stationary
            for i in range(INTERVAL):
                for i in range(100):
                    t_put = randint(MIN_T, MAX_T)
                    mbpms = t_put * 1000
                    pktsp10ms = int(float(mbpms) / (1500 * 8) * 10)
                    for j in range(pktsp10ms):
                        ofile_d.write(str(timestamp) + "\n")
                    ofile_t.write(str(timestamp) + " " + str(t_put) + "\n")
                    timestamp += 10
        if TYPE == "L": # Normal Handoffs
            for i in range(INTERVAL):
                for i in range(100):
                    if i in range(48, 52) and INTERVAL % 20 == 0:
                        t_put = randint(0, 4)
                    else:
                        t_put = randint(MIN_T, MAX_T)
                    mbpms = t_put * 1000
                    pktsp10ms = int(float(mbpms) / (1500 * 8) * 10)
                    for j in range(pktsp10ms):
                        ofile_d.write(str(timestamp) + "\n")
                    ofile_t.write(str(timestamp) + " " + str(t_put) + "\n")
                    timestamp += 10
        if TYPE == "H": # Frequent Handoffs
            for i in range(INTERVAL):
                for i in range(100):
                    if i in range(48, 52) and INTERVAL % 5 == 0:
                        t_put = randint(0, 4)
                    else:
                        t_put = randint(MIN_T, MAX_T)
                    mbpms = t_put * 1000
                    pktsp10ms = int(float(mbpms) / (1500 * 8) * 10)
                    for j in range(pktsp10ms):
                        ofile_d.write(str(timestamp) + "\n")
                    ofile_t.write(str(timestamp) + " " + str(t_put) + "\n")
                    timestamp += 10
        ofile_d.close()
        ofile_t.close()