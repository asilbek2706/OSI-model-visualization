"""
Layers Module: OSI Model Metadata and Educational Content
This module acts as the centralized data repository for the OSI Model Visualization Tool.
It defines the characteristics of each of the seven layers of the Open Systems
Interconnection (OSI) model, including their hierarchical order, functional
descriptions, and Protocol Data Unit (PDU) nomenclature.

The metadata defined here is used by the UI to populate information panels and
by the simulation logic to manage the sequence of encapsulation and decapsulation.
"""

OSI_LAYERS = [
    {
        "name": "Application",
        "number": 7,
        "description": "Layer 7 is the topmost layer, providing network services directly to end-user applications. It is responsible for identifying communication partners, determining resource availability, and synchronizing communication. Common protocols include HTTP for web browsing, SMTP for email, and FTP for file transfers.",
        "pdu": "Data"
    },
    {
        "name": "Presentation",
        "number": 6,
        "description": "Layer 6 ensures that data is in a usable format and is where data encryption, decryption, and compression occur. It acts as a translator between the application layer and the rest of the network, transforming data into a standardized format like JSON, XML, or binary encoded formats like JPEG and GIF.",
        "pdu": "Data"
    },
    {
        "name": "Session",
        "number": 5,
        "description": "Layer 5 is responsible for opening, closing, and managing a session between end-user application processes. it handles authentication and reconnection. Protocols like NetBIOS and RPC operate at this layer to manage the 'dialogue' between two computers, ensuring that the connection stays open while data is being transferred.",
        "pdu": "Data"
    },
    {
        "name": "Transport",
        "number": 4,
        "description": "Layer 4 manages end-to-end communication, providing mechanisms for error recovery and flow control. It breaks large data into smaller 'Segments'. TCP (Transmission Control Protocol) provides reliable, connection-oriented delivery, while UDP (User Datagram Protocol) provides faster but unreliable connectionless delivery.",
        "pdu": "Segment"
    },
    {
        "name": "Network",
        "number": 3,
        "description": "Layer 3 handles logical addressing and the routing of 'Packets' between different networks. It determines the best physical path for the data to take. The Internet Protocol (IP) is the primary protocol at this layer, using IP addresses to identify source and destination hosts across a complex web of routers.",
        "pdu": "Packet"
    },
    {
        "name": "Data Link",
        "number": 2,
        "description": "Layer 2 provides node-to-node data transfer—a link between two directly connected nodes. It handles physical addressing (MAC addresses) and error detection. Data is organized into 'Frames'. Ethernet is the most common protocol here, ensuring that data is correctly formatted for the physical medium and checking for collisions.",
        "pdu": "Frame"
    },
    {
        "name": "Physical",
        "number": 1,
        "description": "Layer 1 is the lowest layer, dealing with the actual physical connection between devices. It defines the electrical, mechanical, and procedural specifications for transmitting raw 'Bits' over a physical medium like copper cables, fiber optics, or radio waves (Wi-Fi). It includes hardware like hubs, repeaters, and cables.",
        "pdu": "Bit"
    }
]

# Layer list in order of sender (Top-down: 7 to 1)
SENDER_LAYERS = OSI_LAYERS

# Layer list in order of receiver (Bottom-up: 1 to 7)
RECEIVER_LAYERS = list(reversed(OSI_LAYERS))
