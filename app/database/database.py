from database_config import PostgresDB
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.models.user import User

pg_db = PostgresDB()

def getUserFromPostgres():
    conn = pg_db.get_conn()
    cur = conn.cursor()

    cur.execute("SELECT user_id, u_name, u_pass FROM flask_user")
    rows = cur.fetchall()
    user = User(id=rows[0][0], name=rows[0][1], password=rows[0][2])
    user.presentation()

getUserFromPostgres()