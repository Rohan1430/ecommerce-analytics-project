print("NEW ANALYTICS FILE RUNNING ✅")
def top_selling_products():
    from .db_connection import get_connection
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.name, SUM(oi.quantity) AS total_sold
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY p.product_id
    ORDER BY total_sold DESC
    LIMIT 5
    """)

    result = cursor.fetchall()
    conn.close()
    return result

def top_users():
    from .db_connection import get_connection
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT u.name, SUM(o.total_amount) AS total_spent
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    GROUP BY u.user_id
    ORDER BY total_spent DESC
    LIMIT 5
    """)

    result = cursor.fetchall()
    conn.close()
    return result

def revenue_by_category():
    from .db_connection import get_connection
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT c.category_name, SUM(oi.quantity * oi.price) AS revenue
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    JOIN categories c ON p.category_id = c.category_id
    GROUP BY c.category_id
    ORDER BY revenue DESC
    """)

    result = cursor.fetchall()
    conn.close()
    return result

def best_rated_products():
    from .db_connection import get_connection
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.name, AVG(r.rating) AS avg_rating
    FROM reviews r
    JOIN products p ON r.product_id = p.product_id
    GROUP BY p.product_id
    ORDER BY avg_rating DESC
    LIMIT 5
    """)

    result = cursor.fetchall()
    conn.close()
    return result

def order_details():
    from .db_connection import get_connection
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT u.name, p.name, oi.quantity, o.total_amount
    FROM orders o
    JOIN users u ON o.user_id = u.user_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    """)

    result = cursor.fetchall()
    conn.close()
    return result
