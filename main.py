import time

def main() -> None:
    plane = Plane()

    kp = 1
    ki = 0
    kd = 0

    setpoint = 0
    error = setpoint - plane.get_roll()
    error_sum = error
    last_error = error
    error_sum = error
    last_time = time.time() - 1

    while True:
        error = plane.get_roll()
        error_sum += error


        # If the error crosses 0, reset the sum of the error
        # to prevent the i term from going out of control
        if error > 0 != last_error > 0:
            error_sum = 0

        p = kp * error
        i = ki * error_sum
        d = kd * ((last_error - error) / (last_time - time.time()))

        output = p + i + d

        plane.roll(output)

        time.sleep(0.02)

# This is not accurate to how the I/O would be handled irl,
# and is just for demonstration
class Plane:
    current_roll = 0.0

    def roll(self, amount: float):
        self.current_roll += amount

    def get_roll(self):
        return self.current_roll
