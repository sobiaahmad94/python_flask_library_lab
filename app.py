from flask import Flask, render_template, request, redirect, url_for

# render_template is so I can render the jinja file
# request is so I can do POST and GET requests

app = Flask(__name__)

from controllers import controller

if __name__ == '__main__':
    app.run(debug=True)