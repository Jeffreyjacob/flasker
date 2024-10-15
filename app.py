from flask import Flask,render_template

# create a Flask Instance

app = Flask(__name__)

# Create a route decorator

@app.route('/')

def index():
    stuff = "This is a <strong>bold</strong> text"
    favorite_pizza = ["Pepperoni","Cheese","Mushrooms",41]
    return render_template("index.html",stuff=stuff,favorite_pizza = favorite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html",name=name)

## Create Custom Error pages

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404


@app.errorhandler(500)
def page_not_found(error):
    return render_template("500.html"),500