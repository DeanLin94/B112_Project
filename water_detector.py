import Jetson.GPIO as GPIO
import time

# Pin 12 對應 BCM 18
sensor_pin = 18

def main():
    # 初始化 GPIO
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    try:
        while True:
            
            curr_value = GPIO.input(sensor_pin)

            if curr_value == GPIO.LOW:
                print("短路", end="")
            else:
                print("開路", end="")
            
            time.sleep(0.5)  # 每 0.5 秒偵測一次
    except KeyboardInterrupt:
        print("停止")
    finally:
        GPIO.cleanup()  # 

if __name__ == "__main__":
    main()