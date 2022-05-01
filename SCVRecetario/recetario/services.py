from flask import session
from recetario.models import Receta,vReceta,Ingrediente,vIngrediente,Valoracion,Paso
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
    vistaReceta.promedio = str(avg[0].Punt)
    
    return vistaReceta

def get_allrecetas():
    
    # Consigo todas las recetas
    all_recetas = Receta.query.all()
    resultados = []

    # Itero entre las recetas y por cada una consigo el promedio de las valoraciones
    for receta in all_recetas:
        vistaReceta = vReceta()
        avg = db.session.query(func.avg(Valoracion.puntaje).label("Punt")).group_by(Valoracion.p_receta).where(Valoracion.p_receta == receta.id).all()
        vistaReceta.id = receta.id
        vistaReceta.nombre = receta.nombre
        vistaReceta.promedio = str(avg[0].Punt)
        resultados.append(vistaReceta)
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
