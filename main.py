from models.book import Book
from models.author import Author
from models.course import Course

def test_instances():
    # Creating test instances
    book1 = Book("The Great Gatsby", 1925, 20, 1, 1)
    book2 = Book("To Kill a Mockingbird", 1960, 25, 2, 1)

    author1 = Author("F. Scott", "Fitzgerald")
    author2 = Author("Harper", "Lee")

    course1 = Course("English Literature")
    course2 = Course("American Literature")

    # Creating authors and courses
    author1.create()
    author2.create()

    course1.create()
    course2.create()

    # Creating books with the assigned author and course
    book1.create()
    book2.create()

    print("Test instances created successfully.")

if __name__ == "__main__":
    test_instances()