from flask import session
from numpy import empty
from sqlalchemy import null
from recetario.models import Receta,Ingrediente,Valoracion,Paso
from recetario.views import vReceta,vIngrediente
from recetario import db
from sqlalchemy.sql import func, or_

def get_receta(idBusqueda):
    
    # Consigo todas la receta por id
    receta = Receta.query.filter_by(id=idBusqueda).first()

    # Consigo el promedio de las valoraciones
    vistaReceta = vReceta()
    avg = db.session.query(func.avg(Valoracion.puntaje).label("Punt")).group_by(Valoracion.p_receta).where(Valoracion.p_receta == receta.id).all()
    vistaReceta.id = receta.id
    vistaReceta.nombre = receta.nombre
    if avg is None:
        vistaReceta.promedio = 0
    else:
        vistaReceta.promedio = str(avg[0].Punt)
    
    return vistaReceta

def get_recetas(searchParam):

    # Inicializo variable resultados
    resultados = []
    # Consigo todas las recetas si searchParam está vacío
    if not searchParam:
        search_recetas = Receta.query.all()
    # Consigo todas las recetas que contengan searchParam en el nombre
    else: 
        search_recetas = Receta.query.filter(Receta.nombre.contains(searchParam))

    # Itero entre las recetas y por cada una consigo el promedio de las valoraciones
    for receta in search_recetas:
        vistaReceta = vReceta()
        avg = db.session.query(func.avg(Valoracion.puntaje).label("Punt")).group_by(Valoracion.p_receta).where(Valoracion.p_receta == receta.id).all()
        vistaReceta.id = receta.id
        vistaReceta.nombre = receta.nombre
        if not avg:
            vistaReceta.promedio = 0
        else:
            vistaReceta.promedio = str(avg[0].Punt)
        resultados.append(vistaReceta)
    return resultados

def get_ingredientes_pax(idBusqueda,pax):

    # Consigo la receta por id
    objetivo = Receta.query.filter_by(id=idBusqueda).first()
    ingredientes = objetivo.get_ingredientes()
    resultados = []

    for ingrediente in ingredientes:
        vistaIngrediente = vIngrediente()
        vistaIngrediente.nombre = ingrediente.nombre
        vistaIngrediente.cantidad = ingrediente.cantidad * int(pax)
        vistaIngrediente.unidad = ingrediente.unidad
        resultados.append(vistaIngrediente)
    
    return resultados

def get_pasos(idBusqueda):
    # Consigo la receta por id
    objetivo = Receta.query.filter_by(id=idBusqueda).first()
    pasos = objetivo.get_pasos()
    return pasos

def get_ranking():
    resultados = get_recetas("")

    listaAsc = sorted(resultados, key=lambda x: x.promedio, reverse=True)
    listaDes = sorted(resultados, key=lambda x: x.promedio)

    return listaAsc,listaDes

def set_valoracionReceta(idreceta,valorUsuario):
    nuevaValoracion = Valoracion()
    nuevaValoracion.puntaje = valorUsuario
    nuevaValoracion.p_receta = idreceta
    db.session.add(nuevaValoracion)
    db.session.commit()
    return 0