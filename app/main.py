#!/usr/bin/env python
from flask import (Flask, render_template, request, jsonify)
from models.animal import Animal
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)


@app.route('/')
def index():
    return "List of products"


@app.route('/animals/add',  methods=['POST'])
def add_animal():
    animal_data = dict(request.form.items())
    Animal.create(
        type_animal=animal_data.get('type_animal'),
        commercial_prep=animal_data.get('commercial_prep'),
        homemade_prep=animal_data.get('homemade_prep'),
    )
    result = {'status': 'success'}
    return jsonify(result)


@app.route('/animals',  methods=['GET'])
def list_animals():
    animals = Animal.select()
    results = []
    for animal in animals:
        results.append(
            {
                'type_animal': animal.type_animal,
             }
            )
    return jsonify(results)

@app.route('/animals/feeds/<type_animal>', methods=['GET'])
def animal_feed(type_animal="cow"):
    animal = (Animal.
              select().
              where(Animal.type_animal==type_animal).
              get())
    result = {
        'type_animal': animal.type_animal,
        'commercial_prep': animal.commercial_prep,
        'homemade_prep': animal.homemade_prep
    }
    return jsonify(result)
if __name__ == '__main__':
    app.run(**app_start_config)
