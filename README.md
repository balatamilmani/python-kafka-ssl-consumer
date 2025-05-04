## Python based Kafka Consumer using SSL Certificate authentication
This is a sample code in `Python` to build a Kafka consumer application that uses SSL Certificate authentication. 

### Note:
<b> The instructions are for the Unix based environment </b>

## Prerequisites
    Python 3.8+
    Kafka cluster accessible via SSL

### SSL Certificate setup
- Have the CA Certificate (`ca-cert.pem`), Client's SSL Key (`client-key.pem`) and Certificate (`client-cert.pem`) in pem format
- In this sample application the pem files are assumed to be available under `ssl-certificates` directory at the project's root, i.e. `<project-root-dir>/ssl-certificates`

## Python Client Setup
### 1. Clone the repository
    git clone https://github.com/balatamilmani/python-kafka-ssl-consumer.git
    cd python-kafka-ssl-consumer

### 2. Create a virtual environment
    python -m venv .venv

### 3. Activate virtual environment
    source .venv/bin/activate

### 4. Verify Python Environment
    # Check Python path
    which python
    # Alternative check
    python -c "import sys; print(sys.executable)"

    # Expected output: ./python-kafka-ssl-consumer/.venv/bin/python
    # If this shows /usr/bin/python, activation failed! Remove .venv and run the following command
    python -m venv --copies .venv #to avoid symlink



### 5. Install dependencies
    pip install -e ".[dev]"

### 6. Configure Environment
#### 6.1 Copy the environment template:
    cp .env.example .env
#### 6.2 Set the Kafka cluster host and topic info as per your environment.
    # Sample
    KAFKA_BROKER=localhost:9092
    KAFKA_GROUP_ID=student-consumer-group
    KAFKA_TOPIC=student-event
    KAFKA_CLIENT_ID=ssl-student-event-consumer
#### 6.3 Verify the SSL certificates are in place
    ssl-certificates/
    ├── ca-cert.pem         # CA certificate
    ├── client-cert.pem     # Client certificate
    └── client-key.pem      # Client private key       

### 7. Running the Consumer
    python -m src.kafka_consumer.consumer