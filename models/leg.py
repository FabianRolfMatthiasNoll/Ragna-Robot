from adafruit_pca9685 import PWMChannel
from models.leg_position import LegPosition

class Leg:
    def __init__(self, upper_servo: PWMChannel, lower_servo: PWMChannel) -> None:
        self.upper_servo = upper_servo
        self.lower_servo = lower_servo

    def set_position(self, position: LegPosition) -> None:
        # Convert position values to duty cycle or pulse width for servos
        self.upper_servo.duty_cycle = position.upper
        self.lower_servo.duty_cycle = position.lower
