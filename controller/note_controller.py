from controller import app, AlchemyEncoder
from flask import request, render_template, redirect, url_for
from model import db
from model.note import Note
from controller.notebook_controller import get_notebook_by_id
import json

@app.route("/", methods=["GET"])
def home_page():
    return render_template("home.html", title="Home")

@app.route("/about", methods=["GET"])
def about_page():
    return render_template("about.html", title="About")

@app.route("/note/<notebook_id>/<note_id>", methods=["GET"])
def view_single_note(notebook_id, note_id):
    note = db.session.query(Note).filter(Note.id == note_id).first()
    return render_template("note.html", title=note.text, notebook_id=notebook_id, note = note)

@app.route("/note/<notebook_id>", methods=["POST"])
def add_note(notebook_id):
    note_data = request.form
    note = Note(**note_data)
    db.session.add(note)
    db.session.commit()
    return redirect( url_for ( "get_notebook_by_id" , notebook_id = notebook_id) )

@app.route("/note/<notebook_id>/edit/<note_id>", methods=["GET"])
def edit_note(notebook_id, note_id):
    note = db.session.query(Note).filter(Note.id == note_id).first()
    return render_template("edit.html", title="Edit Note", note=note, notebook_id = notebook_id)

@app.route("/note/<notebook_id>/update/", methods=["POST"])
def update_note(notebook_id):
    note_data = request.form
    note = db.session.query(Note).filter(Note.id == note_data["id"]).first()
    note.text = note_data["text"]
    db.session.commit()
    return redirect( url_for ( "get_notebook_by_id" , notebook_id = notebook_id) )

@app.route("/note/<notebook_id>/remove/<note_id>", methods=["POST"])
def delete_note(notebook_id, note_id):
    note = db.session.query(Note).filter(Note.id == note_id).first()
    db.session.delete(note)
    db.session.commit()
    return redirect( url_for ( "get_notebook_by_id" , notebook_id = notebook_id) )

