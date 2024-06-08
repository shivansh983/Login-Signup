# Social Networking API

This project is a social networking application API built using Django Rest Framework. The API supports functionalities for user login/signup, searching users, sending/accepting/rejecting friend requests, listing friends, and listing pending friend requests.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [Postman API Evaluations](#postman-api-evaluations)
- [API Endpoints](#api-endpoints)

## Requirements

- Python 3.8+
- Django 3.2+
- Django Rest Framework 3.12+
- Docker (for containerization)

## Installation

1. **Clone the repository:**
   git clone https://github.com/yourusername/social-networking-api.git
   cd social-networking-api
   
Create a virtual environment:
python -m venv djangoenv

Activate the virtual environment:

Windows:
.\djangoenv\Scripts\activate

macOS/Linux:
source djangoenv/bin/activate

Install the dependencies:
pip install -r requirements.txt

Run migrations to set up the database:
python manage.py makemigrations
python manage.py migrate

Create a superuser to access the Django admin panel:
python manage.py createsuperuser

Run the server:
python manage.py runserver
Running the Server

After completing the installation steps, you can run the Django development server using the following command:
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to see the application running.

POSTMAN API:
######
