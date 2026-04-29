🎬 Netflix Microservices API

A scalable backend system inspired by Netflix, built using microservices architecture. This project demonstrates API gateway routing, load balancing, and JWT-based authentication using modern backend technologies.

🚀 Project Overview

This project simulates a real-world streaming platform backend by splitting functionality into independent services. It uses an API Gateway to route requests and distribute traffic across multiple service instances, ensuring scalability and reliability.

🧠 Problem Statement

Traditional monolithic applications struggle with:

Handling high traffic efficiently
Scaling specific components independently
Maintaining system reliability
💡 Solution

This project implements a microservices-based architecture where:

Multiple instances of services run independently
Traffic is routed via an API Gateway
Load is balanced automatically
Authentication is handled securely using JWT tokens
🏗️ Architecture
API Gateway: Traefik (Routing + Load Balancing)
Auth Service: FastAPI (JWT Authentication)
Movies Service: FastAPI (Business Logic)
Containerization: Docker & Docker Compose
⚙️ Tech Stack
Python (FastAPI)
Docker & Docker Compose
Traefik (API Gateway)
JWT (Authentication)
REST APIs
📦 Services
1️⃣ Movies Service
Provides movie data
Multiple instances for load balancing

Endpoints:

GET /movies
GET /movies/{id}
GET /health
2️⃣ Auth Service
Handles authentication using JWT

Endpoints:

POST /login
GET /verify
GET /health
🔄 Load Balancing

Traefik distributes incoming requests across multiple movie service instances.

Test:

http://localhost:8088/movies

Refresh multiple times to see different instances responding.

🔐 Authentication (JWT)
Login:
POST /login
Verify Token:
GET /verify
▶️ How to Run the Project
Step 1: Clone repository
git clone https://github.com/YOUR_USERNAME/netflix-microservices.git
cd netflix-microservices
Step 2: Start services
docker compose up --build
🌐 Access Points
API Gateway: http://localhost:8088
Traefik Dashboard: http://localhost:8080
Movies Service (direct):
http://localhost:8002
http://localhost:8003
http://localhost:8004
Auth Service:
http://localhost:8001
🧪 Testing
Check Load Balancing:
http://localhost:8088/movies
JWT Authentication:
Login → get token
Verify → validate token
📌 Key Features
Microservices Architecture
API Gateway Routing
Load Balancing
JWT Authentication
Dockerized Deployment
🚀 Future Improvements
Protect Movies API with JWT
Add database for user management
Implement user registration
Add role-based access control
👩‍💻 Author

Neelima Vemireddy
GitHub: https://github.com/Neelima2023

⭐ Conclusion

This project demonstrates the design and implementation of a scalable backend system using modern microservices practices. It highlights real-world concepts like load balancing, API gateways, and authentication, making it a strong portfolio project for backend and data-related roles.

