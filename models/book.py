from models.books import *

class Book:
    def __init__(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id # I want to keep this as a str for now but I intend to change it to an int later
    
    def get_book_id(self):
        return self.book_id
    
