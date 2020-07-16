# SI 100B Project: Who is Flying over?

Welcome to the web project of SI 100B, Fall 2020. In this project, you are going to build a web crawler to obtain real time flight data from the website FlightRadar24 and then use it to control the an external cricuit through the GPIO interface of your Raspberry Pi. Let’s get started.

## Get Started

You should have recieved a batch of gears from the SI100B teaching team. Please take good care of them and make sure they are sound and intact when been returned to us. Below is a list of components we hand out. Please check yours agiainst them. If there is any missing or borken one, contact us as soon as possible so that we can give you the replacement.

| Item         | Quantity |
| ------------ | -------- |
| Raspberry Pi | 1        |
| Touch Screen | 1        |
| USB Charger  | 1        |
| Breadboard   | 1        |
| LED          | 4        |
| DuPont line  | Serval   |

First, you need to connect your Raspberry Pi to the internet through Wi-Fi or the Ethernet port on your board. First, connect your Pi to the USB charger, turn on the switch on the charger. Your Pi will be be powered up automatically. The red LED indicator on the corner near the USB connector will light up if your Pi is powered. The green LED indicator next to it will blink if your Pi’s SD card is been accessing.

After the Pi boot up, the user interface will appear on the touch screen connected to your Pi. If you choose to use the wired connection, just plug in a cable to the Ethernet port and the LED indicator on the port will turn on and blink which means a connection is established. Connecting to the Wi-Fi requires you to attach a USB mouse and keyboard to your Pi or use the touch screen provided. Simply choose the network you want to connect to from the drop down menu on the right upper corner of the screen and enter your identity if asked. A side note is that if you are connecting to the campus network via the ShanghaiTech Wi-Fi or through a Ethernet port, you may need to do web portal authentication as you will do for any other devices using those two networks. You can simply open the firefox browser on your Pi or use those handy [scripts](https://github.com/ShanghaitechGeekPie/WifiLoginer).

Then you may need to enable SSH server on you Pi. SSH enables you to connect to your Pi from another computer securely so that you do not need to code on the small screen attached to your Pi. To enable SSH, simply follow the [instruction](https://www.raspberrypi.org/documentation/remote-access/ssh/) from the offical documentation (if you do not know how to open the terminal on your Pi, read [this article](https://magpi.raspberrypi.org/articles/terminal-help) first). If you enabled SSH on your Pi, do remember to change your password for login onto the Pi. To change your password, simply run `passwd` on your terminal window. You may be prompted for your current password. If it is the case, the default password of your Pi is `raspberry`.

To connect to your Pi via SSH, you need a working SSH client on your computer. If it is running macOS or some kind of Linux distribution, your computer is shipped with a SSH client. If you are using Windows, you are recommended to use the [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Before connecting to your Pi, you need to know the IP address of it. On your Pi, run `ip addr` , you will get something like the following:

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether b8:27:eb:xx:xx:xx brd ff:ff:ff:ff:ff:ff
    inet 172.30.15.68/24 brd 172.30.15.255 scope global dynamic noprefixroute eth0
       valid_lft 64032sec preferred_lft 50367sec
    inet6 fe80::3ccf:98ec:ef2:b064/64 scope link
       valid_lft forever preferred_lft forever
3: wlan0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether b8:27:eb:xx:xx:xx brd ff:ff:ff:ff:ff:ff
```

Then for this Pi, the IP address for it is `172.30.15.68` (search for such a field in your output). You could run `ssh pi@172.30.15.68` on you local computer’s terminal to connect to it. Side note: if your Pi is connected to your own router in your dorm, you could only connect to it within the same network as your Pi (i.e., if you connect it to your own dorm router, you will not be able to connect to it through the ShanghaiTech Wi-Fi network without extra configuation).

Another thing you need to do is to install the required packages (dependencies) of the project. You can do this by downloading the packages from the PyPI. In the terminal of your Pi (or a shell SSHed into the Pi), in the root directory of your repo, execute the following: 

```shell
pip3 install -r requirements.txt
```

## Overview

The project contains four parts. Each part requires you to implement a particular functionality of the project. Generally, you have one week of time to finish one part. At the end of each week, you are required to submit your implementation (Python code), a report on how you implement this part. Also, a face-to-face check will be arranged requiring you to explain how your implementation works to a TA.

The 4 parts are:

* **[Part 1](./docs/README.part1.md)**: Build your web crawler;
* **[Part 2](./docs/README.part2.md)**: Control the LEDs via GPIO;
* **[Part 3](./docs/README.part3.md)**: Build control panel;
* **[Part 4](./docs/README.part4.md)**: Do data visualization;

The specification for each part is located in `docs` directory of this repo. Check them for detailed requirements for each step.
