from helper import add_book, delete_book, delete_course, delete_author, display_all_books, find_author_by_id, find_course_by_id, find_book_by_id

def main():
    print("Welcome to the Bookstore")
    while True:
        print("\n1. Add a book\n2. View all books\n3. Delete a book\n4. Find a book by ID\n5. Delete a course\n6. Find a course by ID\n7. Delete an author\n8. Find an author by ID\n9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            display_all_books()
        elif choice == "3":
            book_id = input("Enter the ID of the book you want to delete: ")
            delete_book(book_id)
        elif choice == "4":
            book_id = input("Enter the ID of the book you want to find: ")
            find_book_by_id(book_id)
        elif choice == "5":
            course_id = input("Enter the ID of the course you want to delete: ")
            delete_course(course_id)
        elif choice == "6":
            course_id = input("Enter the ID of the course you want to find: ")
            find_course_by_id(course_id)
        elif choice == "7":
            author_id = input("Enter the ID of the author you want to delete: ")
            delete_author(author_id)
        elif choice == "8":
            author_id = input("Enter the ID of the author you want to find: ")
            find_author_by_id(author_id)
        elif choice == "9":
            exit_program()
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

if __name__ == "__main__":
    main()
