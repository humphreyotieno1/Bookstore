# BOOKSTORE
## Author
Humphrey Otieno - `humphryotieno04@gmail.com`

Welcome to the Bookstore. This system provides a comprehensive solution for managing library resources efficiently. 

## Table of Contents
- Introduction
- Requirements
- Features
- Installation
- Usage

## Introduction
The Bookstore is a Python-based application designed to simplify the management of books, authors, and courses in a library setting. It offers a user-friendly interface for librarians or administrators to perform various tasks such as adding new books, viewing existing books, deleting books, managing authors, and managing courses.

## Requirements
### ORM Requirements
- The application includes a database created and managed using Python ORM methods.
- The data model encompasses at least 2 model classes, representing entities such as books, authors, and courses.
- It establishes at least 1 one-to-many relationship between the model classes.
- Property methods are implemented to enforce constraints and maintain data integrity within each model class.
- ORM methods, including create, delete, get all, and find by id, are provided for each model class.

### CLI Requirements
- The CLI presents user-friendly menus for interacting with the application's functionalities.
- Utilizing loops, the CLI ensures seamless navigation within the application until the user chooses to exit.
- For each entity in the data model (books, authors, courses), the CLI offers options to create, delete, display all, view related entities, and find by attribute.
- User input and object manipulations are validated to provide informative error messages and enhance user experience.
- The project adheres to OOP best practices, with organized folder structures, proper naming conventions, and minimal imports.

## Features
1. Book Management
    - Add New Books: Easily add new books to the system by providing details such as title, publication year, cost, author, and course.
    - View Books: View a list of all books stored in the system, along with their details.
    - Delete Books: Remove books from the system, along with associated authors and courses.
2. Author Management
    - Add New Authors: Add new authors to the system by providing their first name and last name.
    - View Authors: View a list of all authors stored in the system.
    - Delete Authors: Remove authors from the system. Deleting an author also deletes any books associated with them.
3. Course Management
    - Add New Courses: Add new courses to the system by providing the course name.
    - View Courses: View a list of all courses stored in the system.
    - Delete Courses: Remove courses from the system. Deleting a course also deletes any books associated with it.

## Installation
1. Clone the repository

    `git clone https://github.com/humphreyotieno1/Bookstore.git`

2. Navigate to the project directory:
    
    `cd Bookstore`

3. Install the required dependencies:

4. Set up the database by running the provided SQL script (database_setup.sql). Run the main program:

    `python3 main.py`

5. Run the Command Line Interface and follow the prompts to perform various actions such as adding, viewing, or deleting books, authors, and courses.

    `python3 cli.py`
