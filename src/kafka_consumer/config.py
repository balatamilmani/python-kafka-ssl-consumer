from pathlib import Path
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

def find_project_root(marker: str = ".project-root") -> Path:
    """Search upward for a marker file to find the project root."""
    current = Path(__file__).absolute()
    while not (current / marker).exists():
        if current.parent == current:  # Reached filesystem root
            raise FileNotFoundError(f"Marker file '{marker}' not found in any parent directory.")
        current = current.parent
    return current

PROJECT_ROOT = find_project_root()

class KafkaSSLConfig:
    KAFKA_BROKER = os.getenv("KAFKA_BROKER")
    TOPIC = os.getenv("KAFKA_TOPIC")
    GROUP_ID = os.getenv("KAFKA_GROUP_ID")
    KAFKA_CLIENT_ID = os.getenv("KAFKA_CLIENT_ID")
    
    # SSL Paths (adjust based on your cert locations)
    SSL_CAFILE = PROJECT_ROOT / "ssl-certificates" / "ca-cert.pem"
    SSL_CERTFILE = PROJECT_ROOT / "ssl-certificates" / "client-cert.pem"
    SSL_KEYFILE = PROJECT_ROOT / "ssl-certificates" / "client-key.pem"
