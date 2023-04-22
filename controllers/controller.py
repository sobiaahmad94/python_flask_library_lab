from app import app
from flask import Flask, render_template, request
# from the file app.py, import the variable app
from models.books import *

@app.route('/')
def index():
    return render_template("index.jinja", title = "Homepage")


@app.route('/display_all_books')
def display_all_books():
    # all_books = books_list
    return render_template("all_books.jinja", title = "All Books", books_list = books_list)

# display_all_books()







