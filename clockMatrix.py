#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clockMatrix.py

import os
import time
import datetime
# import requests, json
# import subprocess
import multiprocessing
# import RPi.GPIO as GPIO

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

# api_key = "YOUR_API_KEY_HERE"
# base_url = "http://api.openweathermap.org/data/2.5/weather?"
# city_name = "YOUR_CITY_NAME_HERE,YOUR_COUNTRY_CODE_HERE" # Example: "London, GB"
# complete_url = base_url + "appid=" + api_key + "&q=" + city_name

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=2)
lightBright = 2
# lightRead = 600
device.contrast(lightBright * 16)
minute = 1

# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# pin_to_circuit = 7

def info(title):
    print("~"*50)
    print(title)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

# def rc_time(pin_to_circuit):
#     count = 0
#     GPIO.setup(pin_to_circuit, GPIO.OUT)
#     GPIO.output(pin_to_circuit, GPIO.LOW)
#     time.sleep(0.2)
#     GPIO.setup(pin_to_circuit, GPIO.IN)
#     while (GPIO.input(pin_to_circuit) == GPIO.LOW):
#         count += 1
#     return count

# def light():
#     info("Light()")
#     global lightRead
#     global lightBright
#     rcTime = rc_time(pin_to_circuit)
#     print(rcTime)
#     if rcTime < 200:
#         lightBright = 2
#     elif rcTime > 450:
#         lightBright = 0
#     elif rcTime > 200:
#         lightBright = 1
#     device.contrast(lightBright * 16)
#     if lightRead > rcTime:
#         if abs(lightRead-rcTime) > 200 and not int(datetime.datetime.now().strftime('%H')) in range(11,22):
#                 greeting()
#                 weather()

# def network():
#     info("Network()")
#     global network
#     if subprocess.getoutput("/sbin/ifconfig | grep \"inet \" | grep -v 127.0.0.1 | awk '{print $2}'"):
#         show_message(device, "**" + subprocess.getoutput("/sbin/ifconfig | grep \"inet \" | grep -v 127.0.0.1 | awk '{print $2}'") + "**", fill="white", font=proportional(TINY_FONT), scroll_delay=0.05)
#         network = True
#     else:
#         show_message(device, "**no network**", fill="white", font=proportional(TINY_FONT), scroll_delay=0.05)
#         network = False

def clock():
    info("Clock()")
    with canvas(device) as draw:
        if str(datetime.datetime.now().strftime('%H'))[0] == "1":
            text(draw, (2, 1), str(datetime.datetime.now().strftime('%H'))[0], fill="white", font=proportional(LCD_FONT))
        else:
            text(draw, (1, 1), str(datetime.datetime.now().strftime('%H'))[0], fill="white", font=proportional(LCD_FONT))
        if str(datetime.datetime.now().strftime('%H'))[1] == "1":
            text(draw, (9, 1), str(datetime.datetime.now().strftime('%H'))[1], fill="white", font=proportional(LCD_FONT))
        else:
            text(draw, (8, 1), str(datetime.datetime.now().strftime('%H'))[1], fill="white", font=proportional(LCD_FONT))
        text(draw, (15, 1), ":", fill="white", font=proportional(LCD_FONT))
        if str(datetime.datetime.now().strftime('%M'))[0] == "1":
            text(draw, (20, 1), str(datetime.datetime.now().strftime('%M'))[0], fill="white", font=proportional(LCD_FONT))
        else:
            text(draw, (19, 1), str(datetime.datetime.now().strftime('%M'))[0], fill="white", font=proportional(LCD_FONT))
        if str(datetime.datetime.now().strftime('%M'))[1] == "1":
            text(draw, (27, 1), str(datetime.datetime.now().strftime('%M'))[1], fill="white", font=proportional(LCD_FONT))
        else:
            text(draw, (26, 1), str(datetime.datetime.now().strftime('%M'))[1], fill="white", font=proportional(LCD_FONT))

# def weather():
#     info("Weather()")
#     if network:
#         response = requests.get(complete_url) 
#         x = response.json() 
#         if x["cod"] != "404": 
#             y = x["main"]
#             current_temperature = int(y["temp"] - 273.15)
#             current_humidiy = y["humidity"]
#             z = x["weather"]
#             show_message(device, "TEMPERATURE", fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
#             with canvas(device) as draw:
#                 if len(str(current_temperature)) != 2:
#                     if str(current_temperature)[0] == "1":
#                         text(draw, (12, 0), str(current_temperature) + "C", fill="white", font=proportional(LCD_FONT))
#                     else:
#                         text(draw, (11, 0), str(current_temperature) + "C", fill="white", font=proportional(LCD_FONT))
#                 else:
#                     if str(current_temperature)[0] == "1":
#                         text(draw, (9, 0), str(current_temperature) + "C", fill="white", font=proportional(LCD_FONT))
#                     else:
#                         text(draw, (8, 0), str(current_temperature) + "C", fill="white", font=proportional(LCD_FONT))
#             time.sleep(5)
#             show_message(device, "HUMIDITY", fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
#             with canvas(device) as draw:
#                 if len(str(current_humidiy)) == 3:
#                     if str(current_humidiy)[0] == "1":
#                         text(draw, (7, 0), str(current_humidiy) + "C", fill="white", font=proportional(LCD_FONT))
#                     else:
#                         text(draw, (6, 0), str(current_humidiy) + "%", fill="white", font=proportional(LCD_FONT))
#                 else:
#                     if str(current_humidiy)[0] == "1":
#                         text(draw, (10, 0), str(current_humidiy) + "C", fill="white", font=proportional(LCD_FONT))
#                     else:
#                         text(draw, (9, 0), str(current_humidiy) + "%", fill="white", font=proportional(LCD_FONT))
#             time.sleep(5)
#         else:
#             text(draw, (1, 1), "NOT FOUND :(", fill="white", font=proportional(TINY_FONT))

def greeting():
    info("Greeting()")
    if int(datetime.datetime.now().strftime('%H')) in range(4, 11):
        show_message(device, "GOOD MORNING", fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
    elif int(datetime.datetime.now().strftime('%H')) in range(11, 13):
        show_message(device, "HAVE A NICE DAY", fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
    elif int(datetime.datetime.now().strftime('%H')) in range(13, 17):
        show_message(device, "GOOD AFTERNOON", fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
    elif int(datetime.datetime.now().strftime('%H')) in range(17,21):
        show_message(device, "GOOD EVENING", fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
    else:
        show_message(device, "GOOD NIGHT", fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)


if __name__ == '__main__':
    info("__Main__")
#     network()
    greeting()
#     weather()
    while True:
#         p = multiprocessing.Process(target=light)
        q = multiprocessing.Process(target=clock)
#         p.start()
        q.start()
#         p.join()
        q.join()
#         lightRead = rc_time(pin_to_circuit)
        time.sleep(2)
