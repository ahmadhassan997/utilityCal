# Setup to run Sprout and Verus with Mahimahi

> Utility plots can be found in [plots](plots) directory
> scripts to calculate utility can be found in [scripts](scripts/utility.py)

## Utility Functions

To calculate the utilities for each protocol, time has been divided into
bins of size 5ms.

Following are the utility functions used for our graphs.

Here, __*t*__ = throughput and __*d*__ = delay

### Utility Function 1

**Remy Congestion Control Algorithm**

U(t, d) = log(t) - delta * log(d)

### Utility Function 2

**PCC Vivace Congestion Control**

U(t, d) = t^a - b * t * d(d)/dt

### Utility Function 3

**Congestion Control for Future Mobile Networks**

U(t, d) = t * (1 - pRTT)

pRTT = 5 * 10^-4 * |avg_dealy - min_delay| (penalty for latency)
