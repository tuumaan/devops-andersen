from flask import Blueprint, jsonify, request
from flask.wrappers import Response
from emodji import emodji

bp = Blueprint('animals', __name__)

# @bp.route('/', methods=['GET',])
# def index():
#     return jsonify({'hello': 'world'})

@bp.route('/', methods=['POST', 'GET' ])
def main():
    data = request.get_json()
    if not data:
    #  return Response('Empty body', status=400)
        data = {}

    animal: str = data.get('animal', 'microbe')
    sound: str = data.get('sound', 'wazzzuuuup')
    count: int = data.get('count', 1)
    
    animal_emodji = emodji.get(animal, 'THING')
    animal_sound = f'{animal_emodji} says {sound}\n'
    resp_string = str()
    for i in range(count):
        resp_string += animal_sound
    resp_string += 'Made with 🫀 by Maya\n'
    
    return Response(resp_string)
