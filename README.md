# Netflix Microservices API Project

This project is a Netflix-style backend system built using FastAPI and Docker.  
It demonstrates real-world microservices concepts such as API Gateway, Load Balancing, Service Discovery, Security (JWT), and Containerization.

---

## 🚀 Features Implemented

- Movies REST API (Netflix sample data)
- Authentication Service (Login + JWT Token)
- API Gateway using Traefik
- Load Balancing (Multiple Movies Service Instances)
- Service Discovery using Docker + Traefik
- JWT Based Security
- Docker Containerization using Docker Compose

---

## 🛠 Technologies Used

- Python (FastAPI)
- Docker & Docker Compose
- Traefik (API Gateway & Load Balancer)
- JWT Authentication
- REST API Architecture

---

## 📂 Project Structure

netflix-microservices/
│
├── auth-service/
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── movies-service/
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── traefik/
│ └── traefik.yml
│
└── docker-compose.yml


---

## ▶ How To Run The Project

### Step 1: Install Requirements

Make sure you have installed:

- Docker Desktop

### Step 2: Start Project

Open terminal inside the project folder and run:

docker compose up --build

### Step 3: Access Services

| Service | URL |
-------|------
API Gateway | http://localhost:8088
Traefik Dashboard | http://localhost:8080
Auth Swagger UI | http://localhost:8001/docs
Movies Swagger UI | http://localhost:8002/docs

---


## 🔐 Authentication Flow

### Step 1: Login (Get Token)

POST Request:
http://localhost:8088/api/auth/login

Body:

{
"username": "admin",
"password": "admin123"
}


Response:

{
"access_token": "JWT_TOKEN_HERE",
"token_type": "bearer"
}

### Step 2: Access Movies API (Protected)

Use token in header:

Authorization: Bearer YOUR_TOKEN_HERE


GET Request:

http://localhost:8088/api/movies/movies


---

## ⚖ Load Balancing

Multiple Movies service containers are running:

- movies1
- movies2
- movies3

Traefik automatically distributes traffic between them.  
Each response shows which instance handled the request.

Example:

"instance": "movies2"


---

## 🎯 Learning Outcomes

From this project I learned:

- How REST APIs work
- How microservices communicate
- API Gateway implementation
- Load balancing concepts
- JWT authentication and authorization
- Docker containerization
- Production-style backend architecture

---

