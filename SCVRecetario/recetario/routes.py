from sqlalchemy import asc, null
from recetario import app
from recetario import services
from flask import jsonify, render_template, request


@app.route('/')
@app.route('/recetario')
def recetario():
    recetas = services.get_allrecetas()
    return render_template('recetario.html', recetas = recetas)

@app.route('/receta', methods=['GET'])
def receta():
    # Procesos los parametros
    idBusqueda = request.args.get('idBusqueda')
    pax = request.args.get('pax')
    if pax is None:
        pax = 1
    # Traigo la receta pedida
    receta = services.get_receta(idBusqueda)
    # Traigo los pasos de la receta pedida
    pasos =services.get_pasos(idBusqueda)
    # Traigo los ingredientes de la receta pedida
    ingredientes = services.get_ingredientes_pax(idBusqueda,pax)
    return render_template('receta.html', receta = receta, pasos = pasos, ingredientes = ingredientes)

@app.route('/ranking')
def ranking():
    return render_template('ranking.html')

@app.route('/search', methods=['GET'])
def search():
    idBusqueda = request.args.get('searchParam')
    receta = services.get_allreceta(idBusqueda)
    return render_template('recetario.html')