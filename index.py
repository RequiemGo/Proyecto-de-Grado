from enum import unique
from flask import Flask, render_template, request
from flask.helpers import send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

UPLOAD_FOLDER = os.path.abspath("./recursos/")
# Prueba de conexion
app = Flask(__name__)
dbdir = 'mysql+pymysql://root:@localhost:3306/recursos'
app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

db = SQLAlchemy(app)


class Recursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(280), unique=True)
    descripcion = db.Column(db.String(280))
    ruta = db.Column(db.String(100), unique=True)

    def __init__(self, titulo, descripcion, ruta):
        self.titulo = titulo
        self.descripcion = descripcion
        self.ruta = ruta


recurso1 = Recursos('DINÁMICA DE SISTEMAS APLICADA A LA TOMA DE DECISIONES EN LA PRODUCCIÓN Y COMERCIALIZACIÓN PECUARIA DE SANTANDER (COLOMBIA). UN CASO DE APLICACIÓN EN UN HATO GANADERO DE LA PROVINCIA DE GARCÍA ROVIRA',
                    'simulador soportado en un modelo de DS para apoyar la toma de decisiones relacionadas con el proceso de producción y comercialización en un hato ganadero de la provincia de García Rovira.', 'dinamica.pdf')
# db.session.add(recurso1)
# db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Documentos", methods=["GET", "POST"])
def documentos():
    if request.method == "POST":
        f = request.files["ourfiles"]
        filename = f.filename
        f.save(os.path.join(app.config[UPLOAD_FOLDER], filename))
        return send_from_directory(app.config[UPLOAD_FOLDER], filename=filename, as_attachment=True)
    return render_template("page-Documentos.html")


@app.route("/Modelos")
def modelos():
    return render_template("page-Modelos.html")


@app.route("/Recursos multimedia")
def multimedia():
    return render_template("page-Recursos.html")


@app.route("/Simuladores")
def simuladores():
    return render_template("page-Simuladores.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
