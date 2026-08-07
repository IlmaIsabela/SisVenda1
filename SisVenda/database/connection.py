import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "sistemavendas.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"

def get_connection():
    """Estabelece uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row 
    # Permite acessar os resultados como dicionários
    conn.execute("PRAGMA foreign_keys = ON") 
    # ativa o suporte a chaves estrangeiras
    return conn