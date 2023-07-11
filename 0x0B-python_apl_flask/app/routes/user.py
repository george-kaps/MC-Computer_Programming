from flask import Blueprint, request, jasonify
from app.modles.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    username = request.json.get('username') 
    password = request.json.get('password')
    email = request.json.get('email')

    existing_user = User.query.filter_by(username=username).first
    if existing_user:
        return jasonify(massage='Username already taken'), 409
    
    hash_password = b




