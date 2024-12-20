import pyodbc
from config import Config

def get_db_connection():
    """
    Establish and return a connection to the database.
    """
    try:
        conn = pyodbc.connect(
            f"DRIVER={Config.DATABASE_CONFIG['DRIVER']};"
            f"SERVER={Config.DATABASE_CONFIG['SERVER']};"
            f"DATABASE={Config.DATABASE_CONFIG['DATABASE']};"
            f"UID={Config.DATABASE_CONFIG['UID']};"
            f"PWD={Config.DATABASE_CONFIG['PWD']};"
        )
        return conn
    except pyodbc.Error as e:
        raise Exception(f"Database connection failed: {str(e)}")
