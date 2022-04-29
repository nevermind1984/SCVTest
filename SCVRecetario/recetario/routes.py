from recetario import app
from recetario import db
from recetario.models import Receta,Ingrediente,Paso,Valoracion
from flask import jsonify, render_template, request


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route("/recetario", methods=['GET', 'POST'])
def market_page():
    
    if request.method == "GET":
        recetas = Receta.query.all()
        #for receta in recetas
        print(recetas)
        return jsonify(recetas)
    
    
    return 'hello'

