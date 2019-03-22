# set GPIO pin numbering method to BCM
import RPi.GPIO as GPIO
import datetime

SETTINGS = {
    # define pins
    "LIGHT_GPIO": 17,
    "WATER_PUMP_GPIO": 18,
    "VALVE_GPIO": 4,
    "WATER_LEVEL_GPIO": 27,
    
    # timings
    "LIGHT_FROM": 6,  # Hour, Time to turn on light
    "LIGHT_UNTIL": 20,  # Hour, Time to turn off light
    "WATERING_TIMES": [7, 11, 15, 19] # Hours, Times to water the plant basin
    
    "WATER_PUMP_TIME": 20,  # Seconds, how long the pump should be turned on
    "VALVE_TIME": 300, # Seconds, how long to hold the valve open to drain the tank
}


==========================================================================================
==========================================================================================


def readTime():
        #  return the system-time:
        return datetime.datetime.utcnow()
    
def checkLight():
    timestamp = readTime()
    if SETTINGS["LIGHT_FROM"] <= timestamp.hour <= SETTINGS["LIGHT_UNTIL"]:
        # turn light on
        GPIO.setup(SETTINGS["LIGHT_GPIO"], GPIO.OUT, initial=GPIO.LOW) # Relay LOW = ON
    else:
        # turn light off
        GPIO.setup(SETTINGS["LIGHT_GPIO"], GPIO.OUT, initial=GPIO.HIGH)

def checkWaterPlants():
    timestamp = readTime()
        for time in SETTINGS["WATERING_TIMES"]
            if (timestamp.hour == time and timestamp.minute < 10)
                # turn pump on for some seconds
                GPIO.setup(plantObject["WATER_PUMP_GPIO"], GPIO.OUT, initial=GPIO.LOW)
                time.sleep(plantObject["PUMP_TIME"])
                GPIO.output(plantObject["WATER_PUMP_GPIO"], GPIO.HIGH)


def checkDrainPlants():
    timestamp = readTime()
        for time in SETTINGS["WATERING_TIMES"]
            # Drain plants after 10ish minutes
            if (timestamp.hour == time and timestamp.minute > 20)
                # open valve for some seconds
                GPIO.setup(plantObject["VALVE_GPIO"], GPIO.OUT, initial=GPIO.LOW)
                time.sleep(plantObject["VALVE_TIME"])
                GPIO.output(plantObject["VALVE_GPIO"], GPIO.HIGH)
                
==========================================================================================
==========================================================================================


if __name__ == '__main__':
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
 
        # execute functions
        checkLight()
        checkWaterPlants()
        checkDrainPlants()
    except:
        GPIO.cleanup()