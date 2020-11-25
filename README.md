# SI 100B Project: Who is Flying over?

Welcome to the python programming project for SI 100B. In this project, you are going to build a web crawler that runs on a Raspberry Pi (a mini computer) to obtain real time flight data from a website called FlightRadar24 (or an alternative called FlightAware). You are going to control LED lights on an external circuit through the GPIO interface of your Raspberry Pi according to different scenarios and visualize your data analysis through graphs or a website. To be specific, you will build:

1. A crawler to get data from a flight information website;

2. A module that controls LED lights on an external circuit;

3. A module or a website that accepts input parameters to your crawler;

4. A module for analyzing and visualizing your data through plain graphs or a website.

All your programs run on a Raspberry Pi.

## Getting Started

You should have received a batch of gears from the SI 100B teaching team. Please take good care of them and make sure they are in a sound condition when you return them to us. Below is a list of components we hand out. Please check yours against them. If there is anything missing or broken, contact us as soon as possible so that we can give you a replacement.

| Item               | Quantity |
| ------------------ | -------- |
| Raspberry Pi       | 1        |
| LED GPIO connector | 1        |
| USB Charger        | 1        |
| LED                | 4        |
| Ehernet cable      | 1        |

First, you need to connect your Raspberry Pi to the Internet through Wi-Fi or the Ethernet port on your board. First, turn on the switch on the charger and connect your Pi to it. Your Pi will be powered up automatically. The red LED indicator on the corner of the board near the USB connector will light up if your Pi is on. The green LED indicator next to it will blink if your Pi’s SD card has been accessed.

After connecting your Pi to the network, you are going to figure out ways of extending I/O of your Pi. There are two ways of doing it. The first one is the simplest: you are directly connecting a monitor and a set of keyboard and mouse to it. The second one is to connect to it with SSH via network. The second approach is a little more complex but is recommended by the teaching team. We will give you bonus to your project if you choose the SSH way. Below are details for these two. 

### Connect with Keyboard and Mouse

The Pi itself is a single board computer that runs Linux. To make it fully functional, all you need to do is attaching a screen and a set of keyboard and mouse to it. 

The Pi comes with a HDMI port for connecting to your monitor and 4 USB ports for connecting with your mouse and keyboard. If you have compatible hardware, you can connect your Pi to them and use your Pi like what you will do with a normal computer. If you currently do not have them, you can choose to come to the computer lab in TBA. The hours of the lab will be announced on Piazza.

