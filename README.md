# Power BI Flask Web Server

A lightweight Flask REST API for collecting sensor data from a Raspberry Pi and exposing it for display in Power BI or any dashboard tool.

## Features

- Receive sensor readings (temperature, humidity, etc.) via HTTP POST
- Password-protected data ingestion
- In-memory storage with UTC timestamps
- Interactive API docs via Swagger UI
- Dockerized and deployed on Render.com
- CI/CD with GitHub Actions

## Tech Stack

- **Python 3.11** + **Flask** + **flask-smorest**
- **Marshmallow** for request validation
- **django-environ** for environment config
- **Gunicorn** as production WSGI server
- **Docker** + **Render.com** for deployment
- **GitHub Actions** for CI/CD

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/receiver` | Submit sensor data (password required) |
| `GET` | `/dashboard` | Retrieve all sensor readings |
| `DELETE` | `/clear` | Clear all readings (password required) |

### Swagger UI

Interactive docs available at `/swagger-ui` when the server is running.

## Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)

### Local Setup

```bash
# Clone the repo
git clone https://github.com/h0pers/power-bi-flask-web-server.git
cd power-bi-flask-web-server

# Install dependencies
uv sync

# Configure environment
cp .env.example .env
# Edit .env and set your RECEIVER_PASSWORD

# Run the server
python main.py
```

Server will be available at `http://localhost:8080`.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `RECEIVER_PASSWORD` | Password for protected endpoints | required |
| `DEBUG` | Enable Flask debug mode | `False` |

## Usage

### Send sensor data (Raspberry Pi)

```bash
curl -X POST http://localhost:8080/receiver \
  -H "Content-Type: application/json" \
  -H "X-Password: your_password" \
  -d '{"temperature": 23.5, "humidity": 61.2}'
```

### Get all readings

```bash
curl http://localhost:8080/dashboard
```

### Clear readings

```bash
curl -X DELETE http://localhost:8080/clear \
  -H "X-Password: your_password"
```

## Deployment

### Docker

```bash
docker build -t power-bi-server .
docker run -p 8080:8080 -e RECEIVER_PASSWORD=yourpassword power-bi-server
```

### Render.com

Deployments are automated via GitHub Actions on every push to `master`.

To set up manually, configure the following GitHub repository secrets:

| Secret | Description |
|--------|-------------|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_ACCESS_TOKEN` | Docker Hub access token |
| `RENDER_DEPLOY_HOOK_URL` | Render deploy hook URL |

> **Note:** Data is stored in memory and resets on every server restart.
