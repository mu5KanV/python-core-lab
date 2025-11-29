from book import Book
from library import Library

def main():
    
    # Creates a Library instance
    my_library = Library()
    print("Welcome to your Command-Line Library!")

    # Runs until user inputs "Quit"
    while True:

        # Asks user for the command
        print("\nWhat would you like to do?")
        print("  - Type 'Add' to add a new book")
        print("  - Type 'Find' to find a book by ISBN")
        print("  - Type 'Quit' to exit")

        command = input("\nEnter your command: ").strip().title()

        if command == "Add":
            # Handles Adding a Book
            title = input("Enter the book's title : ")
            author = input("Enter the book's author : ")
            isbn = input("Enter the book's ISBN : ")

            # Create a new Book object
            new_book= Book(title,author,isbn)

            try:
                my_library.add_book(new_book)
            except ValueError as e:
                print(f"\nError: {e}")

        elif command == "Find":
            # Handles finding a book
            isbn = input("Enter the ISBN to find: ")

            try:
                found = my_library.find_book(isbn)
                print(f"Found: {found}")
            except KeyError as e:
                print(f"\nError: {e}")

        elif command == "Quit":
            # Handles Quitting 
            print("GoodBye!")
            break

        else:
            # Handles invalid command
            print("Command invalid. Please try again!")

# This makes sure that the file is being run directly and not imported
# __name__ is magic variable that every file has
# If the is being directly run, __name__ have value "__main__"
# If not directly run, it will have the file's name as it's value
if __name__=="__main__":
    main()