After the Pi boots up, the user interface will appear on the screen. If you choose to use the wire connection, just plug in a cable to the Ethernet port and the LED indicator on the port will be turned on and blink, which means a connection is established. Alternatively, you can connect to Wi-Fi. Simply choose the network you want to connect to from the drop-down menu on the upper right corner of the screen and log in with your credentials if asked. A side note is that if you are connecting to the campus network via the ShanghaiTech Wi-Fi or through an Ethernet port, you may need to do web portal authentication as you will do for any other devices using those two networks. You can simply open the FireFox browser on your Pi or use those handy [scripts](https://github.com/ShanghaitechGeekPie/WifiLoginer).

Alternatively, configuring your Pi with a SSH server and debugging on your own computer is also a feasible way.

### Connect with an SSH Terminal

If you do not have any USB keyboard, mouse or monitor, you may need to connect to the Pi via SSH.  SSH allows you to connect to your Pi from another computer securely in the same network. To enable SSH, simply follow the [instructions](https://www.raspberrypi.org/documentation/remote-access/ssh/) in the official documentation. If you have enabled SSH on your Pi, do remember to change your SSH login password. To change your password, simply run `passwd` on your terminal window after login. You may be prompted for your current password. If it is the case, the default password of your Pi is` raspberry`.

To connect to your Pi via SSH, you also need an SSH client on your computer. If it is running macOS or Linux, your computer is shipped with an SSH client. If you are using Windows, you are recommended to use the [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10). To connect to your Pi in this way, you will need to connect your Pi to your laptop with the Ethernet. You will need an Ethernet dongle for this purpose if your laptop is not equipped with Ethernet ports.

After connecting your Pi with your computer with cable, your computer and Pi will both negotiate a set of addresses in the same network called linked local address which could be used to connect to your Pi. Then in your terminal, you can connect to the Pi with `ssh pi@raspberrypi.local` . This way may not work out on some systems (esp. some version of Windows) with limited mDNS support; in this case, consult this [article](https://raspberrypi.stackexchange.com/questions/85747/setting-a-static-ip-from-boot-drive-headless-static-ip) or this [article](https://www.cnblogs.com/sheng9hhd/p/10294859.html) for workarounds.

This will not give your Pi access to the Internet which is needed for this project. You may also need to connect your Pi to the campus wireless network. To do this, you can follow this [documentation](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md) or simply attach a screen and a set of keyboard and mouse to your Pi and connect to `ShanghaiTech` or `eduroam` network (you only need to do this for once and your Pi should be able to connect to the network next time). You may need to do network login via the web portal. In this case, you may use those handy [scripts](https://github.com/ShanghaitechGeekPie/WifiLoginer).

### Install Dependency

Another thing you need to do is to install the required packages (dependencies) of the project. You can do this by downloading the packages from the PyPI. In the terminal of your Pi (or a shell SSHed into the Pi), in the root directory of your repo, execute the following:

```bash
pip3 install -r requirements.txt
```

`requirements.txt` records the detailed required packages.

## Overview

The project contains four parts. Each part requires you to implement a particular functionality of the project. Generally, you have one week of time to finish one part. At the end of each week, you are required to submit your implementation (Python code), a report on how you implement this part. Also, a face-to-face check will be arranged, requiring you to explain how your implementation works to a TA.

The 4 parts are:

- **[Part 1](./docs/README.part1.md)**: Build your web crawler;
- **[Part 2](./docs/README.part2.md)**: Control the LEDs via GPIO;
- **[Part 3](./docs/README.part3.md)**: Build control panel;
- **[Part 4](./docs/README.part4.md)**: Perform data visualization;

The specification for each part is located in` docs` directory of this repo. Check them for detailed requirements for each step.

This project (esp. the framework itself) is only supposed to work in a modern Linux system. During the face-to-face check, your project should only run on the Debian Linux on the Pi from the teaching team. During the face-to-face checking, demostrating the project using other devices or OS is considered invalid and will face score deduction. However, you are highly encouraged to implement and debug it on your local system.

## Collaborating with Your Teammate(s)

The team size is 2 or 3. You need to describe how the workload is divided among the team members in your weekly project report. We take the workload division into consideration when grading.

The best practice is to use git as the versioning and collaborating tool with your teammate(s). With git, you can have a clean split between the *development* phase and the *test* phase. Commonly, you will finish the development phase (writing your prototype) on your own computer then synchronize the code to the Pi and complete your testing part.

## Basics of HTTP and HTML

### HTTP

HTTP, or the Hyper-text Transfer Protocol, is the underlying protocols used by web server and your web browsers to transfer data. Generally, how the HTTP works is that the user agent (your web browser) initializes a connection to the web server and it sends information indicating what resources on the server it wants to access (the URL, like `https://sist.shanghaitech.edu.cn/`) and how it wants to access the resource (e.g., to retrieve or to modify? Formally, it is called method. Examples includes `GET` and `POST`). After receiving the request from the user agent, the server will send back the resources the user want along with a status code indicating the status of the request (is it successful? If an error occurred, is it the problem of the server or the client?).

An example of HTTP request / response is given below:

The client (user agent) send out the following request

```
GET / HTTP/1.1
Host: www.example.com
User-Agent: curl/7.54.0
```

The server will typically reply with the following

```
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Thu, 16 Jul 2020 12:42:13 GMT
Content-Type: text/html; charset=utf-8

<html>
<head>
<title>Welcome</title>
</head>
<body>
<p>It works!</p>
</body>
</html>
```

This conversation is basically for the client trying to get the `/` directory of the server `www.example.com`. The server reply with a `200` status code indicating the request is successful and the content of the requested resource is attached below the headers as `<html>....</html>`. Other possible status codes include `400` indicating the client’s request could not be processed, `404` indicating the resource could not be found on the server and `500` indicating an error occurred inside the server when processing the request.

For more information about HTTP, see the [W3School](https://www.w3schools.com/whatis/whatis_http.asp).

### HTML

HTTP solves the problem of transferring a file from a computer to another. HTML, or the **H**yper **T**ext **M**arkup **L**anguage, solves the problem of encoding the style information of a web page. It represents the documentation as a tree of labels.

For more information about the HTML, see [W3School](https://www.w3schools.com/whatis/whatis_html.asp).

