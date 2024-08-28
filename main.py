import board
import busio
import adafruit_pca9685
from config import I2C_ADDRESSES, PWM_CHANNELS
from models.leg import Leg
from controllers.movement_controller import MovementController

if __name__ == "__main__":
    i2c = busio.I2C(board.SCL, board.SDA)
    
    servo_controller_right = adafruit_pca9685.PCA9685(i2c, address=I2C_ADDRESSES['servo_controller_right'])
    servo_controller_left = adafruit_pca9685.PCA9685(i2c, address=I2C_ADDRESSES['servo_controller_left'])

    leg_front_right = Leg(servo_controller_right.channels[PWM_CHANNELS['leg_front_right_upper']], servo_controller_right.channels[PWM_CHANNELS['leg_front_right_lower']])
    leg_front_left = Leg(servo_controller_left.channels[PWM_CHANNELS['leg_front_left_upper']], servo_controller_left.channels[PWM_CHANNELS['leg_front_left_lower']])
    leg_back_right = Leg(servo_controller_right.channels[PWM_CHANNELS['leg_back_right_upper']], servo_controller_right.channels[PWM_CHANNELS['leg_back_right_lower']])
    leg_back_left = Leg(servo_controller_left.channels[PWM_CHANNELS['leg_back_left_upper']], servo_controller_left.channels[PWM_CHANNELS['leg_back_left_lower']])

    movement_controller = MovementController(leg_front_right, leg_front_left, leg_back_right, leg_back_left)

    # Example usage
    movement_controller.walk_forward()
