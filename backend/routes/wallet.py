from flask import Blueprint, request, jsonify
from models import db, User, Transaction
from utils.utils import require_auth

wallet_bp = Blueprint('wallet', __name__)

@wallet_bp.route('/balance', methods=['GET'])
@require_auth
def get_balance():
    user_id = request.user['user_id']
    user = User.query.get(user_id)
    return jsonify({'balance': user.balance}), 200

@wallet_bp.route('/topup', methods=['POST'])
@require_auth
def topup():
    user_id = request.user['user_id']
    data = request.json
    amount = data.get('amount')
    source = data.get('source', 'self') # self, parent

    if not amount or amount <= 0:
        return jsonify({'message': 'Invalid amount'}), 400

    user = User.query.get(user_id)
    print(f"DEBUG: Topup for user {user_id}, initial balance: {user.balance}, amount to add: {amount}")
    user.balance += amount
    db.session.add(user)

    transaction = Transaction(
        user_id=user_id,
        amount=amount,
        transaction_type='top-up',
        description=f'Top-up via {source}',
        source=source
    )
    db.session.add(transaction)
    db.session.commit()

    return jsonify({'message': 'Top-up successful', 'new_balance': user.balance}), 200

@wallet_bp.route('/share', methods=['GET'])
@require_auth
def share_link():
    # In a real app, this would generate a signed token for a public top-up page
    user_id = request.user['user_id']
    # Mocking a shareable token
    share_token = f"share_{user_id}_mock"
    return jsonify({
        'share_url': f"http://localhost:3000/parent/topup/{share_token}",
        'message': 'Share this link with your parent for remote top-up'
    }), 200
