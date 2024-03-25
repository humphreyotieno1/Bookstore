from helper import add_book, delete_book, delete_course, delete_author, display_all_books, exit_program

def main():
    print("Welcome to the Library Management System!")
    while True:
        print("\n1. Add a book\n2. View all books\n3. Delete a book\n4. Delete a course\n5. Delete an author\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            display_all_books()
        elif choice == "3":
            book_id = input("Enter the ID of the book you want to delete: ")
            delete_book(book_id)
        elif choice == "4":
            course_id = input("Enter the ID of the course you want to delete: ")
            delete_course(course_id)
        elif choice == "5":
            author_id = input("Enter the ID of the author you want to delete: ")
            delete_author(author_id)
        elif choice == "6":
            exit_program()
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()