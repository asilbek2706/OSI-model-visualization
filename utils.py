"""
Utilities Module: Configuration and Visual Constants
This module contains global constants, configuration parameters, and the visual
color palette used throughout the OSI Model Visualization Tool.

By centralizing these values, we ensure visual consistency across the application
and allow for easy adjustment of UI parameters (such as window size or simulation
speed) without modifying the core logic in other modules.
"""

# Professional color palette for each OSI Layer
# Each color is chosen to be distinct for clear visual identification in the UI.
COLORS = {
    "Application": "#FF5733",    # Vibrant Red-Orange
    "Presentation": "#FFC300",   # Bright Yellow
    "Session": "#DAF7A6",        # Soft Lime Green
    "Transport": "#33FF57",      # Emerald Green
    "Network": "#33FFCE",        # Turquoise/Cyan
    "Data Link": "#3390FF",      # Royal Blue
    "Physical": "#8E44AD",       # Deep Purple
}

# --- Graphical User Interface (GUI) Dimensions ---
# Defines the default window size for optimal layout on modern displays.
WINDOW_WIDTH = 1250
WINDOW_HEIGHT = 850

# --- Layout Parameters ---
# Used for scaling elements if needed in future dynamic layouts.
LAYER_HEIGHT = 65
LAYER_WIDTH = 260
SPACING = 25

# --- Simulation Logic Constants ---
# Default multiplier for the simulation speed.
DEFAULT_SPEED = 1.0

# Interval (in milliseconds) for high-frequency updates, such as canvas movement.
ANIMATION_INTERVAL = 50
