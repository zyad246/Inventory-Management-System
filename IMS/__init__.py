from flask import Flask
from IMS.routes.products import products_bp
from IMS.routes.categories import categories_bp
from IMS.routes.locations import locations_bp
from IMS.routes.inventory import inventory_bp
from IMS.routes.reports import reports_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(categories_bp, url_prefix='/categories')
    app.register_blueprint(locations_bp, url_prefix='/locations')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    app.register_blueprint(reports_bp, url_prefix='/reports')

    @app.route('/')
    def home():
        return "Welcome to the Inventory Management API!", 200

    return app
