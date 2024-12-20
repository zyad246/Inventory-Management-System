from flask import Blueprint, request, jsonify
from IMS.db import get_db_connection

locations_bp = Blueprint('locations', __name__)

@locations_bp.route('/', methods=['GET'])
def get_locations():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT location_id, location_name FROM Locations")
        locations = [{"location_id": row[0], "location_name": row[1]} for row in cursor.fetchall()]
        conn.close()
        return jsonify(locations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
