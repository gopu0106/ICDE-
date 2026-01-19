from flask import Blueprint, request, jsonify
from models import db, User, Transaction
from utils.utils import require_auth, require_role
from datetime import datetime

meal_bp = Blueprint('meal', __name__)

@meal_bp.route('/deduct', methods=['POST'])
@require_auth
@require_role('vendor')
def deduct_meal():
    data = request.json
    qr_payload = data.get('qr_payload') # JSON from QR: {"user_id": 1, "expires": TIMESTAMP}
    meal_cost = data.get('meal_cost')
    description = data.get('description', 'Meal')
    venue = data.get('venue', 'Unknown Venue')

    if not qr_payload or not meal_cost:
        return jsonify({'message': 'Missing data'}), 400

    user_id = qr_payload.get('user_id')
    expires = qr_payload.get('expires')

    # Security: Check QR expiry
    if datetime.utcnow().timestamp() > expires:
        return jsonify({'message': 'QR code expired'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if user.balance < meal_cost:
        return jsonify({'message': 'Insufficient balance'}), 400

    user.balance -= meal_cost
    
    transaction = Transaction(
        user_id=user_id,
        amount=-meal_cost, # Store as negative for deductions
        transaction_type='deduction',
        description=description,
        venue=venue
    )
    db.session.add(transaction)
    db.session.commit()

    return jsonify({
        'message': 'Payment successful',
        'new_balance': user.balance,
        'user_id': user.id
    }), 200
