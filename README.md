# teamSenPy
Members: Emmanuel Okeke, Michael Normand, Will Ramirez

This objective of this project was to create a program that would display the temperature(from a connected sensor) when run and 
turn on a fan if the measured temperature was above a set value. 

We used Pythons programming capabilities that are seemlessly integrated to work with controllers and microcontrollers such at the Raspberry pi 3 Model B + .

Rather than using a manually operated controller that requires the user to be vigilant and active during a certain process, we used an approach that utilized the Raspberry Pi's GPIO pins that essentially made it into a Programmable Logic Controller (PLC) with a computer that is the size of a credit card 

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
the circuit diagram can be found at "circuit.png" 

### Notes: 
* Before running this code make sure you enable the one wire interface on your raspberry pi. 
* The code is well commented so it should be pretty easy to follow.

