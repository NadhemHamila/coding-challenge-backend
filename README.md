# Coding Challenge backend

## Getting started
1. **Build Docker Image:** `docker build . -t coding-challenge-docker-image -f ./Docker/Dockerfile`
2. **Run Docker Image (Run Backend server):** `docker run -p 5001:5000 coding-challenge-docker-image`

## Running the integration tests

`pytest src/tests/test_integration.py`

## Available endpoints :

- "/add" : This endpoint will be used to add numbers 
- "/sample10" : This endpoint will be used to sample 10 random numbers
