# Scam Detection Backend

This is a FastAPI-based backend for detecting and explaining scam messages using AI.

## Features
- **Scam Classification**: Uses a Hugging Face model to detect scam messages.
- **Scam Explanation**: Uses OpenAI GPT to explain why a message is a scam.
- **User Q&A**: Allows users to ask follow-up questions about scam messages.
- **Caching with Redis**: Optimizes performance by storing explanations in Redis.

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/scam-detection.git
cd scam-detection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables
Create a **`.env`** file in the project root with the following content:

```
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost/scamdb

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379

# API Keys
OPENAI_API_KEY=your_openai_api_key

# Hugging Face Model
HUGGINGFACE_MODEL=ml6team/roberta-base-cls-phishing

# Model Cache Directory (Optional - Uncomment to use local storage)
# HF_CACHE_DIR=./models/
```
Modify this file according to your environment.

---

## 🛠 Starting Services

### ✅ 1. Start Redis
Redis is required for caching AI-generated scam explanations.

#### **Option 1: Start Redis Locally**
```bash
redis-server
```
Verify Redis is running:
```bash
redis-cli ping
```
Expected output:
```
PONG
```

---

### ✅ 2. Apply Database Migrations
Ensure PostgreSQL is running, then apply migrations:
```bash
alembic upgrade head
```

---

### ✅ 3. Start FastAPI Backend
```bash
uvicorn main:app --reload
```

---

## 🧪 Running Tests

```bash
pytest app/tests/
```

---

## 🔧 Configuration Parameters Explained
| **Parameter** | **Description** |
|-------------|----------------|
| `DATABASE_URL` | PostgreSQL connection string. |
| `REDIS_HOST` | Hostname for Redis server. |
| `REDIS_PORT` | Port for Redis server (default: 6379). |
| `OPENAI_API_KEY` | API key for OpenAI GPT. |
| `HUGGINGFACE_MODEL` | Model name for scam classification. |
| `HF_CACHE_DIR` | Optional: Directory for Hugging Face model cache. |

---

## 🏗 Future Enhancements
- ✅ **Self-hosted AI model**: Replace OpenAI API with LLaMA/Mistral for explanations.
- ✅ **Browser extension**: Real-time phishing detection.
- ✅ **Mobile notifications**: Push alerts for scam detection.

---

## 📜 License
This project is licensed under the MIT License.

---

docker-compose build
docker-compose up -d
