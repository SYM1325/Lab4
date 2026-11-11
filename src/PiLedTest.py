
import time
from hal import hal_input_switch as input_switch
from hal import hal_led as led

print("PiLedTest.py is running on the Raspberry Pi")

def main():
    input_switch.init()
    led.init()

    print("LED Control Program Started - Part(d)")
    print("Switch LEFT (1) = 5 Hz")
    print("Switch RIGHT (0) = 10 Hz for 5 seconds, then OFF")

    right_start_time = None

    try:
        while True:
            switch_position = input_switch.read_slide_switch()

            if switch_position == 1:
              
                right_start_time = None

                led.set_output(0, 1)
                time.sleep(0.1)

                led.set_output(0, 0)
                time.sleep(0.1)

            else:
              
                if right_start_time is None:
                    right_start_time = time.time()

              
                elapsed_time = time.time() - right_start_time

                if elapsed_time < 5:
                    # Blink at 10 Hz
                    led.set_output(0, 1)
                    time.sleep(0.05)

                    led.set_output(0, 0)
                    time.sleep(0.05)

                else:
                    led.set_output(0, 0)
                    time.sleep(0.01)

    except KeyboardInterrupt:
        led.set_output(0, 0)
        print("\nProgram terminated by user")


if __name__ == "__main__":
    main()