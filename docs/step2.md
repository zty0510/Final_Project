# SI 100B Project: Who is Flying over? - Week 2

In this week, you are going to control the GPIO pins to light LEDs accordding to the air traffic information you get from last week’s crawler. GPIO, or *general purpose input and output*, allows you to connect to a general purpose devices and transfer information from/to them. On your Raspberry Pi, the GPIO interface is the 40-pins array on one side of the board.

## Lit the LED

We first try to control a single LED with the GPIO interface of yout Raspberry Pi. First connect a LED to the board following the [documentation](https://www.raspberrypi.org/documentation/usage/gpio/) of the Raspberry Pi (and other online resources, like [this](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)). Write down the pin number you are connecting the LED to. When doing this task, keep the safety of yourself and the board in mind. Remove the power when you are modifing the circuit.

To access the GPIO interface on your Raspberry Pi, you are going to use a Python library called GPIO Zero which should already been installed on your Pi. Read the [documentation](https://gpiozero.readthedocs.io/en/stable/) of the library, learn how to control the blink of the LED you connected to the board. Then write a simple program which allows the LED you connected to the Pi to blink at a certain frequency the user inputs (e.g., 1 Hz). Be prepared to expian the circuit you built and the program you wrote to the TAs.

## Integrate the LED with Your Crawler

In this section you are integrating the LED with the web crawler you wrote in the last week. First you need to finish the circuit. Connect the rest 3 LEDs to the board as you do in the last section so that they form a straight line. Now we are controlling the on and off of the LED based on the crawled data from FlightRadar24.

In the class `State` of `state.py`, we have already initialized some attributes of it. What you need to do is to add some additional attributes and methods such that it could do the following things:

* Perodically check the FlightRadar24 with your cralwer, maintain a list of airplanes (and other attributes of it) in the class;
* Control the on and off of the 4 LEDs you have on the board based on the traffic data. You can desgin your own scheme of how the 4 LEDs will change when the traffic data changes. However, your design should  be reproducible in a vast range of time of a day so that when checking your implementation the TAs could easily observe how the change in traffic will influence the behavior of your LEDs;
* Write a simple demo in the `state.py` such that the behavior of the class could be observed when we run `state.py` directly and importing any thing from the file should not cause the demo to be run.
* Be prepared to explain how the class `State` and the demo works.

**Hint**: For most scheme you design, you need to write the checking of FlightRadar24 and the controlling of the LED in a big loop. For the convenience of the implementation of the following weeks, you are recommended to implement such a loop in `State.spin()`.
