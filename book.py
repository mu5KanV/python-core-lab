class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def __repr__(self):
        return(f"Book(Title: {self.title}, Author: {self.author})")