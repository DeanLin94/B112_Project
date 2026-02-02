import Jetson.GPIO as GPIO
import time


sensor_pin = 18

def main():
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(sensor_pin, GPIO.IN)


    try:
        while True:
            
            curr_value = GPIO.input(sensor_pin)

            if curr_value == GPIO.LOW:
                print("短路", end="")
            else:
                print("開路", end="")
            
            time.sleep(0.5) 
    except KeyboardInterrupt:
        print("停止")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
