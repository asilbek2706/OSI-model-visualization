# OSI Model Layer Visualization Tool

## Project Overview
The OSI Model Layer Visualization Tool is a comprehensive, academic-grade Python-based educational application specifically designed to demystify the inner workings of the Open Systems Interconnection (OSI) model. The OSI model is a world-standard conceptual framework that partitions the complex process of telecommunication and computer networking into seven distinct, manageable abstraction layers. Our tool provides a high-fidelity, dynamic, and interactive simulation of how data travels through these layers, starting from the sender's Application layer, descending through the stack to the Physical medium, and subsequently ascending the receiver's stack to the destination application. By providing a clear, real-time visualization of critical networking processes such as encapsulation (the addition of protocol headers) and decapsulation (the systematic removal of those headers), this tool provides students, educators, and networking enthusiasts with a profound visual understanding of complex concepts that are traditionally difficult to grasp through static textbooks or theoretical lectures alone. It serves as a bridge between abstract theory and the practical reality of data communication.

## Features
- **Comprehensive 7-Layer Visualization**: The application displays a complete, side-by-side view of all seven OSI layers (Application, Presentation, Session, Transport, Network, Data Link, and Physical) for both the sending and receiving entities.
- **Dynamic Coordinate-Based Animation**: Unlike simple state-change visualizers, our tool features a smooth, coordinate-based animation of the packet as it traverses the "Physical Medium" between the two systems.
- **Real-time Encapsulation and Decapsulation**: Users can watch in real-time as headers are programmatically added to the data at each layer on the sender side and stripped away at each layer on the receiver side, demonstrating the transformation of Protocol Data Units (PDUs).
- **Interactive Educational Info Panel**: A dedicated panel provides rich, context-sensitive educational descriptions, PDU names (Data, Segment, Packet, Frame, Bit), and a real-time display of the packet's contents at every stage of the simulation.
- **Full Simulation Control System**: The interface includes a professional suite of controls including Start, Pause, Resume, and Reset buttons, allowing users to analyze the networking process at their own pace or stop to discuss specific layer functions.
- **Variable Speed Control Slider**: A dynamic speed slider allows users to adjust the simulation pace from 0.5x for detailed study to 3.0x for a quick overview of the end-to-end process.
- **Modern and Professional GUI**: Built using the CustomTkinter library, the application features a sleek, dark-themed, and responsive interface that aligns with modern professional software standards, making it ideal for university-level presentations and submissions.

## Technologies Used
- **Python 3.x**: The primary programming language used for the application's core logic, state management, and modular architecture.
- **CustomTkinter**: A modern wrapper for Tkinter that provides high-quality, professional UI components, including themed buttons, frames, and sliders.
- **Tkinter (Standard Library)**: Used for the underlying graphical engine and the Canvas-based animation system for physical transmission.
- **Python-docx**: A powerful library utilized to programmatically generate the 5-8 page academic project synopsis with proper formatting and structure.
- **Threading and Timing**: The application uses non-blocking asynchronous timing (via the after() method) to manage animations and state transitions without freezing the user interface.
- **Modular Software Design**: The project is organized into dedicated modules (`packet.py`, `layers.py`, `animations.py`, `utils.py`) to ensure clean code, high maintainability, and clear separation of concerns.

## Installation Guide
1. **Clone the Project Repository**:
   Start by downloading the project files to your local machine. You can do this by cloning the repository using git:
   ```bash
   git clone https://github.com/your-username/osi-visualization-tool.git
   cd osi-visualization-tool
   ```
2. **Set Up a Virtual Environment (Optional but Recommended)**:
   It is best practice to use a virtual environment to avoid conflicts with other Python projects:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Required Python Libraries**:
   Ensure you have all the necessary dependencies installed by running the following command:
   ```bash
   pip install -r requirements.txt
   ```
   This will install `customtkinter`, `python-docx`, and other support libraries like `darkdetect` and `lxml`.

