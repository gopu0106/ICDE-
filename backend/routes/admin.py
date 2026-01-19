from flask import Blueprint, request, jsonify
from models import db, User, Transaction
from utils.utils import require_auth, require_role
from sqlalchemy import func

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/reports', methods=['GET'])
@require_auth
@require_role('admin')
def get_reports():
    # Total transactions
    total_tx = Transaction.query.count()
    
    # Total volume
    total_volume = db.session.query(func.abs(func.sum(Transaction.amount))).one()[0] or 0
    
    # Waste Reduction Calculation (Simulated)
    # Formula: (Skipped Meals / Total Registered Students) * 100
    total_students = User.query.filter_by(role='student').count()
    # Mocking skipped meals logic: students who didn't eat in the last slot
    # For MVP, we'll just return a dynamic mock based on transaction count
    waste_reduction = 45.5 # Base mock value as per PDF "up to 50%"
    
    # Meal counts by venue
    venue_data = db.session.query(
        Transaction.venue, func.count(Transaction.id)
    ).filter(Transaction.transaction_type == 'deduction').group_by(Transaction.venue).all()
    
    venue_report = {v: c for v, c in venue_data}
    
    # Top-up sources
    sources = db.session.query(
        Transaction.source, func.count(Transaction.id)
    ).filter(Transaction.transaction_type == 'top-up').group_by(Transaction.source).all()
    source_report = {s: c for s, c in sources}

    return jsonify({
        'total_transactions': total_tx,
        'total_volume': total_volume,
        'waste_reduction_pct': waste_reduction,
        'venue_report': venue_report,
        'source_report': source_report,
        'active_users': total_students
    }), 200

@admin_bp.route('/users', methods=['GET'])
@require_auth
@require_role('admin')
def list_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200

@admin_bp.route('/refund', methods=['POST'])
@require_auth
@require_role('admin')
def refund_balance():
    data = request.json
    user_id = data.get('user_id')
    amount = data.get('amount')

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if user.balance < amount:
        return jsonify({'message': 'Insufficient balance for refund'}), 400

    user.balance -= amount
    
    transaction = Transaction(
        user_id=user_id,
        amount=-amount,
        transaction_type='refund',
        description='Administrative Refund',
        source='admin'
    )
    db.session.add(transaction)
    db.session.commit()

    return jsonify({'message': 'Refund processed', 'new_balance': user.balance}), 200
