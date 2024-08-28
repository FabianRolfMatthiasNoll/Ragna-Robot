from concurrent.futures import ThreadPoolExecutor
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
        position1 = LegPosition(upper=1000, lower=2000)
        position2 = LegPosition(upper=1500, lower=2500)

        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.move_leg, "front_right", position1),
                executor.submit(self.move_leg, "front_left", position1),
                executor.submit(self.move_leg, "back_right", position2),
                executor.submit(self.move_leg, "back_left", position2)
            ]
            for future in futures:
                future.result()  # Ensure all threads complete before moving on
