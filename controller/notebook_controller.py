from controller import app, AlchemyEncoder
from flask import request, render_template, redirect, url_for
from model import db
from model.note import Note
from model.notebook import Notebook
import json

@app.route("/notebook", methods = ["GET"])
def get_notebooks():
    notebooks = db.session.query(Notebook).all()
    return render_template("notebooks.html", title="Notebooks", notebooks = notebooks)

@app.route("/notebook", methods = ["POST"])
def add_notebook():
    notebook_data = request.form
    notebook = Notebook(**notebook_data)
    db.session.add(notebook)
    db.session.commit()
    return redirect( url_for ( "get_notebooks" ))

@app.route("/notebook/<notebook_id>")
def get_notebook_by_id(notebook_id):
    notebook = db.session.query(Notebook).filter(Notebook.id == notebook_id).first()
    return render_template("notes.html", title= notebook.title + " " + "notes:", notes=notebook.notes, notebook_id= notebook.id)
