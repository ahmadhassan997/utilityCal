# Installation Guide

Download Mahimahi from:

``` bash
git clone https://github.com/ravinet/mahimahi
```

Download Sprout from:

``` bash
git clone https://github.com/keithw/sprout.git
```

## Essential Libraries

``` bash
sudo apt-get install build-essential git debhelper autotools-dev dh-autoreconf iptables protobuf-compiler libprotobuf-dev pkg-config libssl-dev dnsmasq-base ssl-cert libxcb-present-dev libcairo2-dev libpango1.0-dev iproute2 apache2-dev apache2-bin iptables dnsmasq-base gnuplot iproute2 apache2-api-20120211 libwww-perl
```

## Mahimahi

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

## Sprout

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

## Verus

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
