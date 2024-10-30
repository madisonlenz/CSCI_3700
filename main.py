from flask import Flask, render_template
import util

# Create an application instance
app = Flask(__name__)

# Database connection details
username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'

# Route to update basket_a
@app.route('/api/update_basket_a/')
def update_basket_a():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    
    try:
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
        connection.commit()
        message = "Success!"
    except Exception as error:
        connection.rollback()
        message = f"Error: {error}"
    
    util.disconnect_from_db(connection, cursor)
    return message
    
    # Route to display unique fruits
@app.route('/api/unique')
def unique_fruits():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    unique_fruits_a = []
    unique_fruits_b = []
    error_message = ""

    try:
        # Fetch unique fruits in basket_a that are not in basket_b
        query_a = """
        SELECT DISTINCT fruit_a FROM basket_a
        WHERE fruit_a NOT IN (SELECT DISTINCT fruit_b FROM basket_b)
        """
        cursor.execute(query_a)
        unique_fruits_a = cursor.fetchall()

        # Fetch unique fruits in basket_b that are not in basket_a
        query_b = """
        SELECT DISTINCT fruit_b FROM basket_b
        WHERE fruit_b NOT IN (SELECT DISTINCT fruit_a FROM basket_a)
        """
        cursor.execute(query_b)
        unique_fruits_b = cursor.fetchall()
        
    except Exception as error:
        error_message = str(error)
    finally:
        util.disconnect_from_db(connection, cursor)

    # Calculate the maximum length of the unique fruits lists
    max_length = max(len(unique_fruits_a), len(unique_fruits_b))

    return render_template('unique_fruits.html', 
                           unique_fruits_a=unique_fruits_a, 
                           unique_fruits_b=unique_fruits_b, 
                           error=error_message,
                           max_length=max_length)  # Pass max_length to the template



if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

