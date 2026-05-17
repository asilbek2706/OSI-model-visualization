"""
Animation Manager Module: Simulation State Machine Logic
This module implements the AnimationManager class, which acts as the 'brain' of the
simulation flow. It manages the sequential transitions between the 15 distinct
states of an end-to-end OSI model transmission.

The simulation cycle consists of:
1. Seven stages of downward traversal on the sender side (Layers 7 down to 1).
2. A physical media transmission phase where data moves between systems.
3. Seven stages of upward traversal on the receiver side (Layers 1 up to 7).

The manager handles timing logic, speed adjustments, and the pause/resume/reset
functionality to ensure a smooth and educational user experience.
"""

import time
from layers import OSI_LAYERS

class AnimationManager:
    """
    Coordinates the state transitions and timing for the OSI model simulation.
    Uses a callback system to update the Graphical User Interface (GUI)
    synchronously with the logical state changes.
    """
    def __init__(self, update_callback):
        """
        Initializes the manager with a reference to the UI update function.

        Args:
            update_callback (callable): A function in the main application
                                       that updates widgets based on current state.
        """
        self.update_callback = update_callback
        self.is_running = False
        self.is_paused = False
        self.speed = 1.0
        self.current_step = 0
        # Total steps: 0-6 (Sender), 7 (Physical), 8-14 (Receiver)
        self.total_steps = 15

    def start(self):
        """
        Begins the simulation from the first step (Application Layer).
        """
        self.is_running = True
        self.is_paused = False
        self.current_step = 0
        self.run_loop()

    def pause(self):
        """
        Halts the simulation at the current step.
        """
        self.is_paused = True

    def resume(self):
        """
        Resumes the simulation if it was previously paused.
        """
        if self.is_running:
            self.is_paused = False
            self.run_loop()

    def reset(self):
        """
        Stops the simulation and triggers a full UI/Logical reset.
        """
        self.is_running = False
        self.is_paused = False
        self.current_step = 0
        self.update_callback(self.current_step, "Reset")

    def set_speed(self, speed):
        """
        Adjusts the simulation pace dynamically.

        Args:
            speed (float): A multiplier for the simulation speed (e.g., 0.5x, 2.0x).
        """
        self.speed = speed

    def run_loop(self):
        """
        The core logic loop that advances the simulation state.
        This method checks for pause/stop conditions and triggers the
        callback to notify the GUI that it is time to visualize the next step.
        """
        if not self.is_running or self.is_paused:
            # If the simulation is stopped or paused, we exit the loop.
            # The resume() method will re-invoke this when the user is ready.
            return

        if self.current_step < self.total_steps:
            # Notify the UI to update its appearance and the packet's data
            self.update_callback(self.current_step, "Running")

            # Increment the step for the next iteration
            self.current_step += 1

            # Note: The actual delay and scheduling of the next call to run_loop
            # is handled by the Tkinter after() method in main.py to keep
            # the GUI thread non-blocking and responsive.
        else:
            # Simulation has completed all 15 steps
            self.is_running = False
            self.update_callback(self.current_step, "Finished")
