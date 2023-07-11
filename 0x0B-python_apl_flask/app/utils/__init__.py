from flask_jwt_extented import create_access_token, jwt_required, get_jwt_identity
from flask import jsonify, current_app

def generate_token(user_id):
    access_token = create_access_token(identify=user_id)
    return access_token

def verify(token):
    try:
        user_id_ = get_jwt_identity()
        return user_id
    except Exception as err:
        current_app.logger.error(str(err))
        return 