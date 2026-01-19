from flask import Blueprint, request, jsonify, send_file
import qrcode
import json
import io
import base64
from datetime import datetime, timedelta
from utils.utils import require_auth

qr_bp = Blueprint('qr', __name__)

@qr_bp.route('/generate', methods=['GET'])
@require_auth
def generate_qr():
    user_id = request.user['user_id']
    
    # Payload with 5-minute expiry
    payload = {
        'user_id': user_id,
        'expires': (datetime.utcnow() + timedelta(minutes=5)).timestamp()
    }
    
    qr_data = json.dumps(payload)
    img = qrcode.make(qr_data)
    
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return jsonify({
        'qr_image': f"data:image/png;base64,{img_str}",
        'expires_at': payload['expires']
    }), 200
