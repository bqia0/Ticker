import max7219.led as led
import time
device = led.matrix(cascaded = 4)
device.brightness(1)
while True:
    #device.show_message(time.strftime("%I:%M"))
    device.show_message("Hi Faraz")
    
