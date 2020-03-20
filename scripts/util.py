#!/usr/bin/python
'''
This file contains the basic utility functions that can be used.
'''
import math

MS_PER_BIN = 5 # Milliseconds in each BIN for which average stats are calculated

def ms_to_bin(timestamp):
    '''
    Return the bin to which the given timestamp belongs to
    '''
    return int(timestamp / MS_PER_BIN)

def utility_function_01(throughput, delay, delta = 0.001):
    '''
    Calculate utility using the function : U(t, d) = log(t) - delta * log(d)
    '''
    return math.log(throughput) - delta * math.log(delay)


def utility_function_02(throughput, delay_variation, a = 1, b = 0.1):
    '''
    Calculate utility using the function : U(t, d) = t^a - b * t * d(d)/dt
    '''
    return (throughput ** a) - (b * throughput * delay_variation)


def utility_function_03(throughput, delay_variation, a = 5 * 10**-4):
    '''
    Calculate utility using the function : U(t, d) = t(1 - pRTT)
    '''
    return throughput * (1 - a * abs(delay_variation))



def _print_(utilities):
    '''
    Print the utilities of each epoch
    '''
    print ("            T(Mbps)  Q-D(ms)  Utl  UG")
    for i in range(25):
        print ('Epoch {:^3}  :  {:05.2f}  {:05.2f}  {:05.2f}  {:05.2f}'.format(i, utilities[i].throughput, utilities[i].avg_delay,utilities[i].utility, utilities[i].utility_gain))
    print ("Average Utility : {}".format(cal_average_util(utilities)))

def cal_average_util(utilities):
    '''
    Calculate the average utility of a LOG FILE
    '''
    sum_util = 0
    for i in range(len(utilities)):
        sum_util += utilities[i].utility
    return sum_util/len(utilities)


def _parse_filename(line):
    '''
    Parse a file name to generate legend for the graphs
    Input : ./../logs/sprout_stat_log.up
    Output: sprout
    '''
    pieces = line.split("/")[-1]
    return pieces.split("_")[0]


def _parse_line(line):
    '''
    Parse a single line of the LOG_FILE based on EVENT TYPE
    '''
    pieces = line.split()
    if pieces[1] == "#": # return : "opportunity", timestamp, bytes, None
        return "#", int(pieces[0]), int(pieces[2]), None
    elif pieces[1] == "+": # return "arrival", timestamp, bytes, None
        return "+", int(pieces[0]), int(pieces[2]), None
    elif pieces[1] == "-": # return "departure", timestamp, bytes, delay
        return "-", int(pieces[0]), int(pieces[2]), int(pieces[3])
    elif " ".join(pieces[:-1]) == "# base timestamp:": # return "base", timestamp, None, None
        return "@", int(pieces[-1]), None, None
    else: # return "No Event", None, None, None
        return "!", None, None, None


def _parse_file(filename):
    '''
    Read the contents of a file and store all the values based on EVENT TYPES
    input: file_object
    output: arrival, departure, caapcity and delay dictionaries
    '''
    base_timestamp = None
    arrival = {}
    departure = {}
    capacity = {}
    delay = {}
    line = filename.readline()
    while line:
        event, timestamp, _bytes, _delay = _parse_line(line)
        if event != "!":
            if base_timestamp == None:
                # print("Base Timestamp Not Defined")
                pass
            if event == "@": # record the base timestamp and subtract it from all timestamps
                if base_timestamp == None:
                    base_timestamp = timestamp
            elif event == "+": # arrival event: packet entered the queue
                timestamp -= base_timestamp
                ms_bin = ms_to_bin(timestamp)
                if ms_bin not in arrival.keys():
                    arrival[ms_bin] = _bytes * 8
                else:
                    arrival[ms_bin] += _bytes * 8
            elif event == "-": # departure event: packet left the queue
                timestamp -= base_timestamp
                ms_bin = ms_to_bin(timestamp)
                if ms_bin not in departure.keys():
                    departure[ms_bin] = _bytes * 8
                else:
                    departure[ms_bin] += _bytes * 8
                delay.setdefault(ms_bin, []).append(_delay)
            elif event == "#": # opportunity event: opoortunity to send MSS size packet
                timestamp -= base_timestamp
                ms_bin = ms_to_bin(timestamp)
                if ms_bin not in capacity.keys():
                    capacity[ms_bin] = _bytes * 8
                else:
                    capacity[ms_bin] += _bytes * 8
        line = filename.readline()
    return arrival, departure, capacity, delay

