class Library:
    # Constructor of the class
    def __init__(self):
        # This dictionary will take isbn as key and book object as value
        self.books={}
    
    def add_book(self,book):
        # This methods adds a new book to the library
        if book.isbn in self.books:
            raise ValueError(f"Error: Book with ISBN {book.isbn} already exists!")
        else:
            self.books[book.isbn]= book
            print(f"Success: Added {book.title} to the library!")
        
    def find_book(self,isbn):
        # This method finds an existing book in the library
        if isbn in self.books:
            return self.books[isbn]
        else:
            raise KeyError(f"Book with ISBN {isbn} not found!")