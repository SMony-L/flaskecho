# Flask Echo Server

## Overview

Simple Echo Flask

## Requirements

- Python 3.x
- Flask

## Installation

Clone the repository and install the required packages using the following commands:

```bash
git clone git@github.com:SMony-L/flaskecho.git
cd flaskecho
pip3 install -r requirements.txt
```

## Running the App
```
python3 app.py
```

The server will be available at http://127.0.0.1:5000/.

## Usage
To get a greeting from the server, send a GET request to the /echo endpoint:

```
curl http://127.0.0.1:5000/echo
```

You will receive a response: "Hello from Flask Echo Server".

## Docker Support
Building the Docker Image
```
docker build -t flaskecho:0.0.1 .
```

Running the Container
```
docker run -d -p 5000:5000 flaskecho:latest
```
The application will be accessible at http://localhost:5000/echo
