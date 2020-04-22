#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

"""
Format:
        Capacity | Throughput | Signal-delay | Per-packet-queuing-delay
sprout
cubic
reno
verus2
verus4
verus6
"""

if __name__=="__main__":
    PLTDIR = "./../../plots/handoffs/"
    protocols = ["sprout", "cubic", "reno", "verus2", "verus4", "verus6"]
    colors = ["red", "blue", "green", "yellow", "black", "purple"]
    stationary = np.loadtxt("stats/stationary-stats", usecols = (1,2,3,4))
    normal = np.loadtxt("stats/normal-stats", usecols = (1,2,3,4))
    frequent = np.loadtxt("stats/frequent-stats", usecols = (1,2,3,4))
    ## Stationary
    fig, ax = plt.subplots()
    for i, txt in enumerate(protocols):
        ax.scatter(stationary[i, 2], stationary[i, 1], c = colors[i], label = protocols[i], s = 100)
    ax.legend()
    ax.set_xlabel("Delay(ms)")
    ax.set_ylabel("Throughput(Mbps)")
    ax.set_title("Stationary-15-20")
    ax.invert_xaxis()
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    x_pos = (x_max + x_min) / 2
    y_pos = (y_max + y_min) / 2
    ax.annotate('Better', ha = 'center', va = 'bottom', xytext = (x_pos + 5, y_pos - 1), 
                            xy = (x_pos, y_pos), arrowprops = {'facecolor' : 'green'})
    plt.savefig(PLTDIR + "stationary-15-20")

    ## Normal Handoffs
    fig, ax = plt.subplots()
    for i, txt in enumerate(protocols):
        ax.scatter(normal[i, 2], normal[i, 1], c = colors[i], label = protocols[i], s = 100)
    ax.legend()
    ax.set_xlabel("Delay(ms)")
    ax.set_ylabel("Throughput(Mbps)")
    ax.set_title("Normal-15-20")
    ax.invert_xaxis()
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    x_pos = (x_max + x_min) / 2
    y_pos = (y_max + y_min) / 2
    ax.annotate('Better', ha = 'center', va = 'bottom', xytext = (x_pos + 5, y_pos - 1), 
                            xy = (x_pos, y_pos), arrowprops = {'facecolor' : 'green'})
    plt.savefig(PLTDIR + "normal-15-20")

    ## Frequent Handoffs
    fig, ax = plt.subplots()
    for i, txt in enumerate(protocols):
        ax.scatter(frequent[i, 2], frequent[i, 1], c = colors[i], label = protocols[i], s = 100)
    ax.legend()
    ax.set_xlabel("Delay(ms)")
    ax.set_ylabel("Throughput(Mbps)")
    ax.set_title("Frequent-15-20")
    ax.invert_xaxis()
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    x_pos = (x_max + x_min) / 2
    y_pos = (y_max + y_min) / 2
    ax.annotate('Better', ha = 'center', va = 'bottom', xytext = (x_pos + 5, y_pos - 1), 
                            xy = (x_pos, y_pos), arrowprops = {'facecolor' : 'green'})
    plt.savefig(PLTDIR + "frequent-15-20")