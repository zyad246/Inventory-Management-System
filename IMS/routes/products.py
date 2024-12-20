from flask import Blueprint, request, jsonify
from IMS.db import get_db_connection

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT product_id, product_name, description, price, category_id FROM Products")
        products = [
            {
                "product_id": row[0],
                "product_name": row[1],
                "description": row[2],
                "price": row[3],
                "category_id": row[4]
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@products_bp.route('/', methods=['POST'])
def add_product():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Products (product_name, description, price, category_id) VALUES (?, ?, ?, ?)",
            (data['product_name'], data['description'], data['price'], data['category_id'])
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@products_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product.
    """
    data = request.json
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE Products
            SET product_name = ?, description = ?, price = ?, category_id = ?
            WHERE product_id = ?
            """,
            (data['product_name'], data.get('description'), data['price'], data['category_id'], product_id)
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Product updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product by its ID.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM Products WHERE product_id = ?
            """,
            (product_id,)
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT product_id, product_name, description, price, category_id FROM Products WHERE product_id = ?",
            (product_id,)
        )
        row = cursor.fetchone()
        if row:
            product = {
                "product_id": row[0],
                "product_name": row[1],
                "description": row[2],
                "price": row[3],
                "category_id": row[4]
            }
            return jsonify(product), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()