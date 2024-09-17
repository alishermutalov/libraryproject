# Library Project

## Overview

The Library Project is a Django-based application that provides a RESTful API for managing books. It includes functionalities for creating, reading, updating, and deleting books, as well as user authentication using DJ-Rest-Auth.

## Features

- **Book Management**: CRUD operations for books.
- **User Authentication**: Registration and login functionality.
- **REST API**: Built using Django REST Framework.
- **PostgreSQL Integration**: For database management.
- **Gunicorn**: For serving the application in a production environment.

## Technologies Used

- **Django**: 5.1.1
- **Django REST Framework**: 3.15.2
- **DJ-Rest-Auth**: 6.0.0
- **django-allauth**: 64.2.1
- **psycopg2-binary**: 2.9.9 (PostgreSQL adapter)
- **Gunicorn**: 23.0.0 (WSGI HTTP server)
- **Pipenv**: 2024.0.2 (For package management)

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Create and activate a virtual environment**

    ```bash
    pipenv install
    pipenv shell

3. **Apply migrations**

    ```bash
    python manage.py migrate

4. **Create a superuser**

    ```bash
    python manage.py createsuperuser

5. **Run the development server**

    ```bash
      python manage.py runserver

**Configuration**

Update the DATABASES settings in settings.py to match your PostgreSQL configuration.

    python
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '<database-name>',
            'USER': '<database-user>',
            'PASSWORD': '<database-password>',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

Replace <database-name>, <database-user>, and <database-password> with your actual PostgreSQL database credentials.
**API Endpoints**
**Books**

    List Books
        Endpoint: GET /api/v01/
        Description: Retrieves a list of books.

    Create Book
        Endpoint: POST /api/v01/book/create/
        Description: Creates a new book.

    Book Detail
        Endpoint: GET /api/v01/detail/<slug:slug>/
        Description: Retrieves details of a specific book by its slug.

    Delete Book
        Endpoint: DELETE /api/v01/delete/<slug:slug>/
        Description: Deletes a book by its slug.

    Update Book
        Endpoint: PUT /api/v01/update/<slug:slug>/
        Description: Updates details of a book by its slug.

Authentication

    Login
        Endpoint: POST /api/v01/dj-rest-auth/login/
        Description: Authenticates a user and returns a token.

    Logout
        Endpoint: POST /api/v01/dj-rest-auth/logout/
        Description: Logs out a user and invalidates the token.

    Registration
        Endpoint: POST /api/v01/dj-rest-auth/registration/
        Description: Registers a new user.

Project Structure

    libraryproject/: Contains Django project settings and URL configurations.
    books/: Django app for handling book-related views and endpoints.
    books/urls.py: URL routing for book-related API endpoints.
    libraryproject/urls.py: URL routing for the entire project.
