import util
import matplotlib.pyplot as plt
import numpy as np

class info:
    '''
    Class to store a single LOG value and its utility
    '''
    def __init__(self, _bin, _delays, _departure):
        self.ms_bn = _bin
        self.delays = _delays
        self.avg_delay = sum(_delays) / len(_delays)
        self.min_delay = min(_delays) # same as signal delay
        self.max_delay = max(_delays)
        self.departure = _departure
        self.throughput = _departure / (1000 * util.MS_PER_BIN)
        self.utility_gain = None
        self.utility = None



def utility_mapper(departure, delay, func = 1):
    '''
    Calculate the utility of a LOG_FILE using the utility function
    '''
    # Store all values in a list so they last epoch can be refernced
    utilities = []
    for ms_bin in departure.keys():
        if ms_bin in delay.keys():
            utilities.append(info(ms_bin, delay[ms_bin], departure[ms_bin]))
        else:
            print("Delay Value Not Present")
    if func == 1:
        # Calculate utility for each epoch
        utilities[0].utility = util.utility_function_01(utilities[0].throughput, utilities[0].avg_delay)
        utilities[0].utility_gain = utilities[0].utility
        for i in range(1, len(utilities)):
            utilities[i].utility = util.utility_function_01(utilities[i].throughput, utilities[i].avg_delay)
            utilities[i].utility_gain = utilities[i].utility - utilities[i-1].utility
    elif func == 2:
        utilities[0].utility = util.utility_function_02(utilities[0].throughput, utilities[0].avg_delay)
        utilities[0].utility_gain = utilities[0].utility
        for i in range(1, len(utilities)):
            utilities[i].utility = util.utility_function_02(utilities[i].throughput, utilities[i].avg_delay - utilities[i-1].avg_delay)
            utilities[i].utility_gain = utilities[i].utility - utilities[i-1].utility
    elif func == 3:
        utilities[0].utility = util.utility_function_03(utilities[0].throughput, utilities[0].avg_delay - utilities[0].min_delay)
        utilities[0].utility_gain = utilities[0].utility
        for i in range(1, len(utilities)):
            utilities[i].utility = util.utility_function_03(utilities[i].throughput, utilities[i].avg_delay - utilities[i].min_delay)
            utilities[i].utility_gain = utilities[i].utility - utilities[i-1].utility
    return utilities

def calculate_utility(files_list, util_func = 2):
    '''
    Handler function to calulate all stats
    '''
    stats = {}
    for filename in files_list:
        with open(filename) as file_object:
            arrival, departure, capacity, delay = util._parse_file(file_object)
            utility_values = utility_mapper(departure, delay, util_func)
            # util._print_(utility_values)
            stats[filename] = util.cal_average_util(utility_values)
    return stats

def barplot(utility_stats_1, utility_stats_2, utility_stats_3, _title, _name):
    '''
    Plot the graph with different categories for all utility functions
    '''
    barwidth = 0.25
    legends_1 = list(map(util._parse_filename, utility_stats_1.keys()))
    pos1 = np.arange(len(legends_1))
    pos2 = [x + barwidth for x in pos1]
    pos3 = [x + barwidth for x in pos2]
    f, ax = plt.subplots(figsize=(10, 8))
    plt.bar(pos1, utility_stats_1.values(), width = barwidth, edgecolor = 'white', label = 'Utility Function 1')
    plt.bar(pos2, utility_stats_2.values(), width = barwidth, edgecolor = 'white', label = 'Utility Function 2')
    plt.bar(pos3, utility_stats_3.values(), width = barwidth, edgecolor = 'white', label = 'Utility Function 3')
    plt.xlabel('group', fontweight = 'bold')
    plt.xticks([r + barwidth for r in range(len(legends_1))], legends_1)
    ax.set_ylabel('Utility Values')
    ax.set_title(_title)
    plt.legend()
    plt.savefig("./../plots/" + _name + ".png", dpi=300, format='png', bbox_inches='tight')
    plt.show()
    

def scale(utility_stats):
    '''
    Normalize the utility values so that sum = 1
    '''
    temp = {}
    min_utility = abs(min(min(utility_stats.values()), 0)) 
    for file, utility in utility_stats.items():
        temp[file] = utility + min_utility
    return temp

if __name__ == "__main__":

    # up_files =  ["./../logs/sprout_att_log.up",
    #             "./../logs/verus2_att_log.up",
    #             "./../logs/verus4_att_log.up",
    #             "./../logs/verus6_att_log.up"]
    # down_files = ["./../logs/sprout_att_log.down",
    #               "./../logs/verus2_att_log.down",
    #               "./../logs/verus4_att_log.down",
    #               "./../logs/verus6_att_log.down"]
    up_files =  ["./../logs/sprout_stat_log.up",
                "./../logs/verus2_stat_log.up",
                "./../logs/verus4_stat_log.up",
                "./../logs/verus6_stat_log.up"]
    down_files = ["./../logs/sprout_stat_log.down",
                  "./../logs/verus2_stat_log.down",
                  "./../logs/verus4_stat_log.down",
                  "./../logs/verus6_stat_log.down"]
    up_stats_1 = scale(calculate_utility(up_files, 1))
    up_stats_2 = scale(calculate_utility(up_files, 2))
    up_stats_3 = scale(calculate_utility(up_files, 3))
    down_stats_1 = scale(calculate_utility(down_files, 1))
    down_stats_2 = scale(calculate_utility(down_files, 2))
    down_stats_3 = scale(calculate_utility(down_files, 3))
    print ("UPLINK\n")
    print ("Utility Function 1")
    for file, utility in up_stats_1.items():
        print ("{}   :   {}".format(file, utility))
    print ("\nUtility Function 2")
    for file, utility in up_stats_2.items():
        print ("{}   :   {}".format(file, utility))
    print ("\nUtility Function 3")
    for file, utility in up_stats_3.items():
        print ("{}   :   {}".format(file, utility))
    print ("\nDOWNLINK\n")
    print ("Utility Function 1")
    for file, utility in down_stats_1.items():
        print ("{}   :   {}".format(file, utility))
    print ("\nUtility Function 2")
    for file, utility in down_stats_2.items():
        print ("{}   :   {}".format(file, utility))
    print ("\nUtility Function 3")
    for file, utility in down_stats_3.items():
        print ("{}   :   {}".format(file, utility))
    # barplot(up_stats_1, up_stats_2, up_stats_3, "UpLink Utilities Comparison", "uplink-att")
    barplot(down_stats_1, down_stats_2, down_stats_3, "Stationary DownLink Utilities Comparison", "downlink-stat")