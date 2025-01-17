from models.course import Course
from models.author import Author
from models.book import Book
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_author(author_id):
    author = Author.find_by_id(author_id)
    if not author:
        print("Author not found.")
        return None
    return author

def validate_course(course_id, course_name):
    course = Course.find_by_id(course_id)
    if not course:
        new_course = Course(course_name)
        new_course.create()
        return new_course
    return course

def add_book():
    title = input("Enter the title of the book: ")
    year = int(input("Enter the year of publication: "))
    cost = float(input("Enter the cost of the book: "))
    first_name = input("Enter the author's first name: ")
    last_name = input("Enter the author's last name: ")
    course_id = int(input("Enter the course ID of the book: "))
    course_name = input("Enter the course name: ")
    author_id = input("Enter the author ID of the book: ")
        
    existing_author = Author.find_by_id(author_id)
    if existing_author:
        author_id = existing_author[0]
    else:
        new_author = Author(first_name, last_name)
        new_author.create()
        author_id = new_author.find_by_id(author_id)[0]

    existing_course = Course.find_by_id(course_id)
    if not existing_course:
        new_course = Course(course_name)
        new_course.create()

    new_book = Book(title, year, cost, author_id, course_id)
    new_book.create()
    print("Book added successfully.")

def delete_book(book_id):
    book = Book.find_by_id(book_id)
    if book:
        Book.delete(book_id)
        print("Book deleted successfully.")
    else:
        print("Book not found. Please enter a valid book ID.")

def delete_author(author_id):
    author = Author.find_by_id(author_id)
    if author:
        Author.delete(author_id)
        print("Author deleted successfully.")
    else:
        print("Author not found.")

def delete_course(course_id):
    course = Course.find_by_id(course_id)
    if course:
        Course.delete(course_id)
        print("Course deleted successfully.")
    else:
        print("Course not found.")

def display_all_books():
    books = Book.get_all()
    if books:
        print("All Books:")
        print("{:<30} {:<8} {:<8} {:<14} {:<30}".format("Title", "Year", "Cost", "Author ID", "Course ID"))
        for book in books:
            print("{:<30} {:<8} {:<8} {:<12} {:<30}".format(book[1], book[2], book[3], book[4], book[5]))
    else:
        print("No books found.")

        
def find_author_by_id(author_id):
    author = Author.find_by_id(author_id)
    if author:
        print("Author found:")
        print("{:<5} {:<15} {:<15}".format("ID", "First Name", "Last Name"))
        print("{:<5} {:<15} {:<15}".format(author[0], author[1], author[2]))
    else:
        print("Author not found.")

def find_course_by_id(course_id):
    course = Course.find_by_id(course_id)
    if course:
        print("Course found:")
        print("{:<5} {:<20}".format("ID", "Name"))
        print("{:<5} {:<20}".format(course[0], course[1]))
    else:
        print("Course not found.")

def find_book_by_id(book_id):
    book = Book.find_by_id(book_id)
    if book:
        print("Book found:")
        print("{:<5} {:<20} {:<10} {:<10} {:<10} {:<10}".format("ID", "Title", "Year", "Cost", "Author ID", "Course ID"))
        print("{:<5} {:<20} {:<10} {:<10} {:<10} {:<10}".format(book[0], book[1], book[2], book[3], book[4], book[5]))
    else:
        print("Book not found.")

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()
