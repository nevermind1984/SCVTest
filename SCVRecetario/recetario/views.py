import string
from dataclasses import dataclass

# Vista de Recetas con promedios de valoraciones calculados
@dataclass
class vReceta():
    id : int = 0
    nombre : string = ""
    promedio : float = 0

# Vista de Ingredientes con cantidades por personadas calculadas
@dataclass
class vIngrediente():
    id : int = 0
    nombre : string = ""
    cantidad : float = 0
    unidad : string = ""