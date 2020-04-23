#! /usr/bin/python3
import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    file_t = sys.argv[1]
    filename = str(sys.argv[2])
    thpt = np.loadtxt(file_t)
    plt.plot(thpt[:, 0], thpt[:, 1])
    plt.title(filename)
    plt.savefig("tput-plots/" + filename)
    # plt.show()
