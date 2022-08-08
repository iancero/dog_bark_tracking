from gpiozero import InputDevice

sensor = InputDevice(2)

while True:
    if sensor.is_active:
        print("Active")
    else:
        print("---")