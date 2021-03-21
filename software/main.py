import cv2 as cv
import pyautogui
import numpy as np
#import bluetooth
import serial
import time



ARDUINO_LEFT = serial.Serial("COM15", 9600, timeout=3)
ARDUINO_RIGHT = serial.Serial("COM3", 9600, timeout=3)

NUM_LEDS = 35


def screenCapture():
    run = True
    #cap = cv.VideoCapture(0)

    while(run):
        
        screenshot = pyautogui.screenshot()     #It takes 100ms
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        X_MAX, Y_MAX, channels = screenshot.shape
        X_MAX_div = X_MAX//(NUM_LEDS+1)           #X_MAX // (NUM_LEDS + 1)

        r_left = 0
        g_left = 0
        b_left = 0
        r_right = 0
        g_right = 0
        b_right = 0
        cont = 0

        ARDUINO_LEFT.write(b'w')
        ARDUINO_RIGHT.write(b'w')


        for i in range(0, X_MAX):
            if cont >= X_MAX_div:
                b_left = b_left //((Y_MAX//4)*X_MAX_div)
                g_left = g_left //((Y_MAX//4)*X_MAX_div)
                r_left = r_left //((Y_MAX//4)*X_MAX_div)

                b_right = b_right //((Y_MAX//4)*X_MAX_div)
                g_right = g_right //((Y_MAX//4)*X_MAX_div)
                r_right = r_right //((Y_MAX//4)*X_MAX_div)

                sendColour(str(r_left)+"a", str(g_left)+"a", str(b_left)+"a",
                    str(r_right)+"a", str(g_right)+"a", str(b_right)+"a")
               
               
                b_left = 0
                g_left = 0
                r_left = 0

                b_right = 0
                g_right = 0
                r_right = 0

                cont = 0

            for j in range(0, Y_MAX//4):
                b_left += screenshot.item(i,j,0)
                g_left += screenshot.item(i,j,1)
                r_left += screenshot.item(i,j,2)
            
            for j in range(3*Y_MAX//4, Y_MAX):
                b_right += screenshot.item(i,j,0)
                g_right += screenshot.item(i,j,1)
                r_right += screenshot.item(i,j,2)


            cont += 1

            #cv.imshow('Screen Capture', screenshot)
            

        if cv.waitKey(1) == ord('a'):
            cv.destroyAllWindows()
            run = False

"""
def scanBluetoothDevices():
    print("Scanning for bluetooth devices")
    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
    number_of_devices = len(devices)
    print("Number of devices: " + str(number_of_devices))
    if(number_of_devices > 0):
        for addr, name, device_class in devices:
            print("\n")
            print("Device: ")
            print("Device Name: " + name)
            print("Device MAC Address: " + addr)
            print("Device Class: " + str(device_class))
            print("\n")
"""

def sendColour(r_left, g_left, b_left, r_right, g_right, b_right):
    
    ARDUINO_LEFT.write(r_left.encode())
    ARDUINO_LEFT.write(g_left.encode())
    ARDUINO_LEFT.write(b_left.encode()) 
    
    
    ARDUINO_RIGHT.write(r_right.encode())
    ARDUINO_RIGHT.write(g_right.encode())
    ARDUINO_RIGHT.write(b_right.encode()) 
    
    



if __name__ == "__main__":
    time.sleep(3)
    screenCapture()

