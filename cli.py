import os
from helper import add_book, delete_book, delete_course, delete_author, display_all_books, find_author_by_id, find_course_by_id, find_book_by_id, clear_screen

def main():
    print("Welcome to the Bookstore")
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a book")
        print("2. View all books")
        print("3. Delete a book")
        print("4. Find a book by ID")
        print("5. Delete a course")
        print("6. Find a course by ID")
        print("7. Delete an author")
        print("8. Find an author by ID")
        print("9. Clear screen")
        print("10. Exit")
        
        choice = input("\nEnter your choice: ")
        
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
            clear_screen()
        elif choice == "10":
            exit_program()
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

def exit_program():
    print("\nExiting the program. Goodbye!")
    exit()

if __name__ == "__main__":
    main()
