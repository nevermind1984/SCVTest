from flask import session
from recetario.models import Receta,Ingrediente,Valoracion,Paso
from recetario import db
from sqlalchemy.sql import func, or_

def get_allrecetas():
    
    # Consigo todas las recetas
    all_recetas = Receta.query.all()
    resultados = {}

    # Itero entre las recetas y por cada una consigo el promedio de las valoraciones
    for receta in all_recetas:
        promedio = db.session.query(func.avg(Valoracion.puntaje).label("Punt")).group_by(Valoracion.p_receta).where(Valoracion.p_receta == receta.id).all()
        resultados[receta.nombre] = str(promedio[0].Punt)
    return resultados

def get_search_recetas(searchParam):

    # Consigo todas las recetas que contengan searchParam en el nombre
    search_recetas = Receta.query.filter(Receta.nombre.contains(searchParam))

    # Consigo todas los ingredientes que contengan searchParam en el nombre
    # search_ingredientes = Ingrediente.query.filter(Ingrediente.nombre.contains(searchParam))
    # search_ingredientes = Receta.query.filter(Receta.id in search_ingredientes.id)
    resultados = {}

    for receta in search_recetas:
        promedio = db.session.query(func.avg(Valoracion.puntaje).label("Punt")).group_by(Valoracion.p_receta).where(Valoracion.p_receta == receta.id).all()
        resultados[receta.nombre] = str(promedio[0].Punt)
    return resultados

def get_ingredientes_pax(searchNombre,pax):

    # Consigo la receta por nombre
    objetivo = Receta.query.filter_by(nombre=searchNombre).first()
    ingredientes = objetivo.get_ingredientes()
    resultados = {}

    for ingrediente in ingredientes:
        resultados[ingrediente.nombre] = str(ingrediente.cantidad * int(pax)) + " " + str(ingrediente.unidad)
    
    return resultados

def get_pasos(searchNombre):
    # Consigo la receta por nombre
    objetivo = Receta.query.filter_by(nombre=searchNombre).first()
    pasos = objetivo.get_pasos()
    resultados = {}

    for paso in pasos:
        resultados[paso.descripcion] = ""

    return resultados
