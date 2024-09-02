from adafruit_pca9685 import PWMChannel
from models.leg_position import LegPosition
from config import MAX_PWM_DUTY_CYCLE, MIN_PWM_DUTY_CYCLE

class Leg:
    def __init__(self, upper_servo: PWMChannel, lower_servo: PWMChannel, inverse: bool) -> None:
        self.upper_servo = upper_servo
        self.lower_servo = lower_servo
        self.inverse = inverse

    def set_position(self, position: LegPosition) -> None:
        # Convert position values to duty cycle or pulse width for servos
        if self.inverse:
            position = LegPosition(upper_degree=180 - position.upper_degree, lower_degree=180 - position.lower_degree)
        if not self.inverse:
            position = LegPosition(upper_degree=position.upper_degree - 15, lower_degree=position.lower_degree - 15)
            if position.upper_degree < 0:
                position = LegPosition(upper_degree=0, lower_degree=position.lower_degree)
            if position.lower_degree < 0:
                position = LegPosition(upper_degree=position.upper_degree, lower_degree=0)
                
        upper_pwm_value = self.map_range(position.upper_degree, 0, 180, MIN_PWM_DUTY_CYCLE, MAX_PWM_DUTY_CYCLE)
        lower_pwm_value = self.map_range(position.lower_degree, 0, 180, MIN_PWM_DUTY_CYCLE, MAX_PWM_DUTY_CYCLE)
        self.upper_servo.duty_cycle = int(upper_pwm_value)
        self.lower_servo.duty_cycle = int(lower_pwm_value)

    def map_range(self, value, from_min, from_max, to_min, to_max):
        return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min