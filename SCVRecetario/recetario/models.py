from recetario import db

class Receta(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(length=30), nullable=False) 
    ingredientes = db.relationship('Ingrediente', backref='own_receta', lazy=True)
    valoraciones = db.relationship('Valoracion', backref='own_valoracion', lazy=True)
    pasos = db.relationship('Paso', backref='own_pasos', lazy=True)

    def __repr__(self):
        return f'Receta {self.nombre}'

class Ingrediente(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(length=30), nullable=False) 
    cantidad = db.Column(db.Float(), nullable=False)
    unidad = db.Column(db.String(length=5), nullable=False)
    p_receta = db.Column(db.Integer(), db.ForeignKey('receta.id'))

    def __repr__(self):
        return f'Ingrediente {self.nombre}'

class Valoracion(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    puntaje = db.Column(db.Integer(), nullable=False)
    p_receta = db.Column(db.Integer(), db.ForeignKey('receta.id'))

    def __repr__(self):
        return f'Valoracion {self.puntaje}'

class Paso(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    descripcion = db.Column(db.String(length=40), nullable=False)
    p_receta = db.Column(db.Integer(), db.ForeignKey('receta.id'))

    def __repr__(self):
        return f'Paso {self.descripcion}'
