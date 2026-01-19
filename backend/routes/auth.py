from flask import Blueprint, request, jsonify
from models import db, User
from utils.utils import hash_password, check_password, create_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'student')

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400

    hashed_pw = hash_password(password)
    new_user = User(email=email, password_hash=hashed_pw, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password(password, user.password_hash):
        return jsonify({'message': 'Invalid credentials'}), 401

    token = create_token(user.id, user.role)
    
    # Redirect hint for frontend
    redirect_map = {
        'student': '/student/dashboard',
        'vendor': '/vendor/pos',
        'admin': '/admin/dashboard'
    }
    
    return jsonify({
        'token': token,
        'user': user.to_dict(),
        'redirect': redirect_map.get(user.role, '/')
    }), 200
