import RPi.GPIO as GPIO
import datetime
import time

SETTINGS = {
    # define pins
    "LIGHT_GPIO": 17,
    "WATER_PUMP_GPIO": 18,
    "VALVE_GPIO": 4,
    "WATER_LEVEL_GPIO": 27,
    
    # timings
    "LIGHT_FROM": 6,  # Hour, Time to turn on light
    "LIGHT_UNTIL": 20,  # Hour, Time to turn off light
    "WATERING_TIMES": [7, 11, 15, 19], # Hours, Times to water the plant basin
    
    "WATER_PUMP_TIME": 20,  # Seconds, how long the pump should be turned on
    "VALVE_TIME": 300, # Seconds, how long to hold the valve open to drain the tank
}

def testValve():
    GPIO.setup(SETTINGS["VALVE_GPIO"], GPIO.OUT, initial=GPIO.HIGH)
    print("opened valve");
    time.sleep(5)
    GPIO.output(SETTINGS["VALVE_GPIO"], GPIO.LOW)
    print("closed valve");
    time.sleep(5)
    GPIO.setup(SETTINGS["VALVE_GPIO"], GPIO.LOW, initial=GPIO.HIGH)
    print("opened valve");
    time.sleep(5)
    GPIO.output(SETTINGS["VALVE_GPIO"], GPIO.LOW)
    print("closed valve");
    time.sleep(5)
    GPIO.setup(SETTINGS["VALVE_GPIO"], GPIO.OUT, initial=GPIO.HIGH)
    print("opened valve");
    time.sleep(5)
    GPIO.output(SETTINGS["VALVE_GPIO"], GPIO.LOW)
    print("closed valve");
    time.sleep(5)
    GPIO.setup(SETTINGS["VALVE_GPIO"], GPIO.OUT, initial=GPIO.HIGH)
    print("opened valve");
    
if __name__ == '__main__':
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
 
        # execute function
        testDrainPlants()
    except:
        GPIO.cleanup()
