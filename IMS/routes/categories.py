from flask import Blueprint, request, jsonify
from IMS.db import get_db_connection

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/', methods=['GET'])
def get_categories():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT category_id, category_name FROM Categories")
        categories = [{"category_id": row[0], "category_name": row[1]} for row in cursor.fetchall()]
        conn.close()
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@categories_bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.json
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE Categories
            SET category_name = ?
            WHERE category_id = ?
            """,
            (data['category_name'], category_id)
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Category updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@categories_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM Categories WHERE category_id = ?
            """,
            (category_id,)
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Category deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
