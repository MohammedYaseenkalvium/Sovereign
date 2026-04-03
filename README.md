# Sovereign — DAO Governance for Student Clubs

## 🚀 Overview

Sovereign is a decentralized governance platform designed to bring transparency, accountability, and efficiency to student clubs. It enables members to create proposals, vote democratically, and automatically determine outcomes based on collective decisions.

---

## 🎯 Problem

Student clubs often rely on centralized decision-making, leading to:

* Lack of transparency
* Biased decisions
* Poor member participation

---

## 💡 Solution

Sovereign introduces a DAO-inspired system where:

* Every member has a voice
* Decisions are made through voting
* Outcomes are transparent and automated

---

## 🧩 Core Features

* 🗳️ Proposal creation and management
* ✅ One-member-one-vote system
* 📊 Real-time voting results
* ⏳ Proposal deadlines and status tracking (Active, Passed, Failed)
* 👥 Role-based access (Admin, Member)
* 📱 Clean and intuitive dashboard UI

---

## 🏗️ Architecture

Frontend and backend are separated for scalability:

```
Frontend (Flutter)
        ↓
Django REST API
        ↓
Database (SQLite/PostgreSQL)
```

---

## 🛠️ Tech Stack

### Backend

* Django
* Django REST Framework
* SQLite (development) → PostgreSQL (production)

### Frontend

* Typescript with next.js

### DevOps (Planned)

* Docker
* GitHub Actions (CI/CD)
* Cloud Deployment (AWS / Azure)

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sovereign-dao.git
cd sovereign-dao
```

---

### 2. Backend Setup

```bash
cd backend
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000/
```

---

### 3. Frontend Setup (Flutter)

```bash
cd frontend
flutter pub get
flutter run
```

---

## 🔌 API Endpoints (Core)

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | /api/proposals/  | Create proposal   |
| GET    | /api/proposals/  | Get all proposals |
| POST   | /api/vote/       | Cast vote         |
| GET    | /api/results/:id | Get results       |

---

## 📌 Future Improvements

* 🔐 Authentication & JWT-based security
* ⚡ Real-time voting updates (WebSockets)
* 🪙 Token-based voting system
* 🔔 Notifications for active proposals
* 🌐 Blockchain integration (advanced)

---

## 🧠 Key Highlights

* Built with a focus on real-world governance systems
* Designed for scalability and transparency
* Follows modern full-stack architecture (API + client separation)

---

## 👥 Team

* Muhammad
* (Add your teammates)

---

## 📜 License

This project is for educational and development purposes.

---

## ⭐ Final Note

Sovereign is not just a project — it is a step toward building transparent and democratic systems using modern technology.