## How to Run the Project
1. **Execute the Main Application**:
   Navigate to the project root directory and run the main entry point script:
   ```bash
   python main.py
   ```
2. **Initialize the Simulation**:
   Once the GUI loads, you will see the sender and receiver stacks. Click the "Start" button to begin the data transmission process.
3. **Interactive Simulation Management**:
   - **Pause/Resume**: Use these buttons to halt the simulation at any layer to inspect the packet headers or read the educational descriptions.
   - **Adjust Speed**: Move the slider to the left or right to change how quickly the data moves through the layers and across the physical medium.
   - **Reset**: At any time, click "Reset" to return the packet to its original state and clear all layer highlights.
4. **Generate Documentation**:
   To generate a fresh copy of the academic synopsis document, run:
   ```bash
   python generate_synopsis.py
   ```

## Project Structure
- `main.py`: This is the central hub of the application. It handles the GUI layout, event binding, and the high-level orchestration of the simulation steps.
- `packet.py`: Contains the `Packet` class logic, which is responsible for the string-based encapsulation and decapsulation algorithms.
- `layers.py`: Acts as the data store for the project, containing structured information about each OSI layer, including their names, numbers, PDUs, and educational descriptions.
- `animations.py`: The `AnimationManager` class lives here, managing the 15-stage state machine and handling the pause/resume/reset logic.
- `utils.py`: A configuration file that defines constants such as the professional color palette, window dimensions, and default timing intervals.
- `generate_synopsis.py`: A specialized script that uses `python-docx` to create a detailed, formatted academic synopsis for project submission.
- `requirements.txt`: A standard file listing all external Python packages required to run the tool successfully.

## Working Principle
The application operates on the principle of a deterministic state machine that mirrors the real-world sequential nature of network communication. When a user clicks "Start," the system begins at the sender's Application layer (Layer 7). The `Packet` object is passed through a loop where, at each step, a simulated header string (representing protocol control information) is prepended to the data. This visualizes encapsulation. Once it reaches the Physical layer, the simulation transitions to a coordinate-based animation on a Canvas, showing the packet moving across the screen to represent physical signaling. On the receiver's side, the process is reversed. The `Packet` object undergoes decapsulation, where headers are identified and stripped away in a bottom-up fashion (Layer 1 to Layer 7). The GUI provides constant feedback by highlighting the current active layer and updating the info panel with pedagogical content, providing a holistic and synchronized view of the entire communication cycle.

## Future Improvements
- **Network Protocol Realism**: Future versions could include the simulation of actual protocol handshakes, such as the TCP three-way handshake, or the ARP address resolution process.
- **Multiple Network Nodes**: Expanding the visualization to include intermediate devices like routers and switches to demonstrate the concept of "hop-by-hop" delivery versus "end-to-end" delivery.
- **Simulated Network Impairments**: Adding a "Network Health" toggle that introduces packet loss, latency jitter, or header corruption to show how the Transport and Data Link layers handle errors.
- **Packet Sniffer Integration**: A "Live Log" feature that exports the simulation's packet transformations into a format compatible with tools like Wireshark for further academic analysis.
- **Custom Data Input**: Allowing users to type their own messages and choose specific protocols (like FTP, SMTP, or DNS) to see how different application-layer headers are structured.

## Educational Importance
The OSI model is frequently criticized by students for being overly abstract and disconnected from the reality of modern computing. This tool directly addresses that pedagogical challenge by making the model tangible and visible. It serves as an essential bridge, allowing learners to visualize the "invisible" work their systems perform every time they send a message or load a webpage. By seeing the data change form—transforming from Application Data to Segments, then Packets, then Frames, and finally to Bits—students develop a much more robust and permanent mental model of network architecture. This visual-first approach is scientifically proven to be more effective for complex concept retention than reading alone, making this project an invaluable asset for any computer science curriculum, bootcamp, or networking certification preparation course.
