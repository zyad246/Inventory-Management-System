from flask import Blueprint, jsonify
from IMS.db import get_db_connection

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/inventory_summary', methods=['GET'])
def inventory_summary():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                Products.product_name, 
                Locations.location_name, 
                Inventory.quantity 
            FROM Inventory
            JOIN Products ON Inventory.product_id = Products.product_id
            JOIN Locations ON Inventory.location_id = Locations.location_id
        """)
        summary = [
            {
                "product_name": row[0],
                "location_name": row[1],
                "quantity": row[2]
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return jsonify(summary), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
