import customtkinter as ctk
import tkinter as tk
from packet import Packet
from layers import OSI_LAYERS
from utils import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT
from animations import AnimationManager

class OSIVisualizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("OSI Model Layer Visualization Tool")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Initialize Core components
        self.packet = Packet()
        self.animator = AnimationManager(self.on_animation_update)

        # Configure Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.setup_ui()

    def setup_ui(self):
        # Title Label
        self.title_label = ctk.CTkLabel(self, text="OSI Model Layer Visualization Tool", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=20)

        # Sender Column
        self.sender_frame = ctk.CTkFrame(self)
        self.sender_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        ctk.CTkLabel(self.sender_frame, text="SENDER", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        self.sender_layer_widgets = []
        for layer in OSI_LAYERS:
            btn = ctk.CTkButton(self.sender_frame, text=f"{layer['number']}. {layer['name']}",
                                fg_color="gray", state="disabled", width=200)
            btn.pack(pady=5)
            self.sender_layer_widgets.append(btn)

        # Transmission/Animation Area
        self.anim_frame = ctk.CTkFrame(self)
        self.anim_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")
        ctk.CTkLabel(self.anim_frame, text="TRANSMISSION MEDIA", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)

        self.status_var = tk.StringVar(value="Status: Ready")
        self.status_label = ctk.CTkLabel(self.anim_frame, textvariable=self.status_var, font=ctk.CTkFont(size=14))
        self.status_label.pack(pady=10)

        self.packet_canvas = tk.Canvas(self.anim_frame, width=350, height=100, bg="#2b2b2b", highlightthickness=0)
        self.packet_canvas.pack(pady=20)
        self.packet_rect = self.packet_canvas.create_rectangle(10, 30, 110, 70, fill="#3390FF", outline="white")
        self.packet_text = self.packet_canvas.create_text(60, 50, text="Packet", fill="white", font=("Arial", 10, "bold"))
        self.packet_canvas.pack_forget() # Hide initially

        self.info_panel = ctk.CTkTextbox(self.anim_frame, width=300, height=300)
        self.info_panel.pack(pady=20)
        self.info_panel.insert("0.0", "Welcome to the OSI Visualization Tool.\nClick 'Start' to begin the simulation.")
        self.info_panel.configure(state="disabled")

        # Receiver Column
        self.receiver_frame = ctk.CTkFrame(self)
        self.receiver_frame.grid(row=1, column=2, padx=20, pady=10, sticky="nsew")
        ctk.CTkLabel(self.receiver_frame, text="RECEIVER", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        self.receiver_layer_widgets = []
        for layer in reversed(OSI_LAYERS):
            btn = ctk.CTkButton(self.receiver_frame, text=f"{layer['number']}. {layer['name']}",
                                fg_color="gray", state="disabled", width=200)
            btn.pack(pady=5)
            self.receiver_layer_widgets.append(btn)

        # Control Panel
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.grid(row=2, column=0, columnspan=3, pady=20, padx=20, sticky="ew")

        self.start_btn = ctk.CTkButton(self.control_frame, text="Start", command=self.start_sim)
        self.start_btn.grid(row=0, column=0, padx=10, pady=10)

        self.pause_btn = ctk.CTkButton(self.control_frame, text="Pause", command=self.pause_sim)
        self.pause_btn.grid(row=0, column=1, padx=10, pady=10)

        self.resume_btn = ctk.CTkButton(self.control_frame, text="Resume", command=self.resume_sim)
        self.resume_btn.grid(row=0, column=2, padx=10, pady=10)

        self.reset_btn = ctk.CTkButton(self.control_frame, text="Reset", command=self.reset_sim)
        self.reset_btn.grid(row=0, column=3, padx=10, pady=10)

        ctk.CTkLabel(self.control_frame, text="Speed:").grid(row=0, column=4, padx=5)
        self.speed_slider = ctk.CTkSlider(self.control_frame, from_=0.5, to=3.0, command=self.change_speed)
        self.speed_slider.set(1.0)
        self.speed_slider.grid(row=0, column=5, padx=10)

    def update_info(self, text):
        self.info_panel.configure(state="normal")
        self.info_panel.delete("0.0", "end")
        self.info_panel.insert("0.0", text)
        self.info_panel.configure(state="disabled")

    def on_animation_update(self, step, state):
        if state == "Reset":
            self.reset_ui()
            return

        if state == "Finished":
            self.status_var.set("Status: Transmission Complete")
            return

        # Handle Step Visualization
        if step < 7:
            # Sender Side Encapsulation
            layer = OSI_LAYERS[step]
            self.packet.encapsulate(layer['name'])
            self.status_var.set(f"Status: Encapsulating at {layer['name']} Layer")

            # Highlight Sender Layer
            for i, widget in enumerate(self.sender_layer_widgets):
                if i == step:
                    widget.configure(fg_color=COLORS[layer['name']])
                else:
                    widget.configure(fg_color="gray")

            self.update_info(f"Layer {layer['number']}: {layer['name']}\n\n{layer['description']}\n\nPDU: {layer['pdu']}\n\nCurrent Packet:\n{self.packet.get_full_packet()}")

        elif step == 7:
            # Physical Transmission Animation
            self.status_var.set("Status: Transmitting over Physical Medium...")
            self.packet_canvas.pack(pady=20)
            self.animate_packet_movement()
            self.update_info("Data is now being transmitted as bits over the physical medium (cables, radio waves, etc.). This step involves physical signaling.")

        elif step < 15:
            # Receiver Side Decapsulation
            idx = step - 8
            layer = OSI_LAYERS[6 - idx]
            self.packet.decapsulate()
            self.status_var.set(f"Status: Decapsulating at {layer['name']} Layer")

            # Highlight Receiver Layer
            for i, widget in enumerate(self.receiver_layer_widgets):
                if i == idx:
                    widget.configure(fg_color=COLORS[layer['name']])
                else:
                    widget.configure(fg_color="gray")

            self.update_info(f"Layer {layer['number']}: {layer['name']}\n\n{layer['description']}\n\nPDU: {layer['pdu']}\n\nCurrent Packet:\n{self.packet.get_full_packet()}")
            if step == 14:
                self.packet_canvas.pack_forget()

        # Schedule next step if not paused
        if self.animator.is_running and not self.animator.is_paused:
            delay = int(2000 / self.animator.speed)
            self.after(delay, self.animator.run_loop)

    def start_sim(self):
        self.reset_sim()
        self.animator.start()

    def pause_sim(self):
        self.animator.pause()

    def resume_sim(self):
        self.animator.resume()

    def reset_sim(self):
        self.animator.reset()
        self.packet.reset()
        self.reset_ui()

    def animate_packet_movement(self, pos=10):
        if not self.animator.is_running or self.animator.is_paused or self.animator.current_step != 8:
             # step was 7 when triggered, it increments to 8 in animator.run_loop BEFORE next after()
             # Wait, my logic: update_callback(step, "Running"); current_step += 1.
             # So when step is 7, current_step becomes 8.
             pass

        if pos < 240:
            self.packet_canvas.move(self.packet_rect, 5 * self.animator.speed, 0)
            self.packet_canvas.move(self.packet_text, 5 * self.animator.speed, 0)
            self.after(20, lambda: self.animate_packet_movement(pos + 5))
        else:
            # Reset packet position for next time
            self.packet_canvas.coords(self.packet_rect, 10, 30, 110, 70)
            self.packet_canvas.coords(self.packet_text, 60, 50)

    def reset_ui(self):
        for widget in self.sender_layer_widgets:
            widget.configure(fg_color="gray")
        for widget in self.receiver_layer_widgets:
            widget.configure(fg_color="gray")
        self.status_var.set("Status: Ready")
        self.packet_canvas.pack_forget()
        self.packet_canvas.coords(self.packet_rect, 10, 30, 110, 70)
        self.packet_canvas.coords(self.packet_text, 60, 50)
        self.update_info("Welcome to the OSI Visualization Tool.\nClick 'Start' to begin the simulation.")

    def change_speed(self, val):
        self.animator.set_speed(float(val))

if __name__ == "__main__":
    app = OSIVisualizerApp()
    app.mainloop()
