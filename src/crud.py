from db_connection import get_connection

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    conn.close()
    return data


def add_product(name, price, stock, category_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO products (name, price, stock, category_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, price, stock, category_id))

    conn.commit()
    conn.close()
