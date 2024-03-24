from models.course import Course
from models.author import Author
from models.book import Book

def main():
    print("Welcome to the Library Management System!")
    while True:
        print("\n1. Add a book\n2. View all books\n3. Delete a book\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            display_all_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            exit_program()
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

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
        author_id = new_author.find_by_id(first_name, last_name)[0]

    existing_course = Course.find_by_id(course_id)
    if not existing_course:
        new_course = Course(course_name)
        new_course.create()

    new_book = Book(title, year, cost, author_id, course_id)
    new_book.create()
    print("Book added successfully.")

def delete_book():
    book_id = input("Enter the ID of the book you want to delete: ")
    book = Book.find_by_id(book_id)
    if book:
        author_id = book.author_id
        book.delete()
        author = Author.find_by_id(author_id)
        if author:
            author.delete()
            print("Book and associated author deleted successfully.")
        else:
            print("Author not found.")
    else:
        print("Book not found. Please enter a valid book ID.")


def display_all_books():
    books = Book.get_all()
    if books:
        print("All Books:")
        for book in books:
            print(book)
    else:
        print("No books found.")

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

if __name__ == "__main__":
    main()
