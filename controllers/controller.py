from app import app
from flask import Flask, render_template, request, redirect, url_for
# I learned about redirect and url_for
# from the file app.py, import the variable app
from models.books import *
from models.book import *

# homepage view
@app.route('/home')
def index():
    return render_template("index.jinja", title = "Home")

# displaying all books available view
@app.route('/display_all_books')
def display_all_books():
    # all_books = books_list
    return render_template("all_books.jinja", title = "Display All Books", books_list = books_list)

# display_all_books()

# this below didn't work, so I had to try again
# @app.route('/add_new_book', methods=['POST']) # I tried to do <add_new_book> etc but wasn't working so I removed those < >
# def add_new_book():
#     books_list.title = request.form['title']
#     books_list.author = request.form['author']
#     books_list.genre = request.genre['genre']
#     return render_template("add_new_book.jinja", books_list = books_list)


# I used this resource to sort out a 405 error I kept getting: https://stackoverflow.com/questions/42018603/handling-get-and-post-in-same-flask-view
# adding a new book to books_list page
@app.route('/add_new_book', methods=["GET","POST"])
def add_new_book():
    # I want to use POST so I can take info entered in the input boxes and add them to the books list
    if request.method == "POST":
        new_book = Book(request.form['title'], request.form['author'], request.form['genre'], request.form['book_id'])
        # I'm creating a new object, grabbing the title, author and genre but I want to try to change this a bit 
    # appended the new_book variable to the books_list list
        books_list.append(new_book)
        return redirect(url_for('display_all_books'))
    # getting the template and setting books_list to books_list variable
    return render_template("add_new_book.jinja", books_list = books_list)

# function that figures out the book_id to determine whether to exclude or include it in the list first of all might've been better

# I had issues with GET and POST working so I found a resource that said you could put multiple methods together but do a conditional
@app.route('/remove_book', methods=["GET", "POST"])
def remove_book():
    if request.method == "POST":
        # book_id variable set
        book_id = request.form['book_id']
        # for loop to go through all of the books_list books and see if the book_id matches the variable book_id (so if what id is entered matches what's on the display_all_books page)
        for book in books_list:
            # if the id entered matches an id that is in the books_list list, then that specific book will be removed
            # used remove() to delete it
            # break is a keyword that stops the looping so basically when (if I suppose) the book_id entered matches a book_id that is already in books_list, then it'll be removed. If that's in the first iteration, it'll stop there, if it's in the 1000th interation it'll loop until that point but stop there. I only have 4 books here though atm! Hahaha!
            if book.get_book_id() == book_id:
                books_list.remove(book)
                break
            # I read about url_for so I imported it, so it takes us back to the display all books table page
        return redirect(url_for('display_all_books'))
    # this is to take the remove_book template and use it, I don't think I need the title here but I just put it here
    return render_template("remove_book.jinja", title="Remove Book")
