from flask import Flask, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "database"),
        database=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        port=os.getenv("DB_PORT", "5432")
    )

@app.route("/")
def home():
    return jsonify({
        "message": "3-Tier Docker Application API",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/api/tasks")
def get_tasks():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT id, title, completed FROM tasks ORDER BY id")
        tasks = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(tasks)
    except Exception as e:
        app.logger.exception("Database query failed")
        return jsonify({"error": "Database unavailable"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
