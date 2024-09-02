from concurrent.futures import ThreadPoolExecutor
from time import sleep
from models.leg import Leg
from models.leg_position import LegPosition

class MovementController:
    def __init__(self, front_right: Leg, front_left: Leg, back_right: Leg, back_left: Leg) -> None:
        self.legs = {
            "front_right": front_right,
            "front_left": front_left,
            "back_right": back_right,
            "back_left": back_left
        }

    def move_leg(self, leg_name: str, position: LegPosition) -> None:
        leg = self.legs[leg_name]
        leg.set_position(position)

    def walk_forward(self) -> None:
        position1 = LegPosition(upper_degree=0, lower_degree=0)
        position2 = LegPosition(upper_degree=90, lower_degree=90)
        # while True:
        #     print("Walking forward")
        #     with ThreadPoolExecutor() as executor:
        #         futures = [
        #             executor.submit(self.move_leg, "front_right", position1),
        #             executor.submit(self.move_leg, "front_left", position1),
        #             executor.submit(self.move_leg, "back_right", position1),
        #             executor.submit(self.move_leg, "back_left", position1)
        #         ]
        #         for future in futures:
        #             future.result()  # Ensure all threads complete before moving on
        #     sleep(2)
        #     print("Walking forward 2")
        #     with ThreadPoolExecutor() as executor:
        #         futures = [
        #             executor.submit(self.move_leg, "front_right", position2),
        #             executor.submit(self.move_leg, "front_left", position2),
        #             executor.submit(self.move_leg, "back_right", position2),
        #             executor.submit(self.move_leg, "back_left", position2)
        #         ]
        #         for future in futures:
        #             future.result()  # Ensure all threads complete before moving on
        #     sleep(2)
        with ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(self.move_leg, "front_right", position2),
                    executor.submit(self.move_leg, "front_left", position2),
                    executor.submit(self.move_leg, "back_right", position2),
                    executor.submit(self.move_leg, "back_left", position2)
                ]
                for future in futures:
                    future.result()  # Ensure all threads complete before moving on