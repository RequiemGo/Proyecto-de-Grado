from enum import unique
from flask import Flask, render_template, request
from flask import current_app
from flask.globals import session
from flask.helpers import send_file, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import os
from flask_ngrok import run_with_ngrok

UPLOAD_FOLDER = "recursos/"
# Prueba de conexion
app = Flask(__name__)
run_with_ngrok(app)
dbdir = 'mysql+pymysql://root:@localhost:3306/recursos'
#dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/recursos.db"
app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

db = SQLAlchemy(app)


class Recursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(280), )
    descripcion = db.Column(db.String(280))
    ruta = db.Column(db.String(100))

    def __init__(self, titulo, descripcion, ruta):
        self.titulo = titulo
        self.descripcion = descripcion
        self.ruta = ruta


recurso1 = Recursos(titulo='DINÁMICA DE SISTEMAS APLICADA A LA TOMA DE DECISIONES EN LA PRODUCCIÓN Y COMERCIALIZACIÓN PECUARIA DE SANTANDER (COLOMBIA). UN CASO DE APLICACIÓN EN UN HATO GANADERO DE LA PROVINCIA DE GARCÍA ROVIRA',
                    descripcion='simulador soportado en un modelo de DS para apoyar la toma de decisiones relacionadas con el proceso de producción y comercialización en un hato ganadero de la provincia de García Rovira.', ruta=UPLOAD_FOLDER)
recurso2 = Recursos("prueba", "esto es una prueba", UPLOAD_FOLDER)

recurso3 = Recursos('de nuevo', 'here we go again', UPLOAD_FOLDER)
recurso4 = Recursos('a ver ', 'como fue', UPLOAD_FOLDER)
try:
    db.session.add(recurso1)
    db.session.add(recurso2)
    db.session.add(recurso3)
    db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)
    # db.session.add(recurso4)

    db.session.commit()
except exc.IntegrityError:
    db.session.rollback()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Documentos", methods=["GET", "POST"])
def documentos():
    if request.method == "POST":
        #f = request.files["ourfiles"]
        #filename = f.filename
        #f.save(os.path.join(app.config[UPLOAD_FOLDER], filename))
        uploads = os.path.join(current_app.root_path,
                               app.config[UPLOAD_FOLDER])
        return send_from_directory(directory=uploads, filename=filename, as_attachment=True)
    return render_template("page-Documentos.html")


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    print(uploads)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


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
    app.run()
