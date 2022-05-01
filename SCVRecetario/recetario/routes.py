from sqlalchemy import asc, null
from recetario import app
from recetario import services
from flask import jsonify, render_template, request, redirect, url_for


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
    # Combo box de valores
    puntajes = [1,2,3,4,5]
    return render_template('receta.html', receta = receta, pasos = pasos, ingredientes = ingredientes, puntajes = puntajes)

@app.route('/ranking')
def ranking():
    listaAsc,listaDes = services.get_ranking()
    return render_template('ranking.html', listaAsc = listaAsc ,listaDes = listaDes )

@app.route('/search', methods=['GET'])
def search():
    idBusqueda = request.args.get('searchParam')
    receta = services.get_allreceta(idBusqueda)
    return render_template('recetario.html')

@app.route('/guardarValoracion', methods=['POST'])
def guardarValoracion():
    valorUsuario = request.form.get('valorUsuario')
    idreceta = request.form.get('idreceta')
    services.set_valoracionReceta(idreceta,valorUsuario)
    return redirect(url_for('recetario'))