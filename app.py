from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #Lo que sea que referencies aqui debe estar en la carpeta templates

@app.route('/home/<string:name>') #<DataType:variableName>
def hello(name): #si planeas usar la variable de arriba pss asegurate que lo de () este igual a lo de <>
    return "Hello, "+  name #este pedo sirve para URL dinamicos

@app.route('/home/users/<string:name>/posts/<int:id>')
def helloID(name, id):
    return "Hello, " + name + ", your id is: " + str(id)

@app.route('/onlyget', methods=["GET"]) #Especificas el metodo que vas a usar
def get_req():
    return "You can only get this webpage"


#Good practice
if __name__ == "__main__":
    app.run(debug=True) #returns errors

