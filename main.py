"""
Main Module: OSI Model Layer Visualization Tool
This is the entry point of the application. It implements the Graphical User Interface (GUI)
using the CustomTkinter library, providing an interactive and modern experience for
visualizing the complex workings of the 7-layer OSI model.

The application orchestrates the interaction between the Packet logic, the Animation
state machine, and the visual representation of the networking stacks. It handles
user inputs, updates real-time informative panels, and manages a Canvas-based
coordinate animation for physical transmission.

Author: Professional Software Engineering Team
Subject: Computer Networking Educational Tools
"""

import customtkinter as ctk
import tkinter as tk
from packet import Packet
from layers import OSI_LAYERS
from utils import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT
from animations import AnimationManager

class OSIVisualizerApp(ctk.CTk):
    """
    The main application class that defines the UI layout and handles event orchestration.
    Inherits from ctk.CTk to provide a modern dark-themed window.
    """
    def __init__(self):
        super().__init__()

        # Window Metadata and Configuration
        self.title("Academic OSI Model Visualization Tool")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Initialize Core Logic Components
        self.packet = Packet()
        self.animator = AnimationManager(self.on_animation_update)

        # Configure Responsive Grid Layout
        self.grid_columnconfigure(0, weight=1) # Sender Column
        self.grid_columnconfigure(1, weight=1) # Animation/Info Column
        self.grid_columnconfigure(2, weight=1) # Receiver Column
        self.grid_rowconfigure(1, weight=1)    # Main Content Row

        self.setup_ui()

    def setup_ui(self):
        """
        Constructs the complex UI hierarchy including frames, buttons, labels, and the canvas.
        Organizes the interface into logical sections: Sender, Transmission/Info, and Receiver.
        """
        # Global Application Title
        self.title_label = ctk.CTkLabel(self, text="OSI Model Layer Visualization Tool",
                                        font=ctk.CTkFont(size=26, weight="bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=25)

        # --- Sender Stack Section ---
        self.sender_frame = ctk.CTkFrame(self)
        self.sender_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        ctk.CTkLabel(self.sender_frame, text="SENDER (Host A)",
                     font=ctk.CTkFont(size=18, weight="bold")).pack(pady=15)

        self.sender_layer_widgets = []
        for layer in OSI_LAYERS:
            # Create a button for each layer to visualize the stack.
            # These are disabled as they are for display purposes only.
            btn = ctk.CTkButton(self.sender_frame, text=f"{layer['number']}. {layer['name']}",
                                fg_color="gray", state="disabled", width=220, height=40)
            btn.pack(pady=5)
            self.sender_layer_widgets.append(btn)

        # --- Central Transmission and Information Section ---
        self.anim_frame = ctk.CTkFrame(self)
        self.anim_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")
        ctk.CTkLabel(self.anim_frame, text="TRANSMISSION MEDIUM",
                     font=ctk.CTkFont(size=18, weight="bold")).pack(pady=15)

        # Status Display (Reactive to simulation state)
        self.status_var = tk.StringVar(value="Status: System Ready")
        self.status_label = ctk.CTkLabel(self.anim_frame, textvariable=self.status_var,
                                         font=ctk.CTkFont(size=14, slant="italic"))
        self.status_label.pack(pady=10)

        # Canvas for Physical Bitstream Animation
        self.packet_canvas = tk.Canvas(self.anim_frame, width=350, height=100,
                                       bg="#1d1e1e", highlightthickness=0)
        self.packet_canvas.pack(pady=20)
        # Create the visual representation of the 'Packet'
        self.packet_rect = self.packet_canvas.create_rectangle(10, 30, 110, 70, fill="#3390FF", outline="white")
        self.packet_text = self.packet_canvas.create_text(60, 50, text="Packet/Bit", fill="white",
                                                         font=("Arial", 10, "bold"))
        self.packet_canvas.pack_forget() # Hidden until physical layer is reached

        # Rich Educational Information Panel
        self.info_panel = ctk.CTkTextbox(self.anim_frame, width=320, height=320, font=("Segoe UI", 12))
        self.info_panel.pack(pady=20)
        self.info_panel.insert("0.0", "Welcome to the Academic OSI Visualization Tool.\n\n"
                                      "This tool demonstrates the end-to-end communication cycle.\n"
                                      "Click 'Start' to begin the simulation.")
        self.info_panel.configure(state="disabled")

        # --- Receiver Stack Section ---
        self.receiver_frame = ctk.CTkFrame(self)
        self.receiver_frame.grid(row=1, column=2, padx=20, pady=10, sticky="nsew")
        ctk.CTkLabel(self.receiver_frame, text="RECEIVER (Host B)",
                     font=ctk.CTkFont(size=18, weight="bold")).pack(pady=15)

        self.receiver_layer_widgets = []
        # Receiver stack is displayed from Physical (bottom) up to Application (top)
        for layer in reversed(OSI_LAYERS):
            btn = ctk.CTkButton(self.receiver_frame, text=f"{layer['number']}. {layer['name']}",
                                fg_color="gray", state="disabled", width=220, height=40)
            btn.pack(pady=5)
            self.receiver_layer_widgets.append(btn)

        # --- Simulation Control Panel ---
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.grid(row=2, column=0, columnspan=3, pady=25, padx=20, sticky="ew")

        # Interaction Buttons
        self.start_btn = ctk.CTkButton(self.control_frame, text="Start Simulation", command=self.start_sim, fg_color="#27ae60", hover_color="#2ecc71")
        self.start_btn.grid(row=0, column=0, padx=15, pady=15)

        self.pause_btn = ctk.CTkButton(self.control_frame, text="Pause", command=self.pause_sim)
        self.pause_btn.grid(row=0, column=1, padx=10, pady=15)

        self.resume_btn = ctk.CTkButton(self.control_frame, text="Resume", command=self.resume_sim)
        self.resume_btn.grid(row=0, column=2, padx=10, pady=15)

        self.reset_btn = ctk.CTkButton(self.control_frame, text="Reset System", command=self.reset_sim, fg_color="#c0392b", hover_color="#e74c3c")
        self.reset_btn.grid(row=0, column=3, padx=15, pady=15)

        # Speed Control Slider
        ctk.CTkLabel(self.control_frame, text="Simulation Speed:").grid(row=0, column=4, padx=5)
        self.speed_slider = ctk.CTkSlider(self.control_frame, from_=0.5, to=3.0, command=self.change_speed)
        self.speed_slider.set(1.0)
        self.speed_slider.grid(row=0, column=5, padx=15)

    def update_info(self, text):
        """
        Updates the text content in the educational information panel.
        """
        self.info_panel.configure(state="normal")
        self.info_panel.delete("0.0", "end")
        self.info_panel.insert("0.0", text)
        self.info_panel.configure(state="disabled")

    def on_animation_update(self, step, state):
        """
        The main callback function triggered by the AnimationManager.
        Synchronizes the logical state (step) with the visual representation.

        Args:
            step (int): The current stage of the simulation (0-14).
            state (str): Current status string ('Running', 'Reset', 'Finished').
        """
        if state == "Reset":
            self.reset_ui()
            return

        if state == "Finished":
            self.status_var.set("Status: Transmission Successful")
            self.update_info("Transmission Complete.\n\nThe original data has been successfully delivered to the destination application.")
            return

        # Handle Step-specific Visualization Logic
        if step < 7:
            # SENDER SIDE: Encapsulation Phase (Descending stack)
            layer = OSI_LAYERS[step]
            self.packet.encapsulate(layer['name'])
            self.status_var.set(f"Status: Encapsulating at Layer {layer['number']} ({layer['name']})")

            # Update UI Highlights
            for i, widget in enumerate(self.sender_layer_widgets):
                if i == step:
                    widget.configure(fg_color=COLORS[layer['name']])
                else:
                    widget.configure(fg_color="gray")

            self.update_info(f"--- LAYER {layer['number']}: {layer['name']} ---\n\n"
                             f"FUNCTION: {layer['description']}\n\n"
                             f"PDU: {layer['pdu']}\n\n"
                             f"ENCAPSULATED DATA:\n{self.packet.get_full_packet()}")

        elif step == 7:
            # PHYSICAL MEDIUM: Transmission Phase
            self.status_var.set("Status: Transmitting Data Bits...")
            self.packet_canvas.pack(pady=20)
            self.animate_packet_movement()
            self.update_info("--- PHYSICAL TRANSMISSION ---\n\n"
                             "Data has been converted into electrical, optical, or radio signals. "
                             "It is currently moving across the communication channel between Host A and Host B.")

        elif step < 15:
            # RECEIVER SIDE: Decapsulation Phase (Ascending stack)
            idx = step - 8
            # The receiver processes in reverse order of the list (bottom up)
            layer = OSI_LAYERS[6 - idx]
            self.packet.decapsulate()
            self.status_var.set(f"Status: Decapsulating at Layer {layer['number']} ({layer['name']})")

            # Update UI Highlights
            for i, widget in enumerate(self.receiver_layer_widgets):
                if i == idx:
                    widget.configure(fg_color=COLORS[layer['name']])
                else:
                    widget.configure(fg_color="gray")

            self.update_info(f"--- LAYER {layer['number']}: {layer['name']} ---\n\n"
                             f"FUNCTION: {layer['description']}\n\n"
                             f"PDU: {layer['pdu']}\n\n"
                             f"DECAPSULATED DATA:\n{self.packet.get_full_packet()}")

            # Hide the transmission canvas once it reaches the first receiver layer
            if idx == 0:
                self.packet_canvas.pack_forget()

        # Schedule the next step if the simulation is active
        if self.animator.is_running and not self.animator.is_paused:
            # Delay is calculated dynamically to support variable speed
            delay = int(2000 / self.animator.speed)
            self.after(delay, self.animator.run_loop)

    def start_sim(self):
        """Initializes and begins the simulation sequence."""
        self.reset_sim()
        self.animator.start()

    def pause_sim(self):
        """Pauses the active simulation."""
        self.animator.pause()

    def resume_sim(self):
        """Resumes a paused simulation."""
        self.animator.resume()

    def reset_sim(self):
        """Triggers a logic and UI reset."""
        self.animator.reset()
        self.packet.reset()
        self.reset_ui()

    def animate_packet_movement(self, pos=10):
        """
        Handles the frame-by-frame coordinate movement on the Canvas.

        Args:
            pos (int): The current X-coordinate of the packet element.
        """
        # Safety check: only animate if we are in the physical transmission step
        if not self.animator.is_running or self.animator.is_paused or self.animator.current_step != 8:
             return

        if pos < 240:
            # Move both the rectangle and the text element
            self.packet_canvas.move(self.packet_rect, 5 * self.animator.speed, 0)
            self.packet_canvas.move(self.packet_text, 5 * self.animator.speed, 0)
            # 20ms update interval for smooth 50 FPS-like movement
            self.after(20, lambda: self.animate_packet_movement(pos + 5))
        else:
            # Reset visual coordinates for future use
            self.packet_canvas.coords(self.packet_rect, 10, 30, 110, 70)
            self.packet_canvas.coords(self.packet_text, 60, 50)

    def reset_ui(self):
        """
        Restores all UI elements to their original 'Ready' state.
        """
        for widget in self.sender_layer_widgets:
            widget.configure(fg_color="gray")
        for widget in self.receiver_layer_widgets:
            widget.configure(fg_color="gray")
        self.status_var.set("Status: System Ready")
        self.packet_canvas.pack_forget()
        self.packet_canvas.coords(self.packet_rect, 10, 30, 110, 70)
        self.packet_canvas.coords(self.packet_text, 60, 50)
        self.update_info("Welcome to the Academic OSI Visualization Tool.\n\n"
                         "This tool demonstrates the end-to-end communication cycle.\n"
                         "Click 'Start' to begin the simulation.")

    def change_speed(self, val):
        """Updates the animation speed based on the slider value."""
        self.animator.set_speed(float(val))

if __name__ == "__main__":
    # Launch the application
    app = OSIVisualizerApp()
    app.mainloop()
