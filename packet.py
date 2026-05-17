"""
Packet Module: Encapsulation and Decapsulation Logic
This module defines the Packet class, which serves as the primary data structure for the
OSI Model Visualization Tool. It simulates the real-world process of network communication
by programmatically adding and removing protocol headers as data traverses the OSI stack.

The class provides methods to encapsulate data by wrapping it in layer-specific headers
on the sender side and decapsulate it by stripping those headers on the receiver side.
This implementation uses a string-based approach to provide a clear visual representation
of Protocol Data Units (PDUs) throughout the transmission lifecycle.
"""

class Packet:
    """
    Represents a data packet traveling through the OSI model layers.
    Handles the logical transformation of data from a simple message into a
    fully encapsulated frame and back again to its original form.
    """
    def __init__(self, data="Hello, Network!"):
        """
        Initializes a new Packet instance with the original payload.

        Args:
            data (str): The initial user data to be transmitted.
                        Defaults to "Hello, Network!".
        """
        self.original_data = data
        self.payload = data
        self.headers = []  # Stack used to keep track of added headers for correct decapsulation
        self.current_layer_index = 0
        self.is_encapsulating = True  # Flag to track if the packet is descending (sender) or ascending (receiver)

    def encapsulate(self, layer_name):
        """
        Simulates the encapsulation process at a specific OSI layer.
        In networking, each layer adds its own control information (header) to the data
        received from the layer above. This method mimics that by prepending a
        bracketed layer name to the current payload string.

        Args:
            layer_name (str): The name of the OSI layer currently processing the packet.

        Returns:
            str: The updated payload containing the new header.
        """
        header = f"[{layer_name}_Header]"
        self.headers.append(header)
        self.payload = f"{header} {self.payload}"
        return self.payload

    def decapsulate(self):
        """
        Simulates the decapsulation process at the receiver side.
        As a packet moves up the stack, each layer removes the header intended for it.
        This method identifies and removes the most recently added header from the
        payload string, effectively reversing the encapsulation process.

        Returns:
            str: The header that was removed, or None if no headers remain.
        """
        if self.headers:
            header = self.headers.pop()
            # We use replace with count=1 to ensure we only remove the outermost header
            # matching the current layer's expectation, preserving the rest of the payload.
            self.payload = self.payload.replace(header + " ", "", 1)
            return header
        return None

    def get_full_packet(self):
        """
        Returns the current state of the packet, including all active headers.

        Returns:
            str: The fully or partially encapsulated/decapsulated payload.
        """
        return self.payload

    def reset(self):
        """
        Resets the packet to its initial state.
        This is used when the simulation is restarted, clearing all headers
        and restoring the payload to the original user-provided data.
        """
        self.payload = self.original_data
        self.headers = []
        self.current_layer_index = 0
        self.is_encapsulating = True
