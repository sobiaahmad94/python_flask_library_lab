from app import app
from flask import Flask, render_template, request
# from the file app.py, import the variable app
from models.books import *

@app.route('/home')
def index():
    return render_template("index.jinja", title = "Home")


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
@app.route('/add_new_book', methods=["GET","POST"])
def add_new_book():
    # I want to use POST so I can take info entered in the input boxes and add them to the books list
    if request.method == 'POST':
        new_book = Book(request.form['title'], request.form['author'], request.form['genre'])
        # I'm creating a new object, grabbing the title, author and genre but I want to try to change this a bit 
    # appended the new_book variable to the books_list list
        books_list.append(new_book)
    # getting the template and setting books_list to books_list variable
    return render_template("add_new_book.jinja", books_list=books_list)







