from flask import Blueprint, request, jsonify
from models import Transaction
from utils.utils import require_auth

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('', methods=['GET'])
@require_auth
def list_transactions():
    user_id = request.user['user_id']
    role = request.user['role']
    
    # If admin, they could potentially see all, but for MVP keep it user-scoped 
    # unless specified. However, for audit, we'll keep it user-scoped.
    query = Transaction.query.filter_by(user_id=user_id)
    
    venue = request.args.get('venue')
    type_ = request.args.get('type')
    
    if venue:
        query = query.filter_by(venue=venue)
    if type_:
        query = query.filter_by(transaction_type=type_)
        
    transactions = query.order_by(Transaction.timestamp.desc()).all()
    return jsonify([t.to_dict() for t in transactions]), 200
