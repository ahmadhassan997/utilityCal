#! /usr/bin/python3
import os

if __name__ == "__main__":
    print ("Starting Experiment....")
    print ("The experiment will take a lot of time.") 
    print ("So sit back and relax or you can complete your other assignments.") 
    print ("I know you've been procrastinating!\n")
    # set the forwarding port
    os.system("sudo sysctl -w net.ipv4.ip_forward=1")
    curr_dir = os.getcwd()
    wk_dir = curr_dir + "/scripts/run/"

    # RUN STATIONARY TRACE EXPERIMENTS
    os.system(wk_dir + "run-verus-stat")
    os.system(wk_dir + "run-sprout-stat")
    os.system(wk_dir + "run-cubic-stat")
    os.system(wk_dir + "run-reno-stat")


    # RUN AT&T TRACE EXPERIMENT
    os.system(wk_dir + "run-verus-att")
    os.system(wk_dir + "run-sprout-att")
    os.system(wk_dir + "run-cubic-att")
    os.system(wk_dir + "run-reno-att")


    # create plots
    # mm-throughput-graph bin log
    # mm-tput-dual-graph bin log1 log2
    # mm-tput-delay-graph bin log1 log2 log3 log4