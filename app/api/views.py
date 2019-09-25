from flask import jsonify, request
from ..serializers import UserSchema
from ..models import User
from .. import db
from . import api


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@api.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']

    new_user = User(username,email)

    db.session.add(new_user)
    db.session.commit()
    data = {
        'username': username,
        'email': email,
    }
    return jsonify(data)


@api.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


@api.route("/user/<id>", methods = ["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


@api.route("/user/<id>", methods = ["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username  = username

    db.session.commit()
    return  user_schema.jsonify(user)


@api.route("/user/<id>",methods = ["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return  user_schema.jsonify(user)
