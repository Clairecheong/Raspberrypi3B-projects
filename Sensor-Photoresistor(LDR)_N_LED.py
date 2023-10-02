#import the python libraries needed
import RPi.GPIO as GPIO #import library RPi.GPIO & calling it GPIO
import time             #import time library to call time.sleep (delay)

#set the GPIO mode to Broadcom pin
GPIO.setwarnings(False)#Broadcom(BCM) use to configure Raspberry Pi pins using the Broadcom channel num.

GPIO.setmode(GPIO.BCM)#Suppresse any warnings generated by RPi.GPIO library

#set the pins and if its an output or input
LDR=22                 #assign GPIO pin number 22 as LDR
LED= 17                #assign GPIO pin number 17 as LED
GPIO.setup(22, GPIO.IN)#set the 22/ LDR GPIO pin as an input
GPIO.setup(17,GPIO.OUT)#set the 17/ LED GPIO pin as an output

#--------- Coding Situation: When Light is detected LED off. & When light is not detected LED on. (Street lamp automation) ---------
while True:
    LDR_State = GPIO.input(16)     #resigning pin 16 as LDR_state instead of LDR

    if LDR == GPIO.HIGH:           #When LDR detects light
        GPIO.output(17, False)     #turn LED off
        print("light detected")    #Print "light detected" in the terminal
        time.sleep(2)              #wait for 2seconds
    else:                          #When LDR does not detect light
        print ("no light detected")#print "no light detected"in the terminal
        GPIO.output(17,True)       #turn LED on
        time.sleep(5)              #wait for 5seconds

#Clean up GPIO and release resources
GPIO.cleanup #Clean up