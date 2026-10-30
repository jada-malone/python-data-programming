# PROGRAM: EggTimer
# PURPOSE: To represent a simple timer for cooking eggs.
# INPUT: Start and stop commands.
# PROCESS: Tracks time duration between start and stop.
# OUTPUT: Displays the total duration.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

import time

class EggTimer:
    """A simple egg timer class."""

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.is_running = False

    def start(self):
        """Starts the timer."""
        if self.is_running:
            raise RuntimeError("Timer is already running.")
        self.start_time = time.time()
        self.is_running = True
        print("Timer started.")

    def stop(self):
        """Stops the timer and calculates the duration."""
        if not self.is_running:
            raise RuntimeError("Timer is not running. Start the timer first.")
        self.end_time = time.time()
        self.is_running = False
        duration = self.calculate_duration()
        print(f"Timer stopped. Duration: {duration:.2f} seconds.")

    def calculate_duration(self):
        """Calculates the duration between start and end times."""
        if self.start_time is None or self.end_time is None:
            raise RuntimeError("Timer must be started and stopped to calculate duration.")
        return self.end_time - self.start_time
