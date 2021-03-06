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
    os.system(wk_dir + "run-cubic-granularity-.5")
    # os.system(wk_dir + "run-cubic-granularity-1")
    # os.system(wk_dir + "run-cubic-granularity-1.5")
    os.system(wk_dir + "run-reno-granularity-.5")
    # os.system(wk_dir + "run-reno-granularity-1")
    # os.system(wk_dir + "run-reno-granularity-1.5")
    os.system(wk_dir + "run-sprout-granularity-.5")
    # os.system(wk_dir + "run-sprout-granularity-1")
    # os.system(wk_dir + "run-sprout-granularity-1.5")
    os.system(wk_dir + "run-verus-granularity-.5")
    # os.system(wk_dir + "run-verus-granularity-1")
    # os.system(wk_dir + "run-verus-granularity-1.5")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/sprout_stationary-15-20-0.5.down > ./plots/sprout_stationary-15-20-0.5-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/sprout_stationary-15-20-1.0.down > ./plots/sprout_stationary-15-20-1.0-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/sprout_stationary-15-20-1.5.down > ./plots/sprout_stationary-15-20-1.5-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/cubic_stationary-15-20-0.5.down > ./plots/cubic_stationary-15-20-0.5-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/cubic_stationary-15-20-1.0.down > ./plots/cubic_stationary-15-20-1.0-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/cubic_stationary-15-20-1.5.down > ./plots/cubic_stationary-15-20-1.5-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/reno_stationary-15-20-0.5.down > ./plots/reno_stationary-15-20-0.5-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/reno_stationary-15-20-1.0.down > ./plots/reno_stationary-15-20-1.0-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/reno_stationary-15-20-1.5.down > ./plots/reno_stationary-15-20-1.5-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus2_stationary-15-20-0.5.down > ./plots/verus2_stationary-15-20-0.5-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus4_stationary-15-20-0.5.down > ./plots/verus4_stationary-15-20-0.5-downlink.html")
    os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus6_stationary-15-20-0.5.down > ./plots/verus6_stationary-15-20-0.5-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus2_stationary-15-20-1.0.down > ./plots/verus2_stationary-15-20-1.0-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus4_stationary-15-20-1.0.down > ./plots/verus4_stationary-15-20-1.0-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus6_stationary-15-20-1.0.down > ./plots/verus6_stationary-15-20-1.0-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus2_stationary-15-20-1.5.down > ./plots/verus2_stationary-15-20-1.5-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus4_stationary-15-20-1.5.down > ./plots/verus4_stationary-15-20-1.5-downlink.html")
    # os.system("./mahimahi/scripts/mm-throughput-graph 500 ./logs/verus6_stationary-15-20-1.5.down > ./plots/verus6_stationary-15-20-1.5-downlink.html")