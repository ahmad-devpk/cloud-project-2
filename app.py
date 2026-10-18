from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    db_status = ""
    try:
        conn = mysql.connector.connect(
            host=os.environ.get('DB_HOST', 'db'),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', 'mysecretpassword'),
            database=os.environ.get('DB_NAME', 'testdb')
        )
        db_status = "Successfully connected to MySQL Database!"
    except Exception as e:
        db_status = f"Database connection error: {e}"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Developer-First AWS Infrastructure</title>
        <style>
            body {{ background-color: #0b0f19; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }}
            .card {{ background: #161f33; display: inline-block; padding: 30px; border-radius: 12px; border: 1px solid #2d3748; }}
            .status {{ color: #48bb78; font-weight: bold; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Developer-First AWS Infrastructure</h1>
            <p>Cloud Computing Practice Project 2</p>
            <div class="status">{db_status}</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
