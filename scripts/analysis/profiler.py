#! /usr/bin/python3
import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    file_d = sys.argv[1]
    file_t = sys.argv[2]
    # delay = np.loadtxt(file_d)
    thpt = np.loadtxt(file_t)
    # plt.plot(delay)
    plt.plot(thpt[:, 0], thpt[:, 1])
    plt.plot()
    plt.show()
