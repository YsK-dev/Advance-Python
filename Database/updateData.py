import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",       # Database server address
    user="root",           # Database username
    password="Asd171307.", # Database password
    database="yskweb"      # Database name
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Define a function to update data in the 'products' table by ID
def updateDatabyID(name, price, id):
    # SQL query to update the 'name' and 'price' columns in the 'products' table
    # The `%s` placeholders are used to safely insert parameters (prevents SQL injection)
    sql = "UPDATE products SET name=%s, price=%s WHERE id=%s"  # %40 is tax :) (commented joke)
    
    # Parameters to pass into the SQL query (name, price, and id)
    params = (name, price, id)
    
    # Execute the SQL query with the provided parameters
    cursor.execute(sql, params)
    
    try:
        # Commit the transaction to save changes to the database
        db.commit()
        
        # Print the number of rows affected by the update
        print(f"{cursor.rowcount} is the number of affected rows")
    
    except mysql.connector.Error as e:
        # Handle any errors that occur during the execution
        print("Oops! Error -->", e)
    
    finally:
        # Close the cursor and database connection to free up resources
        cursor.close()
        db.close()

# Call the function to update the product with id=4
updateDatabyID("Huawei", 13445434, 4)

#With queries to run and tasks to fulfill,