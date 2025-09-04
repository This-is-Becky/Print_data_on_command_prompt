# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:28:52 2024

@author: beckylin
"""
import serial

ser = serial.Serial("COM16")
ser.baudrate = 115200

try: 
    while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            print(f"data: {line}")

                
except KeyboardInterrupt:
        print("\nStopped by user.")
finally:
        ser.close()
        print("Closed serial and file.")