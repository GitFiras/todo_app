from flask import Blueprint, jsonify, request

from . import db
from .models import ToDo

ToDoApi = Blueprint('todo_api', __name__)


@ToDoApi.route('/create', methods=['POST'])
def create_todo():

    try:
        todo = ToDo.from_dict(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 200


@ToDoApi.route('')
def get_todo(task):
    todo = ToDo.query.filter(ToDo.task == task).first()
    if todo is None:
        return 'to do task has not been found', 404
    return jsonify(todo.to_dict()), 200


@ToDoApi.route('<id>', methods=['PUT'])
def update_todo(task):
    todo = ToDo.query.filter(ToDo.task == task).first()
    if todo is None:
        return 'to do task has not been found', 404
    return jsonify(todo.to_dict()), 200


@ToDoApi.route('<id>', methods=['DELETE'])
def delete_todo(task):
    todo = ToDo.query.filter(ToDo.task == task).first()
    del todo
    if todo is None:
        return 'to do task has not been found', 404
    return jsonify(todo.to_dict()), 200
