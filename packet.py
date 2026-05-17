class Packet:
    """
    Represents a data packet traveling through the OSI model.
    Handles encapsulation (adding headers) and decapsulation (removing headers).
    """
    def __init__(self, data="Hello, Network!"):
        self.original_data = data
        self.payload = data
        self.headers = []  # Stack for encapsulation
        self.current_layer_index = 0
        self.is_encapsulating = True  # True for sender (down), False for receiver (up)

    def encapsulate(self, layer_name):
        """Adds a header for the given layer."""
        header = f"[{layer_name}_Header]"
        self.headers.append(header)
        self.payload = f"{header} {self.payload}"
        return self.payload

    def decapsulate(self):
        """Removes the top-most header."""
        if self.headers:
            header = self.headers.pop()
            # Remove the header from the payload string
            # This is a simplified visual representation
            self.payload = self.payload.replace(header + " ", "", 1)
            return header
        return None

    def get_full_packet(self):
        return self.payload

    def reset(self):
        self.payload = self.original_data
        self.headers = []
        self.current_layer_index = 0
        self.is_encapsulating = True
