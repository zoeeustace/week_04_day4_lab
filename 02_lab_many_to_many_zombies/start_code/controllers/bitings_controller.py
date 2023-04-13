from flask import Blueprint, Flask, redirect, render_template, request
from repositories import biting_repository, zombie_repository, human_repository, zombie_type_repository
from models.biting import Biting

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all() # NEW
    return render_template("bitings/index.html", bitings=bitings)

# NEW
@bitings_blueprint.route('/bitings/new' methods = ['GET'])
def new_bite():
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template("bitings/new.html", humans = humans, zombies = zombies)

# CREATE
@bitings_blueprint.route('/bitings', methods = ['POST'])
def create_bite():
    human_id = request.form['human_id']
    zombie_id = request.form['zombie_id']
    human = human_repository.select(human_id)
    zombie = zombie_repository.select(zombie_id)
    biting = Biting(human, zombie)
    biting_repository.save(biting)
    return redirect('/bitings')
# EDIT
@bitings_blueprint.route('/bitings/<id>/edit')
def edit_biting(id):
    biting = biting_repository.select(id)
    return render_template('bitings/edit.html', biting = biting)
# UPDATE
@bitings_blueprint.route('/bitings/<id>', methods = ['POST'])
def update_bitings(id):
    human_id = request.form['human_id']
    zombie_id = request.form['zombie_id']
    human = human_repository.select(human_id)
    zombie = zombie_repository.select(zombie_id)
    biting = Biting(human, zombie, id)
    biting_repository.update(biting)

    return redirect('/bitings')

# DELETE
