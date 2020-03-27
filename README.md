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

where delta = 0.001 (value can be adjusted)

### Utility Function 2

**PCC Vivace Congestion Control**

U(t, d) = t^a - b * t * d(d)/dt

d(d)/dt = Delay Gradient i.e. change in delay experienced from last bin

where a = 1, b = 0.1 (values can be adjusted)

### Utility Function 3

**Congestion Control for Future Mobile Networks**

U(t, d) = t * (1 - pRTT)

pRTT = 5 * 10^-4 * |avg_dealy - min_delay| (penalty for latency)

## Installation Guide

Download Mahimahi from:

``` bash
git clone https://github.com/ravinet/mahimahi
```

Download Sprout from:

``` bash
git clone https://github.com/keithw/sprout.git
```

### Essential Libraries

``` bash
sudo apt-get install build-essential git debhelper autotools-dev dh-autoreconf iptables protobuf-compiler libprotobuf-dev pkg-config libssl-dev dnsmasq-base ssl-cert libxcb-present-dev libcairo2-dev libpango1.0-dev iproute2 apache2-dev apache2-bin iptables dnsmasq-base gnuplot iproute2 apache2-api-20120211 libwww-perl
```

### Mahimahi

``` bash
cd mahimahi
```

``` bash
./autogen.sh && ./configure && make
```

``` bash
sudo make install
```

``` bash
sudo sysctl -w net.ipv4.ip_forward=1
```

``` bash
cd ..
```

### Sprout

``` bash
cd sprout
```

``` bash
./autogen.sh && ./configure && make
```

``` bash
sudo make install
```

``` bash
cd ..
```

### Verus

``` bash
cd custom-verus
```

``` bash
sudo apt-get install build-essential autoconf libasio-dev libalglib-dev libboost-system-dev
```

``` bash
sudo apt-get update
```

``` bash
./bootstrap.sh
```

``` bash
./configure
```

``` bash
make
```

``` bash
cd ..
```
