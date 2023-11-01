# Personal Library Project

## Description
This is a personal project to track books I've read, complete with titles, authors, summaries, and personal ratings. The application, built with Django, allows for adding, updating, and deleting books in my reading list. It features a search functionality that lets me find books by title, author, minimum rating, or publication date.

Additionally, a simple Django REST framework API with CRUD functionalities underpins the app, allowing for straightforward data management and potential future integration with other applications or personal projects.

## Features:
- Book Management: User can add, update, delete, and search books in the list
- Simple Django REST API with CRUD operations.

## Technology Stack:
- Back-End: Django, Django Rest Framework, Python.
- Front-End: HTML, CSS.
- Version Control: Git, GitHub.

## Installation:
Clone the repository

```commandline
git clone https://github.com/quynhnle135/django-library-project.git
```

Navigate to the project

```commandline
cd django-library-project
```

Set up a virtual environment

```commandline
# Install virtualenv if it's not installed
python -m pip install virtualenv

# Create a virtual environment in the project directory
python -m venv env

# Activate the virtual environment
source env/bin/activate  # On Windows, use "env\Scripts\activate"
```

Install project dependencies

```commandline
pip install requirements.txt
```

Run the development server

```commandline
python3 manage.py runserver
```

## Screenshots of Library features
Book list before adding any book to it
![(1) book-list-before.png](screenshots%2F%281%29%20book-list-before.png)

Add new book
![(2) add-book.png](screenshots%2F%282%29%20add-book.png)

Book list after adding several books
![(3)after-adding-books.png](screenshots%2F%283%29after-adding-books.png)

Search books by title
![(4) search-book-by-title.png](screenshots%2F%284%29%20search-book-by-title.png)

Search books by author
![(5) search-book-by-author.png](screenshots%2F%285%29%20search-book-by-author.png)

Search books by rating
![(6) search-book-by-rating.png](screenshots%2F%286%29%20search-book-by-rating.png)

Book detail
![(7) book-detail.png](screenshots%2F%287%29%20book-detail.png)

## Screenshots of Library API features

View all books in the list
![(9) book-list.png](screenshots%2F%289%29%20book-list.png)

Add new book
![(8) add-book.png](screenshots%2F%288%29%20add-book.png)

View book's detail, delete, and update
![(10) book-detail.png](screenshots%2F%2810%29%20book-detail.png)