from models.book import Book
from models.author import Author
from models.course import Course
from database import myTables

def instances():
    myTables()
    print("Welcome to the Library Management System!")
    
    author1 = Author("F. Scott", "Fitzgerald")
    author2 = Author("Harper", "Lee")
    author1.create()
    author2.create()

    course1 = Course("English Literature")
    course2 = Course("American Literature")
    course1.create()
    course2.create()
    
    book1 = Book("The Great Gatsby", 1925, 20, 1, 1)
    book2 = Book("To Kill a Mockingbird", 1960, 25, 2, 1)
    book1.create()
    book2.create()

    print("Test instances created successfully.")

if __name__ == "__main__":
    instances()
