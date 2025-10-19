# Milestone1.py - This is the Python code template that will be used
# for Milestone 1, demonstrating the use of PWM to fade an LED in and
# out.
#
# This code works with the test circuit that was built for Assignment 1-4.
#
#------------------------------------------------------------------
#         Author         |         Date
#------------------------------------------------------------------
# Christopher Davidson           9/14/2025
#------------------------------------------------------------------
#
#------------------------------------------------------------------
# Change History
#------------------------------------------------------------------
# Version   |   Description
#------------------------------------------------------------------
#    1          Initial Development
#------------------------------------------------------------------
#
# Load the GPIO interface from the Raspberry Pi Python Module
# The GPIO interface will be available through the GPIO object
import RPi.GPIO as GPIO
#
# Load the time module so that we can utilize the sleep method to
# inject a pause into our operation
import time
#
# Setup the GPIO interface
#
# 1. Turn off warnings for now - they can be useful for debugging more
#    complex code.
# 2. Tell the GPIO library we are using Broadcom pin-numbering. The
#    Raspberry Pi CPU is manufactured by Broadcom, and they have a
#    specific numbering scheme for the GPIO pins. It does not match
#    the layout on the header. However, the Broadcom pin numbering is
#    what is printed on the GPIO Breakout Board, so this should match!
# 3. Tell the GPIO library that we are using GPIO line 18, and that
#    we are using it for Output. When this state is configured, setting
#    the GPIO line to true will provide positive voltage on that pin.
#    Based on the circuit we have built, positive voltage on the GPIO
#    pin will flow through the LED, through the resistor to the ground
#    pin and the LED will light up.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Configure a PWM instance on GPIO line 18, with a frequency of 60Hz
pwm18 = GPIO.PWM(18, 60)

# Start the PWM instance on GPIO line 18 with 0% duty cycle
pwm18.start(0)

# ================================================================
# LAB STEP 2: Frequency sweep at 50% duty (ran to observe then disabled w/comment)
# for f in [60, 50, 45, 40, 35, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10]:
#     print(f"Observe: {f} Hz (2s)")
#     pwm18.ChangeFrequency(f)
#     time.sleep(2)
# # Recorded observation of ~30 Hz.
# pwm18.stop()
# GPIO.cleanup()
# ================================================================

# ================================================================
# LAB STEP 3: Duty-cycle steps at 60 Hz (ran to observe then disabled w/comment):
# pwm18 = GPIO.PWM(18, 60)   # ensure 60 Hz baseline
# pwm18.start(50)            # start at 50% duty
# for dc in [45, 40, 35, 30, 25, 20, 15, 10]:
#     print(f"Observe: {dc}% (1s)")
#     pwm18.ChangeDutyCycle(dc)
#     time.sleep(1)
# # Recorded observation of ~25%.
# pwm18.stop()
# GPIO.cleanup()
# ================================================================

# Configure the loop variable so that we can exit cleanly when the user
# issues a keyboard interrupt (CTRL-C)

repeat = True
while repeat:
    try:
        # Loop from 0 to 100 in increments of 5, and update the dutyCycle
        # accordingly, pausing 1/10th of a second between each update
        # Fade up from 0% to 100% duty in 5% steps with 0.1 s delay - Chris D.
        # range stop is exclusive; 101 ensure we include 100 and 0
	for duty in range(0, 101, 5):
            pwm18.ChangeDutyCycle(duty)
            time.sleep(0.1)

        # Loop from 100 to 0 in increments of -5, and update the dutyCycle
        # accordingly, pausing 1/10th of a second between each update
        # Fade down from 100% to 0% duty in -5% steps with 0.1 s delay - Chris D.
        # range stop is exclusive; -1 ensure we include 100 and 0
	for duty in range(100, -1, -5):
            pwm18.ChangeDutyCycle(duty)
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Stop the PWM instance on GPIO line 18
        print('Stopping PWM and Cleaning Up')
        pwm18.stop()
        GPIO.cleanup()
        repeat = False

# Cleanup the GPIO pins used in this application and exit
GPIO.cleanup()