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
    "WATERING_TIMES": [7, 11, 15, 19], # Hours, Times to water the plant basin
    
    "WATER_PUMP_TIME": 20,  # Seconds, how long the pump should be turned on
}


#==========================================================================================
#==========================================================================================


def readTime():
    #  return the system-time:
    return datetime.datetime.now()
    
def checkLight():
    timestamp = readTime()
    if SETTINGS["LIGHT_FROM"] <= timestamp.hour < SETTINGS["LIGHT_UNTIL"]:
        # turn light on
        GPIO.setup(SETTINGS["LIGHT_GPIO"], GPIO.OUT, initial=GPIO.HIGH) # Relay HIGH = ON
        print("\tLight on, ");
    else:
        # turn light off
        GPIO.setup(SETTINGS["LIGHT_GPIO"], GPIO.OUT, initial=GPIO.LOW)
        print("\tLight off, ");

def checkWaterPlants():
    timestamp = readTime()
    for time in SETTINGS["WATERING_TIMES"]:
        if timestamp.hour == time and timestamp.minute == 0:
            print("\tFilled basin, ");
            # Close Valve
            GPIO.setup(SETTINGS["VALVE_GPIO"], GPIO.OUT, initial=GPIO.LOW)  # Valve LOW = Closed
            # turn pump on for some seconds
            GPIO.setup(SETTINGS["WATER_PUMP_GPIO"], GPIO.OUT, initial=GPIO.HIGH)
            time.sleep(SETTINGS["PUMP_TIME"])
            GPIO.setup(SETTINGS["WATER_PUMP_GPIO"], GPIO.OUT, initial=GPIO.LOW)


def checkDrainPlants():
    timestamp = readTime()
    for time in SETTINGS["WATERING_TIMES"]:
        # Drain plants after 15ish minutes
        if timestamp.hour == time and timestamp.minute == 15:
            # open valve for some seconds
            GPIO.setup(SETTINGS["VALVE_GPIO"], GPIO.OUT, initial=GPIO.HIGH) # Valve HIGH = Open
            print("\tDrained basin, ");
                
#==========================================================================================
#==========================================================================================


if __name__ == '__main__':
    try:
        print("Ebb and Flow @ %s:" % readTime().strftime("%Y-%m-%d %H:%M"))
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
 
        # execute functions
        checkLight()
        checkWaterPlants()
        checkDrainPlants()
        GPIO.setup(SETTINGS["WATER_PUMP_GPIO"], GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(SETTINGS["WATER_PUMP_GPIO"], GPIO.OUT, initial=GPIO.LOW)

    except:
        GPIO.cleanup()
