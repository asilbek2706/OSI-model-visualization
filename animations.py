import time
from layers import OSI_LAYERS

class AnimationManager:
    """
    Manages the state and logic of the OSI model simulation.
    """
    def __init__(self, update_callback):
        self.update_callback = update_callback
        self.is_running = False
        self.is_paused = False
        self.speed = 1.0
        self.current_step = 0
        # Steps: 0-6 sender (down), 7 transition, 8-14 receiver (up)
        self.total_steps = 15

    def start(self):
        self.is_running = True
        self.is_paused = False
        self.current_step = 0
        self.run_loop()

    def pause(self):
        self.is_paused = True

    def resume(self):
        if self.is_running:
            self.is_paused = False
            self.run_loop()

    def reset(self):
        self.is_running = False
        self.is_paused = False
        self.current_step = 0
        self.update_callback(self.current_step, "Reset")

    def set_speed(self, speed):
        self.speed = speed

    def run_loop(self):
        if not self.is_running or self.is_paused:
            return

        if self.current_step < self.total_steps:
            self.update_callback(self.current_step, "Running")
            self.current_step += 1

            # Calculate delay based on speed
            delay = int(1000 / self.speed)
            # Use a timer to trigger next step (this will be handled by the GUI mainloop)
            # but for logic we just define it here.
        else:
            self.is_running = False
            self.update_callback(self.current_step, "Finished")
