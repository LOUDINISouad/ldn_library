# ldn_library

## Overview

ldn_library is a Django-based web application designed to manage a library system. It provides functionalities for adding books, deleting books, inserting users, and borrowing books.

## Features

- **Add Book**: Users can add books to the library database by providing the title, author, and other relevant information.
- **Delete Book**: Users with appropriate permissions can delete books from the library database based on the book's ID.
- **Insert User**: Users can be added to the system by providing their first name, last name, and email address.
- **Borrow Book**: Users can borrow books from the library by specifying the book ID and user ID.

## Installation

1. Clone the repository:
    ```bash
    git clone [repository-url](https://github.com/LOUDINISouad/ldn_library)
    cd ldn_library
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # Linux/Mac
    # Or
    .\venv\Scripts\activate  # Windows
    ```


3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```
     ### Usage

### Accessing the Application

- You can access the application's web interface by opening your web browser and navigating to [http://localhost:8000/MyLibrary/](http://localhost:8000/MyLibrary/).
  
### Interacting with the API using Postman

- Alternatively, you can use Postman to interact with the application's API endpoints directly.
- Postman allows you to send HTTP requests to the API endpoints and view the responses.
- Here's how you can use Postman to interact with the API endpoints:
  1. Open Postman.
  2. Create a new request.
  3. Set the request type (GET, POST, DELETE, etc.).
  4. Enter the URL for the desired API endpoint (e.g., `http://localhost:8000/MyLibrary/books`).
  5. Send the request and view the response.
  
## API Endpoints

- **Add Book**: `POST /MyLibrary/books`
- **Delete Book**: `DELETE /MyLibrary/books/<book_id>`
- **Insert User**: `POST /MyLibrary/users`
- **Borrow Book**: `POST /MyLibrary/borrow_book/<book_id>/<user_id>`



    




