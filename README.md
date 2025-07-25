# GzPharma API

This is the backend API for the GzPharma application, a platform for managing pharmaceutical items.

## Technologies Used

*   **Backend:** Django, Django REST Framework
*   **Database:** PostgreSQL
*   **Authentication:** Token Authentication
*   **API Documentation:** drf-yasg (Swagger)
*   **Containerization:** Docker, Docker Compose
*   **Web Server:** Gunicorn
*   **Other Libraries:**
    *   `django-filter` for filtering querysets.
    *   `django-cors-headers` for handling Cross-Origin Resource Sharing (CORS).
    *   `Pillow` for image handling.

## Setup and Installation

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

*   Python 3.x
*   PostgreSQL
*   Docker and Docker Compose (for containerized setup)

### 1. Clone the repository

```bash
git clone <repository-url>
cd gzpharma
```

### 2. Set up Environment Variables

Create a `.env` file in the root directory of the project. Copy the contents below and replace the placeholder values with your actual configuration.

```
SECRET_KEY='your-super-secret-key'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
DATABASE_URL='psql://your_db_user:your_db_password@localhost:5432/gzpharma'
STATIC_URL='/static/'
STATIC_ROOT='/path/to/your/project/staticfiles'
MEDIA_URL='/media/'
MEDIA_ROOT='/path/to/your/project/mediafiles'
```

### 3. Install Dependencies

It is recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

## Running with Docker

Alternatively, you can run the application using Docker Compose.

1.  Make sure you have created the `.env` file as described above. The `DATABASE_URL` should point to the database service in `docker-compose.yml`.

    ```
    DATABASE_URL='psql://user:password@db:5432/gzpharma'
    ```

2.  Build and run the containers.

    ```bash
    docker-compose up --build -d
    ```

The application will be available at `http://localhost:8000`.

## API Documentation

Once the server is running, you can access the Swagger API documentation at:

-   `http://127.0.0.1:8000/swagger/`

## Project Structure

-   `gzpharma/`: Main Django project configuration.
-   `item/`: Django app for managing pharmaceutical items.
-   `users/`: Django app for user management and authentication.
-   `infrastructure/`: Contains configuration for services like Nginx.
-   `init-scripts/`: SQL scripts for database initialization.
-   `Dockerfile`: Defines the Docker image for the application.
-   `docker-compose.yml`: Defines the services, networks, and volumes for the Docker application.

## System Functionality

The GzPharma API is a **Pharmaceutical Item Management System** that serves as the backend for an application designed to track and manage pharmaceutical products.

### Core Features:

#### User Management
The system provides a complete user authentication and management system with the following capabilities:

- **User Registration:** New users can create an account by providing their first name, last name, and a unique email address.
- **User Login:** Registered users can log in to obtain an authentication token, which is required to access protected API endpoints.
- **Profile Management:** Logged-in users can view and update their own profile information.
- **Password Reset:** Users can securely reset their passwords.
- **Admin Interface:** The Django admin panel is configured for comprehensive user management, including permissions and staff status.

#### Pharmaceutical Item Management
This is the central feature of the application, allowing for the management of pharmaceutical items through a RESTful API. Key functionalities include:

- **Create, Read, Update, Delete (CRUD):** A full set of CRUD operations for managing items, including their name, price, and discount.
- **Bulk Deletion:** An endpoint is available to delete all items from the database at once.
- **Filtering and Searching:** The API supports filtering items based on their attributes, allowing for efficient data retrieval.
- **Data Association:** Items are associated with a `sheetName`, which can be used to group or categorize products. 