from flask import Blueprint, request, jsonify
from IMS.db import get_db_connection

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT inventory_id, product_id, location_id, quantity FROM Inventory")
        inventory = [
            {
                "inventory_id": row[0],
                "product_id": row[1],
                "location_id": row[2],
                "quantity": row[3]
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return jsonify(inventory), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
