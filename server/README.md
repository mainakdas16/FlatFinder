# 💸 Flat Finder Backend

A backend service built using **FastAPI**, **PostgreSQL**, and **Alembic**, **Docker** designed to let users find their flatmates!

---

## 🏁 Running the backend locally

### 1. Clone the Repository

```bash
git clone https://github.com/mainakdas16/FlatFinder.git
cd FlatFinder/server
```

### 2. Create a `.env` File

Create a `.env` file in the server folder with the following content (replace placeholder values with your own):

```env
POSTGRES_DB=your_database_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=localhost
POSTGRES_HOST_CONTAINER=db
POSTGRES_PORT=5432
```

### 3. Run with Docker Compose

Ensure Docker and Docker Compose are installed, then run:

```bash
docker-compose up --build
```

This will spin up:

- FastAPI app
- PostgreSQL database container
