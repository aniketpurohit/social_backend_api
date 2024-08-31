
# Social Network API

This project is a Django REST Framework-based Social Network API that allows users to register, authenticate, manage profiles, send friend requests, and more. It also includes auto-generated API documentation using `drf-yasg` and can be deployed using Docker.

## Features

- **User Registration and Authentication**
- **Profile Management**
- **Friend Requests**
- **API Documentation** (Swagger and ReDoc)
- **Dockerized Deployment**
- **JWT Authentication** via `djoser`

## Installation

### Prerequisites

- Python 3.8+
- Docker (for containerized deployment)


### 1. Clone the Repository

```sh
git clone https://github.com/aniketpurohit/social_backend_api.git
cd socialnetwork
```

### 2. Install Dependencies
Create a virtual environment and install the required Python packages.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


### 3. Configure Environment Variables
Create a .env file in the root directory of the project to configure environment variables

### 4. migrate and Run server

```
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
```



