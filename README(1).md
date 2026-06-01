# 🎨 Collaborative Whiteboard Backend

> A real-time collaborative whiteboard and chat backend built with **FastAPI**, **WebSockets**, **Redis Pub/Sub**, **PostgreSQL**, **JWT Authentication**, and **Docker**.

---

## ✨ Features

### 🔐 Authentication
- User Signup & Login
- JWT-based Authentication
- Protected WebSocket Connections

### 💬 Real-Time Communication
- Public Room Chat
- Private Messaging
- Typing Indicators
- Online User Presence
- WebSocket-Based Communication

### 🖌️ Collaborative Whiteboard
- Real-Time Drawing Events
- Room-Based Collaboration
- Drawing History Persistence
- Board State Recovery

### 📈 Scalability
- Redis Pub/Sub Integration
- Multi-Instance Ready Architecture
- Event Broadcasting

### 🗄️ Database
- PostgreSQL with SQLAlchemy ORM
- Persistent Chat Messages
- Persistent Whiteboard Events

### 🐳 Infrastructure
- Docker & Docker Compose
- Environment Variable Configuration

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Real-Time | WebSockets |
| Database | PostgreSQL |
| Cache / Pub-Sub | Redis |
| ORM | SQLAlchemy |
| Auth | JWT |
| Containerization | Docker |

---

## 📁 Project Structure

```
app/
├── database/
├── models/
├── routes/
├── schemas/
├── services/
├── websocket/
│   ├── handler/
│   ├── redis/
│   ├── schemas/
│   └── manager.py
├── core/
├── main.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/whiteboard
REDIS_URL=redis://redis:6379
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 🚀 Running Locally

### 1. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL

```bash
docker compose up postgres
```

### 4. Start Redis

```bash
docker compose up redis
```

### 5. Run Application

```bash
uvicorn main:app --reload
```

---

## 🐳 Running with Docker

```bash
docker compose up --build
```

| Service | URL |
|---|---|
| Application | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |

---

## 🔌 WebSocket Connection

```
ws://localhost:8000/ws/{room}?token=JWT_TOKEN
```

**Example:**

```
ws://localhost:8000/ws/main?token=YOUR_TOKEN
```

---

## 📨 Supported Events

### Chat Message
```json
{
  "type": "message",
  "message": "Hello World"
}
```

### Typing Indicator
```json
{ "type": "typing" }
```

### Stop Typing
```json
{ "type": "stop_typing" }
```

### Private Message
```json
{
  "type": "private_message",
  "to": "username",
  "message": "Hello"
}
```

### Drawing Event
```json
{
  "type": "draw",
  "x1": 100,
  "y1": 100,
  "x2": 150,
  "y2": 150,
  "color": "black",
  "size": 2
}
```

---

## 🏗️ Architecture

```
Client
   │
   ▼
WebSocket
   │
   ▼
FastAPI
   │
   ├── PostgreSQL (Persistence)
   │
   └── Redis Pub/Sub
            │
            ▼
      Connected Clients
```

---

## 🔮 Future Improvements

- [ ] Cursor Tracking
- [ ] Undo / Redo
- [ ] Shape Tools
- [ ] Infinite Canvas
- [ ] File Uploads
- [ ] User Roles & Board Permissions
- [ ] Kubernetes Deployment

---

## 👤 Author

**Krishna Sharma**

Built for learning scalable real-time backend systems using FastAPI, Redis, PostgreSQL, Docker, and WebSockets.
