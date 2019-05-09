# teamSenPy
Members: Emmanuel Okeke, Michael Normand, Will Ramirez

This objective of this project was to create a program that would display the temperature(from a connected sensor) when run and 
turn on a fan if the measured temperature was above a set value. 
We used Pythons integration into the Raspbian OS as well as the RPi.GPIO library to create this project. 

To run this code the only module you would need is RPi.GPIO. To install it, follow the steps below:

````
pip install RPi.GPIO 
````

or 
````
$ sudo apt-get update
$ sudo apt-get install python-rpi.gpio python3-rpi.gpio
````

### Circuit Diagram
the circuit diagram can be found at "circuit.png".

### Demo Videos
these can be found in the demo folder. The shorter video has the fan running with a 5v voltage and the longer video has the fan running at a 3.3v voltage.

### Notes: 
* Before running this code make sure you enable the one wire interface on your raspberry pi. This link (https://www.raspberrypi-spy.co.uk/2018/02/enable-1-wire-interface-raspberry-pi/) will help.  
* The code is well commented so it should be pretty easy to follow.


