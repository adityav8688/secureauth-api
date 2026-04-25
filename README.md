# 🔐 SecureAuth API

A JWT-based authentication backend built with **FastAPI** and **PostgreSQL**. Handles user registration, login, and token-based access control — designed to be modular and reusable across any project.

---

## 🚀 Features

- User registration & login
- JWT token generation with 24-hour expiry
- Password hashing for secure storage
- Protected route middleware
- Clean modular structure (models, schemas, auth, routes)
- Auto table creation on startup via SQLAlchemy

---

## 🗂️ Project Structure

```
secureauth-api/
├── main.py          # App entry point, router registration, DB init
├── auth.py          # JWT token creation logic
├── securities.py    # Password hashing & token verification
├── user.py          # User route handlers (register, login)
├── models.py        # SQLAlchemy DB models
├── schemas.py       # Pydantic request/response schemas
└── database.py      # DB engine & session setup
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/adityav8688/secureauth-api.git
cd secureauth-api
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose passlib[bcrypt]
```

### 4. Configure the database
Update the database URL in `database.py`:
```python
DATABASE_URL = "postgresql://username:password@localhost/dbname"
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

The API will be live at `http://127.0.0.1:8000`

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT token |

---

## 🔑 How JWT Works Here

- On login, a JWT token is generated with a **24-hour expiry**
- Token is signed using `HS256` algorithm with a secret key
- Protected routes validate the token before granting access

---

## 📌 Notes

- Make sure PostgreSQL is running before starting the server
- Tables are auto-created on app startup — no manual migration needed
- Replace `SECRET_KEY` in `auth.py` with a strong, environment-based secret before deploying

---

## 👤 Author

**Vegulla Aditya**
📧 adityavegulla@gmail.com
🔗 [GitHub](https://github.com/adityav8688)