import time
try:
    import Jetson.GPIO as GPIO
except ImportError:
    raise SystemExit('Jetson.GPIO package is required on Jetson hardware')

PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)

try:
    for _ in range(10):
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(0.5)
finally:
    GPIO.cleanup()
