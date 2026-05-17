OSI_LAYERS = [
    {
        "name": "Application",
        "number": 7,
        "description": "Provides network services to applications. Examples: HTTP, FTP, SMTP.",
        "pdu": "Data"
    },
    {
        "name": "Presentation",
        "number": 6,
        "description": "Translates, encrypts, and compresses data. Examples: JPEG, GIF, SSL/TLS.",
        "pdu": "Data"
    },
    {
        "name": "Session",
        "number": 5,
        "description": "Manages sessions between applications. Examples: NetBIOS, RPC.",
        "pdu": "Data"
    },
    {
        "name": "Transport",
        "number": 4,
        "description": "Provides end-to-end communication and error recovery. Examples: TCP, UDP.",
        "pdu": "Segment"
    },
    {
        "name": "Network",
        "number": 3,
        "description": "Handles logical addressing and routing. Examples: IP, ICMP.",
        "pdu": "Packet"
    },
    {
        "name": "Data Link",
        "number": 2,
        "description": "Handles physical addressing and error detection on the local link. Examples: Ethernet, MAC.",
        "pdu": "Frame"
    },
    {
        "name": "Physical",
        "number": 1,
        "description": "Transmits raw bit stream over the physical medium. Examples: Cables, Hubs.",
        "pdu": "Bit"
    }
]

# Layer list in order of sender (Top-down)
SENDER_LAYERS = OSI_LAYERS
# Layer list in order of receiver (Bottom-up)
RECEIVER_LAYERS = list(reversed(OSI_LAYERS))
