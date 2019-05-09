#import the necessary modules
import RPi.GPIO as gpio
import os
import glob
import time

cutoff_temp_c = 27

blue_led = 17
red_led = 15
fan = 14   # fan and green lcd use same pin

gpio.setwarnings(False)
#set the pin numbering system to BCM
gpio.setmode(gpio.BCM)

#set up pins for output or input
gpio.setup(blue_led, gpio.OUT)
gpio.setup(red_led, gpio.OUT)
gpio.setup(fan, gpio.OUT)

# collect the file address that the sensor dumps data into. 
## first load the w1-gpio and w1-therm kernel modules
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
sensor_file_name = glob.glob('/sys/bus/w1/devices/'+'28*')[0] + '/w1_slave'

# Goes to the sensor "file" to read the data dumped by the sensor 
## this is because the sensor uses a one-wire interface
def read_native_temp():
        sensor_file = open(sensor_file_name, 'r')
        data = sensor_file.readlines()
        sensor_file.close()
        return data

# from the data, first parse it to determine if the data is correct (checking for the YES)
##then check for the temp, usually 2 place after only equals sign. 
def read_actual_temp():
    raw_data = read_native_temp()
    while raw_data[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        raw_data = read_native_temp()
    equals_pos = raw_data[1].find('t=')
    if equals_pos != -1:
        temp_string = raw_data[1][equals_pos+2:]
        celsius = float(temp_string)/1000.0
        farenheit = (celsius *(9.0/5.0))+32.0
    return celsius, farenheit

#Checks if the cut off of temp has been reached and then turns on the fan and correct LED as needed
def isithot(cutoff_temp_c, temp):
    temp_c = temp[0]
    if cutoff_temp_c < temp_c:
        gpio.output(fan, 1)
        gpio.output(red_led, 0)
    else:
        gpio.output(fan, 0)
        gpio.output(red_led, 1)
    return

#when program starts, ask if user would like a new temp.
print("Do you want to override the default cutoff temp of 27C?")
cutoff_temp_override = input("If so enter new temp or leave blank: ")
if cutoff_temp_override and type(cutoff_temp_override) == int:
    cutoff_temp_c = cutoff_temp_override

# first read the temp and then check if its above the cutoff
while True:
    temp = read_actual_temp()
    gpio.output(blue_led, 1)
    isithot(cutoff_temp_c, temp)
    time.sleep(0.5)
    print (temp)
    gpio.output(blue_led, 0)
    time.sleep(1)



 

    
    
