import time
import board
import busio
import adafruit_bno055

# creates I2C communication path
i2c = busio.I2C(board.SCL, board.SDA)

# creates a sensor object to make easier calls to the BNO055 class
sensor = adafruit_bno055.BNO055(i2c)

# give the BNO055 some time to power on completely
time.sleep(3)

while True:
    print("Calibration:  (sys, gyro, accel, mag) {}".format(sensor.calibration_status))
    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    print("Euler angle: {}".format(sensor.euler))
    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    print()

    time.sleep(1)