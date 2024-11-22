from database_config import PostgresDB
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.models.user import User

pg_db = PostgresDB()

def getUserFromPostgres(user_name: str):
    try:
        conn = pg_db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT user_id, u_name, u_pass FROM flask_user WHERE u_name = %s", (user_name,))

        row = cur.fetchone()
        if row:
            user = User(id=row[0], name=row[1], password=row[2])
            user.presentation()
        else:
            print("No user with that name was found in the database!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def putUserInPostgres(user: User):
    try:
        conn = pg_db.get_conn()
        cur = conn.cursor()

        cur.execute("INSERT INTO flask_users (u_name, u_pass) VALUES (%s, %s)", (user.name, user.password))
        conn.commit()

        print(f"User {user.name} was succesfuly added to the database!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def deleteUserFromPostgres(user: User):
    try:
        conn = pg_db.get_conn()
        cur = conn.cursor()

        cur.execute("DELETE FROM flask_users WHERE u_name = %s", (user.name,))
        conn.commit()

        print(f"User {user.name} was succesfuly DELETED from the database!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


# getUserFromPostgres(user_name='cgouvea')
# putUserInPostgres(user=User(name="jorgin", password="teste123", id=None))
# deleteUserFromPostgres(user=User(name="jorgin", password="teste123", id=None))