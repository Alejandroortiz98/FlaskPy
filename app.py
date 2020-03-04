from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  # 1.- import sql alchemy
from datetime import datetime

app = Flask(__name__)
# 2.- tell flask where tf is the DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
#         ^path to where DB is stored
# '///' relative path o sea que esta dentro de la misma carpeta que app.py
# '////' absolute path que si te tienes que meter a otra carpeta y la madre

db = SQLAlchemy(app)  # 3.- create your database
# 4.- design your db


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
# primary key must always be unique
    title = db.Column(db.String(100), nullable=False)
# mullable = True can't be null
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog Post ' + str(self.id)


all_posts = [  # inicio diccionario de listas
    {
        'title': 'Post 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'author': 'Alex'
    },
    {
        'title': 'Post 2',
        'content': 'sed do eiusmod tempor incididunt ut labore et dolore magna'
    }
]
# fin diccionario de listas


@app.route('/')
def index():
    return render_template('index.html')
    # Lo que sea que referencies aqui debe estar en la carpeta templates


@app.route('/posts')
def posrs():
    return render_template('posts.html', posts=all_posts)
    # donde sea que se haya referenciado el html tambien puedes
    # referenciar una variable


@app.route('/home/<string:name>')  # <DataType:variableName>
def hello(name):
    # si planeas usar la variable de arriba pss
    # asegurate que lo de () este igual a lo de <>
    return "Hello, " + name  # este pedo sirve para URL dinamicos


@app.route('/home/users/<string:name>/posts/<int:id>')
def helloID(name, id):
    return "Hello, " + name + ", your id is: " + str(id)


@app.route('/onlyget', methods=["GET"])
# Especificas el metodo que vas a usar
def get_req():
    return "You can only get this webpage"


# Good practice
if __name__ == "__main__":
    app.run(debug=True)  # returns errors
