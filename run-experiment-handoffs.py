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
    os.system(wk_dir + "run-verus-stationary")
    os.system(wk_dir + "run-sprout-stationary")
    os.system(wk_dir + "run-cubic-stationary")
    os.system(wk_dir + "run-reno-stationary")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/sprout_stationary-15-20.down > ./plots/sprout_stationary-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/cubic_stationary-15-20.down > ./plots/cubic_stationary-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/reno_stationary-15-20.down > ./plots/reno_stationary-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus2_stationary-15-20.down > ./plots/verus2_stationary-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus4_stationary-15-20.down > ./plots/verus4_stationary-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus6_stationary-15-20.down > ./plots/verus6_stationary-15-20-downlink.html")


    # RUN NORMAL HANDOFF TRACE EXPERIMENT
    os.system(wk_dir + "run-verus-normal")
    os.system(wk_dir + "run-sprout-normal")
    os.system(wk_dir + "run-cubic-normal")
    os.system(wk_dir + "run-reno-normal")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/sprout_normal-15-20.down > ./plots/sprout_normal-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/cubic_normal-15-20.down > ./plots/cubic_normal-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/reno_normal-15-20.down > ./plots/reno_normal-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus2_normal-15-20.down > ./plots/verus2_normal-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus4_normal-15-20.down > ./plots/verus4_normal-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus6_normal-15-20.down > ./plots/verus6_normal-15-20-downlink.html")

    # # RUN FREQUENT HANDOFF TRACE EXPERIMENT
    os.system(wk_dir + "run-verus-frequent")
    os.system(wk_dir + "run-sprout-frequent")
    os.system(wk_dir + "run-cubic-frequent")
    os.system(wk_dir + "run-reno-frequent")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/sprout_frequent-15-20.down > ./plots/sprout_frequent-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/cubic_frequent-15-20.down > ./plots/cubic_frequent-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/reno_frequent-15-20.down > ./plots/reno_frequent-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus2_frequent-15-20.down > ./plots/verus2_frequent-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus4_frequent-15-20.down > ./plots/verus4_frequent-15-20-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus6_frequent-15-20.down > ./plots/verus6_frequent-15-20-downlink.html")


    # mm-throughput-graph bin log
    # mm-tput-dual-graph bin log1 log2
    # mm-tput-delay-graph bin log1 log2 log3 log4